import librosa
import os
import csv
import numpy as np
from sklearn.preprocessing import StandardScaler

dataset_path = "../KONACNO"  # path do snimaka

num_mfcc = 14  # broj mfcc koeficijenata koje uzimamo u obzir
n_fft = 8192  # ovaj broj nisam dirao, mislim da je uredu da ovako ostane
n_sample = 28  # na koliko dijelova dijelimo izvorni snimak, ako snimak traje 1s, a ovaj parametar je 10, onda svakih
# 100ms računamo mfcc
delta = 1  # delta = 0 --> ne računaju se delta_mfcc, delta = 1 --> računaju se delta_mfcc

if __name__ == "__main__":

    scalerMfcc = StandardScaler()  # scaler za normalizaciju audio zapisa
    header = np.arange((delta + 1)*num_mfcc * n_sample + 1)  # prvi red u csv fajlu

    with open('trening_14_8192_28.csv', 'w', encoding='UTF8', newline='') as d:  # za pisanje csv fajla
        # u csv fajl zapisujem mfcc svih snimaka za treniranje i to na način da zapisujem 10 prvih koeficijenata
        # pa 10 drugih koeficijenata pa 10 trećih koeficijenata, ako je 10 broj semplova snimka
        writer = csv.writer(d)
        writer.writerow(header)

        for i, (dirpath, dirnames, filenames) in enumerate(os.walk(dataset_path)):
            if dirpath is not dataset_path:
                for f in filenames:
                    file_path = os.path.join(dirpath, f)
                    signal, sample_rate = librosa.load(file_path)
                    signal = librosa.util.normalize(signal)  # normalizacija audio zapisa

                    mfcc = librosa.feature.mfcc(signal, sample_rate, n_mfcc=num_mfcc, n_fft=n_fft,
                                                hop_length=int(len(signal) / n_sample))
                    mfcc = mfcc[:, :n_sample]  # dodato zbog izdvajanja jednog seta od n_samplova mfcc-a

                    if delta:
                        delta_mfcc = librosa.feature.delta(mfcc)
                        delta_mfcc = delta_mfcc[:, :n_sample]
                        scalerMfcc.fit(delta_mfcc)
                        delta_mfcc = scalerMfcc.transform(delta_mfcc)
                        delta_mfcc = delta_mfcc.flatten()

                    scalerMfcc.fit(mfcc)  # Scaler fitujemo sa MFCC-om
                    mfcc = scalerMfcc.transform(mfcc)  # transformišem koeficijente na stari izgled
                    mfcc = mfcc.flatten()  # postavljam sve koeficijente u jedan red

                    if delta:
                        mfcc = np.append(int(i - 1), mfcc)
                        mfcc = np.append(mfcc, delta_mfcc)
                    else:
                        mfcc = np.append(int(i - 1),
                                         mfcc)  # dodajem ispred "cifru" ispred svih mfcc-a koji su izračunati upravo
                    # za tu cifru
                    writer.writerow(mfcc)


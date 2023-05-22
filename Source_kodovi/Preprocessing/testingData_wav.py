import librosa
import os
import csv
import numpy as np
from sklearn.preprocessing import StandardScaler

dataset_path = "../Isam/testcifre_folder_normaliziran"  # path do snimaka

sample_rate = 44100

if __name__ == "__main__":

    header = np.arange(sample_rate + 1)  # prvi red u csv fajlu
    br = 0

    with open('testing_wav_44100.csv', 'w', encoding='UTF8', newline='') as d:  # za pisanje csv fajla
        # u csv fajl zapisujem sve uzorke svih fileova
        writer = csv.writer(d)
        writer.writerow(header)

        for i, (dirpath, dirnames, filenames) in enumerate(os.walk(dataset_path)):
            if dirpath is not dataset_path:
                for f in filenames:
                    br = br + 1
                    # if br > 20:
                    #     break
                    file_path = os.path.join(dirpath, f)
                    signal, sample_rate = librosa.load(file_path, sr = None)

                    signal = np.append(int(i - 1), signal)
                    writer.writerow(signal)
                    print('Dodan', file_path[-9:])
                    print('Sample rate =', sample_rate)
                    
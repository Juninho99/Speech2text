import librosa
import os
import csv
import numpy as np
import random
from sklearn.preprocessing import StandardScaler
from scipy.io.wavfile import write

dataset_path = "C:/Users/Muamer/Documents/GitHub/Speech2text/Isam/testcifre_folder_normaliziran"  # path do snimaka

if __name__ == "__main__":

    yourpath = dataset_path
    br = 0
    for root, dirs, files in os.walk(yourpath, topdown=False):
        for name in files:
            if name[-4:] != '.wav':
                continue
            br = br + 1
            # if br > 20:
            #     break
            file_path = os.path.join(root, name)
            signal, sample_rate = librosa.load(file_path, sr=44100)
            print('Sample rate:', sample_rate)
            duzina = np.size(signal)
            zeljena_duzina = 1*sample_rate
            if duzina < zeljena_duzina:
                dodatna_duzina = zeljena_duzina - duzina
                if dodatna_duzina%2 == 0:
                    dodatna_duzina_prije = dodatna_duzina/2
                    dodatna_duzina_poslije = dodatna_duzina/2
                else:
                    dodatna_duzina_prije = (dodatna_duzina+1)/2
                    dodatna_duzina_poslije = (dodatna_duzina-1)/2
                dodatna_duzina_prije = int(dodatna_duzina_prije)
                dodatna_duzina_poslije = int(dodatna_duzina_poslije)
                signal = np.append(np.zeros(dodatna_duzina_prije), signal)
                signal = np.append(signal, np.zeros(dodatna_duzina_poslije))
            if duzina > zeljena_duzina:
                oduzeta_duzina = duzina - zeljena_duzina
                if oduzeta_duzina%2 == 0:
                    oduzeta_duzina_prije = oduzeta_duzina/2
                    oduzeta_duzina_poslije = oduzeta_duzina/2
                else:
                    oduzeta_duzina_prije = (oduzeta_duzina+1)/2
                    oduzeta_duzina_poslije = (oduzeta_duzina-1)/2
                oduzeta_duzina_prije = int(oduzeta_duzina_prije)
                oduzeta_duzina_poslije = int(oduzeta_duzina_poslije)
                signal = signal[oduzeta_duzina_prije:-oduzeta_duzina_poslije]
                # signal = np.append(np.zeros(dodatna_duzina_prije), signal)
                # signal = np.append(signal, np.zeros(dodatna_duzina_poslije))

            # print(dodatna_duzina_prije, type(dodatna_duzina_prije))
            # file_path = file_path[:-4] + 'norm.wav'
            signal = librosa.util.normalize(signal)  # normalizacija amplitude audio zapisa
            write(file_path, sample_rate, signal)
            print('Napravljen', file_path, br)



        
        # for name in dirs:
        #     print(os.path.join(root, name))
        #     # stuff

        # file_path = os.path.join(dirpath, f)
        # # print(file_path)
        # signal, sample_rate = librosa.load(file_path)

        # signal = librosa.util.normalize(signal)  # normalizacija audio zapisa

        # print(signal.shape)
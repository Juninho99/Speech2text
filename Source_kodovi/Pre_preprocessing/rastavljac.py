import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.io.wavfile import read
from scipy.io import wavfile
import scipy.io
import numpy as np
import matplotlib
import sounddevice as sd
from scipy.io.wavfile import write


th_val = 0.12
th_dur = 0.22
min_duz_rijeci = 0.05
max_broj_snimaka = 10000

fs, data = wavfile.read('./dugi_snimci/20.wav')
broj_snimka = 299

luft = int(th_dur * fs)
min_brind_rijeci = int(min_duz_rijeci*fs)

# Nadji interval kada je tisina duzine luft (th_dur sekundi), 
# buka (svakih barem th_dur ima preko th_val), pa opet tisina duzine luft

# data = data[:, 0]

length = data.shape[0] / fs
br_uz = data.shape[0]

time = np.linspace(0., length, data.shape[0])

zadnja_buka = 0
zadnja_tisina = 0
pocetak = 0
snimam = False

data = data / (2 ** 16)



for i in range(br_uz):
	if broj_snimka >= max_broj_snimaka:
		break

	if abs(data[i]) > th_val:
		zadnja_buka = i
		if not snimam:
			snimam = True
			pocetak = i
	else:
		zadnja_tisina = i

	# popravi za min duz rijeci, skontaj sta treba uraditi, desi se da 1 predje th_val, to mora biti

	if snimam and i - zadnja_buka > luft and i - luft - pocetak < min_brind_rijeci:
		snimam = False

	if (snimam and i - zadnja_buka > luft) or (snimam and i - zadnja_buka > 0*int(float(luft)/2) and i == br_uz-1):
		#if broj_snimka == 56:
		#	print(i, zadnja_buka, snimam, luft, min_duz_rijeci)
		# Snimio rijec, treba zapisati od pocetak - luft do sada
		snimam = False
		filename = str(broj_snimka) + '.wav'
		if broj_snimka < 10:
			filename = '0' + filename
		if broj_snimka < 100:
			filename = '0' + filename
		# if broj_snimka < 1000:
		# 	filename = '0' + filename
		filename = 'pojedinacne_cifre/test' + filename 
		broj_snimka = broj_snimka + 1

		write(filename, fs, data[(pocetak - luft):i])
		print('Napravio', filename)

"""
	if abs(data[i,0]) > th_val:
		tren_poc_tis = i

	if i-tren_poc_tis > th_dur_ind and i-tren_poc_sn > min_duz_rijeci_ind:
		tren_poc_sn = tren_poc_sn - luft
		if tren_poc_sn < 0:
			tren_poc_sn = 0
		# Snimi od tren_poc_sn do sad

		filename = str(broj_snimka) + '.wav'
		if broj_snimka < 10:
			filename = '0' + filename
		if broj_snimka < 100:
			filename = '0' + filename
		broj_snimka = broj_snimka + 1

		write(filename, fs, data[tren_poc_sn:i,:])
		print('Pravim', filename)

		tren_poc_sn = i
		tren_poc_tis = i

"""

# write(filename, fs, tmp_data)

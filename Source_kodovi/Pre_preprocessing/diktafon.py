import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100  # Sample rate
Trec = 1  # Duration of recording
N = 1

print('fs =',fs/1000,'kHz')
# print('Trec =',Trec,'s')
print('N =',N,'snimaka')
print('Upisite duzinu snim(a)ka (Trec)')
Trec = int(input())
print('Upisite broj snimaka (N)')
N = int(input())

while N > 1000:
	print('Maksimalna vrijednost za N je 1000, upisite ponovo N.')
	N = int(input())

for i in range(N):
	filename = str(i) + '.wav'
	if i < 10:
		filename = '0' + filename
	if i < 100:
		filename = '0' + filename
	filename = 'diktafon_Muamer_' + filename
	print('Spremni za snimanje za file', filename, '?')
	input()
	myrecording = sd.rec(int(Trec * fs), samplerate=fs, channels=2)
	sd.wait()  # Wait until recording is finished
	write(filename, fs, myrecording)  # Save as WAV file

print('Gotovo snimanje.')

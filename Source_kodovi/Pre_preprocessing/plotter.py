import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.io.wavfile import read
from scipy.io import wavfile
import scipy.io
import numpy as np
import matplotlib
matplotlib.use('TKAgg')

samplerate, data = wavfile.read('dugi_snimci/20.wav')

length = data.shape[0] / samplerate
data = data / (2 ** 16)
print(length)


time = np.linspace(0., length, data.shape[0])

plt.plot(time, data[:], label="Left channel")

#plt.plot(time, data[:, 1], label="Right channel")

# plt.legend()

plt.xlabel("Time [s]")

plt.ylabel("Amplitude")

plt.show()
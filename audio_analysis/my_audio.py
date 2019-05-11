import numpy
import wave
import math
from scipy.signal import lfilter, hamming
from audiolazy.lazy_lpc import lpc

spf = wave.open('hodYMC.wav', 'r')

# Get file as numpy array.
x = spf.readframes(-1)
x = numpy.fromstring(x, 'Int16')
# Get Hamming window.
N = len(x)
w = numpy.hamming(N)


# Apply window and high pass filter.
x1 = x * w
x1 = lfilter([1],[1., 0.63], x1)


# Get LPC.
Fs = spf.getframerate()
ncoeff = int(2 + Fs / 1000)
A= lpc.kautocor(x1, ncoeff)




# Get roots.
rts = numpy.roots(A.numerator)
rts = [r for r in rts if numpy.imag(r) >= 0]

# Get angles.
angz = numpy.arctan2(numpy.imag(rts), numpy.real(rts))

# Get frequencies.
Fs = spf.getframerate()
frqs = sorted(angz * (Fs / (2 * math.pi)))

frqs = [fr for fr in frqs if fr > 0]
frqs = frqs[:4]

frqs = [round(fr,2) for fr in frqs]

print(frqs)

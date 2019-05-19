import numpy
import wave
import math
from scipy.signal import lfilter, hamming
from audiolazy.lazy_lpc import lpc

class Formant_analyzer():
	formants = []

	def getFormants(self, soundFile):
		#spf = wave.open('hadYMC.wav', 'r')
		spf = wave.open(soundFile, 'r')
		Fs = spf.getframerate()
		dt = 1/Fs
		# Get file as numpy array.
		x = spf.readframes(-1)

		x = numpy.fromstring(x, 'Int16')

		# Get Hamming window.
		I0 = int(round(len(x)*0.25))
		Iend = int(round(len(x)*0.8))
		N = len(x[I0:Iend])
		#N = len(x)
		x = x[I0:Iend]
		w = numpy.hamming(N)



		# Apply window and high pass filter.
		x1 = x * w
		x1 = lfilter([1.],[1., 0.63], x1)


		# Get LPC.

		ncoeff = int(2 + Fs / 1000)
		A= lpc.autocor(x1, ncoeff)



		# Get roots.
		rts = numpy.roots(A.numerator)

		rts = [r for r in rts if numpy.imag(r) >= 0]

		# Get angles.
		angz = numpy.arctan2(numpy.imag(rts), numpy.real(rts))

		# Get frequencies.
		Fs = spf.getframerate()

		frqs = sorted(angz * (Fs / (2 * math.pi)))

		frqs = [fr for fr in frqs if fr > 0 and not fr<300]
		frqs = frqs[:6]

		frqs = [round(fr,2) for fr in frqs]
		self.formants = frqs




import numpy
import wave
import math
from scipy.signal import lfilter, hamming
from audiolazy.lazy_lpc import lpc
from scipy.io.wavfile import write

class Formant_analyzer():
	formants = []

	def getFormants(self, soundFile):
		#spf = wave.open('hadYMC.wav', 'r')

		spf = wave.open(soundFile, 'r')

		print('spf type:'+str(type(spf)))

		Fs = spf.getframerate()

		print('Fs type:'+str(type(Fs)))
	
		dt = 1/Fs
		# Get file as numpy array.
		x = spf.readframes(-1)

		print('x type:'+str(type(x)))

		x = numpy.fromstring(x, 'Int16')
		print('x type:'+str(type(x)))
		
		#remove the fourth byte
		a = 3

		newnump = numpy.delete(x,numpy.arange(len(x)/(a+1))*(a+1)+a)
		#remove the third byte
		b = 2

		newnump = numpy.delete(newnump,numpy.arange(len(newnump)/(b+1))*(b+1)+b)

		originalfile = newnump  #now the new numpy array is a mono sound
		write('originalfile.wav', Fs, originalfile)

		x = newnump

		'''
		file_len = len(x)
		file_max = max(x)
		print(file_len)
		print(file_max)
		i = numpy.where(x == max(x))
		print(i)
		#i = int(i)


		
		I0 = int(round(file_max*1.5))

		Iend = int(round((file_len-file_max)*0.63)+file_max)

		N = len(x[I0:Iend])
		x = x[I0:Iend]
	

		tmpfile = x[I0:Iend]
		write('tmpfile.wav', Fs, tmpfile)
		'''

		# Get Hamming window.
		N = len(x)

		print(x[0:5])
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

		frqs = [fr for fr in frqs if fr > 0 and not fr<100]
		frqs = frqs[:2]

		frqs = [round(fr,2) for fr in frqs]
		self.formants = frqs






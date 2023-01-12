#1-D Discrete Fourier Transfrom
import numpy as np
import scipy.fft
x=np.array([1,2,3,4,5])
y=fft(x)
print(y)
i_y=scipy.fft.ifft(y)
print(i_y)
#2-D Fourier Transform
a=np.array([[1,2,5,6],[6.5,4.5,5,3]])
b=scipy.fft.fft2(a)
print(b)
#Discrete Cosine Transform
c=scipy.fft.dct(a)
print(c)
#Discrete Sine Transform
s=scipy.fft.dst(a)
print(s)
#inverse discrete Cosine and Sine
i_c=scipy.fft.idct(c)
i_s=scipy.fft.idst(s)
print(i_c)
print(i_s)

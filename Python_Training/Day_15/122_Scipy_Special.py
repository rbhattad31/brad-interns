from scipy.special import cbrt
print(cbrt(8))
print(cbrt(512))
print(cbrt(900))
from scipy.special import comb
print(comb(4,2))
print([comb(6,1),comb(6,2),comb(6,3),comb(6,4)])
from scipy.special import exp10
print(exp10(6))
from scipy.special import exprel
print(exprel(0))
from scipy.special import gamma
print(gamma(60))
from scipy.special import lambertw
print([lambertw(1),lambertw(0),lambertw(56),
	lambertw(68),lambertw(10)])
from scipy.special import logsumexp
a = [1, 2, 3, 4, 5]
print(logsumexp(a))
from scipy.special import perm
a=[perm(6,1),perm(6,2),perm(6,3),perm(6,4)]
print(a)

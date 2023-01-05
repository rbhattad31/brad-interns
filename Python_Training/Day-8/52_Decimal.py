import decimal
"""
a=decimal.Decimal(4.5).exp()
b=decimal.Decimal(4.5).sqrt()
c=decimal.Decimal(4.5).ln()
d=decimal.Decimal(4.5).log10()
e=decimal.Decimal(4.5).as_tuple()
f=decimal.Decimal(10).fma(2,3)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
"""
"""
a=decimal.Decimal(-9.23)
b=decimal.Decimal(8.22)
print(a.compare(b))
print(a.compare_total_mag(b))
print(a.max(b))
print(a.min(b))

print(a.copy_abs())
print(b.copy_negate())
print(b.copy_sign(a))
"""
"""
a=decimal.Decimal(1000)
b=decimal.Decimal(1111)
print(a.logical_and(b))
print(a.logical_or(b))
print(a.logical_xor(b))
print(a.logical_invert())
"""
"""
a=decimal.Decimal(96.48)
print(a.next_plus())
print(a.next_minus())
"""
"""
a=decimal.Decimal(10.23)
b=decimal.Decimal(16.320000)
print(a.next_toward(b))
print(b.normalize())
"""
a=decimal.Decimal(2343509394029424234334563465)
print(a.rotate(-2))
print(a.shift(2))







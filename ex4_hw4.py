import math as m
from scipy.stats import f

nA   = 10
VarA = 1.25
nB   = 8
VarB = 0.28
a    = 0.1


F_test   = VarA / VarB
quantile = f.ppf(1 - a / 2, nA - 1, nB - 1)

print(f"F = {F_test}")
print(f"The critical region is the ({quantile}, +inf)")


if F_test > abs(quantile) :
    print("The t value is into the critical region.")
    print(f"Therefore, A and B has the same quality with significance level a = {a}")
else:
    print("The t value is out of the critical region.")
    print(f"A and B has not the same quality with significance level a = {a}")
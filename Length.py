import matplotlib.pyplot as plt
import math
a_in = float(input('a >> '))
b_in = float(input('b >> '))
p = int(input('p >> '))

func_1 = lambda x: math.cos(x) # cos(x)
func_2 = lambda x: math.cos(x) + 0.1*x**2
func_3 = lambda x: -(math.tanh(x-math.pi/2))
func_4 = lambda x: -0.2 * (x-math.pi)**3 + 0.5*(x-math.pi)**2 + 1


def func_curve_len(func, a, b, eps):
    global X
    global Y
    X = []
    Y = []
    x = a
    len_f = 0
    p = pow(10, -eps)
    while x < b:
        len_f += math.sqrt((func(x-p)-func(x))**2 + p ** 2)
        X.append(x)
        Y.append(func(x))
        x += p
    x = b
    len_f += math.sqrt((func(x - p) - func(x))**2 + p ** 2)
    return len_f


print(f'{func_curve_len(func_1, a_in, b_in, p):.3f}')
Y1 = Y
print(f'{func_curve_len(func_2, a_in, b_in, p):.3f}')
Y2 = Y
print(f'{func_curve_len(func_3, a_in, b_in, p):.3f}')
Y3 = Y
print(f'{func_curve_len(func_4, a_in, b_in, p):.3f}')
Y4 = Y
plt.plot(X, Y1)
plt.plot(X, Y2)
plt.plot(X, Y3)
plt.plot(X, Y4)
plt.show()
# plt.plot(X, Y)
# plt.show()

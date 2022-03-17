import numpy as np


def f(x):
    assert len(np.shape(x)) == 2 and np.shape(x)[0] == 2
    x = np.reshape(x, newshape=(2,))
    return 100 * (x[1] - x[0] ** 2) ** 2 + (1 - x[0]) ** 2


def nabla_f(x):
    assert len(np.shape(x)) == 2 and np.shape(x)[0] == 2
    x = np.reshape(x, newshape=(2,))
    nabla_f_x1 = -400 * x[0] * (x[1] - x[0] ** 2) + 2 * (x[0] - 1)
    nabla_f_x2 = 200 * (x[1] - x[0] ** 2)
    return np.array([nabla_f_x1, nabla_f_x2]).reshape(-1, 1)


def armijo(x, d):
    assert len(np.shape(x)) == 2 and np.shape(x)[0] == 2
    assert len(np.shape(d)) == 2 and np.shape(d)[0] == 2

    c1 = 1e-3
    gamma = 0.9
    alpha = 1

    while f(x + alpha * d) > f(x) + c1 * alpha * np.dot(nabla_f(x).T, d):
        alpha = gamma * alpha
    return alpha


if __name__ == '__main__':
    x = np.array([-1, 1]).reshape(-1, 1)
    d = np.array([1, 1]).reshape(-1, 1)
    print(armijo(x, d))

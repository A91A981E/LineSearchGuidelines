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


def goldstein(x, d):
    assert len(np.shape(x)) == 2 and np.shape(x)[0] == 2
    assert len(np.shape(d)) == 2 and np.shape(d)[0] == 2

    a = 0
    b = np.inf
    alpha = 1
    c1 = 0.1  # 可接受系数
    c2 = 1 - c1
    beta = 2  # 试探点系数

    while np.fabs(a - b) > 1e-5:
        if f(x + alpha * d) <= f(x) + c1 * alpha * np.dot(nabla_f(x).T, d):
            if f(x + alpha * d) >= f(x) + c2 * alpha * np.dot(nabla_f(x).T, d):
                break
            else:
                a = alpha
                # alpha = (a + b) / 2
                if b < np.inf:
                    alpha = (a + b) / 2
                else:
                    alpha = beta * alpha
        else:
            b = alpha
            alpha = (a + b) / 2

    return alpha


if __name__ == '__main__':
    x = np.array([-1, 1]).reshape(-1, 1)
    d = np.array([1, 1]).reshape(-1, 1)
    print(f(x))
    print(goldstein(x, d))

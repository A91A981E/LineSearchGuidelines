# Line Search Guidelines

Three Line Search Guidelines are included in this repo, Armijo, Goldstein and Wolfe respectively. Python version implementation.

## Armijo

Let $d^k$ refers to a direction of descent in $x^k$, if:
$$
f(x^k + \alpha d^k)\leq f(x^k) + c_1\alpha\nabla f(x^k)^\text Td^k
$$
then we said step length $\alpha$ satisfies **Armijo** Guidelines.



## Goldstein 

Let $d^k$ refers to a direction of descent in $x^k$, if:
$$
f(x^k + \alpha d^k)\leq f(x^k) + c\alpha\nabla f(x^k)^\text Td^k\\
f(x^k + \alpha d^k)\geq f(x^k) + (1-c)\alpha\nabla f(x^k)^\text Td^k
$$
then we said step length $\alpha$ satisfies **Goldstein** Guidelines, while $c\in(0, \frac12)$.



## Wolfe

Let $d^k$ refers to a direction of descent in $x^k$, if:
$$
f(x^k + \alpha d^k)\leq f(x^k) + c_1\alpha\nabla f(x^k)^\text Td^k\\
\nabla f(x^k+\alpha d^k)^\text Td^k\geq c_2\nabla f(x^k)^\text T d^k
$$
then we said step length $\alpha$ satisfies **Wolfe** Guidelines, while $c_1, c_2\in(0, \frac12)$ and $c_1<c_2$.

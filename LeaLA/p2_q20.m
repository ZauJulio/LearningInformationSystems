clc;
clear;

A = [
    0 1 1 1;
    1 0 1 1;
    1 1 0 1;
    1 1 1 0;
];

det(A)
A^-1

A = [
    0 1 1 1 1;
    1 0 1 1 1;
    1 1 0 1 1;
    1 1 1 0 1;
    1 1 1 1 0;
];

det(A)
A^-1

A = [
    0 1 1 1 1 1;
    1 0 1 1 1 1;
    1 1 0 1 1 1;
    1 1 1 0 1 1;
    1 1 1 1 0 1;
    1 1 1 1 1 0;
];

det(A)
A^-1

A = [
    0 1 1 1 1 1 1;
    1 0 1 1 1 1 1;
    1 1 0 1 1 1 1;
    1 1 1 0 1 1 1;
    1 1 1 1 0 1 1;
    1 1 1 1 1 0 1;
    1 1 1 1 1 1 0;
];

det(A)
A^-1

% A determinante dessa matriz é igual ao seu grau,
% com sinal trocado caso a divisão do grau por 2 não seja exata.

% Toda matriz A(n x n) elevada  a -1, assume valores
% correspondentes a subtração de 1/n dos valores.
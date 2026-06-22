clc;
clear;

% A.

A = [
    5 1 2  2   0;
    3 3 2 -1 -12;
    8 4 4 -5  12;
    2 1 1  0  -2;
];

B = A(:,[1,2, 4])


rref(A)

% As colunas de variáveis livres sempre podem ser escritas
% como uma combinação linear das colunas pivô, logo o sistema
% possui infinitas de soluções.

% B. Null space span A

null(A)

% C.


% Injetora


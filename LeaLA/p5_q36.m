clc;
clear;

J = randi([0,9], 6, 4);
K = randi([0,9], 4, 7);

A = J*K

rA = rref(A)

C = A(:,[1, 2, 3, 4]) % Col A - Colunas com pivô
N = null(A) % Null A
R = rA([1, 2, 3, 4],:) % Row A - Linhas não nulas

% B)

M = null(transpose(A))
S = [transpose(R), N]
T = [C M]


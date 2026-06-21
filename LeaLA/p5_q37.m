clc;
clear;

A = [
     7 -9 -4  5  3 -3 -7;
    -4  6  7 -2 -6 -5  5;
     5 -7 -6  5 -6  2  8;
    -3  5  8 -1 -7 -4  8;
     6 -8 -5  4  4  9  3; 
];


format rat

rA = rref(A)

C = A(:,[1, 2, 4, 6]); % Col A - Colunas com pivô
R = rA([1, 2, 3, 4],:); % Row A - Linhas não nulas


C * R % = matriz original
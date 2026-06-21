clc;
clear;

w = [
    1;
    2;
    1;
    0;
];

A = [
    -8  5 -2  0;
    -5  2  1 -2;
    10 -8  6 -3;
     3 -2  1  0;
];

B = [A, w]

rref(B)

A * w

% A * w = espaço nulo
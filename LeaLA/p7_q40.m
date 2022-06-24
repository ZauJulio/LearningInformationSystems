clc
clear
% questãoa 40 pagina 7
a = [9 43 5 6 -1;
     14 15 -7 -5 -4;
      -8 -6 12 -5 -9;
      -5 -6 -4 9 8;
      13 14 15 3 11]

x = [0;0;0;0;0]

ax =[a x]
rref(ax)
%é injetora pois possui apenas uma solução

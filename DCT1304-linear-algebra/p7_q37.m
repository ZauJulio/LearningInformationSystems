clc
clear
% questãoa 37 pagina 7
a = [-5 6 -5 -6;
      8 3 -3 8;
      2 9 5 -12;
      -3 2 7 -12]

x = [0;0;0;0]

ax =[a x]
rref(ax)
%Não vai ser injetora pós possui várias soluções

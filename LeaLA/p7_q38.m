clc
clear
% questãoa 38 pagina 7
a = [-7 5 9 -9;
      5 6 4 -4;
      4 8 0 7;
      -6 -6  6 5]

x = [0;0;0;0]

ax =[a x]
rref(ax)
%É injetora pois possui uma única solução

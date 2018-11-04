clear;
clc;
A = [3 0 0 0 ];
for i = [0:1:24]
    A = [A ; 3  8+4*i 4*i+9 4*i+10 ]
    A = [A ; 3  9+4*i 4*i+10 4*i+11 ]
end
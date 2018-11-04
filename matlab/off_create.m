clear;
clc;

cnt = 0;

Point = [ 0 0 0 ]

for j = [1:1:60] 
    cnt = cnt + 1;
    
    Point = [ Point ; -0.030 -0.0300 -0.030+0.001*j];
    Point = [ Point ;  0.030 -0.0300  -0.030+0.001*j];
    Point = [ Point ; -0.030  0.0400  -0.030+0.001*j];
    Point = [ Point ;  0.030  0.0400 -0.030+0.001*j];
    
end
    


A = [3 0 0 0 ];
for q = [0:1:59]
    A = [A ; 3  8+4*q 4*q+9 4*q+10 ];
    A = [A ; 3  9+4*q 4*q+10 4*q+11 ];
end
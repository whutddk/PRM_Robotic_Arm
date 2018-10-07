% 安诺6轴机械臂建模
% 武汉理工大学
% 李锐戈

clc;
clear;

Pb = [1,0,0,0;  0,1,0,0;    0,0,1,0;    0,0,0,1];

theta1 = pi/2;
theta2 = pi/2;

Ts_b = [cos(theta1) ,-sin(theta1),0,0;  sin(theta1),cos(theta1),0,0;    0,0,1,0;  0,0,0,1];
Ta_s = [cos(theta2),0,sin(theta2),0;    0,1,0,0;    -sin(theta2),0,cos(theta2),264;  0,0,0,1];
Te_a = [1,0,0,0;    0,1,0,0;    0,0,1,225;    0,0,0,1];

Pb*Ts_b* Ta_s*Te_a


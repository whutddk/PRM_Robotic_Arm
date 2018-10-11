% 安诺6轴机械臂建模
% 武汉理工大学
% 李锐戈

clc;
clear;

%aim point

AIM_X = 100;
AIM_Y = -100;
AIM_Z = 200;

%syms AIM_X AIM_Y AIM_Z;

TB_tail =[1,0,0,AIM_X;  0,1,0,AIM_Y;  0,0,1,AIM_Z;  0,0,0,1]; 

%tool_x = 0;
%tool_y = 0;
%tool_z = 14;

syms tool_x tool_y tool_z;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%DH_TAB = [ 0,0,0,theta1;    -pi/2,0,0,theta2;   0,225,0,theta3; -pi/2,0,217.3,theta4;   pi/2,0,0,theta5;    -pi/2,0,0,theta6 ];

PB = [1,0,0,0;  0,1,0,0;    0,0,1,0;    0,0,0,1];   %固定参数

TB_0 = [1,0,0,0;    0,1,0,0;    0,0,1,264;  0,0,0,1];   %固定参数
T6_t = [1,0,0,tool_x;    0,1,0,tool_y;    0,0,1,40+tool_z;   0,0,0,1];    %固定参数
R6_T = T6_t(1:3,1:3);                                   %固定参数
RT_6 = R6_T';                                           %固定参数

T0_B = [1,0,0,0;    0,1,0,0;    0,0,1,-264; 0,0,0,1];   %固定参数

Ttail_6 = [1,0,0,0; 0,1,0,0;    0,0,1,-54;    0,0,0,1]; %固定参数
%Ttail_6 = [ RT_6, -RT_6 * T6_t(1:3,4);0,0,0,0 ];

T0_6 = T0_B * TB_tail * Ttail_6;

P06 = T0_6(:,4);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
theta1_result = atan( (AIM_Y) / (AIM_X) );


SIN_THETA3 =  (225^2 +  217.3^2 - (AIM_X)^2 - (AIM_Y)^2 -  (AIM_Z - 318)^2 ) / ( 2*225*217.3 );

theta3_result = asin(SIN_THETA3);

%如何判定？
u = (217.3 * sin(theta3_result) - 225) / ((AIM_Z - 318) - 217.3  * cos(theta3_result)) - sqrt( ((217.3*sin(theta3_result) -225)  / ( (AIM_Z - 318) - 217.3 * cos(theta3_result)))^2 - (((AIM_Z - 318)+217.3*cos( theta3_result ))/((AIM_Z - 318)-217.3*cos(theta3_result))) );

theta2_result = atan(u)  * 2 ;



T01 = [cos(theta1_result),-sin(theta1_result),0,0;    sin(theta1_result),cos(theta1_result),0,0;                    0,0,1,0;                          0,0,0,1];
T12 = [cos(theta2_result),-sin(theta2_result),0,0;	0,0,1,0;    -sin(theta2_result),-cos(theta2_result),0,0;          0,0,0,1];
T23 = [cos(theta3_result),-sin(theta3_result),0,225;  sin(theta3_result),cos(theta3_result),0,0;                 	0,0,1,0;                          0,0,0,1];

%验算前几点
%P6_0 =T01 * T12 * T23 * [0;217.3;0;1]
syms theta1 theta2 theta3;

T01 = [cos(theta1),-sin(theta1),0,0;    sin(theta1),cos(theta1),0,0;                    0,0,1,0;                          0,0,0,1];
T12 = [cos(theta2),-sin(theta2),0,0;	0,0,1,0;    -sin(theta2),-cos(theta2),0,0;          0,0,0,1];
T23 = [cos(theta3),-sin(theta3),0,225;  sin(theta3),cos(theta3),0,0;                 	0,0,1,0;                          0,0,0,1];


T0_3 = T01 * T12 * T23;
R0_3 = T0_3(1:3,1:3);

R3_0 = R0_3';

%R3_0 =  
%[ cos(theta1)*cos(theta2)*cos(theta3) - cos(theta1)*sin(theta2)*sin(theta3)     ,cos(theta2)*cos(theta3)*sin(theta1) - sin(theta1)*sin(theta2)*sin(theta3)      , - cos(theta2)*sin(theta3) - cos(theta3)*sin(theta2)]
%[- cos(theta1)*cos(theta2)*sin(theta3) - cos(theta1)*cos(theta3)*sin(theta2)    , - cos(theta2)*sin(theta1)*sin(theta3) - cos(theta3)*sin(theta1)*sin(theta2)   ,  sin(theta2)*sin(theta3) - cos(theta2)*cos(theta3)]
%[-sin(theta1)                                                                   ,     cos(theta1)                                                               ,            0]

%默认单位方向
%R0_6 = T0_6(1:3,1:3)

%R3_6 = R3_0 * R0_6;


syms theta4  theta5 theta6;

R34 = [cos(theta4),-sin(theta4),0;  sin(theta4),cos(theta4),0;  0,0,1];
R45 = [cos(theta5),0,sin(theta5);    0,1,0;  -sin(theta5),0,cos(theta5)];
R56 = [cos(theta6),-sin(theta6),0;	sin(theta6),cos(theta6),0;	0,0,1];

%R34*R45 *R56 = 
%[ cos(theta4)*cos(theta5)*cos(theta6) - sin(theta4)*sin(theta6), - cos(theta6)*sin(theta4) - cos(theta4)*cos(theta5)*sin(theta6), cos(theta4)*sin(theta5)]
%[ cos(theta4)*sin(theta6) + cos(theta5)*cos(theta6)*sin(theta4),   cos(theta4)*cos(theta6) - cos(theta5)*sin(theta4)*sin(theta6), sin(theta4)*sin(theta5)]
%[                                      -cos(theta6)*sin(theta5),                                         sin(theta5)*sin(theta6),             cos(theta5)]

%得cos(theta5) = 0
%  ( R3_6(3,2) ) / ( R3_6(3,1) ) )   =  cos(theta1) / sin(theta1)
% R3_6(2,3) /  R3_6(1,3) = sin(theta2)*sin(theta3) -
% cos(theta2)*cos(theta3)       /    - cos(theta2)*sin(theta3) - cos(theta3)*sin(theta2)



%theta5_result = acos(  R3_6(3,3));
theta5_result = pi / 2;
theta6_result = atan( cos(theta1_result) / sin(theta1_result) );
theta4_result = atan ( ( sin(theta2_result)*sin(theta3_result) -  cos(theta2_result)*cos(theta3_result) )      /   ( - cos(theta2_result)*sin(theta3_result) - cos(theta3_result)*sin(theta2_result) ) );



%%%验算

TB_0 = [1,0,0,0;    0,1,0,0;    0,0,1,264;  0,0,0,1];
T6_t = [1,0,0,0;    0,1,0,0;    0,0,1,40+14;   0,0,0,1];
T01 = [cos(theta1_result),-sin(theta1_result),0,0;    sin(theta1_result),cos(theta1_result),0,0;                    0,0,1,0;                          0,0,0,1];
T12 = [cos(theta2_result),-sin(theta2_result),0,0;	0,0,1,0;    -sin(theta2_result),-cos(theta2_result),0,0;          0,0,0,1];
T23 = [cos(theta3_result),-sin(theta3_result),0,225;  sin(theta3_result),cos(theta3_result),0,0;                 	0,0,1,0;                          0,0,0,1];
T34 = [cos(theta4_result),-sin(theta4_result),0,0;    0,0,1,217.3;    -sin(theta4_result),-cos(theta4_result),0,0;      0,0,0,1];
T45 = [cos(theta5_result),-sin(theta5_result),0,0;    0,0,-1,0;    sin(theta5_result),cos(theta5_result),0,0;          0,0,0,1];
T56 = [cos(theta6_result),-sin(theta6_result),0,0;    0,0,1,0;    -sin(theta6_result),-cos(theta6_result),0,0;          0,0,0,1];

P0_6 =  T01 * T12 * T23 * T34 * T45 * T56;

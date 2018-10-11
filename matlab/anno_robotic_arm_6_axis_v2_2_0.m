% 安诺6轴机械臂建模
% 武汉理工大学
% 李锐戈

clc;
clear;

%aim point
TB_tail =[1,0,0,100;  0,1,0,-100;  0,0,1,200;  0,0,0,1]; 

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%DH_TAB = [ 0,0,0,theta1;    -pi/2,0,0,theta2;   0,225,0,theta3; -pi/2,0,217.3,theta4;   pi/2,0,0,theta5;    -pi/2,0,0,theta6 ];

PB = [1,0,0,0;  0,1,0,0;    0,0,1,0;    0,0,0,1];

TB_0 = [1,0,0,0;    0,1,0,0;    0,0,1,264;  0,0,0,1];
T6_t = [1,0,0,0;    0,1,0,0;    0,0,1,40+14;   0,0,0,1];
R6_T = T6_t(1:3,1:3);
RT_6 = R6_T';

T0_B = [1,0,0,0;    0,1,0,0;    0,0,1,-264; 0,0,0,1];

Ttail_6 = [1,0,0,0; 0,1,0,0;    0,0,1,-54;    0,0,0,1];
%Ttail_6 = [ RT_6, -RT_6 * T6_t(1:3,4);0,0,0,0 ];

T0_6 = T0_B * TB_tail * Ttail_6;

P06 = T0_6(:,4);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
theta1_result = atan(P06(2,1)/P06(1,1));


SIN_THETA3 =  (225^2 +  217.3^2 - (P06(1,1))^2 - (P06(2,1))^2 - (P06(3,1))^2 ) / ( 2*225*217.3 );

theta3_result = asin(SIN_THETA3);

%如何判定？
u = (217.3 * sin(theta3_result) - 225) / (P06(3,1) - 217.3  * cos(theta3_result)) - sqrt( ((217.3*sin(theta3_result) -225)  / ( P06(3,1) - 217.3 * cos(theta3_result)))^2 - ((P06(3,1)+217.3*cos( theta3_result ))/(P06(3,1)-217.3*cos(theta3_result))) );

theta2_result = atan(u)  * 2 ;



T01 = [cos(theta1_result),-sin(theta1_result),0,0;    sin(theta1_result),cos(theta1_result),0,0;                    0,0,1,0;                          0,0,0,1];
T12 = [cos(theta2_result),-sin(theta2_result),0,0;	0,0,1,0;    -sin(theta2_result),-cos(theta2_result),0,0;          0,0,0,1];
T23 = [cos(theta3_result),-sin(theta3_result),0,225;  sin(theta3_result),cos(theta3_result),0,0;                 	0,0,1,0;                          0,0,0,1];

%验算前几点
%P6_0 =T01 * T12 * T23 * [0;217.3;0;1]

T0_3 = T01 * T12 *T23;
R0_6 = T0_6(1:3,1:3);
R0_3 = T0_3(1:3,1:3);
R3_0 = R0_3';
R3_6 = R3_0 * R0_6;

theta5_result = acos(  R3_6(3,3));

R45 = [cos(theta5_result),0,sin(theta5_result);    0,1,0;  -sin(theta5_result),0,cos(theta5_result)];

theta6_result = -atan( ( R3_6(3,2) ) / ( R3_6(3,1) ) );
theta4_result = atan ( R3_6(2,3) /  R3_6(1,3) );



%%%验算

TB_0 = [1,0,0,0;    0,1,0,0;    0,0,1,264;  0,0,0,1];
T6_t = [1,0,0,0;    0,1,0,0;    0,0,1,40+14;   0,0,0,1];
T01 = [cos(theta1_result),-sin(theta1_result),0,0;    sin(theta1_result),cos(theta1_result),0,0;                    0,0,1,0;                          0,0,0,1];
T12 = [cos(theta2_result),-sin(theta2_result),0,0;	0,0,1,0;    -sin(theta2_result),-cos(theta2_result),0,0;          0,0,0,1];
T23 = [cos(theta3_result),-sin(theta3_result),0,225;  sin(theta3_result),cos(theta3_result),0,0;                 	0,0,1,0;                          0,0,0,1];
T34 = [cos(theta4_result),-sin(theta4_result),0,0;    0,0,1,217.3;    -sin(theta4_result),-cos(theta4_result),0,0;      0,0,0,1];
T45 = [cos(theta5_result),-sin(theta5_result),0,0;    0,0,-1,0;    sin(theta5_result),cos(theta5_result),0,0;          0,0,0,1];
T56 = [cos(theta6_result),-sin(theta6_result),0,0;    0,0,1,0;    -sin(theta6_result),-cos(theta6_result),0,0;          0,0,0,1];

P0_6 =  T01 * T12 * T23 * T34 * T45 * T56

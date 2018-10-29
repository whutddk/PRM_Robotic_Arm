% 安诺6轴机械臂PRM算法EDGE查找表生成
% 武汉理工大学
% 李锐戈
clear;
clc;

precision = 5;
space_length = 1000;
edge_require = 1024;

Pose = [0,0,0,0,0,0];
Truetable = [false(32768,1)];
Pose_sum = 1;


edge_cnt = 0;
X = 0;
Y = 0;
Z = 0;

%当edge_cnt 《 edge_require
%while (edge_cnt < edge_require)
    %随机生成6维点
    shoulderAngle = randi ([-27000,9000])/100;
    armAngle = randi ([0,18000])/100;
    elbowAngle = randi ([0,18000])/100;
    wristAngle = randi ([-18000,18000])/100;
    fingerAngle =  randi ([-9000,9000])/100;
    toolAngle = randi ([-18000,18000])/100;
    
    endPose = [shoulderAngle armAngle elbowAngle wristAngle fingerAngle toolAngle];
    Pose = [Pose;endPose];
    
    Pose_sum = Pose_sum+ 1;
    
    %当检测数小于姿态树
    Pose_cnt = 1;
    while( Pose_cnt < Pose_sum  )
        tab = [false(32768,1)];
                        %检测6维点和当前的前面所有点的距离，不算自己
        startPose = Pose(Pose_cnt ,:);
        
        %6维步进角，用1K步进
        shorderDis = (startPose(1) - endPose(1)) / 1000;
        armDis = (startPose(2) - endPose(2)) / 1000;
        elbowDis = (startPose(3) - endPose(3)) / 1000;
        wristDis = (startPose(4) - endPose(4)) / 1000;
        fingerDis = (startPose(5) - endPose(5)) / 1000;
        toolDis = (startPose(6) - endPose(6)) / 1000;
        
        for ( i = 1:1:1000 )
            
            
        end
        
        
        
                        %满足要求距离要求（可以不管，因为是查找表，可以全连接）
    %开始XYZ矩阵清零机械角度步进。
    %开始遍历XYZ栅格，算距离，符合的栅格将其XYZ矩阵标1，
    %所有栅格的集（矩阵）对应一条路径（EDGE）编号，及首尾节点信息
    %根据XYZ矩阵打出1*32786布林矩阵。
    
    
    Pose_cnt = Pose_cnt + 1;
    edge_cnt = edge_cnt + 1;
    end
%end

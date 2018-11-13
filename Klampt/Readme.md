# 脚本备注

----------------------------
## 产生碰撞模型
* 主函数main.PY
    - 需要带空list的edge.json
    - anno_check.xml 地图模型及相关障碍机器人模型（KLAMPT）
    - 实际psoe.json
    - 实际edgeIndex.json
* 预先使用create_Pose_edge.PY生成Pose 和edge对，
    - 以方便断点，
    - 及edge约束
    - 后期代码确认Pose点位置，实际路径

------------------------

## 产生真值表
* creatTT。py 产生空的真值表
    - 产生trueTable.json空表
* checkoutTT.py 根据上一层的edge.json产生实际真值表
    - 其实是矩阵转置

----------------------------

## 产生Verilog
*  createLUTVerilog.py产生可以直接用的verilog
    - prm_LUT.v 为生成的代码
    - 采用分开不压缩case查找表，综合速度快，资源消耗小

----------------------------------






-----------------------------------


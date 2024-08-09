import numpy as np
from scipy.optimize import minimize

# 定义机械臂的连杆参数（标准DH参数）
d = [600, 0, 0, 1200, 0, 0]
a = [0, 300, 1200, 300, 0, 0]
alpha = [0, -np.pi/2, 0, -np.pi/2, -np.pi/2, -np.pi/2]

# 定义前向运动学函数（标准DH）
def fkine(q, initial_q):
    T = np.eye(4)
    for i in range(len(q)):
        T = T @ np.array([
            [np.cos(q[i] + initial_q[i]), -np.sin(q[i] + initial_q[i])*np.cos(alpha[i]), np.sin(q[i] + initial_q[i])*np.sin(alpha[i]), a[i]*np.cos(q[i] + initial_q[i])],
            [np.sin(q[i] + initial_q[i]), np.cos(q[i] + initial_q[i])*np.cos(alpha[i]), -np.cos(q[i] + initial_q[i])*np.sin(alpha[i]), a[i]*np.sin(q[i] + initial_q[i])],
            [0, np.sin(alpha[i]), np.cos(alpha[i]), d[i]],
            [0, 0, 0, 1]
        ])
    return T

# 定义目标位置
target_pos = np.array([1500, 1200, 200])

# 定义目标函数，即机械臂末端与目标点的距离的平方
def distance_func(q, initial_q):
    T = fkine(q, initial_q)
    end_effector_pos = T[:3, 3]
    return np.linalg.norm(end_effector_pos - target_pos)

# 初始猜测的关节角度
q0 = np.zeros(6)

# 初始状态
initial_q = np.array([0, -np.pi/2, 0, np.pi, -np.pi/2, 0])

# 设定优化参数和约束（关节角度限制，已转换为弧度，相对于初始状态）
bounds = [(np.radians(lim[0]) + np.radians(initial_q[i]), np.radians(lim[1] )+ np.radians(initial_q[i])) for i, lim in enumerate([
    [-160, 160],
    [-150, 15],
    [-200, 80],
    [-180, 180],
    [-120, 120],
    [-180, 180]
])]

# 使用 SLSQP 优化算法
result_slsqp = minimize(lambda q: distance_func(q, initial_q), q0, method='SLSQP', bounds=bounds)
q_opt_slsqp = result_slsqp.x
fval_slsqp = result_slsqp.fun

# 使用 L-BFGS-B 优化算法
result_lbfgs = minimize(lambda q: distance_func(q, initial_q), q0, method='L-BFGS-B', bounds=bounds)
q_opt_lbfgs = result_lbfgs.x
fval_lbfgs = result_lbfgs.fun
q_opt_slsqp_deg = np.degrees(q_opt_slsqp)
q_opt_lbfgs_deg = np.degrees(q_opt_lbfgs)
# 输出优化结果
print("使用 SLSQP 优化算法的关节角度（弧度）:")
print(q_opt_slsqp)
print("使用 SLSQP 优化算法的关节角度:")
print(q_opt_slsqp_deg)
print("最小化的距离:", fval_slsqp)

print("\n使用 L-BFGS-B 优化算法的关节角度（弧度）:")
print(q_opt_lbfgs)
print("\n使用 L-BFGS-B 优化算法的关节角度:")
print(q_opt_lbfgs_deg)
print("最小化的距离:", fval_lbfgs)
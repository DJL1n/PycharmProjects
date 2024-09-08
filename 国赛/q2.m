clc; clear;
close all;

%% 精度设置
dt = 0.01; % 设置时间步长为0.01秒，用于迭代计算

%% 曲线绘制
% 定义参数
r0 = 16 * 55;  % 初始半径，单位为厘米，这里16代表圈数，55代表每圈的半径
pitch = 55;    % 螺距，单位为厘米，这里指的是圆周上相邻两点的纵向距离
k = pitch / (2 * pi);  % 计算每弧度的半径增量，用于极坐标方程中

% 生成角度向量，从0开始，逆时针旋转16圈，总共1000个点
theta = linspace(0, -16 * 2 * pi, 1000);

% 极坐标方程，计算半径r
r = r0 + k * theta;

% 将极坐标转换为笛卡尔坐标系下的x和y
x1 = r .* cos(theta);
y1 = r .* sin(theta);

%% 信息初始化
% 定义板凳把手之间的长度
L1 = 341 - 55; 
L = 220 - 55;

% 初始化龙头走过的曲线距离和板凳连起来的折线距离
Long = 0; 
sum_L = 0;

% 初始化位置和速度
v0 = 100; % 初始速度，单位为厘米/秒
r0 = 16 * 55; % 初始半径，单位为厘米
w0 = v0 / r0; % 初始角速度，通过初始速度除以初始半径计算得出

%% 路径方程
pitch = 55;  % 螺距，单位为厘米
k = pitch / (2 * pi);  % 每弧度的半径增量

%% 输出表格初始化
save = zeros(448, 301); % 初始化一个448行301列的零矩阵，用于保存计算结果

%% 状态信息初始化
N = 224; % 定义成员数量，包括龙尾前和龙尾后

% 初始化成员位置（x，y）和每个成员走过的距离S
x = r0 * ones(1, N); 
y = zeros(1, N); 
S = zeros(1, N);

% 初始化板凳间夹角alpha，线速度v_L和木板速度v_M
alpha = 2 * asin(0.5 * L / r0) * ones(1, N); 
v_L = zeros(1, N); 
v_M = zeros(1, N); 
w = zeros(1, N);

% 初始化成员位置的极坐标（角度theta和半径rho）
theta0 = 0; 
thetaN = -16 * 2 * pi;
theta = theta0 * ones(1, N); 
rho = r0 * ones(1, N);

%% 迭代过程
num = 1; % 初始化进入板凳的数量
alpha(1) = 2 * asin(0.5 * L1 / r0);
v_L(1) = v0; % 设置第一个成员的线速度为初始速度
v_M(1) = v_L(1) * cos(alpha(1)); % 计算第一个成员的木板速度
w(1) = v_L(1) / r0; % 计算第一个成员的角速度

% 开始迭代计算，时间从0到430秒
for t = 0:dt:430 
    Long = v0 * t; % 计算龙头走过的曲线距离
    
    % 判断并更新进入板凳的数量
    if (-theta(num)) >= alpha(num)
        num = num + 1;
        if num > N
            num = N; % 如果超过成员数量，设置为最大值N
        end
    end
    
    % 遍历每个成员，更新他们的位置和速度
    for i = 1:num
        % 更新成员的位置，通过减去角速度乘以时间步长来更新角度
        theta(i) = theta(i) - w(i) * dt;
        rho(i) = r0 + k * theta(i); % 更新极坐标下的半径
        
        % 更新速度
        if i == 1
            % 对第一个成员特殊处理
            alpha(i) = 2 * asin(0.5 * L1 / rho(i));
            v_L(i) = v0;
            v_M(i) = v_L(i) * cos(0.5 * alpha(i));
            w(i) = v_L(i) / rho(i);
        else
            % 对其他成员更新速度
            alpha(i) = 2 * asin(0.5 * L / rho(i));
            v_L(i) = v0;
            v_M(i) = v_M(i - 1) * cos(0.5 * alpha(i)); % 更新木板速度
            w(i) = v_L(i) / rho(i); % 更新角速度
        end
        
        % 将极坐标转换为笛卡尔坐标
        x(i) = rho(i) * cos(theta(i));
        y(i) = rho(i) * sin(theta(i));
        
        % 每隔1秒保存一次位置数据
        if mod(t, 1) == 0
            save(2 * i - 1, t + 1) = x(i);
            save(2 * i, t + 1) = y(i);
        end
    end
end

% 将保存的数据除以100并四舍五入到小数点后6位
save_6 = round(save / 100, 6);
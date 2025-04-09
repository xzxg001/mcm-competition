% clc,clear;
% % 定义样本量
% n = [20, 30, 40, 50, 60, 70, 80];
% 
% % 初始化结果矩阵
% X = zeros(length(n), 2);
% 
% % 假设比例
% p0 = 0.1;
% 
% % 显著性水平
% alpha1 = 0.05; % 单边显著性水平 0.05
% alpha2 = 0.10; % 单边显著性水平 0.10
% 
% % 计算每个样本量下的 X 值
% for i = 1:length(n)
%     ni = n(i);  % 当前样本量
% 
%     % 计算 t 分布的临界值
%     u1 = abs(tinv(alpha1, ni - 1)); % 单边显著性水平
%     u2 = abs(tinv(alpha2, ni - 1)); % 单边显著性水平
% 
%     % 计算统计量 X
%     X1 = (u1 * sqrt(p0 * (1 - p0)) / sqrt(ni) + p0) * ni;
%     X2 = (u2 * sqrt(p0 * (1 - p0)) / sqrt(ni) + p0) * ni;
% 
%     % 取整
%     X(i, 1) = floor(X1);
%     X(i, 2) = floor(X2);
% end
% 
% % 显示结果
% disp('Rounded X values for different sample sizes:');
% disp(array2table(X, 'VariableNames', {'X_0.05', 'X_0.10'}, 'RowNames', cellstr(num2str(n'))));
% 
% %%
% clc;
% clear;
% 
% % 定义样本量
% n = [20, 30, 40, 50, 60, 70, 80];
% 
% % 初始化结果矩阵
% X = zeros(length(n), 2);
% 
% % 假设比例
% p0 = 0.1;
% 
% % 显著性水平
% alpha1 = 0.05; % 单边显著性水平 0.05
% alpha2 = 0.10; % 单边显著性水平 0.10
% 
% % 计算每个样本量下的 X 值
% for i = 1:length(n)
%     ni = n(i);  % 当前样本量
% 
%     % 计算正态分布的临界值
%     u1 = norminv(1 - alpha1); % 单边显著性水平
%     u2 = norminv(1 - alpha2); % 单边显著性水平
% 
%     % 计算统计量 X
%     X1 = (u1 * sqrt(p0 * (1 - p0)) / sqrt(ni) + p0) * ni;
%     X2 = (u2 * sqrt(p0 * (1 - p0)) / sqrt(ni) + p0) * ni;
% 
%     % 取整
%     X(i, 1) = floor(X1);
%     X(i, 2) = floor(X2);
% end
% 
% % 显示结果
% disp('Rounded X values for different sample sizes:');
% disp(array2table(X, 'VariableNames', {'X_0.05', 'X_0.10'}, 'RowNames', cellstr(num2str(n'))));
% 
% 
% 
% %%
% 
% 
% clc;
% clear;
% 
% % 定义常数
% a = 0.05;   % 置信水平
% p0 = 0.1;   % 假设比例
% 
% % 定义X的范围
% X_values = 0:1:10;  % 自变量 X 从 0 到 10 的范围
% 
% % 定义一个函数以n为隐变量解方程
% n_values = zeros(size(X_values));  % 初始化n的存储空间
% 
% % 遍历每一个X值，找到相应的n
% for i = 1:length(X_values)
%     X = X_values(i);  % 当前的X值
% 
%     % 定义待求解的函数
%     fun = @(n) (tinv(a, n) * sqrt(p0 * (1 - p0)) / sqrt(n) + p0) * n - X;
% 
%     % 使用fsolve找到n值
%     n_solution = fsolve(fun, 10);  % 选择初始猜测值 10
% 
%     n_values(i) = n_solution;  % 存储求解结果
% end
% 
% % 显示结果
% disp('X values and corresponding n values:');
% disp(table(X_values', n_values', 'VariableNames', {'X', 'n'}));
% 
% % 绘制X与n的关系图
% plot(X_values, n_values, 'LineWidth', 2);
% xlabel('X');
% ylabel('n');
% title('X 与 n 的关系图');
% grid on;
% 
% %%
% clc;
% clear;
% 
% % 定义常数
% a1 = 0.05;  % 第一组置信水平
% a2 = 0.1;   % 第二组置信水平
% p0 = 0.1;   % 假设比例
% 
% % 定义X的范围
% X_values = 0:1:10;  % 自变量 X 从 0 到 10 的范围
% 
% % 初始化n的存储空间
% n_values_a1 = zeros(size(X_values));  % 置信水平为 0.05 时的 n
% n_values_a2 = zeros(size(X_values));  % 置信水平为 0.1 时的 n
% 
% % 遍历每一个X值，找到相应的n
% for i = 1:length(X_values)
%     X = X_values(i);  % 当前的X值
% 
%     % 置信水平 a = 0.05
%     fun1 = @(n) (tinv(a1, n) * sqrt(p0 * (1 - p0)) / sqrt(n) + p0) * n - X;
%     n_solution_a1 = fsolve(fun1, 10);  % 使用初始猜测值 10
%     n_values_a1(i) = n_solution_a1;  % 存储求解结果
% 
%     % 置信水平 a = 0.1
%     fun2 = @(n) (tinv(a2, n) * sqrt(p0 * (1 - p0)) / sqrt(n) + p0) * n - X;
%     n_solution_a2 = fsolve(fun2, 10);  % 使用初始猜测值 10
%     n_values_a2(i) = n_solution_a2;  % 存储求解结果
% end
% 
% % 显示结果
% disp('X values and corresponding n values for a = 0.05 and a = 0.1:');
% disp(table(X_values', n_values_a1', n_values_a2', 'VariableNames', {'X', 'n_a_0_05', 'n_a_0_1'}));
% 
% % 绘制X与n的关系图
% figure;
% plot(X_values, n_values_a1, '-o', 'LineWidth', 2, 'DisplayName', 'a = 0.05');
% hold on;
% plot(X_values, n_values_a2, '-x', 'LineWidth', 2, 'DisplayName', 'a = 0.1');
% xlabel('X');
% ylabel('n');
% title('X 与 n 的关系图（不同置信水平）');
% legend('show');
% grid on;

%% 正态分布，式子转换后 

clc;
clear;

% 定义常数
a1 = 0.05;  % 第一组置信水平
a2 = 0.1;   % 第二组置信水平
p0 = 0.1;   % 假设比例

% 计算正态分布的分位数
z1 = norminv(1 - a1 / 2);  % 对于 a = 0.05
z2 = norminv(1 - a2 / 2);  % 对于 a = 0.1

% 定义X的范围
X_values = 1:1:10;  % 自变量 X 从 0 到 10 的范围

% 初始化n的存储空间
n_values_a1 = zeros(size(X_values));  % 置信水平为 0.05 时的 n
n_values_a2 = zeros(size(X_values));  % 置信水平为 0.1 时的 n

% 遍历每一个X值，找到相应的n
for i = 1:length(X_values)
    X = X_values(i);  % 当前的X值
    
    % 置信水平 a = 0.05
    fun1 = @(n) (X - p0 * n)^2 - (z1^2 * p0 * (1 - p0) * n);
    n_solution_a1 = fsolve(fun1, 10);  % 使用初始猜测值 10
    n_values_a1(i) = n_solution_a1;  % 存储求解结果
    
    % 置信水平 a = 0.1
    fun2 = @(n) (X - p0 * n)^2 - (z2^2 * p0 * (1 - p0) * n);
    n_solution_a2 = fsolve(fun2, 10);  % 使用初始猜测值 10
    n_values_a2(i) = n_solution_a2;  % 存储求解结果
end

% 显示结果
disp('X values and corresponding n values for a = 0.05 and a = 0.1:');
disp(table(X_values', n_values_a1', n_values_a2', 'VariableNames', {'X', 'n_a_0_05', 'n_a_0_1'}));

% 绘制X与n的关系图
figure;
plot(X_values, n_values_a1, '-o', 'LineWidth', 2, 'DisplayName', 'a = 0.05');
hold on;
plot(X_values, n_values_a2, '-x', 'LineWidth', 2, 'DisplayName', 'a = 0.1');
xlabel('X');
ylabel('n');
title('X 与 n 的关系图（不同置信水平）');
legend('show');
grid on;

%% 正态分布，未转换式子
clc;
clear;

% 定义常数
a1 = 0.05;  % 第一组置信水平
a2 = 0.1;   % 第二组置信水平
p0 = 0.1;   % 假设比例

% 计算正态分布的分位数
z1 = norminv(1 - a1 / 2);  % 对于 a = 0.05
z2 = norminv(1 - a2 / 2);  % 对于 a = 0.1

% 定义X的范围
X_values = 1:1:10;  % 自变量 X 从 0 到 10 的范围

% 初始化n的存储空间
n_values_a1 = zeros(size(X_values));  % 置信水平为 0.05 时的 n
n_values_a2 = zeros(size(X_values));  % 置信水平为 0.1 时的 n

% 遍历每一个X值，找到相应的n
for i = 1:length(X_values)
    X = X_values(i);  % 当前的X值
    
    % 置信水平 a = 0.05
    fun1 = @(n) (z1 * sqrt(p0 * (1 - p0)) / sqrt(n) + p0) * n - X;
    n_solution_a1 = fsolve(fun1, 10);  % 使用初始猜测值 10
    n_values_a1(i) = n_solution_a1;  % 存储求解结果
    
    % 置信水平 a = 0.1
    fun2 = @(n) (z2 * sqrt(p0 * (1 - p0)) / sqrt(n) + p0) * n - X;
    n_solution_a2 = fsolve(fun2, 10);  % 使用初始猜测值 10
    n_values_a2(i) = n_solution_a2;  % 存储求解结果
end

% 显示结果
disp('X values and corresponding n values for a = 0.05 and a = 0.1:');
disp(table(X_values', n_values_a1', n_values_a2', 'VariableNames', {'X', 'n_a_0_05', 'n_a_0_1'}));

% 绘制X与n的关系图
figure;
plot(X_values, n_values_a1, '-o', 'LineWidth', 2, 'DisplayName', 'a = 0.05');
hold on;
plot(X_values, n_values_a2, '-x', 'LineWidth', 2, 'DisplayName', 'a = 0.1');
xlabel('X');
ylabel('n');
title('X 与 n 的关系图（不同置信水平）');
legend('show');
grid on;

%% 正态分布，未转换式子取整
clc;
clear;

% 定义常数
a1 = 0.05;  % 第一组置信水平
a2 = 0.1;   % 第二组置信水平
p0 = 0.1;   % 假设比例

% 计算正态分布的分位数
z1 = norminv(1 - a1 / 2);  % 对于 a = 0.05
z2 = norminv(1 - a2 / 2);  % 对于 a = 0.1

% 定义X的范围
X_values = 1:1:20;  % 自变量 X 从 0 到 10 的范围

% 初始化n的存储空间
n_values_a1 = zeros(size(X_values));  % 置信水平为 0.05 时的 n
n_values_a2 = zeros(size(X_values));  % 置信水平为 0.1 时的 n

% 遍历每一个X值，找到相应的n
for i = 1:length(X_values)
    X = X_values(i);  % 当前的X值
    
    % 置信水平 a = 0.05
    fun1 = @(n) (z1 * sqrt(p0 * (1 - p0)) / sqrt(n) + p0) * n - X;
    n_solution_a1 = fsolve(fun1, 10);  % 使用初始猜测值 10
    n_values_a1(i) = ceil(n_solution_a1);  % 向上取整并存储求解结果
    
    % 置信水平 a = 0.1
    fun2 = @(n) (z2 * sqrt(p0 * (1 - p0)) / sqrt(n) + p0) * n - X;
    n_solution_a2 = fsolve(fun2, 10);  % 使用初始猜测值 10
    n_values_a2(i) = ceil(n_solution_a2);  % 向上取整并存储求解结果
end

% 显示结果
disp('X values and corresponding n values for a = 0.05 and a = 0.1 (rounded up):');
disp(table(X_values', n_values_a1', n_values_a2', 'VariableNames', {'X', 'n_a_0_05', 'n_a_0_1'}));

% 绘制X与n的关系图
figure;
plot(X_values, n_values_a1, '-o', 'LineWidth', 2, 'DisplayName', 'a = 0.05');
hold on;
plot(X_values, n_values_a2, '-x', 'LineWidth', 2, 'DisplayName', 'a = 0.1');
xlabel('X');
ylabel('n');
title('X 与 n 的关系图（不同置信水平, 结果向上取整）');
legend('show');
grid on;
%% 验证
% clc,clear;

% 参数设置
total_count = 10000;  % 总体数量
defective_rate = 0.10; % 次品比例
simulation_count = 1000; % 模拟次数

% 定义 n_values
% n_values_a1 = [2, 6, 11, 17, 23, 29, 36, 42, 49, 56];
% n_values_a2 = [3, 7, 13, 19, 26, 33, 40, 47, 54, 62];
X_values = 1:20;  % 对应的X值

% 初始化结果存储
probability_a1 = zeros(size(X_values));
probability_a2 = zeros(size(X_values));

% 生成总体
total_parts = [ones(1, round(total_count * defective_rate)), zeros(1, round(total_count * (1 - defective_rate)))];
total_parts = total_parts(randperm(total_count)); % 随机打乱总体

% 模拟过程
for i = 1:length(X_values)
    X = X_values(i);
    
    % 置信水平 a = 0.05
    n_a1 = n_values_a1(i);
    count_a1 = 0;
    
    % 置信水平 a = 0.1
    n_a2 = n_values_a2(i);
    count_a2 = 0;
    
    for j = 1:simulation_count
        % 随机抽取
        sample_a1 = total_parts(1:n_a1);
        sample_a2 = total_parts(1:n_a2);
        
        % 计算次品数
        defective_count_a1 = sum(sample_a1);
        defective_count_a2 = sum(sample_a2);
        
        % 判断是否小于对应的X
        if defective_count_a1 < X
            count_a1 = count_a1 + 1;
        end
        if defective_count_a2 < X
            count_a2 = count_a2 + 1;
        end
        
        % 打乱总体以供下次模拟
        total_parts = [ones(1, round(total_count * defective_rate)), zeros(1, round(total_count * (1 - defective_rate)))];
        total_parts = total_parts(randperm(total_count));
    end
    
    % 计算概率
    probability_a1(i) = count_a1 / simulation_count;
    probability_a2(i) = count_a2 / simulation_count;
end

% 显示结果
disp('Probability of defective count being less than X for a = 0.05 and a = 0.1:');
disp(table(X_values', probability_a1', probability_a2', 'VariableNames', {'X', 'P_a_0_05', 'P_a_0_1'}));

% 绘制结果图
figure;
plot(X_values, probability_a1, '-o', 'LineWidth', 2, 'DisplayName', 'a = 0.05');
hold on;
plot(X_values, probability_a2, '-x', 'LineWidth', 2, 'DisplayName', 'a = 0.1');
xlabel('X');
ylabel('R');
title('最大容忍次数X与R的关系图');
legend('show');
grid on;

%%
% 参数设置
N = 10000;  % 样本总数
n_simulations = 100000;  % 模拟次数
sample_size = 10000;  % 每次抽样的样本数
defect_rate = 0.05;  % 次品率

% 生成10000个样品，次品率为10%
sample = rand(N, 1) < defect_rate;

% 模拟抽样100000次，每次抽样10000个样本并计算次品率
pro = zeros(n_simulations, 1);
for i = 1:n_simulations
    cnt = sum(sample(randi([1 N], sample_size, 1)));  % 随机抽样
    pro(i) = cnt / sample_size;  % 计算次品率
end

% 对次品率数据进行排序
pro = sort(pro);

% 计算95%置信区间
lower_bound = pro(round(n_simulations * 0.025));
upper_bound = pro(round(n_simulations * 0.975));

fprintf('95%% 置信区间的下分位点: %.4f\n', lower_bound);
fprintf('95%% 置信区间的上分位点: %.4f\n', upper_bound);

% 绘制次品率的概率分布
figure;
histogram(pro, 100, 'Normalization', 'pdf');
hold on;
% 绘制核密度估计
[f, xi] = ksdensity(pro);
plot(xi, f, 'LineWidth', 2);
title('10000个随机样本次品率的概率分布', 'FontSize', 16);
xlabel('次品率', 'FontSize', 14);
ylabel('概率密度', 'FontSize', 14);
grid on;
hold off;


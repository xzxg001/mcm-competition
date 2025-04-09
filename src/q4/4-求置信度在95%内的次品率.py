import math
import random
import matplotlib.pyplot as plt
import seaborn as sns

N = 10000
n_defect = 1000

sample = []

# 生成10000个样品，次品率为10%
for i in range(N):
    if random.random() < 0.2:
        sample.append(1)
    else:
        sample.append(0)

pro = []
# 模拟抽样100000次，每次抽10000个样本并计算次品率
for i in range(100000):
    cnt = 0
    for j in range(1000):
        index = random.randint(0, N-1)
        if sample[index]:
            cnt += 1
    pro.append(cnt / 1000)

# 排序次品率列表
pro = sorted(pro)

# 输出样本中的第250个和第99750个次品率值
# print(pro[250], pro[100000-250])
# 计算95%置信区间的上下限
lower_bound = pro[int(100000 * 0.025)]
upper_bound = pro[int(100000 * 0.975)]

print(f"95% 置信区间的下分位点: {lower_bound}")
print(f"95% 置信区间的上分位点: {upper_bound}")
# 使用Seaborn的kdeplot绘制平滑核密度估计图，同时美化图形
plt.figure(figsize=(10, 6))
sns.histplot(pro, bins=100, kde=True, color='b', stat="density", linewidth=0)
plt.title("10000个随机样本次品率的概率分布", fontsize=16)
plt.xlabel("次品率", fontsize=14)
plt.ylabel("概率", fontsize=14)
plt.grid(True)
plt.show()

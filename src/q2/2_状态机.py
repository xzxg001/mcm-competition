import random
from math import ceil

parameters = [
    [0.1, 4, 2, 0.1, 18, 3, 0.1, 6, 3, 56, 6, 5],
    [0.2, 4, 2, 0.2, 18, 3, 0.2, 6, 3, 56, 6, 5],
    [0.1, 4, 2, 0.1, 18, 3, 0.1, 6, 3, 56, 30, 5],
    [0.2, 4, 1, 0.2, 18, 1, 0.2, 6, 2, 56, 30, 5],
    [0.15, 4, 8, 0.15, 18, 1, 0.1, 6, 2, 56, 10, 5],
    [0.05, 4, 2, 0.05, 18, 3, 0.05, 6, 3, 56, 10, 40]
]
N=100
# a1 = 0.2
# r1 = 4
# k1 = 1
# a2 = 0.2
# r2 = 18
# k2 = 1
# a3 = 0.2
# r3 = 6
# k3 = 2
# price = 56
# change = 30
# dismantle = 5

def l000(A):
    cost, profit = 0, 0
    cost += A*r3  # 装配成本
    hege = A*(1-a1)**2*(1-a3)   # 合格
    buhege = A - hege    # 不合格
    profit += hege*price    # 获利
    cost += buhege*change   # 退换损失
    return profit - cost - A*(r1+r2)


def l010(A):
    cost, profit = 0, 0
    cost += A*r3  # 装配成本
    cost += A*k3  # 检验成本
    hege = A*(1-a1)**2*(1-a3)   # 合格
    buhege = A - hege    # 不合格
    profit += hege*price    # 获利
    return profit - cost - A*(r1+r2)


def l100(A):
    cost, profit = 0, 0
    cost += A*(k1+k2)   # 检测零件成本
    A = A*(1-a1)
    cost += A*r3  # 装配成本
    hege = A*(1-a3)     # 合格
    buhege = A - hege
    profit = hege*price
    cost += buhege*change
    return profit - cost - A*(r1+r2)


def l110(A):
    cost, profit = 0, 0
    cost += A*(k1+k2)  # 检验成本
    A = A-A*a1
    cost += A*r3  # 装配成本
    cost += A*k3  # 检验成本
    hege = A*(1-a3)   # 合格
    buhege = A - hege    # 不合格
    profit += hege*price    # 获利
    return profit - cost - A*(r1+r2)

def l011(A):  # 0 1 1
    global a1, a2, a3
    Cost = 0
    Profit = 0
    cost = 0
    profit = 0
    error = A * a1  # 本身存在的不合格数
    Acount = A
    while 1:
        cost += A * (r3 + k3)  # 装配成本r+检测成本k
        Cost += cost
        hege = A * (1 - a1) * (1 - a2) * (1 - a3)  # 合格品数量
        buhege = A - hege  # 不合格数量
        profit += hege * price  # 获利
        Profit += profit
        # 对下一轮推测，是否进行下一循环
        a1 = error / buhege  # 换概率
        a2 = a1
        lasthege = buhege * (1 - a1) * (1 - a2) * (1 - a3)  # 下一轮合格品数量
        lastprofit = lasthege * price  # 下一轮预计获利
        lastcost = buhege * dismantle + buhege * r3 + buhege * k3
        if lastprofit < lastcost:
            return Profit - Cost - (r1 + r2) * Acount  # 最后的利润
        Cost += buhege * dismantle
        cost, profit = 0, 0
        A = buhege  # 用于下一轮
        if buhege <= 1:
            return Profit - Cost - (r1 + r2) * Acount  # 最后的利润


# print(l011(100))


def l001(A):  # 0 0 1
    global a1, a2, a3
    Cost = 0
    Profit = 0
    cost = 0
    profit = 0
    error = A * a1  # 本身存在的不合格数
    Acount = A
    while 1:
        cost += A * r3  # 装配成本
        
        hege = A * (1 - a1) * (1 - a2) * (1 - a3)  # 合格品数量
        buhege = A - hege  # 不合格数量
        profit += hege * price  # 获利
        Profit += profit  # 更新获利
        cost += buhege * change  # 不合格品的调换价
        Cost += cost  # 更新成本
        # 对下一轮预测
        a1 = error / buhege
        a2 = a1
        lasthege = buhege * (1 - a1) * (1 - a2) * (1 - a3)  # 合格品数量
        lastbuhege = buhege - lasthege
        if lasthege * price < buhege * dismantle + lastbuhege * change + buhege * r3:
            return Profit - Cost - (r1 + r2) * Acount  # 最后的利润
        Cost += buhege * dismantle
        cost, profit = 0, 0
        if buhege <= 1:
            return Profit - Cost - (r1 + r2) * Acount  # 最后的利润
        A = buhege  # 用于下一轮


# print(l001(100))


def l101(A):  # 1 0 1
    global a1, a2, a3
    Cost = 0
    Profit = 0
    cost = 0
    profit = 0
    error = A * a1  # 本身存在的不合格数
    cost += A * (k1 + k2)  # 加上检测费用
    Acount = A
    A = A - error
    while 1:
        cost += A * r3  # 装配成本
        hege = A * (1 - a3)
        buhe = A - hege
        profit += hege * price  # 获利
        cost += buhe * change  # 不合格品的调换价
        Cost += cost
        Profit += profit
        # 对下一轮进行预测
        lasthege = buhe * (1 - a3)
        lastbuhege = buhe - lasthege
        lastprofit = lasthege * price
        lastcost = lastbuhege * change + buhe * dismantle + buhe * r3
        if lastprofit < lastcost:
            return Profit - Cost - (r1 + r2) * Acount  # 最后的利润
        Cost += buhe * dismantle
        cost, profit = 0, 0
        A = buhe  # 用于下一轮
        if buhe <= 1:
            return Profit - Cost - (r1 + r2) * Acount  # 最后的利润


# print(l101(100))


def l111(A):  # 1 1 1

    global a1, a2, a3
    Cost = 0
    Profit = 0
    cost = 0
    profit = 0
    error = A * a1  # 本身存在的不合格数
    cost += A * (k1 + k2)  # 加上检测费用
    A = A - error
    Acount = A
    while 1:
        cost += A * r3  # 装配成本
        cost += A * k3  # 检验成本k
        hege = A * (1 - a3)
        buhe = A - hege
        profit += hege * price  # 获利
        Profit+=profit
        Cost += cost
        # 预测，判断是佛拆卸
        lasthege = buhe * (1 - a3)
        lastbuhe = buhe - lasthege
        lastprofit = lasthege * price
        lastcost = buhe * dismantle + buhe * k3 + buhe * r3
        if lastprofit < lastcost:
            return Profit - Cost - (r1 + r2) * Acount  # 最后的利润
        Cost += buhe * dismantle
        cost, profit = 0, 0
        A = buhe  # 用于下一轮
        if buhe <= 1:
            return Profit - Cost - (r1 + r2) * Acount  # 最后的利润


# print(l111(100))
# score = []
# score.append([str(0) + str(0) + str(0), front(100, 0, 0, 0)])
# score.append([str(0) + str(1) + str(0), front(100, 0, 1, 0)])
# score.append([str(1) + str(0) + str(0), front(100, 1, 0, 0)])
# score.append([str(1) + str(1) + str(0), front(100, 1, 1, 0)])
#
# score.append([str(0) + str(0) + str(1), front(100, 0, 0, 1)])
# score.append([str(0) + str(1) + str(1), front(100, 0, 1, 1)])
# score.append([str(1) + str(0) + str(1), front(100, 1, 0, 1)])
# score.append([str(1) + str(1) + str(1), front(100, 1, 1, 1)])
# 对结果进行排序
# sorted_data = sorted(score, key=lambda x: x[1], reverse=True)
# print(sorted_data)

result = []
for i in range(6):
    para = parameters[i]
    a1 = para[0]
    r1 = para[1]
    k1 = para[2]
    a2 = para[3]
    r2 = para[4]
    k2 = para[5]
    a3 = para[6]
    r3 = para[7]
    k3 = para[8]
    price = para[9]
    change = para[10]
    dismantle = para[11]
    score = []
    score.append(['000', l000(N)])

    para = parameters[i]
    a1 = para[0]
    r1 = para[1]
    k1 = para[2]
    a2 = para[3]
    r2 = para[4]
    k2 = para[5]
    a3 = para[6]
    r3 = para[7]
    k3 = para[8]
    price = para[9]
    change = para[10]
    dismantle = para[11]
    score.append(['010', l010(N)])

    para = parameters[i]
    a1 = para[0]
    r1 = para[1]
    k1 = para[2]
    a2 = para[3]
    r2 = para[4]
    k2 = para[5]
    a3 = para[6]
    r3 = para[7]
    k3 = para[8]
    price = para[9]
    change = para[10]
    dismantle = para[11]
    score.append(['100', l100(N)])

    para = parameters[i]
    a1 = para[0]
    r1 = para[1]
    k1 = para[2]
    a2 = para[3]
    r2 = para[4]
    k2 = para[5]
    a3 = para[6]
    r3 = para[7]
    k3 = para[8]
    price = para[9]
    change = para[10]
    dismantle = para[11]
    score.append(['110', l110(N)])

    para = parameters[i]
    a1 = para[0]
    r1 = para[1]
    k1 = para[2]
    a2 = para[3]
    r2 = para[4]
    k2 = para[5]
    a3 = para[6]
    r3 = para[7]
    k3 = para[8]
    price = para[9]
    change = para[10]
    dismantle = para[11]
    score.append(['001', l001(N)])

    para = parameters[i]
    a1 = para[0]
    r1 = para[1]
    k1 = para[2]
    a2 = para[3]
    r2 = para[4]
    k2 = para[5]
    a3 = para[6]
    r3 = para[7]
    k3 = para[8]
    price = para[9]
    change = para[10]
    dismantle = para[11]
    score.append(['011', l011(N)])

    para = parameters[i]
    a1 = para[0]
    r1 = para[1]
    k1 = para[2]
    a2 = para[3]
    r2 = para[4]
    k2 = para[5]
    a3 = para[6]
    r3 = para[7]
    k3 = para[8]
    price = para[9]
    change = para[10]
    dismantle = para[11]
    score.append(['101', l101(N)])

    para = parameters[i]
    a1 = para[0]
    r1 = para[1]
    k1 = para[2]
    a2 = para[3]
    r2 = para[4]
    k2 = para[5]
    a3 = para[6]
    r3 = para[7]
    k3 = para[8]
    price = para[9]
    change = para[10]
    dismantle = para[11]
    score.append(['111', l111(N)])
    sorted_data = sorted(score, key=lambda x: x[1], reverse=True)
    print(sorted_data)
    result.append(sorted_data[0])
print(result)

Num = 100
alpha = 0.1
r1, r2, r3, r4, r5, r6, r7, r8, r9, r10 = 2, 8, 12, 2, 8, 12, 8, 12, 8, 8
k1, k2, k3, k4, k5, k6, k7, k8, k9, k10 = 1, 1, 2, 1, 1, 2, 1, 2, 4, 6
w = 200
g = 40
h1, h2 = 6, 10

xuanze = ['000', '001(0)', '001(1)', '110', '111(0)', '111(1)']


# 组装半成品1的利润W
def Get_half1_W00():
    return -100 * (r1 + r2 + r3 + r9)


def Get_half1_W01(c):
    n = 1
    Q = 0
    # 求Q的极限
    alpha2 = 1 - (1 - alpha) ** 4
    while n:
        if (r9 + k9 + h1) * 100 * alpha2 ** n < 0.000001:
            break
        else:
            Q += (r9 + k9 + h1) * 100 * alpha2 ** n
            n += 1
    return -100 * (r1 + r2 + r3) - 100 * (r9 + k9) - Q * c


def Get_half1_W10():
    return -100 * (r1 + r2 + r3 + k1 + k2 + k3) - 100 * (1 - alpha) * r9


def Get_half1_W11(c):
    n = 1
    Q = 0
    # 求Q的极限
    while n:
        # print(1, Q)
        if (r9 + k9 + h1) * 100 * (1 - alpha) * alpha ** n < 0.000001:
            break
        else:
            Q += (r9 + k9 + h1) * 100 * (1 - alpha) * alpha ** n
            n += 1
    return -100 * (r1 + r2 + r3 + k1 + k2 + k3) - 100 * (1 - alpha) * (r9 + k9) - Q * c


result = [Get_half1_W00(), Get_half1_W01(0), Get_half1_W01(1), Get_half1_W10(), Get_half1_W11(0),
          Get_half1_W11(1)]
print(result)
G1 = [max(Get_half1_W00(), Get_half1_W01(0), Get_half1_W01(1)), max(Get_half1_W10(), Get_half1_W11(0),
                                                                    Get_half1_W11(1))]


# 组装半成品2的利润W
def Get_half2_W11(c):
    n = 1
    Q = 0
    # 求Q的极限
    while n:
        # print(2, Q)
        if (r9 + k9 + h1) * 100 * (1 - alpha) * alpha ** n < 0.000001:
            break
        else:
            Q += (r9 + k9 + h1) * 100 * (1 - alpha) * alpha ** n
            n += 1
    return -100 * (r4 + r5 + r6 + k4 + k5 + k6) - 100 * (1 - alpha) * (r9 + k9) - Q * c


def Get_half2_W01(c):
    n = 1
    Q = 0
    # 求Q的极限
    alpha2 = 1 - (1 - alpha) ** 4
    while n:
        if (r9 + k9 + h1) * 100 * alpha2 ** n < 0.000001:
            break
        else:
            Q += (r9 + k9 + h1) * 100 * alpha2 ** n
            n += 1
    return -100 * (r4 + r5 + r6) - 100 * (r9 + k9) - Q * c


def Get_half2_W10():
    return -100 * (r4 + r5 + r6 + k4 + k5 + k6) - 100 * (1 - alpha) * r9


def Get_half2_W00():
    return -100 * (r4 + r5 + r6 + r9)


result = [Get_half2_W00(), Get_half2_W01(0), Get_half2_W01(1), Get_half2_W10(), Get_half2_W11(0),
          Get_half2_W11(1)]
print(result)
G2 = [max(Get_half2_W00(), Get_half2_W01(0), Get_half2_W01(1)), max(Get_half2_W10(), Get_half2_W11(0),
                                                                    Get_half2_W11(1))]


# 组装半成品3的利润W
def Get_half3_W11(c):
    n = 1
    Q = 0
    # 求Q的极限
    while n:
        # print(2, Q)
        if (r9 + k9 + h1) * 100 * (1 - alpha) * alpha ** n < 0.000001:
            break
        else:
            Q += (r9 + k9 + h1) * 100 * (1 - alpha) * alpha ** n
            n += 1
    return -100 * (r7 + r8 + k7 + k8) - 100 * (1 - alpha) * (r9 + k9) - Q * c


def Get_half3_W01(c):
    n = 1
    Q = 0
    # 求Q的极限
    alpha2 = 1 - (1 - alpha) ** 3
    while n:
        if (r9 + k9 + h1) * 100 * alpha2 ** n < 0.000001:
            break
        else:
            Q += (r9 + k9 + h1) * 100 * alpha2 ** n
            n += 1
    return -100 * (r7 + r8) - 100 * (r9 + k9) - Q * c


def Get_half3_W10():
    return -100 * (r7 + r8 + k7 + k8) - 100 * (1 - alpha) * r9


def Get_half3_W00():
    return -100 * (r7 + r8) - 100 * r9


result = [Get_half3_W00(), Get_half3_W01(0), Get_half3_W01(1), Get_half3_W10(), Get_half3_W11(0),
          Get_half3_W11(1)]
print(result)
G3 = [max(Get_half3_W00(), Get_half3_W01(0), Get_half3_W01(1)), max(Get_half3_W10(), Get_half3_W11(0),
                                                                    Get_half3_W11(1))]

# 组装成品的利润W
def Down11(a, b, c, e):
    n = 1
    Q = 0
    # 求Q的极限
    alpha = 0.1
    alpha1 = 1 - (1 - alpha) ** 3
    alpha2 = 1 - (1 - (alpha if a else alpha1)) * (1 - (alpha if b else alpha1)) * (1 - (alpha if c else alpha1))
    while n:
        if (r10 + k10 + h2) * 100 * (1 - alpha2) ** n * alpha2 ** n < 0.000001:
            break
        else:
            Q += (r10 + k10 + h2) * 100 * (1 - alpha2) ** n * alpha2 ** n
            n += 1
    return -100 * 3 * k9- 100 * (1-alpha2) * (r10 + k10) - Q * e


def Down10(a, b, c):
    alpha = 0.1
    alpha1 = 1 - (1 - alpha) ** 3
    alpha2 = 1 - (1 - (alpha if a else alpha1)) * (1 - (alpha if b else alpha1)) * (1 - (alpha if c else alpha1))
    return -100*3*k9 - 100*(1-alpha2)*r10


def Down00():
    return -100*r10


def Down01(a, b, c, e):
    n = 1
    Q = 0
    # 求Q的极限
    alpha = 0.1
    alpha1 = 1 - (1 - alpha) ** 3
    alpha2 = 1 - (1 - (alpha if a else alpha1)) * (1 - (alpha if b else alpha1)) * (1 - (alpha if c else alpha1))
    while n:
        if (r10 + k10 + h2) * 100 * (1 - alpha2) ** n < 0.000001:
            break
        else:
            Q += (r10 + k10 + h2) * 100 * (1 - alpha2) ** n
            n += 1
    return -100 * (r10 + k10) - Q * e



# print(G1)
# print(G2)
# print(G3)


# 成本卖出后产生的利润
def Get_G4(a, b, c, f):
    n = 1
    Q = 0
    # 求Q的极限
    alpha = 0.1
    alpha1 = 1 - (1 - alpha) ** 3
    alpha2 = 1 - (1 - (alpha if a else alpha1)) * (1 - (alpha if b else alpha1)) * (1 - (alpha if c else alpha1))
    while n:
        if (r10 + k10 + h2) * 100 * alpha2 ** n - 100 * (1 - alpha2) ** n * alpha2 ** n < 0.000001:
            break
        else:
            Q += (r10 + k10 + h2) * 100 * alpha2 ** n - 100 * (1 - alpha2) ** n * alpha2 ** n
            n += 1
    return 100 * w - 100 * alpha2 * g - Q * f


result = []

for i in range(2):
    for j in range(2):
        for k in range(2):
            temp = G1[i] + G2[j] + G3[k]
            for o in range(2):
                for e in range(2):
                    t = max(Down11(i, j, k, e), Down00(), Down01(i, j, k, e), Down10(i, j, k))
                    result.append([f'{i}{j}{k}{o}{e}', G1[i], G2[j], G3[k], Get_G4(i, j, k, o), t, temp + Get_G4(i, j, k, o)+ t])



for i in range(len(result)):
    print(i+1, result[i])
for i in sorted(result,  key=lambda x: x[6], reverse=True):
    print(i)


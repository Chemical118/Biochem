from random import randint as r
import matplotlib.pyplot as plt
from matplotlib import rc
# import numpy as np
# from math import exp
import pyperclip as cp

num = 500000
setting = 20
xti = [i + 1 for i in range(setting)]

c_0 = []
c_1 = []
c_2 = []
c_3 = []
c_4 = []
out = [0 for _ in range(setting)]
c_num = dict([(0, 0), (1, 2), (2, 1), (3, 2), (4, 3), (5, 3), (6, 4)])


def check():
    t = [0 for _ in range(7)]
    for q in Biochem.li:
        t[q.type] += 1
    print(t)
    c_0.append(t[0] / num * 100)
    c_1.append(t[2] / num * 100)
    c_2.append((t[1] + t[3]) / num * 100)
    c_3.append((t[4] + t[5]) / num * 100)
    c_4.append(t[6] / num * 100)
    Biochem.moved += 1
    if t[6] == num or Biochem.moved >= setting:
        return True
    else:
        return False


class Biochem:
    li = []
    moved = 0

    def __init__(self):
        self.type = 0
        Biochem.li.append(self)

    def move(self):
        if self.type == 6:
            return
        t = r(1, 4)
        be = self.type
        if self.type == 0:
            if t <= 2:
                self.type = 1
            else:
                self.type = 2
        elif self.type == 1:
            if t <= 2:
                self.type = 5
            elif t == 3:
                self.type = 4
        elif self.type == 2:
            if t <= 2:
                self.type = 1
            elif t == 3:
                self.type = 3
        elif self.type == 3:
            if t <= 2:
                self.type = 1
        elif self.type == 5:
            if t == 1:
                self.type = 4
        elif self.type == 4:
            if t <= 3:
                self.type = 6
        out[Biochem.moved] += (c_num[self.type] - c_num[be])


for _ in range(num):
    Biochem()
while True:
    for i in Biochem.li:
        i.move()
    if check():
        break
out = list(map(lambda t: t/max(out)*3, out))
out_ratio = []

# for i in range(len(out) - 1):
#     out_ratio.append(out[i]/out[i+1])

cp.copy("\n".join(map(str, out)))
print("Copy!")
# cp.copy("\n".join(map(str, out_ratio)))
# print("Copy!")
# nut = np.array(out)

rc('font', family="NanumGothic")

fig = plt.figure(1, figsize=(9.60, 7.20))
ax = fig.add_subplot()

ax.plot(xti, c_1, label='1개 13C')
ax.plot(xti, c_2, label='2개 13C')
ax.plot(xti, c_3, label='3개 13C')
ax.plot(xti, c_4, label='4개 13C')

ax.legend()
plt.xlabel("TCA cycle 횟수")
plt.ylabel("비율 (%)")
plt.title("실험 결과")
plt.xticks(xti)

# fit = np.polyfit(xti, np.log(nut), 1)
# nfit = np.zeros(setting)
# for i in range(setting):
#     nfit[i] = exp(fit[1]) * exp(fit[0] * xti[i])

# for i in range(len(out) - 1):
#     print(out[i+1]/out[i], sep=" ")

# fig2 = plt.figure(2, figsize=(9.60, 7.20))
# plt.scatter(xti, out, s=10)
# plt.plot(xti, nfit)
# plt.xlabel("TCA cycle 횟수")
# plt.ylabel("나간 13C의 상대량")
# plt.title("실험 결과")
# plt.xticks(xti)

fig3 = plt.figure(3, figsize=(9.60, 7.20))
plt.plot(xti, out)
plt.xlabel("TCA cycle 횟수")
plt.ylabel("나간 12C의 상대량")
plt.title("실험 결과")
plt.xticks(xti)

plt.show()

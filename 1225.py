import random
import matplotlib.pyplot as plt


# 参考 https://magazine.techacademy.jp/magazine/21160
# こっちのほうが早い
def rand_ints_nodup(a, b, k):
    data = []
    while len(data) < k:
        n = random.randint(a, b)
        if not n in data:
            data.append(n)
    return data


def S_k(data, k):
    if k == 1:
        return data[0]
    if k == 2:
        last = len(data)
        while True:
            n = 0
            scan = data[0]
            if last == k - 1 or int(scan) == 1:
                return 0
            if data[k - 1] < int(scan):
                take = data[k - 1]
                return take
            k += 1
    else:
        scan = data[0:k - 2]
        n = scan.index(min(scan))
    last = len(data)
    while True:
        if last == k - 1 or scan[n] == 1:
            return 0
        if data[k - 1] < scan[n]:
            take = data[k - 1]
            return take
        k += 1


def make_data(n):
    data = []
    while True:
        data.append(random.randint(1, n))
        if len(data) == n:
            data = sorted(set(data), key=data.index)

        if len(data) == n:
            break
    return data


def probability(n, k, m):
    suc, fol = 0, 0
    for i in range(m):
        data = make_data(n)
        take = S_k(data, k)
        if take == 1:
            suc += 1
        else:
            fol += 1
    suc_p = suc / m
    fol_p = fol / m
    return suc, fol, suc_p, fol_p


def probability_use_rand(n, k, m):
    suc, fol = 0, 0
    for i in range(m):
        data = rand_ints_nodup(1, n, n)
        take = S_k(data, k)
        if take == 1:
            suc += 1
        else:
            fol += 1
    suc_p = suc / m
    fol_p = fol / m
    return suc, fol, suc_p, fol_p


# probability(全体の人数,秘書の人数,試行回数)
all_num = 100
kou = 0
number = 10000
success_s = []
success_f = []
for i in range(all_num):
    # suc, fol, suc_p, fol_p = probability(all_num, i, number)
    suc, fol, suc_p, fol_p = probability_use_rand(all_num, i, number)
    success_s.append(suc_p)
    success_f.append(fol_p)
    print(i)
print('最もベストな人とお見合いできる確率は',max(success_s)*100,'%で',success_s.index(max(success_s)),'人目である')
plt.plot(success_s, label='P_success')
plt.plot(success_f, label='P_false')
plt.legend()
plt.show()

# print('成功した回数',suc,'逆', fol, suc_p*100,'%', fol_p*100,'%')

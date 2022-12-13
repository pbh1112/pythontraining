x = 9
tong_chia_3 = 0
tong_chia_5 = 0

for i in range(9+1):
    if i % 3 == 0:
        if i % 5 == 0:
            tong_chia_3 += i
            tong_chia_5 += i
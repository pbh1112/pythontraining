# Bài 1: Lấy số x là user input, print ra kết quả là tổng của các số chẵn, của các số lẻ, của các số chia hết cho 3, và của các số chia hết cho 5
def hw_1(x):

    tong_chan = 0
    tong_le = 0
    tong_chia_het_cho_3 = 0
    tong_chia_het_cho_5 = 0

    for i in range(x + 1):
        if i % 2 == 0:
            tong_chan += i
        else:
            tong_le += i 
        if i % 3 == 0:
            tong_chia_het_cho_3 += i
        if i % 5 == 0:
            tong_chia_het_cho_5 += i 

    print(tong_chan)
    print(tong_le)
    print(tong_chia_het_cho_3)
    print(tong_chia_het_cho_5)

def main():
    x = int(input("Nhập x: "))
    hw_1(x)
    return
if __name__ == '__main__':
    main() 

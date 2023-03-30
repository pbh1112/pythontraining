import random

def main():
    hw1()
    hw2()
    return

# HW1: Chỉnh lại bài tập guest book với tất cả user input bắt buộc là số nguyên
def hw1():
    print("\nHW1: Guess Book")

    def input_interger(mess):
        while True:
            x = input(mess)
            if not x.isdigit() or int(x) <= 0:
                print(f"* Vui lòng nhập số nguyên dương!")
            else:
                return int(x)

    empty_seats = input_interger("[Check] Số ghế còn trống trong nhà hàng: ")
    orderer = input_interger("[Check] Số khách đang chờ tại quầy: ")
    require_seats = 0
    i = 1
    successful_order = {}
    failed_order = {}

    while i <= orderer:
        a = input(f"\n[Ask customer {i}]\n- Quý khách cho tôi xin tên được chứ: ")
        b = input_interger("- Quý khách đặt bàn mấy người: ")

        if b <= empty_seats - require_seats:
            successful_order[a.title()] = b       
            require_seats += b
            i += 1
        else:
            failed_order[a.title()] = b
            i += 1

    print(f"\n[Record]\nNhà hàng xin chân thành cảm ơn các quý khách.\nSau đây là trạng thái order của các quý khách:")

    for i in successful_order:
        print(f"- Bạn {i} đã đặt thành công bàn {successful_order[i]} người")

    for i in failed_order:
        print(f"- Mong bạn {i} thông cảm. Nhà hàng không đủ chỗ cho {failed_order[i]} người")


# HW2: Battleship (ez):
# Co 2 nguoi choi
# Voi moi nguoi choi, cho phep nhap so luong tau va so luong tau khong duoc vuot qua 7, so luong tau cua 2 nguoi choi phai giong nhau

# Sau khi nhap so luong tau, generate ra mot list tau, voi moi con tau duoc danh so random tu 1-30
# Vi du: list tau cua nguoi choi 1 [1, 5, 25, 30]

# Moi nguoi choi se lan luot duoc doan so lan tuong ung voi so luong tau va so lan doan nay it nhat la 3 (user input)
# Sau khi het luot doan, kiem tra xem ai ban trung tau nguoi khac nhieu hon 


def hw2():
    print("\nHw2: Battleship")
    def gen_list(n):
        list = []
        for i in range(n):
            x = random.randint(1, 30)
            list.append(x)
        return list

    def input_int_1_7(mess):
        while True:
            x = input(mess)
            if not x.isdigit() or int(x) < 1 or int(x) > 7:
                print("* Vui lòng nhập số nguyên từ 1 đến 7!")
            else:
                return int(x)

    def input_int_1_30(mess):
        while True:
            x = input(mess)
            if not x.isdigit() or int(x) < 1 or int(x) > 30:
                print("* Vui lòng nhập số nguyên từ 1 đến 30!")
            else:
                return int(x)

    so_tau = input_int_1_7("Số lượng tàu cấp cho mỗi người chơi (1-7): ")
    lst_1 = gen_list(so_tau)
    lst_2 = gen_list(so_tau)
    round = 1
    score_1 = 0
    score_2 = 0

    print(f"\nĐiểm danh tàu của hai người chơi:\n- Người chơi 1: {lst_1}\n- Người chơi 2: {lst_2}")


    while round <= 3 or round <= so_tau:
        print(f"\nRound {round}:")
        user_1_turns = input_int_1_30("- Lượt của người chơi 1 (1-30): ")
        user_2_turns = input_int_1_30("- Lượt của người chơi 2 (1-30): ")

        if user_1_turns in lst_2:
            score_1 += 1
            lst_2.remove(user_1_turns)
        if user_2_turns in lst_1:
            score_2 += 1
            lst_1.remove(user_2_turns)

        print(f"-> [Round {round}] Điểm số của người chơi 1 và 2 là {score_1} : {score_2}")
        round += 1

    if score_1 < score_2:
        print(f"\n[Game Over] Người chơi 2 chiến thắng. Tỉ số trung cuộc: {score_1} : {score_2}\n")
    elif score_1 > score_2:
        print(f"\n[Game Over] Người chơi 1 chiến thắng. Tỉ số trung cuộc: {score_1} : {score_2}\n")
    elif score_1 == score_2:
        print(f"\n[Game Over] Hai người chơi hoà nhau. Tỉ số trung cuộc: {score_1} : {score_2}\n")

if __name__ == '__main__':
  main()

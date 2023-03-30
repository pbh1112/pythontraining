import random

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

def main():
    hw2()
    return

if __name__ == '__main__':
  main()
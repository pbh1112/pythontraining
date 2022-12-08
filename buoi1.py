#1. Tạo hàm:
#1.1. Chào hỏi
def greetings():
  print("\nChào mừng đến với buổi tiệc")


#1.2. Hàm nhập lượng khách tối đa mà nhà hàng có thể nhận
def max_guests():
  return int(input("Số khách tối đa hôm nay? "))
  


#1.3. Hàm hỏi tên
def get_user_name():
  return input("Bạn tên gì? ")


#1.4. Hàm hỏi số người đi cùng
def get_user_party_number():
  return int(input("Bạn đặt bàn bao nhiêu người? "))


#1.5. Hàm lưu giá trị vào máy
def user_record(a, b):
  return a, b


#1.6.1. hàm cộng số lượng khách qua list, tuple (dùng cho cách 1)
def total_guests_1(a, b, c): 
  return a[1] + b[1] + c[1]       # a, b, c ở đây là list, tuple


#1.6.2. Hàm cộng số lượng khách qua interger (dùng cho Cách 2)
def total_guests_2(a, b, c): 
  return a + b + c         # a, b, c ở đây là số nguyên


#1.7. List toàn bộ thông tin các khách hàng
def list_guests(a, b, c): # a, b, c là list, tuple
  lst = []
  lst.append(a)
  lst.append(b)
  lst.append(c)
  print(f"Bên em xin xác nhận lại các thông tin bên em nhận được ạ: {lst}")


#1.8. Hàm so sánh lượng khách đến với tổng lượng khách tối đa có thể nhận
def compare_with_max_guests(a, b, c):
  if a < b:
    print(
      f"Chúng tôi thiếu chỗ cho {b - a} người trong nhóm của bạn. Đoàn của {c.title()} vui lòng giảm số người nhé\n"
    )
  else:
    print(f"chúng tôi có đủ chỗ cho các bạn. Xin mời vào!\n")


# #2. Chạy chương trình
# # Cách 1:
# def main():
#   greetings()
#   x = max_guests()
#   user_1 = user_record(get_user_name(), get_user_party_number())
#   user_2 = user_record(get_user_name(), get_user_party_number())
#   user_3 = user_record(get_user_name(), get_user_party_number())
#   y = total_guests_1(user_1, user_2, user_3)
#   list_guests(user_1, user_2, user_3)
#   compare_with_max_guests(x, y, user_3[0])
#   return
# if __name__ == '__main__':
#   main()


# # Cách 2:
# def main():
#   greetings()
#   x = max_guests()
#   user_1 = list(user_record(get_user_name(), get_user_party_number())).pop(1)
#   user_2 = list(user_record(get_user_name(), get_user_party_number())).pop(1)
#   user_3 = list(user_record(get_user_name(), get_user_party_number())).pop(1)
#   y = total_guests_2(user_1, user_2, user_3)
#   compare_with_max_guests(x, y, 'bạn thứ 3')
#   return


# if __name__ == '__main__':
#   main()
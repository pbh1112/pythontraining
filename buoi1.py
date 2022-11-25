# Xử lý thông tin: Năm hiện tại
import datetime
curent_year = datetime.datetime.now()

# I. Input:
# - Hỏi tên người dùng
user_name = input("Chào bạn! Bạn tên gì thể? ")
# - Hỏi năm sinh của người dùng
user_year_of_birth = int(input("Bạn sinh năm bao nhiêu? "))
# - Hỏi tên của bố người dùng
dad_name = input("Bố bạn tên là gì? ")
# - Hỏi năm sinh của bố người dùng
dad_year_of_birth = int(input("Bố bạn sinh năm bao nhiêu thế? "))
# - Hỏi tên của mẹ người dùng
mom_name = input("Mẹ bạn tên là gì? ")
# - Hỏi năm sinh của mẹ người dùng
mom_year_of_birth = int(input("Mẹ bạn sinh năm bao nhiêu thế? "))

# Xử lý thông tin: Cách xưng hô
if dad_year_of_birth < 1973:
  call_user_dad = "bác"
else:
  call_user_dad = "chú"

if mom_year_of_birth < 1975:
  call_user_mom = "bác"
else:
  call_user_mom = "cô"

# II. Output/Print:
# - Chào + tên người dùng
# - Thông báo năm hiện tại
# - Người dùng bao nhiêu tuổi
# - Bố người dùng bao nhiêu tuổi
# - Mẹ người dùng bao nhiêu tuổi
# - Bố mẹ người dùng sinh ra người dùng năm họ bao nhiêu tuổi
print(
  f"\nHello!\nRất vui được làm quen với {user_name.title()}\nNăm này là năm {str(curent_year.year)}\nVậy là năm nay {user_name.title()} đã {str(curent_year.year - user_year_of_birth)} tuổi\n{call_user_dad} {dad_name.title()} tròn {str(curent_year.year - dad_year_of_birth)} tuổi\nVà {call_user_mom} {mom_name.title()} {str(curent_year.year - mom_year_of_birth)} tuổi\nLúc bạn chào đời, bố bạn {str(user_year_of_birth - dad_year_of_birth)} tuổi, còn mẹ bạn {str(user_year_of_birth - mom_year_of_birth)} tuổi"
)

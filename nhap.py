def main():
  greetings()
  user_1 = user_record(get_user_name(), get_user_party_number())
  user_2 = user_record(get_user_name(), get_user_party_number())
  user_3 = user_record(get_user_name(), get_user_party_number())
  guest_book = []
  guest_book.append(user_1)
  guest_book.append(user_2)
  guest_book.append(user_3)
  print(guest_book)
  return

def greetings():
  print("Welcome to the party")
  return

def get_user_name():
  user_name = input("What is your name?")
  return user_name

def get_user_party_number():
  user_party_number = int(input("How many people do you bring along with you?"))
  return user_party_number

def user_record(user_name, user_party_number):
  return user_name, user_party_number


if __name__ == '__main__':
  main()
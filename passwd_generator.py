#Password Generator Project
import random
def generate_password():
  list_of_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  list_of_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  list_of_symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  nr_of_letters = int(input('Enter number of letters you want in your password: '))
  nr_of_symbols = int(input('Enter number of symbols you want in your password: '))
  nr_of_numbers = int(input('Enter number of numbers you want in your password: '))

  password_list = []
  
  for char in range(nr_of_letters):
    password_list.append(random.choice(list_of_letters))

  for char in range(nr_of_symbols):
    password_list += random.choice(list_of_symbols)

  for char in range(nr_of_numbers):
    password_list += random.choice(list_of_numbers)

  random.shuffle(password_list)

  password = ""
  for char in password_list:
    password += char
  return password

print(generate_password())
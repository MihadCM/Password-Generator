import random

print("RANDOM PASSWORD CREATOR")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!','@','#','$','%','^','&','*','(',')','+']
numbers = ['1','2','3','4','5','6','7','8','9','0']
total_letters = int(input("How many letters would you like to insert in your password\n"))
total_symbols = int(input("how many symbols would you like to insert in your password\n"))
total_numbers = int(input("how many numbers would you like to insert in your password\n"))
password_list = []
for i in range(total_letters):
    password_list.append(random.choice(letters))

for i in range(6):
    password_list.append(random.choice(letters))

for i in range(1):
    password_list.append(random.choice(symbols))

for i in range(1):
    password_list.append (random.choice(numbers))

random.shuffle(password_list)
password = ""
for i in password_list:
    password += i
print(f"Your Password is: {password} ")

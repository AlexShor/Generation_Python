alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#num_sys_from = int(input("Number systems from: "))
num_sys_from = 10
num_sys_to = 2
#number = list(input("Number: "))
number = "513"

def change_num(number):
    new_number = []
    for digit in number:
        digit = str(digit)
        if not digit.isdigit(): new_number.append(10 + alph.index(digit.upper()))
        elif int(digit) > 9: new_number.append(alph[int(digit)-10])
        else: new_number.append(digit)
    return new_number

# def num_sys_calculation(number):
#     result = 0
#     for i in range(len(number)):
#         result += int(number[i]) * (num_sys_from**(len(number)-1-i))
#     return result

# number = change_num(list("1AF2"))

if num_sys_to == 10: print(int(number, num_sys_from))
else:
    result = []
    num = int(number)
    while num >= num_sys_to:
        result.append(num % num_sys_to)
        num = num // num_sys_to
        if num < num_sys_to: result.append(num)
    print(*change_num(result)[::-1], sep="")

#print(num_sys_calculation(number))
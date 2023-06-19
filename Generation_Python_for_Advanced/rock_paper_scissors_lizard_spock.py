t, r = input(), input()
n = ["камень", "бумага", "ножницы", "Спок", "ящерица"]
a = abs(n.index(t) - n.index(r))
if a == 0: print('ничья')
elif (n.index(t) < n.index(r) and a % 2 == 0) != (n.index(t) > n.index(r) and a % 2 != 0): print('Тимур')
else: print('Руслан')
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      СТВН
#
# Created:     10.03.2023
# Copyright:   (c) СТВН 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

phone_dict = {9104467935: 'AAY', 9035335521: 'AAY', 9015924200: 'AAY'}
b = input('Ввести номер для проверки')
bb = int(b)
for number, name in phone_dict.items():
    if bb == number:
        print (f"Введенный номер {number} присуствует в базе !!!")
        break
print ("\nПроверка окончена NO!!!")
for i in phone_dict.values():
    print (i)
print (len(phone_dict.values()))
with open('verbs20.txt') as f:
    print (f.readline().strip())
    print (f.readline())
    length = (f.readlines())
    print (len(length))

with open('verbs20.txt', 'a') as f:
    f.write('add new verb\n')


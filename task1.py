#Напишите программу, которая принимает
 #на вход вещественное число и 
 #показывает сумму его цифр.(Сделать для строки)

 #   *Пример:*

 #   - 6782 -> 23
 #   - 0,56 -> 11

num = input("Введите число ")

def summa(num):
    if float (num) < 0:
        num = float(num) * (-1)
    number = 0
    
    for i in str(num):
        if i != '.':
            number += int(i)
    return number


print (f'Сумма чисел равна{summa(num)}')




    
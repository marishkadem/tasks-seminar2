#Реализуйте алгоритм нахождения(генерации) 
#рандомного(случайного) числа.
#(Не используя библиотеки связанные с рандомом)

import datetime 

min_n = 10
max_n = 100

def get_rand():
    return datetime.datetime.now().microsecond%10

n = get_rand()

print(int(len(str(min_n))))
print(n)
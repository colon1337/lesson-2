#Пользователь вводит два числа (возможно дробные), вывести результат их сложения, вычитания, умножения, деления, возведения в степень, деления по модулю, целочисленного деления.
print('Введите 2 числа')
a=float(input('первое число:'))
b=float(input('второе число:'))
sum=a+b
min=a-b
umn=a*b
dell=a/b
step=a**b
mod=a%b
cel=a//b
print(f'Суммна чисел равна: {sum}')
print(f'Разность чисел равна: {min}')
print(f'Произведение чисел равно: {umn}')
print(f'Частное чисел равно: {dell}')
print(f'Возведение числа {a} в степень {b} равно: {step}')
print(f'Деление {a} по модулю {b} равна: {mod}')
print(f'Целое число от деление {a} на число {b} равна: {cel}')
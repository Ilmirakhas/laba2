import random

def find_multiples(x):

 while True:
  x_str = input(f"Введите цифру X (кратность): ")
  if x_str.isdigit() and len(x_str) == 1 and x_str != "0": 
   x = int(x_str)
   break
  else:
   print("Некорректный ввод. Введите одну цифру.")

 numbers = [random.randint(0, 200) for _ in range(10)]
 multiples = list(filter(lambda number: number % x == 0, numbers))
 print(f"Список чисел: {numbers}")
 print(f"Числа, кратные {x}: {multiples}")

find_multiples(0)
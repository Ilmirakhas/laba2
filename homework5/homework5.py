def get_number():
 
  for i in range(30):
    if i % 2 != 0:
      yield i


generator = get_number()

count = 0
for number in generator:
  if count == 0:
    print(f"Первое значение: {number}")
  if count == 4:
    print(f"Пятое значение: {number}")
  count += 1
print(f"Последнее значение: {number}")
import numpy
import time

startTime = time.time()  # время начала замера

items = numpy.random.randint(100000, size=100000)
print(len(items), items[:10 ** 9])
a = sum(items)
print(a)
if a % 2 != 0:
    print("сумма нечетная")
else:
    print("четная:(")

endTime = time.time()  # время конца замера
totalTime = endTime - startTime  # вычисляем затраченное время
print("Время, затраченное на выполнение данного кода = ", totalTime)


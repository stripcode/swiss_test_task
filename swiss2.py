# -*- coding: utf-8 -*-
from Queue import LifoQueue, Full

# Потокобезопасная очередь размер в 5 элементов
bucket = LifoQueue(5)

def putToBucket(el):
  # Метод принимает элемент и если очередь полна эелемент не попадает в очередь
  try:
    bucket.put_nowait(el)
  except Full as e:
    print("Очередь полна и не может принять элемент %s" % el)

for i in range(0, 9):
  putToBucket(i)
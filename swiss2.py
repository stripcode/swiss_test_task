# -*- coding: utf-8 -*-
from Queue import LifoQueue

# Потокобезопасная очередь размер в 5 элементов
bucket = LifoQueue(5)

def putToBucket(el):
  # Метод принимает элемент и если очередь полна эелемент не попадает в очередь
  try:
    bucket.put_nowait(el)
  except:
    pass

for i in range(0, 9):
  putToBucket(i)
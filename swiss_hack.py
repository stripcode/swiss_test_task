# -*- coding: utf-8 -*-

class A(object):
  def __init__(self, value):
    self._value = value

  def foo(self):
    self.bar()
    return self._value

# Грязный хак - но как вариант
def fun():
  pass

A.bar = fun


def call_foo(inst):
  try:
    assert isinstance(inst, A)
    if inst.foo() < 10:
      return True
    else:
      return False
  except AttributeError:
    return False
  finally:
    return False

print(call_foo(A(5)))
# -*- coding: utf-8 -*-

def fun(self):
  pass

class meta(type):
    def __new__(mcs, name, bases, dict):
      dict["bar"] = fun
      return type.__new__(mcs, name, bases, dict)

class A(object):
  __metaclass__ = meta

  def __init__(self, value):
    self._value = value

  def foo(self):
    self.bar()
    return self._value

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
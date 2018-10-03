# -*- coding: utf-8 -*-

class meta(type):
    def __new__(mcs, name, bases, dict):
      def fun():
          pass
      cls = type.__new__(mcs, name, bases, dict)
      cls.bar = fun
      return cls

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
  except AttributeError as e:
    return False
  finally:
    return False

print(call_foo(A(5)))
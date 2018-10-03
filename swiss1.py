def decorator(cls):
  def fun(a):
    pass
  cls.bar = fun
  return cls

@decorator
class A(object):
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
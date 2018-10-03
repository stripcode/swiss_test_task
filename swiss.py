class A(object):
  def __init__(self, value):
    self._value = value

  def foo(self):
    self.bar()
    return self._value

  def __getattr__(self, name):
    if name == "bar":
      def bar():
        pass
      return bar
    else:
      raise AttributeError("attr not found")


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
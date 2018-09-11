# assert
#  (ensure something is true)
assert False, "error!"

# del
#  (delete from dictionary)
X = {"a": 1, "c": 2}
del X["c"]

# except
try:
    a = 1 / 0
except ZeroDivisionError as e:
    print(e)

# exec
#  (run a string as python)
exec('print("Testing exec")')

# finally
#  (do this no matter what!)

# global
#  (declare global variable)
global a

# is
#  (like == to test equality)
1 is 1

# lambda
#  (create a short anonymous function)
s = lambda y: y ** y
s(3)


# pass
#  (this block is empty)
def empty():
    pass


# yield
#  (pause here and return to caller)
def generate():
    yield 0.5


generate().next()

# raise
#  (raise exception when things go wrong)
raise ValueError("No")

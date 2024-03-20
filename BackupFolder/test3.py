import time
import traceback


def fun1(n):
    try:
        print("in try..")
        time.sleep(2)
        print(n**n)
        raise KeyError
        return n**n
    finally:
        print("in finally")
        time.sleep(5)
        print("finally reason", traceback.format_exc())


x = fun1(5)
print("got x", x)

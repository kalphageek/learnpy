class BizException(Exception):
    pass


try:
    number = float('hello')
    print(number)
except ValueError as e:
    raise BizException(e)

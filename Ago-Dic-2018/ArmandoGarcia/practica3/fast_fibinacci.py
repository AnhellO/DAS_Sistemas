import time
from decorators import memoize

@memoize
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 2) + fibonacci(num - 1)

start = time.time()
print("fibonacci: %s " % fibonacci(200))
end = time.time()
print('\033[93m]' + 'Runnig time {} secs'.format(end - start))

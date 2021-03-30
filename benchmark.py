# xxHash: [714, 722, 730, 777, 675, 719]
# CPython: [2849, 3161, 3496, 2733, 2946, 2947]
import time, contextlib


@contextlib.contextmanager
def time_it():
    CTM = lambda: round(time.time() * 1000)
    start = CTM()
    yield
    print(CTM() - start, 'ms')


class Foo:
    def __init__(self, name):
        self.name = name
    
    def __hash__(self):
        return hash(self.name)
    
    def __eq__(self, other):
        return hash(self) == hash(other)


print('Allocating entities')
foos = [Foo('a' * i) for i in range(100_000)]
print('Compariing')

with time_it():
    for i in range(1, len(foos)):
        assert foos[i] != foos[i - 1]

print('Done')


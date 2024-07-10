from typing import TYPE_CHECKING, Collection, Callable, TypeVar, Generic

# Example from the sheet
def myAbs(x : float) -> float:
  """Take the absolute of the floating-point input"""
  if x < 0:
    return (-x)
  else:
    return x

# Q1
def mean(x : float, y : float) -> float:
  return (x + y) / 2.0

# Q2
# def badMean(x : float, y : float) -> float:
#   return (x + y + "hello") / 2.0

# Q3
if TYPE_CHECKING:
  reveal_type(len)

# Q4
def meanN(xs : Collection[float]) -> float:
  sum = 0.0
  for x in xs:
    sum+=x
  return (sum / len(xs))

# Q5
T = TypeVar('T')
def meanGen(xs : Collection[float], transform : Callable[[float], T]) -> T:
  sum = 0.0
  for x in xs:
    sum+=x
  return transform(sum)

example1 = meanGen([5,10,15,20], lambda x: x / 4.0)
print(example1)

# Q6
S = TypeVar('S')
U = TypeVar('U')
def reduce(xs : Collection[T], combiner : Callable[[T,S],S], initial : S, transform: Callable[[S], U]) -> U:
  acc = initial
  for x in xs:
    acc = combiner(x,acc)
  return transform(acc)

def meanNew(xs : Collection[float]) -> float:
  return reduce(xs, lambda x, y: x + y, 0.0, lambda x: x / len(xs))

example2 = meanNew([5,10,15,20])
print(example2)

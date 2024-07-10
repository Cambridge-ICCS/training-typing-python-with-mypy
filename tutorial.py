from typing import TYPE_CHECKING

# Definition with a type signature
flag : bool = True

# Simple function with its typing information on inputs and return
def plus(x : int, y : int) -> int:
  return (x + y)

# Some functions return the 'None' value which has type 'None'
# (e.g. print)
def greet(name: str) -> None:
   """Say hello to everyone"""
   print("Hi " + name)

greet("Summer School Participants")

# Another example with floats
def myAbs(x : float) -> float:
  """Take the absolute of the floating-point input"""
  if x < 0:
    return (-x)
  else:
    return x

# Example with list data structure which is _parameterised_
# by another type: the type of the elements
def greet_all_list(names : list[str]) -> None:
  for name in names:
    greet(name)

# We can generalise this with the 'super class' of `Iterable`
# objects
from typing import Iterable

def greet_all(names : Iterable[str]) -> None:
  for name in names:
    greet(name)

greetAll(["Alice", "Baiba", "Cornelius"])
greetAll({"hi":42,"test":55})
greetAll(("A", "B", "C", "D"))

def myDiv(x : float, y : float) -> (float | None):
   if y != 0: return x / y
   else:      return None

myDict : dict[str, float | str] = {"temp" : 273.0, "units": "Kelvin"}

if TYPE_CHECKING:
  reveal_type(len)

from typing import Any

# def first(xs : list[Any]) -> Any:
#   return xs[0]

# not much information
def notfirst(xs : list[Any]) -> Any:
  return 422934809234

from typing import Any, TypeVar

T = TypeVar("T")

# or in python 3.10 and below:
# def first(xs : list[type(T)]) -> type(T):
def first(xs : list[T]) -> T:
  return xs[0]

example0 = first([1,2,3,4])
#reveal_type(example0)
example1 = first(["hi","hola"])
#reveal_type(example1)

from typing import Callable
S = TypeVar('S')
def memo(f : Callable[[S], T], x : S) -> tuple[S,T]:
  return (x, f(x))

# what about functions that return multiple outputs?
# It's really just at tuple:

def foo(x : T) -> tuple[T,T]:
  return x, x

a, b = foo(42)
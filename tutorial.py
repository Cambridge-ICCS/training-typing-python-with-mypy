# Examples from the workshop session, live coding mostly

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

greet_all(["Alice", "Baiba", "Cornelius"])
greet_all({"hi":42,"test":55})
greet_all(("A", "B", "C", "D"))

def myDiv(x : float, y : float) -> (float | None):
   if y != 0: return x / y
   else:      return None

myDict : dict[str, float | str] = {"temp" : 273.0, "units": "Kelvin"}

# Classes are used as at type names
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

h : Complex = Complex(3.0, -4.5)

# Querying the types
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  reveal_type(len)

# A simple example working with parameteric types
def first_str(xs : list[str]) -> str:
  return xs[0]

# If we want to do the same thing but on lists of integers
# we might think of doing:

def first_int(xs : list[int]) -> int:
  return xs[0]

# But this leads to code duplication...
# We could use 'Any' which types anything
from typing import Any
def first_any(xs : list[Any]) -> Any:
  return xs[0]

# But this does not provide much information: the following
# has the same type but does something very different
def notfirst(xs : list[Any]) -> Any:
  return 422934809234

# *Instead* we can use parametric polymorphism
# creating a _type variable_ that quantifies over all types
from typing import TypeVar

T = TypeVar("T")
def first(xs : list[T]) -> T:
  return xs[0]

# or in python 3.10 and below:
# def first(xs : list[type(T)]) -> type(T):

# Now we can reuse the function at different types as normal:
example0 = first([1,2,3,4])
example1 = first(["hi","hola"])
#reveal_type(example1)

# Example of the Callable interface
from typing import Callable
S = TypeVar('S')
def memo(f : Callable[[S], T], x : S) -> tuple[S,T]:
  return (x, f(x))

# What about functions that return multiple outputs?
# It's really just as tuple:
def copy(x : T) -> tuple[T,T]:
  return x, x

a, b = copy(42)

# Escape hatch
borked = 0 / "hello" # type: ignore
import numpy as np

# Simple approach: use the ndarray class name in typing
myArray : np.ndarray = np.ndarray(shape=(2,2), dtype=float)

# External typing library for numpy:
import numpy.typing as npt

# Creating an ndarray (but unknown element type)
def as_array(a: npt.ArrayLike) -> np.ndarray:
    return np.array(a)

# Using the parametric NDArray we can parameterise the type of the numpy array
def scale_array(a: float, arr: npt.NDArray[np.float64]) -> npt.NDArray[np.float64]:
    return a*arr
import numpy as np

def square(x):
    """Calculate the square energy of the signal.

    This calculates the square. It's self-explanatory.

    Parameters
    ----------
    x : ndarray
        The signal used to compute the energy.

    Returns
    -------
    energy : float
        The sum of the squares of the input signal.
    """
    return np.sum(x**2)

def abs_area(x, y):
    """Calculate the area under the curve y(x).

    Parameters
    ----------
    x : ndarray
        Ordinate (independent variable).
    y : ndarray
        Coordinate (dependent variable).

    Returns
    -------
    area : float
        The area under the curve y(x).
    """
    dx = (x[-1] - x[0]) / len(x)
    return 0.5*dx * (y[0] + 2*np.sum(y[1:-2] + y[-1]))

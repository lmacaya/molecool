import numpy as np
"""
This module is for functions which perform measurements.
"""


def calculate_distance(rA, rB):
    """
    Calculate the distance between two points.

    Parameters
    ----------
    rA, rB : np.ndarray
        The coordinates of each point.

    Returns
    -------
    distance : float
        The distance between the two points.

    Examples
    --------
    >>> r1 = np.array([0, 0, 0])
    >>> r2 = np.array([0, 0.1, 0])
    >>> calculate_distance(r1, r2)
    0.1
    """

    if isinstance(rA, np.ndarray) is False or isinstance(rB, np.ndarray) is False:
        raise TypeError("rA and rB must be numpy arrays")
    dist_vec = (rA - rB)
    distance = np.linalg.norm(dist_vec)
    if distance == 0.0:
        raise Exception("Two atoms are located in the same point in space")
    return distance


def calculate_angle(rA, rB, rC, degrees=False):
    """
    Calculate the angle between three points.

    Parameters
    ----------
    rA, rB, rC : np.ndarray
        The coordinates of each point.
    degrees : boolean
        Return angle in degrees.

    Returns
    -------
    angle : float
        The angle between the two points in radians. If degrees = True, return angle in degrees

    Examples
    --------
    >>> r1 = np.array([0.1, 0, 0])
    >>> r2 = np.array([0, 0.1, 0])
    >>> r3 = np.array([0, 0, 0.1])
    >>> calculate_distance(r1, r2, r3)
    1.0471975511965979
    >>> calculate_distance(r1, r2, r3, degrees=True)
    60.00000000000001
    """

    AB = rB - rA
    BC = rB - rC
    theta = np.arccos(
        np.dot(AB, BC) / (np.linalg.norm(AB) * np.linalg.norm(BC)))

    if degrees:
        return np.degrees(theta)
    else:
        return theta

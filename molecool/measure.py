import numpy as np

"""
This module is for functions which perform measurements.
"""


def calculate_distance(rA, rB):
    if isinstance(rA, np.ndarray) is False or isinstance(rB, np.ndarray) is False:
        raise TypeError("rA and rB must be numpy arrays")
    dist_vec = (rA - rB)
    distance = np.linalg.norm(dist_vec)
    if distance == 0.0:
        raise Exception("Two atoms are located in the same point in space")
    return distance


def calculate_angle(rA, rB, rC, degrees=False):
    AB = rB - rA
    BC = rB - rC
    theta = np.arccos(
        np.dot(AB, BC) / (np.linalg.norm(AB) * np.linalg.norm(BC)))

    if degrees:
        return np.degrees(theta)
    else:
        return theta

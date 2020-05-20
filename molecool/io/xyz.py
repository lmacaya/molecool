import numpy as np

"""
Functions for manipulating xyz files.
"""


def open_xyz(file_location):
    """Open and read coordinates and atom symbols from a xyz file.

    Parameters
    ----------
    file_location : str
        The location of the xyz file to read in.

    Returns
    -------

    symbols : list
        The atomic symbols of the xyz file.
    coords : np.ndarray
        The coordinates of the xyz file.

    """

    xyz_file = np.genfromtxt(
        fname=file_location, skip_header=2, dtype='unicode')
    symbols = xyz_file[:, 0]
    coords = (xyz_file[:, 1:])
    coords = coords.astype(np.float)
    return symbols, coords


def write_xyz(file_location, symbols, coordinates):
     """Write coordinates and atom symbols to a xyz file.

    Parameters
    ----------
    file_location : str
        The location of the xyz file to write in.
    symbols : list
        The atomic symbols of the xyz file.
    coords : np.ndarray
        The coordinates of the xyz file.

    Returns
    -------
    None

    """
    num_atoms = len(symbols)

    with open(file_location, 'w+') as f:
        f.write('{}\n'.format(num_atoms))
        f.write('XYZ file\n')

        for i in range(num_atoms):
            f.write('{}\t{}\t{}\t{}\n'.format(symbols[i],
                                              coordinates[i, 0], coordinates[i, 1], coordinates[i, 2]))

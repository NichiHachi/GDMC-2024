import numpy as np


def parallel(segment, distance, normal=np.array([0, 1, 0])):
    """Get parallel segment in 3D space at a distance.

    Args:
        segment (np.array, np.array): start and end points of the segement.
        distance (int): distance between both segment. Thickness in the context of a line. Positive direction means left.

    Returns:
        (np.array(), np.array()): parallel segment.
    """
    return (orthogonal(segment[0], segment[1], distance, normal), orthogonal(segment[1], segment[0], -distance, normal))


def orthogonal(origin, point, distance, normal=np.array([0, 1, 0])):
    """Get orthogonal point from a given one at the specified distance in 3D space with normal direction.

    Args:
        origin (tuple or np.array): origin
        point (tuple or np.array): (point-origin) makes the first vector. Only the direction is used.
        distance (int): distance from the origin. Thickness in the context of a line. Positive direction means left.
        normal (list or np.array, optional): second vector. Defaults to the vertical [0, 1, 0].

    Raises:
        ValueError: if vectors are not linearly independent.

    Returns:
        np.array: (x y z)

    >>>orthogonal((5, 5, 5), (150, 5, 5), 10)
    [ 5.  5. 15.]
    """
    vector = np.subtract(point, origin)
    magnitude = np.linalg.norm(vector)
    normalized_vector = vector / magnitude
    orthogonal = np.cross(normalized_vector, normal)

    if np.array_equal(orthogonal, np.zeros((3,))):
        raise ValueError("The input vectors are not linearly independent.")

    orthogonal = np.add(np.multiply(orthogonal, distance), origin)
    return orthogonal

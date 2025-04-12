from typing import Tuple

def add_vectors(v1:Tuple[int], v2:Tuple[int])->None:
    for elem1, elem2 in zip(v1, v2, strict=True):
        print(elem1+elem2)

add_vectors(v1, v2)
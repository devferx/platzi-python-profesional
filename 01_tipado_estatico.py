from typing import Dict, List, Tuple


def suma(a: int, b: int) -> int:
    return a + b


positives: List[int] = [1, 2, 3, 4, 5]

users: Dict[str, int] = {
    "argentina": 1,
    "mexico": 24,
    "colombia": 45,
}


contries: List[Dict[str, str]] = [
    {"name": "Argentina", "people": "45000"},
    {"name": "Mexico", "people": "900000"},
    {"name": "Colombia", "people": "9999999"},
]


numbers: Tuple[int, float, int] = (1, 0.5, 1)

coordinatesType = List[Dict[str, Tuple[int, int]]]

coordinates: coordinatesType = [
    {
        "coord1": (1, 2),
        "coord2": (3, 5),
    },
    {
        "coord1": (0, 1),
        "coord2": (8, -1),
    },
]

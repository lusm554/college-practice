import random
import string
import logging
import argparse
from typing import Any
import re

# Parse input arguments
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--debug", help="Enable debug level", action="store_true")
parser.add_argument("-t", "--test", help="Test program", action="store_true")
input_args = parser.parse_args()

# Get debug level. Default is WARNING.
LOG_LEVEL = logging.WARNING if not input_args.debug else logging.DEBUG

# logging settings
logging.basicConfig(format="[%(asctime)s] %(levelname)s - %(message)s", level=LOG_LEVEL)

def generate_input(elems_cnt: int = 5, max_size: int = 100, filling_entity: [list, str] = string.ascii_letters) -> list[list[Any]]:
    """
    Generates lists with random count of ascii letters.

    Parameters
    ----------
    elems_cnt : int, optional
        The count of elems generated

    max_size : int, optional
        The size of random elements

    filling_entity : [list, str], optional
        An entity from which values are randomly taken
    """
    try:
        random_input = [
            [random.choice(filling_entity)
            for j in range(random.randint(0, max_size))]
            for i in range(elems_cnt)
        ]
    except Exception as err:
        logging.critical(f"ERROR while generating input")
        raise err
    else:
        logging.debug(f"Generated input arrs [{', '.join([f'[{len(i)}]' for i in random_input])}] with {elems_cnt=}, {max_size=}, {filling_entity=}")
    return random_input

def check_alpha_order(lst: [[Any]]) -> None:
    """
    Prints if lists elems in alphabetical order.

    Parameters
    ---------- 
    lst : [[Any]]
        Nested list of lists with ascii letters.
    """
    _res = []
    if not all([re.match(r"[^\W\d_]", "".join(elem if type(elem[0]) == str else str(elem))) for elem in lst]):
        lst = []
    try:
        for i, elem in enumerate(lst):
            if elem == sorted(elem) and len(elem) > 0:
                logging.debug(f"Array {i} in alpha order: {elem}")
                print(f"An array of {i} in alphabetical order")
                _res.append(elem)
            else:
                logging.debug(f"Array {i} not in alpha order: {elem}")
    except Exception as err:
        logging.critical("ERROR while checking aplhabet order")
        raise err
    else:
        logging.debug("Procedure check_alpha_order done")
    if input_args.test: return _res
    

def tests():
    test_entities = {
        "ALL_ALPHA_ORDER": {
            "entity": [
                ['I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q'],
                ['m', 'n', 'o', 'p', 'q', 'r', 's', 't'],
                ['x', 'y']
            ],
            "shouldbe": 3
        },
        "SEVERAL_ALPHA_ORDER": {
            "entity": [
                ['k', 'l', 'm', 'n'],
                ['H', 'B']
            ],
            "shouldbe": 1
        },
        "EMPTY_ARR": {
            "entity": [],
            "shouldbe": 0
        },
        "NON_ASCII": {
            "entity": [[1, 2, 3, 4]],
            "shouldbe": 0
        }
    }

    for test_name, test in test_entities.items():
        print(f"Test: {test_name}")
        res = check_alpha_order(test['entity'])
        if len(res) != test['shouldbe']:
            print(f"Test fail. Should be {test['shouldbe']}, not {len(res)}")
        else:
            print("Test success.")

def main():
    # bad solution
    if input_args.test:
        tests()
    else:
        input_entity = generate_input() + [['a', "b", "c"]]
        check_alpha_order(input_entity)
        logging.debug("Main done")



if __name__ == "__main__":
    main()
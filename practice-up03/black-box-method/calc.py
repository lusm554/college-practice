from functools import reduce 
from collections.abc import Callable

INFO = 1
CALC = 2
EXIT = 3

def get_mode() -> int:
    menu = """
    1. Get info about operations.
    2. Calculate/compute operation.
    3. Exit.
    Input number(1, 2, 3).
    """
    print(menu)
    mode = int(input("Action number: "))
    print()
    return mode

def get_input() -> (str, list[int]):
    cmd = input("Which command? ")
    args = list(map(int, input("Input args by coma(like 1, 2, 3): ").split(", ")))
    return (cmd, args)

def get_oper(oper_name: str, opers: dict) -> Callable:
    for op_names, op_entity in opers.items():
        if oper_name in op_names:
            return op_entity["action"]
    raise ValueError(f"Operation {oper_name} not found.")
    

def show_info(opers: dict) -> None:
    opers_names = "\n\n".join([f'{opbody["desc"]}:\n{", ".join(op)}' for op, opbody in opers.items()]) + "\n"
    print(opers_names)

def main():
    opers = {
        ("add", "plus", "sum"): {
            "action": lambda *args: sum(args),
            "desc": "This function adds two numbers"
        },
        ("substract", "minus", "min"): {
            "action": lambda *args: reduce(lambda x, y: x-y, args),
            "desc": "This function subtracts two numbers"
        },
        ("multiply", "mult"): {
            "action": lambda *args: reduce(lambda x, y: x*y, args),
            "desc": "This function multiplies two numbers"
        },
        ("divide", "div"): {
            "action": lambda *args: reduce(lambda x, y: x/y, args),
            "desc": "This function divides two numbers"
        }
    }

    while 1:
        try:
            mode = get_mode()
            if mode == INFO:
                show_info(opers) 
            elif mode == CALC:
                cmd, args = get_input()
                oper = get_oper(cmd, opers)
                res = oper(*args)
                print(f"Result: {res}")
                print()
            elif mode == EXIT:
                exit()
        except Exception as e:
            print(f"Exception: {e}")
            print()
        
        

if __name__ == "__main__":
    main()

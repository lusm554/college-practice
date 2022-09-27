from functools import reduce 

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
            print()
            opers_names = "\n\n".join([f'{opbody["desc"]}:\n{", ".join(op)}' for op, opbody in opers.items()]) + "\n"
            print(opers_names)
            cmd = input("Which command? ")
            args = list(map(int, input("Input args by coma(like 1, 2, 3): ").split(", ")))
            # iter
        except Exception as e:
            print(f"Exception: {e}")
        
        

if __name__ == "__main__":
    main()

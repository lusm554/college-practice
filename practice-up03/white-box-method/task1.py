def check_sum_of2(trgl: dict) -> None:
    for iside, ival in trgl.items():
        for jside, jval in trgl.items():
            if iside == jside: break
            #print(f"{iside=} {jside=}")
            anside = "ABC".replace(iside, "").replace(jside, "")
            if (ival + jval) < trgl[anside]:
                raise ValueError(f"Sum of {jside} and {iside} should not be smaller than {anside} side")

def get_triangle() -> dict:
    trgl = dict(A=None, B=None, C=None) 
    
    for side in trgl.keys():
        raw_val = int(input(f"Input for side {side}: "))
        assert raw_val > 0, "Val should be more then 0"
        trgl[side] = raw_val

    check_sum_of2(trgl)
    return trgl

def show_trgl_info(trgl: dict) -> None:
    target = len(set(trgl.values()))

    a, b, c = trgl.values()
    s = sum(trgl.values()) / 2
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

    print()
    if target == 3:
        print("Разносторонний треугольник.")
    elif target == 2:
        print("Равнобедренный треугольник.")
    elif target == 1:
        print("Равносторонний треугольник.")
    print(f"Площадь треугольника = {area}")

def main():
    try:
        trgl = get_triangle()
        show_trgl_info(trgl)
    except Exception as e:
        raise e
        print(f"While running task1.py error:\n{e}")


if __name__ == "__main__":
    main()


def rename(f):
    words = {
        "числитель": "numerator",
        "знаменатель": "denominator",
        "НОД": "GCD",
        "числительСокращенный": "numeratorAbbreviated",
        "знаменательСокращенный": "denominatorReduced"
    }
    newf = "renamed_"+f

    with open(f, "r") as file:
        content = file.read()
    
    for w_from, w_to in words.items():
        content = content.replace(w_from, w_to)
    
    with open(newf, "w") as file:
        file.write(content)

if __name__ == "__main__":
    filename = "Program.c"
    rename(filename)


with open("t.ttxt", "r") as f:
    r = {}
    tname = ""
    for line in f:
        if ":" in line:
            tname = line[line.find('"')+1:line.rfind('"')]
        if line.count("-") >= 2:
            l = line.split()[1]
            if tname in r:
                r[tname].append(l)
            else:
                r[tname] = []
                r[tname].append(l)

for t, v in r.items():
    fields = [f"    {i} INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL" if ii==0 \
              else f"    {i}" for ii, i in enumerate(v)]
    fields = ",\n".join(fields)
    shape = \
    f"""CREATE TABLE {t} (\n{fields}\n);"""
    print(shape)
    print()
    
    fields = ",".join(["NULL" if i==0 else " " for i, vi in enumerate(v)])
    shape = \
    f"""INSERT INTO {t}\nVALUES\n    ({fields})"""
    print(shape)
    print()
    print()

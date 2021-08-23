import csv

file_path = "test.csv"
d:dict[str,list[dict[str,int]]] = {}
with open(file_path) as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row.get("stdn") in d:
            d[row.get("stdn")].append({row.get("subject"):int(row.get("cp"))})
        else:
            d[row.get("stdn")] = [{row.get("subject"):int(row.get("cp"))}]


for k,v in d.items():
    print(f"Student {k}:")
    sum = 0
    for x in v:
        
        for k,v in x.items():
            sum += v
            print(f"{k:<10}{v:>7} cp")
    print(f"Total: {sum} cp")
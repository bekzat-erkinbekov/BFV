data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")
designations = [i for i in data if i[0] != "0"]
codes = [i for i in data if i[0] == "0"]

operators = dict()
i = 0
while i < len(codes):
    operators[designations[i]] = {codes[i]}
    i += 1

del operators["Fonex"]
del operators["Katel"]

operators["O!"].add("0700")
operators["O!"].add("0500")
operators["Megacom"].add("0999")
operators["Megacom"].add("0555")
operators["Beeline"].add("0222")
operators["Beeline"].add("0777")

for i in operators:
    print(f"{i} - {operators[i]}")

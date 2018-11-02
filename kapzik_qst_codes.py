nb = 0
codes = []

# Pas de Y, pas de H.
# Pas de C, de Q mais un K
#        G         J

# voyelle - consonne - voyelle
voyelles = "AEIOU"
# pas de S pour ne pas confondre avec Z
consonnes = "BDFJKLMNPRTVWXZ"  # 15 lettres
for v1 in voyelles:
    for c in consonnes:
        for v2 in voyelles:
            code = v1+c+v2
            if code not in ["ANU", "AXA", "IPU", "OKU"]:
                nb += 1
                codes.append(code)

# consonne - voyelle - consonne
voyelles = "AEIOU"
consonnes = "BDFJKLMNPRSTVWXZ"  # 16 lettres
for c1 in consonnes:
    for v in voyelles:
        for c2 in consonnes:
            code = c1+v+c2
            if code not in ["BIT", "DIK", "DUK", "FAF", "FUK", "KUL",
                            "NOM", "PUT", "SEX",
                            "TEP", "ZEX", "ZOB", "ZUT"]:
                nb += 1
                codes.append(code)

for code in codes:
    print(code, end=" ")
print()
print(nb)


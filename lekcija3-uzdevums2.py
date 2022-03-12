## Izveido programmu, kas aprēķina suņa vecumu - suņa gados. 1 cilvēka gads ir 4 suņa gadu, bet pirmie 2 ir vienādi ar 10.5 gadiem.

suna_vecums = float(input("Ievadiet suņa vecumu: "))

if suna_vecums <= 2 and suna_vecums >= 0:
    summa = suna_vecums * 5.25
    print("Suņa vecums", summa)

elif suna_vecums > 2:
    summa = suna_vecums * 4 + 2.5
    print("Suņa vecums", summa)


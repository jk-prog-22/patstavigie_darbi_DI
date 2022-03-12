## Izveido programmu, kas nosaka vai lietotāja ievadītais skaitlis ir pāra vai nepāra.

skaitlis = int(input("Ievadi skaitli:"))

if skaitlis % 2 == 0:
    print(skaitlis," = pāra skaitlis")
else:
    print(skaitlis, " = nepāra skaitlis")

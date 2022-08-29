matkustajan_hyttiluokka = input("kerro hyttiluokkasi")

if matkustajan_hyttiluokka == "lux":
    print("parvekkeellinen hytti yläkannella")
elif matkustajan_hyttiluokka == "A":
    print("ikkunallinen hytti autokannen yläpuolella")
elif matkustajan_hyttiluokka == "B":
    print(" ikkunaton hytti autokannen yläpuolella")
elif matkustajan_hyttiluokka == "C":
    print("ikkunaton hytti autokannen alapuolella")
else:
    print("Väärä hyttiluokka")
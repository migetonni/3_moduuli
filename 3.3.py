Sukupuolesi = input("nainen/mies")
hg_arvosi = int(input("Anna hg_arvosi"))

if hg_arvosi >=117 and hg_arvosi <=175 and Sukupuolesi == "nainen":
    print("hemoglobiiniarvo on normaali")
elif hg_arvosi <117 and Sukupuolesi == "nainen":
    print("Hemoglobiiniarvosi on alhainen")
elif hg_arvosi >175 and Sukupuolesi == "nainen":
    print("Hemoglobiiniarvosi on korkea")

if hg_arvosi >=134 and hg_arvosi <=195 and Sukupuolesi == "mies":
    print("Hemoglobiiniarvo on normaali")
elif hg_arvosi <134 and Sukupuolesi == "mies":
    print("Hemoglobiiniarvosi on alhainen")
elif hg_arvosi >195 and Sukupuolesi == "mies":
    print("Hemoglobiiniarvosi on korkea")

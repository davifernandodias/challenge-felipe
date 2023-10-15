name_hero = input("Type Hero name: ")
level_hero = int(input("Type Hero level: "))
if level_hero <= 1000:  # FERRO
    print(f"The hero {name_hero} is at level level Ferro.")

elif level_hero >=1001 and level_hero <=2000: # BRONZE
    print(f"The hero {name_hero} is at level level Bronze.")

elif level_hero >=2001 and level_hero <=5000:  # PRATA
    print(f"The hero {name_hero} is at level level Prata.")

elif level_hero >=6001 and level_hero <=7000: # OURO
    print(f"The hero {name_hero} is at level level Ouro.")

elif level_hero >=7001 and level_hero <=8000: # PLATINA DIAMANTE
    print(f"The hero {name_hero} is at level level Platina Diamante.")

elif level_hero >=8001 and level_hero <=9000: # ASCENDENTE
    print(f"The hero {name_hero} is at level level Ascedente.")

elif level_hero >=9001 and level_hero <=10000: # IMORTAL
    print(f"The hero {name_hero} is at level level Imortal.")

elif level_hero >=10001: # RADIANTE
    print(f"The hero {name_hero} is at level level Radiante.")

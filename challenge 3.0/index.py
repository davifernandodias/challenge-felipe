class hero:   # create objecto hero
    def __init__(self, nome,idade,tipo_hero):
        self.nome = nome
        self.idade = idade
        self.tipo_hero = {
            1 : "GUERREIRO",  # available classes of heroes
            2 : "MAGO",
            3 : "MONGE",
            4 : "NINJA"
        }

        self.tipo_atack = {      # class  atack of hero
        1 : "used sword.",
        2 : "used magic.",
        3 : "used martial arts.",
        4 : "used shuriken."

        }

    def atacar(self):      # class atack hero
     if style_hero_set == 1: 
        print(f"The {self.tipo_hero[style_hero_set].lower()}, attacked using {self.tipo_atack[1]} ")
     if style_hero_set == 2: 
        print(f"The {self.tipo_hero[style_hero_set].lower()}, attacked using {self.tipo_atack[2]} ")
     if style_hero_set == 3: 
        print(f"The {self.tipo_hero[style_hero_set].lower()}, attacked using {self.tipo_atack[3]} ")
     if style_hero_set == 4: 
        print(f"The {self.tipo_hero[style_hero_set].lower()}, attacked using {self.tipo_atack[4]} ")

name_hero_set = input("Type name your Hero: ")    # input name hero
age_hero_set = int(input("Type age your Hero: ")) # input age hero
                                                  # info class heros
molde = """                                       
 [1] GUERREIRO
 [2] MAGO
 [3] MONGE
 [4] NINJA
"""
print(molde)                         

style_hero_set = int(input("Enter type Hero: "))  # get value from class


hero_true = hero(name_hero_set,age_hero_set,style_hero_set) # assign the hero object to a hero_true variable and assign
#                                                              the vestments with the input made
print(f"NAME: {hero_true.nome.upper()}\nAGE: {hero_true.idade}\nCLASS: {hero_true.tipo_hero[style_hero_set]}\n")  
# show the name: calling the variable hero_true assign the vestments name, age, type
hero_true.atacar()
# call the hero_true.attack variable by calling the attack class
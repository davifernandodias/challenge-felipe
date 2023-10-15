def vitorias_derrotas (victory,defeat):
    return victory - defeat 

total_de_vitorias = vitorias_derrotas(int(input("Type win: ")),int(input("Type defeat: "))) # RESULT

def setar_rank(max_vitorias):  # FUNCTION TO SET THE RANK ACCORDING TO TOTAL WINS (VICTORIES - DEFEATS)
 if max_vitorias < 10:
    print(f"The Hero has a balance of {max_vitorias} it is level in Ferro!") # FERRO

 elif max_vitorias >=11 and max_vitorias <=20:
    print(f"The hero has a balance of {max_vitorias} it is level in Bronze!") # BRONZE

 elif max_vitorias >=21 and max_vitorias <=50:
    print(f"The hero has a balance of {max_vitorias} it is level in Prata!") # PRATA

 elif max_vitorias >=51 and max_vitorias <=80:
    print(f"The hero has a balance of {max_vitorias} it is level in Ouro!") # OURO

 elif max_vitorias >=81 and max_vitorias <=90:
    print(f"The hero has a balance of {max_vitorias} it is level in Diamante!") # DIAMANTE

 elif max_vitorias >=91 and max_vitorias <=100:
    print(f"The hero has a balance of {max_vitorias} it is level in Lendário!") # LENDÁRIO

 elif max_vitorias >= 101:
    print(f"The hero has a balance of {max_vitorias} it is level in Imortal!") # IMORTAL


setar_rank(total_de_vitorias)
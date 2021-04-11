import anim
from anim import Pokemon
def agregarPokemon():
    print("bienvenido a la batalla pokemon ")
    nombrePokemon = input("ingrese el nombre del pokemon ")
    puntosAtaque = input("ingrese los puntos de ataque ")
    vidaTotal = input("ingresa la vida total ")

def entrarCombate(pokelist ):
    vita=pokelist[0].vidaTotal
    vita2=pokelist[1].vidaTotal
    pod=pokelist[0].puntosAtaque
    pod2=pokelist[1].puntosAtaque

    
    while vita>0:
        print("el pokemon "+pokelist[0].nombrePokemon+"ataco a "+pokelist[1].nombrePokemon)
        pokelist[1].vidaTotal



if __name__=="__main__":
    opcion=0
    pokelist=[]
    while opcion!=3:
        print("1.inscribir pokemon")
        print("2.entrar al combate")
        print("3.abandonar la batalla")
        opcion= int(input("seleccione una opcion"))
        if opcion==1:
            pokelist.append(agregarPokemon)
        elif opcion==2:
            break
            print("total pokemons:"+str(len(pokelist)))
            pokelist.append(entrarCombate)


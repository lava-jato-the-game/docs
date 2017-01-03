# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
image jair peixe = "jair_peixe.jpg"

define j = Character("Jair", color="#221f66")

label start:

    scene bg room

    show jair peixe
    with fade

    j "Ola brasil. Eu sou o bolsonaro e esse é o meu peixe!!"

    j "Prazer em conhece-lo!"

    j "e Bem vindo ao Lava Jato - tales of corruption"

    return

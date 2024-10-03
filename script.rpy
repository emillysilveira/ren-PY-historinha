# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

define bg = ("images/uma casa simples.png")

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene uma casa simples:
        size(1920, 1080)
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eillen neutro at center with dissolve
   


    # These display lines of dialogue.

    "Ola pessoal !!!"

    e "meu nome e eillen."

    e "vamos conversar!"

menu:

     " O que voce gosta de comer?"
     "chocolate":
         jump chocolate

     "macarrao":
         jump macarrao

label chocolate:

     e "Eu gosto de chocolate!"

     return

label macarrao:
    
     e "Eu gosto de macarrao!"

     return


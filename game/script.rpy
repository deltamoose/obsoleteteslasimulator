# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Elon")

#define pov = Character("[povname]")


# The game starts here.

# python:
    #povname = renpy.input("What is your name?")
    #povname = povname.strip()

    #if not povname:
        #povname = "Pika Chu"

#pov "My name is [povname]!"

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg americana at truecenter

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show elon pray at truecenter

    # These display lines of dialogue.

    e "Hello."

    e "You may know me as the insanely successful billionare Elon Musk."

    show elon smile at truecenter

    e "But there is much more to who I am than just my money."

    e "I think you'll realize that I am much different than the public view."

    show elon what at truecenter

    e "But that's enough about me for now."

    $ player_name = renpy.input("What is your name?")

    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name="Space X"

    e "Wonderful to meet you, %(player_name)s!"

    #povname = renpy.input(prompt, default='your name', allow=None, exclude='{}', length=None, with_none=None,  pixel_width=None)










    # This ends the game.

    return

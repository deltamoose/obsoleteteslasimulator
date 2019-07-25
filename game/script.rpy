# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Elon")

define f = Character("Henrik")


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


    scene bg america at truecenter
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    image elon pray = "elon pray.png"
    show elon pray at truecenter
    with dissolve

    # These display lines of dialogue.

    e "{cps=20}Hello.{/cps=20}"

    e "{cps=20}You may know me as the insanely successful {i}billionare{/i} Elon Musk, {/cps=20}"

    e "{cps=20}founder, CEO, and lead designer of {i}SpaceX{/i}; {/cps=20}"

    e "{cps=20}or as the co-founder, CEO, and product architect of {i}Tesla Motors{/i}. {/cps=20}"

    e "{cps=20}But starting today, I'm just your boss.{/cps=20}"

    image elon smile = "elon smile.png"
    show elon smile at truecenter

    e "{cps=20}There is much more to who I am than just my money.{/cps=20}"

    e "{cps=20}For better or worse, {/cps=20}"
    e "{cps=20}I think you'll realize that I am much different than the public view.{/cps=20}"

    show elon what at truecenter

    e "{cps=30}But that's enough about me for now.{/cps=30}"

    $ player_name = renpy.input("What is your name?")

    $ player_name = player_name.strip()

    if player_name == "Henrik Fisker" or player_name == "henrik fisker":
        $ player_name="not henrik"
        show elon what
        e "{cps=20}You're not Fisker!{/cps=20}"
        e "{cps=20}Don't sully your image with our rival's name!{/cps=20}"

    if player_name == "not henrik" or player_name == "Not Henrik" or player_name == "not Henrik":
        $ player_name="funny one"
        show elon smile
        e "{cps=20}You're a funny one!{/cps=20}"
        e "{cps=20} I think you'll fit in just fine at Tesla!{/cps=20}"

    if player_name == "":
        $ player_name="Space X"

    if player_name == "Elon Musk" or player_name == "elon musk":
        $ player_name="not elon"
        e "{cps=20}I'm flattered, but I assure you{/cps=20}"
        show elon smile
        e "{cps=20}you're not Elon, I am.{/cps=20}"

    if player_name=="not Elon" or player_name=="not elon" or player_name=="Not Elon":
        $ player_name="Doppel Ganger"
        show elon smile
        e"{cps=20}You're a funny one!{/cps=20}"
        e"{cps=20}I think you'll fit in just fine at Tesla!{/cps=20}"


    show elon standing


    e "{cps=20}Wonderful to meet you, %(player_name)s!{/cps=20}"

    e "{cps=20}I hope you enjoy working with me at Tesla.{/cps=20}"

    e "{cps=40}Well, see you {i}tomorrow{/i}!{/cps=40}"


    show henrik intimidating

    f "{cps=20}I'm glad he's finally gone.{/cps=20}"

    f "{cps=30}'Who am {i}I{/i}?' You ask?{/cps=30}"

    f "{cps=20}That is irrelevant.{/cps=20}"

    f "{cps=30}But I'll tell you what is not irrelevant:{/cps=30}"

    f "{cps=10}{i}Tesla Automotive's highly confidential car blueprints{/i}{/cps=10}"

    f "{cps=20}It's rather simple.{/cps=20}"

    f "{cps=10}You {s}steal{/s} ahem, {i}retrieve{/i} the plans for me and I'll see to it that you never have to work a single day again.{/cps=10}"

    f "{cps=20}Here is my {i}card{/i}.{/cps=20}"

    f "{cps=20}Call me and tell me what you think.{/cps=20}"

    menu:
        "Accept Henrik's offer immediately":
            f "{cps=30}I look forward to working with you, %(player_name)s{/cps=30}"

        "Reject Henrik's ridiculous proposal.  You are a loyal Tesla employee!":
            f "{cps=30} I see...{/cps=30}"
            f "{cps=30} You are certainly welcome to reconsider.{/cps=30}"


    label after_menu:

        "{cps=25}My meeting with Henrik put me on edge, but I steeled myself to face what tommorrow would bring.{/cps=25}"
        










    #povname = renpy.input(prompt, default='your name', allow=None, exclude='{}', length=None, with_none=None,  pixel_width=None)










    # This ends the game.

    return

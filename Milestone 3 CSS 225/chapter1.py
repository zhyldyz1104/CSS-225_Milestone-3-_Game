import globalvariables


def start_game():
    print("Player starts in Andalusian village.")


def talk_to_villagers():
    talk = input(f"{globalvariables.username},Do you want to talk to villagers? ")
    if talk == "yes":
        print("Talking to villagers...")
        talk = True
    else:
        print("Continue")
        talk = False
    return talk  # returns the boolean True or alse


def gain_knowledge_of_omens():
    print("Gained knowledge of omens.")


def visit_gypsy():
    visit = input("Do you wanna visit gypsy?")
    if visit == "yes":
        print("Visiting gypsy...")
        visit = True
    else:
        print("Continue")
        visit = False
    return visit


def receive_prophecy():
    print(f"{globalvariables.username},Received prophecy about treasure.")


def sell_sheep():
    sell = input(f"{globalvariables.username},Do you wanna sell sheep?")
    if sell == "yes":
        print("Selling sheep...")
        sell = True
    else:
        print("Continue")
        sell = False

    return sell


def gain_gold():
    print("Gained gold from selling sheep.")


def depart_for_desert():
    print("Departing for the desert... End of Chapter 1.")


def play_chapter():
    print(f"{globalvariables.username}, you are a simple shepherd boy in Andalusia.")
    print("You dream of something more — a treasure, a journey, a destiny.")
    print("Your story begins in a quiet village surrounded by hills and sheep.")
    # Collecting all functions so i can use only one line to call chapter 1 in Main.py
    if talk_to_villagers():
        gain_knowledge_of_omens()
    if visit_gypsy():
        receive_prophecy()
    if sell_sheep():
        gain_gold()
    depart_for_desert()

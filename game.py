import random

class Game:
    def __init__(self):
        response = input("\nWelcome to Harry Potter Simulator! Enter your name and press enter to start your wizarding Journey! " )
        player_1 = Player(response)
        

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        print(f"\nWelcome {self.name}! Remember, it's very important that you spell your spells correctly. Who knows what might happen if you don't!\n")

class Encounter:
    def __init__(self, prompt, spells, outcomes):
        self.prompt = prompt
        self.spells = spells
        self.outcomes = outcomes

# Define all encounters
encounter_1 = Encounter("You have an intrusive though about Professor Snape and you’d like to write it down, but your quill is on the other side of the room.", 
("Accio", "Aguamenti", "Lumos", "Wingardium Leviosa"), 
("“Accio quill!” you shout. The quill neatly flies into your hand.", "Aguamenti is cast", "Lumos is cast", "Wingardium Leviosa is cast" ))
encounter_2 = Encounter("You have a sudden urge to go for a midnight hike in the Forbidden Forest. Fantastic idea! You gather all of your supplies: wand, hiking boots, Bernie Bott’s Every Flavor Trail Mix… but wait! You forgot the water!", 
("Lumos", "Aguamenti", "Avada Kedavra", "Expecto Patronum"), 
(1, 2, 3, 4))

# Initialize the game and get player 1 input
game_1 = Game()

# Randomly generate the order of encounters
encounter_list = [encounter_1, encounter_2]
random.shuffle(encounter_list)

# Iterate through encounters
for encounter in encounter_list:
    print(encounter.prompt + "\n")
    rand_spells = list(encounter.spells)
    random.shuffle(rand_spells)
    for spell in rand_spells:
        print(spell)
    print("\n")
    choice = input("Which spell do you choose? ").capitalize()
    if choice == encounter.spells[0]:
        print(encounter.outcomes[0])
    elif choice == encounter.spells[1]:
        print(encounter.outcomes[1])
    elif choice == encounter.spells[2]:
        print(encounter.outcomes[2])
    elif choice == encounter.spells[3]:
        print(encounter.outcomes[3])
    else:
        choice = random.randint(0,3)
        print(f"You babble incoherently but somehow manage to cast {encounter.spells[choice]}.")
        print(encounter.outcomes[choice])
import random

class Game:
    def __init__(self):
        response = str(input("\nWelcome to Harry Potter Simulator! Enter your name and press enter to start your wizarding Journey! " ))
        self.player_1 = Player(response)
        print(f"\nWelcome {self.player_1.name}! Remember, it's very important that you spell your spells correctly. Who knows what might happen if you don't!")
        input("\n>>>>> Press enter to continue. ")
        print("********************")

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

class Encounter:
    def __init__(self, prompt, spells, outcomes):
        self.prompt = prompt
        self.spells = spells
        self.outcomes = outcomes

def final_ranking(score):
    print(f"Thanks for playing! Your final score is {score}. This gives you the title of: ")
    if score == 40:
        print("Basically Dumbledore but better!")
    elif score < 40 and score >= 36:
        print("Hero of Hogwarts!")
    elif score < 35 and score >= 32:
        print("Expert Wizard!")
    elif score < 40 and score >= 28:
        print("Skilled Duelist!")
    elif score < 40 and score >= 24:
        print("Problem-Solver!")
    elif score < 40 and score >= 20:
        print("1st Year Neville Longbottom!")
    elif score < 16:
        print(f"You're a wizard {game.player_1.name}! Wait, no you're not, you're just {game.player_1.name}!")
    print("\n")
    
# Define all encounters
encounter_1 = Encounter("\nYou have an intrusive though about Professor Snape and you’d like to write it down, but your quill is on the other side of the room.", 
("Accio", "Aguamenti", "Lumos", "Wingardium Leviosa"), 
("“Accio quill!” you shout. The quill neatly flies into your hand.", 
"“Aguamenti!” Your goblet of water overflows, floating the quill to your feet. You have the quill but your socks are wet.", 
"“Lumos!” Your wand lights up the room. Cool! but you’re not sure why you did that.", 
"“Wingardium Levi-OH-sah!” Your inkwell soars into the air, dumping its contents all over your desk. Nice!" ))

encounter_2 = Encounter("\nYou have a sudden urge to go for a midnight hike in the Forbidden Forest. Fantastic idea! You gather all of your supplies: wand, hiking boots, Bernie Bott’s Every Flavor Trail Mix… but wait! You forgot the water!", 
("Lumos", "Aguamenti", "Avada Kedavra", "Expecto Patronum"), 
("“Lumos!” Your wand lights up the room, and you see you did, in fact, already pack your water.", 
"“Aguamenti!” The front pocket on your backpack fills with water.", 
"“Avada Kedavra!” A burst of green light shoots from the tip of your wand and strikes a nearby ant crawling on the floor. The ant emits a tiny scream and instantly drops to the ground, motionless. A wave of guilt washes over you as you realize the consequences of your actions.", 
"“Expecto Patronum” Your patronus, a sloth, appears in front of you. It does nothing and now you’re tired and want chocolate."))

encounter_3 = Encounter("\n“Muggle cars are so cool!” you think to yourself. You decide to head to the local used car lot and get your own sweet ride. You scan the lot when suddenly… a blue Ford Anglia! You decide to purchase it, but then you remember you barely have any money. Oops!",
("Alohomora", "Wingardium Leviosa", "Mimblewimble", "Confundo"),
("“Alohomora!” The door lock pops open. You drive away in your new ride, destined to be the coolest person at Hogwarts.",
"“Wingardium Levi-OH-sah!” The car lifts off the ground. You take it with you and decide to open the lock later.",
"A salesman approaches as you cast: “Mimblewimble!”. You tell the salesman you’ll buy the car for 500 galleons under market price. The salesman mumbles aggressively, but ultimately decides to draw up the paperwork for you.",
"A salesman approaches as you cast: “Confundo!” The salesman is oblivious to your inclination to purchase the car and instead confuses you with the fast food delivery man he was expecting. He runs you off the lot screaming at you about a sandwich."))

encounter_4 = Encounter("\nYou lay down to take a nap when suddenly, you remember you’re late for Quidditch practice! You rush to the chest at the foot of the bed to collect your gear when you spot a comically small spider on the latch. EEEEEEEE!",
("Avada Kedavra", "Confundo", "Wingardium Leviosa", "Accio"),
("“Avada Kadavra!” A burst of green light shoots from the end of your wand. The spider is immediately dispatched. You turn to your roomate and exclaim “I saved us from the spider!”. Your roommate pees their pants.",
"“Confundo!” The spider furrows it brow and apologizes “Sorry, I must have the wrong house!” and scurries away.",
"“Wingardium Levi-OH-sah!” The spider soars into the air directly over your head. You quickly reach under the spider to grab your broomstick and run away screaming.",
"“Accio Spider!” The spider flies off the chest and directly onto your forehead. You pass out from fright and wake up in the medical ward."))

encounter_5 = Encounter("\nYou’ve been camped out all day for The Weird Sisters concert. As you arrive at the door to present your ticket to the bouncer, you realize you’ve left it in you dorm room.",
("Confundo", "Incendio", "Decendo", "Accio"),
("“Confundo!” The bouncer becomes confused and wanders off into the crowd. Kind of a mean thing to do but you can get into the concert now!",
"“Incendio!” You set the bouncer’s pants ablaze. He tries to pull off his pants and falls on to the ground. That was a really mean thing to do but at least you got into the concert.",
"“Decendo” The bouncers pants are thrusted onto the ground. He looks at you angrily and chased you as you run into the concert hall.",
"You point your wand in the direction of your dorm room. “Accio ticket!” Nothing happens. The bouncer throws you out of line. While walking back to your room, your ticket soars through the air and eventually slaps you in the face, but the concert is over already."))
# Initialize the game and get player 1 input
game = Game()

# Randomly generate the order of encounters
encounter_list = [encounter_1, encounter_2, encounter_3, encounter_4, encounter_5]
random.shuffle(encounter_list)

# Iterate through encounters
for encounter in encounter_list:
    print(encounter.prompt + "\n")
    rand_spells = list(encounter.spells)
    random.shuffle(rand_spells)
    for spell in rand_spells:
        print(spell)
    choice = input("\nWhich spell do you choose? ").title()
    if choice == encounter.spells[0]:
        print(encounter.outcomes[0])
        game.player_1.score += 3
    elif choice == encounter.spells[1]:
        print(encounter.outcomes[1])
        game.player_1.score += 2
    elif choice == encounter.spells[2]:
        print(encounter.outcomes[2])
        game.player_1.score += 1
    elif choice == encounter.spells[3]:
        print(encounter.outcomes[3])
        game.player_1.score += 0
    else:
        choice = random.randint(0,3)
        print(f"You babble incoherently but somehow manage to cast {encounter.spells[choice]}.")
        print(encounter.outcomes[choice])
        game.player_1.score += abs(choice - 3)
    input("\n>>>>> Press enter to continue. ")
    print("********************")

# Multiplying by two since I'm too lazy to write 5 more scenarios
final_ranking(game.player_1.score*2)
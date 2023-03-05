import time
import random
import os


def print_slow(text):
    message = ""
    for letter in text:
        time.sleep(0.001)
        print(letter, end = "", flush = True)


class Player:
    messages = {
        "police" : {
            "move" : ["I'm on the move!", "Pursuit in progress!", "I'm getting closer."],
            "shoot" : ["Shots fired!", "I think I hit them!", "That was so shaky!"],
            "cover" : ["I'm taking cover!", "Cover me!", "Hyaah! *Jumps behind cover*"]
        },
        "robber": {
            "move": ["This pig is still chasing me!", "Won't they quit it?", "I'm running as fast as I can!"],
            "shoot": ["Take this pig!", "I hope you like holes in your shirt!", "Don't move while I shoot!"],
            "cover": ["I'll hide here for a bit...", "Can they see me here?", "Woah! I better take cover"]
        },
    }

    def __init__(self, name, occupation, distance = 0):
        self.name = name
        self.health = ["💛", "💛", "💛", "💛", "💛"]
        self.ammo = ["💥", "💥", "💥", "💥", "💥"]
        self.energy = ["⚡", "⚡", "⚡", "⚡", "⚡"]
        self.occupation = occupation
        self.distance = distance
        self.cover = False

    def roll_dice(self):
        die = ["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","8️⃣","9️⃣","🔟"]
        result = random.randint(0, 9)
        for i in range(10):
            face = random.choice(die)
            print('\r' + face, end='')
            time.sleep(0.1)
        print("\r" + " "*len(die[result]), end="")
        print(die[result])
        return result + 1

    def move(self):
        distance = self.roll_dice()
        if "⚡" in self.energy:
            self.distance += distance
            self.energy.remove("⚡")
            self.energy.append("  ")
            print_slow("You moved " + str(distance) + " steps!\n")
        else:
            print_slow("I'm too tired to move, I better take cover...")
            self.take_cover()
        time.sleep(1)

    def shoot(self, target):
        if "💥" in self.ammo:
            self.ammo.remove("💥")
            self.ammo.append("  ")
            if self.roll_dice() > 5:
                target.health.remove("💛")
                target.health.append("  ")
                print("\nBANG! 💥")
                print("\nIT'S A HIT!")
            else:
                print("\nYOU MISSED!")
        else:
            print_slow("\nI have no ammo! I'll take cover!")
            self.take_cover()
        time.sleep(1)

    def take_cover(self):
        print("\n*You take cover*")
        if "💥" * 5 not in self.ammo:
            for i in range(len(self.ammo)):
                self.ammo.pop()
            while len(self.ammo) < 5:
                    self.ammo += "💥"
        if "⚡" * 5 not in self.energy:
            for i in range(len(self.energy)):
                self.energy.pop()
            while len(self.energy) < 5:
                self.energy += "⚡"
        # while len(self.energy) < 5:
        #     self.energy += "⚡"
        # time.sleep(1)






players = []


def game_over(player):
    loser = police if player.occupation == "robber" else robber

    if player.occupation == "police":
        if "💛" not in loser.health:
            print("\nOfficer {} killed Robber {}! \nYou recovered all the money!".format(
                player.name, loser.name))
        else:
            print("\nOfficer {} caught the Robber {}!\nYou are going to jail, punk!".format(player.name, loser.name))
    else:
        if "💛" not in loser.health:
            print("\Robber {} killed Officer {} \nYou got away with the money!".format(
                player.name, loser.name))
        else:
            print("\Robber {} has escaped from Officer {} \nYou got away with the money!".format(
                player.name, loser.name))
    print("\n\n\nGAME OVER")
    input()

def intro_scene():
    print_slow(
        "We have a fugitive on the run!\nWe need an officer in the area.\nReport for duty and state your name!\n")
    police = Player(input("Enter your name: "), "police")
    players.append(police)
    print_slow(
        "\nOk Officer {}, you are now officially on pursuit!\n".format(police.name))
    print_slow("The perp you are trying to catch is called...\n")
    robber = Player(input("Enter your name: "), "robber")
    players.append(robber)
    print_slow("\n{} has stolen a bunch of stuff,\nso you better catch them,\nbefore they steal more stuff I guess...\n".format(robber.name))
    time.sleep(2)
    os.system("cls")

def player_info():

    target = robber
    player = police


    player_health = " ".join(player.health)
    player_ammo = " ".join(player.ammo)
    player_energy = " ".join(player.energy)
    target_health = " ".join(target.health)
    target_ammo = " ".join(target.ammo)
    target_energy = " ".join(target.energy)
    print("""
                    Officer {player}'s Stats       VS      Robber {target}'s Stats
            ———————————————————————————————————————————————————————————————————————
            Health |{player_health}                       {target_health}
            Ammo   |{player_ammo}                       {target_ammo}
            Energy |{player_energy}                       {target_energy}
          """.ljust(500, " ").format(
        player = player.name,
        player_health = player_health, 
        player_ammo = player_ammo, 
        player_energy = player_energy,
        target = target.name,
        target_health = target_health,
        target_ammo = target_ammo,
        target_energy = target_energy
        ))
    
def player_distance():
    starting_distance = 25
    player_distance = starting_distance + robber.distance - police.distance
    return player_distance

def make_decision(player, target):
    target = robber if player.occupation == "police" else police
    if len(player.health) > 0 and len(target.health) > 0:
        player_info()
        print(
            """
            What will you do next?

            1. Move
            2. Shoot
            3. Cover

            Type "1", "2" or "3"
            """
        )

        decision = input("Enter choice: ")

        if decision == "1":
            if player.occupation == "police":
                print("Officer {player} chose to chase Robber {target}".format(player = player.name, target = target.name))
            else:
                print("Robber {player} chose to escape from Officer {target}".format(
                    player=player.name, target=target.name))
            player.move()
            print(random.choice(player.messages[player.occupation]["move"]))

        elif decision == "2":     
            if player.occupation == "police":
                print("Officer {player} chose to shoot Robber {target}".format(
                    player=player.name, target=target.name))
            else:
                print("Robber {player} chose to shoot Officer {target}".format(
                    player=player.name, target=target.name))
            print(random.choice(player.messages[player.occupation]["shoot"]))
            player.shoot(target)

        elif decision == "3":
            if player.occupation == "police":
                print("Officer {player} chose to cover from Robber {target}".format(
                    player=player.name, target=target.name))
            else:
                print("Robber {player} chose to cover from Officer {target}".format(
                    player=player.name, target=target.name))
            player.take_cover()
            print(random.choice(player.messages[player.occupation]["cover"]))

        else:
            print("Please type either \"1\", \"2\" or \"3\"")
            make_decision(player, target)
    return player


def game_logic(player):
    target = robber if player.occupation == "police" else police
    distance = player_distance()
    while "💛" in player.health and "💛" in target.health:
        for player in players:
            if "💛" in player.health and 0 < distance < 50:
                print("—" * 40)
                print("It's "+ player.name + "'s Turn")
                print("—" * 40)
                print("Distance between players: ", distance)
                print("{}'s travelled distance: ".format(player.name), player.distance)
                winner = make_decision(player, target)
                distance = player_distance()
                time.sleep(2)
                os.system("cls")
            elif 0 >= distance or distance >= 50 or "💛" not in player.health:
                    game_over(winner)
                    return

intro_scene()
police = players[0]
robber = players[1]
game_logic(police)
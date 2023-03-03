import time
import random
import os


def print_slow(text):
    message = ""
    for letter in text:
        time.sleep(0.03)
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
        result = random.randint(8, 9)
        for i in range(10):
            face = random.choice(die)
            print('\r' + face, end='')
            time.sleep(0.1)
        print("\r" + " "*len(die[result]), end="")
        print(die[result])
        return result + 1

    def move(self):
        distance = self.roll_dice()
        self.distance += distance
        self.energy.pop()
        if len(self.energy) > 0:
            print_slow("You moved " + str(distance) + " steps!\n")
        else:
            print_slow("I'm too tired to move, I better take cover...")
            self.take_cover()
        time.sleep(1)

    def shoot(self, target):
        self.ammo.pop()
        if len(self.ammo) > 0:
            if self.roll_dice() > 6:
                target.health.pop()
                print("\nBANG! 💥")
                print("IT'S A HIT!")
            else:
                print("\nYOU MISSED!")
        else:
            print_slow("I have no ammo! I'll take cover!")
            self.take_cover()
        time.sleep(1)

    def take_cover(self):
        print("*You take cover")
        while len(self.ammo) < 5:
            self.ammo += "💥"
        while len(self.energy) < 5:
            self.energy += "⚡"
        time.sleep(1)






players = []


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


def player_info(player, target):

    print_slow(("\nIt's " + str(player.name) + "'s turn\n").upper())
    print("\nHealth: ", (' '.join(map(str, player.health))), "\nAmmo: ",
          (' '.join(map(str, player.ammo))), "\nEnergy: ", (' '.join(map(str, player.energy))))
    if player.occupation == "police":
        total_distance = target.distance + 20 - player.distance
        print("\nDistance to robber: ", total_distance)
        return total_distance
    else:
        total_distance = player.distance + 20 - target.distance
        print("\nDistance from police: ", total_distance)
        return total_distance


def make_decision(player, target):
    print_slow(
        "\nWhat will you do now?\n1. Move 🏃‍♂️\n2. Shoot 💥\n3. Take Cover 🛡\n"
    )
    decision = input("Enter answer: ")
    if decision == "1":
        if len(player.energy) > 0:
            message = random.choice(player.messages[player.occupation]["move"])
            time.sleep(1)
            player.move()
        else:
            message = "I'm too tired to move!"
    elif decision == "2":
        if len(player.ammo) > 0:
            message = random.choice(
                player.messages[player.occupation]["shoot"])
            time.sleep(1)
            player.shoot(target)
        else:
            message = "Out of ammo!"
    elif decision == "3":
        message = random.choice(
            player.messages[player.occupation]["cover"])
        time.sleep(1)
        player.take_cover()
    else: 
        print_slow("\nPlease select a valid option.\n Type either 1, 2 or 3")
        make_decision(player, target)
    print(str(player.name).upper() + " SAYS: " + str(message).upper())
    time.sleep(2)
    os.system("cls")


def game_logic():
    while len(police.health) > 0 and len(robber.health) > 0 and 1 <= player_info(player, target).total_distance <= 50:
        for player in players:
            target = None
            for p in players:
                if p != player:
                    target = p
                    break
            while len(player.health) > 0:
                player_info(player, target)
                make_decision(player, target)
                break

def game_over():
    print("\nThe game has ended")

intro_scene()

police = players[0]
robber = players[1]

game_logic()
game_over()



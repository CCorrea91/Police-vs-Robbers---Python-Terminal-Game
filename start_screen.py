import os
from sounds import play_sound, sound_library
    
# Intro screen
def start_sequence():
    start_screen = """
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░██████╗░░█████╗░██╗░░░░░██╗░█████╗░███████╗░░░░░░
░░░░░░░██╔══██╗██╔══██╗██║░░░░░██║██╔══██╗██╔════╝░░░░░░
░░░░░░░██████╔╝██║░░██║██║░░░░░██║██║░░╚═╝█████╗░░░░░░░░
░░░░░░░██╔═══╝░██║░░██║██║░░░░░██║██║░░██╗██╔══╝░░░░░░░░
░░░░░░░██║░░░░░╚█████╔╝███████╗██║╚█████╔╝███████╗░░░░░░
░░░░░░░╚═╝░░░░░░╚════╝░╚══════╝╚═╝░╚════╝░╚══════╝░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░██╗░░░██╗░██████╗░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░██║░░░██║██╔════╝░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░╚██╗░██╔╝╚█████╗░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░╚████╔╝░░╚═══██╗░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░╚██╔╝░░██████╔╝░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░╚═╝░░░╚═════╝░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
██████╗░░█████╗░██████╗░██████╗░███████╗██████╗░░██████╗
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔════╝
██████╔╝██║░░██║██████╦╝██████╦╝█████╗░░██████╔╝╚█████╗░
██╔══██╗██║░░██║██╔══██╗██╔══██╗██╔══╝░░██╔══██╗░╚═══██╗
██║░░██║╚█████╔╝██████╦╝██████╦╝███████╗██║░░██║██████╔╝
╚═╝░░╚═╝░╚════╝░╚═════╝░╚═════╝░╚══════╝╚═╝░░╚═╝╚═════╝░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                                        ʙʏ Cᴀʀʟᴏs Cᴏʀʀᴇᴀ
"""
    print(start_screen)
    return

#Ask player to hear the game rules
def how_to_play():
    
    rules = """
        HOW TO PLAY:
            1. You need 2 players to play
            2. Each player starts with 5 Hearts, 5 Ammo & 5 Energy
            3. Choose to Move, Shoot, or Go behind cover on your turn
            4. Moving consumes 1 Energy, shooting consumes 1 Ammo and reduces opponent's health by 1
            5. Going behind cover fully restores Ammo and Energy, and avoids damage from being shot
            6. Moving or shooting automatically makes you lose cover
            7. The game ends when a player loses all their hearts or the distance between players reaches 0 or 50.
            
        RULES:
            1. There is a 50%\ chance to hit your opponent when shooting
            2. The first player to lose all their Health loses.
            3. If the distance between players reaches 0, the police officer catches the robber.
            4. If the distance between player reaches 50, the robber escapes the police officer
            5. Health can't be restored
        """
        
        
    decision = input(
        "Hit Enter to continue... \ntype \"1\" to read the rules & learn how to play.\n")
    
    play_sound(sound_library["press_enter"])
    os.system("cls")
    
    if decision == "1":
        print(rules)
        start_game = input("Press Enter to start the game or\nPress \"2\" to go back\n")
        play_sound(sound_library["press_enter"])
        
        if start_game == "2":
            os.system("cls")
            start_sequence()
            how_to_play()
            
    os.system("cls")
    return


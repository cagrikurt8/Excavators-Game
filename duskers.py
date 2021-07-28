import datetime
import os.path
import sys
import time
import random


def create_file():
    if os.path.isfile("high_scores.txt") is False:
        file = open("high_scores.txt", 'w')
        file.close()

    if os.path.isfile("save_file.txt") is False:
        with open("save_file.txt", "w") as file:
            for i in range(2):
                file.write("empty\n")
            file.write("empty")


class Excavators:

    def __init__(self):
        self.titanium = 0
        self.robots = 3
        self.titanium_scan = False
        self.enemy_encounter_scan = False
        self.player_name = "User"
        self.GAME_NAME = """\
            
███████╗██╗░░██╗░█████╗░░█████╗░██╗░░░██╗░█████╗░████████╗░█████╗░██████╗░░██████╗
██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██║░░░██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔════╝
█████╗░░░╚███╔╝░██║░░╚═╝███████║╚██╗░██╔╝███████║░░░██║░░░██║░░██║██████╔╝╚█████╗░
██╔══╝░░░██╔██╗░██║░░██╗██╔══██║░╚████╔╝░██╔══██║░░░██║░░░██║░░██║██╔══██╗░╚═══██╗
███████╗██╔╝╚██╗╚█████╔╝██║░░██║░░╚██╔╝░░██║░░██║░░░██║░░░╚█████╔╝██║░░██║██████╔╝
╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚═════╝░
                         """
        self.GAME_HUB = f"""\
║════════════════════════════════════════════════════════════════════════════════║
╬   ╬╬╬╬╬╬╬   ╬     ╬   ╬╬╬╬╬╬╬   ╬     ╬   ╬╬╬╬╬╬╬   ╬     
╬╬╬╬╬     ╬╬╬╬╬     ╬╬╬╬╬     ╬╬╬╬╬     ╬╬╬╬╬     ╬╬╬╬╬     
    ╬╬╬╬╬╬╬             ╬╬╬╬╬╬╬             ╬╬╬╬╬╬╬         
   ╬╬╬   ╬╬╬           ╬╬╬   ╬╬╬           ╬╬╬   ╬╬╬        
   ╬       ╬           ╬       ╬           ╬       ╬        
   ╬       ╬           ╬       ╬           ╬       ╬        
   ╬       ╬           ╬       ╬           ╬       ╬        
   
   Titanium: {self.titanium}
║════════════════════════════════════════════════════════════════════════════════║
║                  [Ex]plore                          [Up]grade                  ║
║                  [Save]                             [M]enu                     ║
║════════════════════════════════════════════════════════════════════════════════║
                        """
        self.GAME_MENU = """\
                             ║════════════════════════║
                             ║           MENU         ║
                             ║                        ║
                             ║[Back] to game          ║
                             ║ Return to [Main] Menu  ║
                             ║[Save] and exit         ║
                             ║[Exit] game             ║
                             ║════════════════════════║
                         """
        self.GAME_SAVE = """\
                            ║══════════════════════════════║
                            ║    GAME SAVED SUCCESSFULLY   ║
                            ║══════════════════════════════║
                         """
        self.GAME_LOAD = """\
                            ║══════════════════════════════║
                            ║    GAME LOADED SUCCESSFULLY  ║
                            ║══════════════════════════════║
                         """
        self.UPGRADE = """\
                         ║══════════════════════════════║
                         ║         UPGRADE STORE        ║
                         ║                        Price ║
                         ║[1] Titanium Scan         250 ║
                         ║[2] Enemy Encounter Scan  500 ║
                         ║[3] New Robot            1000 ║
                         ║                              ║
                         ║[Back]                        ║
                         ║══════════════════════════════║
                       """
        self.GAME_OVER = """\
                         ║══════════════════════════════║
                         ║          GAME OVER!          ║
                         ║══════════════════════════════║
                        """

        self.args = sys.argv

        try:
            self.seed = self.args[1]
        except IndexError:
            self.seed = 0
        try:
            self.min = float(self.args[2])
        except IndexError:
            self.min = 0
        try:
            self.max = float(self.args[3])
        except IndexError:
            self.max = 0
        try:
            self.locations = self.args[4]
        except IndexError:
            self.locations = "High,street/Green,park/Destroyed,Arch"

        self.locations = self.locations.split("/")
        self.locations = [location.replace(",", " ") for location in self.locations]
        self.location_options = list()
        self.file_lines = open("save_file.txt", "r").readlines()

    def welcome_screen(self):
        self.print_animation(self.GAME_NAME)
        self.print_animation("\n[New] Game\n[Load] Game\n[High] Scores\n[Help]\n[Exit]")

        print()

        self.print_animation("\nYour command:")
        player_choice = input().lower()

        print()

        if player_choice == "new":
            self.new()

        elif player_choice == "load":
            self.load()

        elif player_choice == "high":
            self.high_scores()

        elif player_choice == "help":
            self.help()
            self.welcome_screen()

        elif player_choice == "exit":
            self.print_animation("\nThanks for playing, bye!")

        else:
            self.print_animation("\nInvalid input")

    def print_animation(self, output, wait="short"):
        for c in output:
            sys.stdout.write(c)
            if wait == "short":
                time.sleep(self.min)
            elif wait == "long":
                time.sleep(self.max)

    def new(self):
        self.titanium = 0
        self.robots = 3
        self.titanium_scan = False
        self.enemy_encounter_scan = False
        self.update_hub()

        self.print_animation("Enter your name:")
        player_name = input()
        self.player_name = player_name
        
        print()

        self.print_animation(f"Greetings, commander {player_name}")
        self.print_animation("\nAre you ready to begin?")
        self.print_animation("\n\t[Yes] [No] Return to [Main] Menu")

        print()

        self.print_animation("\nYour command:")
        player_choice = input().lower()

        print()

        while player_choice == "no":
            self.print_animation("\nHow about now.")
            self.print_animation("\nAre you ready to begin?")
            self.print_animation("\n\t[Yes] [No] Return to [Main] Menu")

            print()

            self.print_animation("\nYour command:")
            player_choice = input().lower()

            print()

        if player_choice == "main":
            self.welcome_screen()

        elif player_choice == "yes":
            self.play()

    def load(self):
        self.location_options.clear()
        self.print_animation("\tSelect save slot:")
        save_slots = list()

        self.update_file_lines()

        print()

        for idx, slot in enumerate(self.file_lines):
            self.print_animation(f"\t\t[{idx + 1}] {slot}")
            save_slots.append(slot.strip("\n"))

        print("\n")

        player_choice = input("Your command:").lower()

        if player_choice == "1":
            if save_slots[0] == "empty":
                self.print_animation("Empty slot!\n\n")
                self.load()
            else:
                user_data = save_slots[0].split()
                self.player_name = user_data[0]
                self.titanium = int(user_data[2])
                self.robots = int(user_data[4])

                if len(user_data) == 11:
                    if user_data[10] == "enemy_info":
                        self.enemy_encounter_scan = True
                    elif user_data[10] == "titanium_scan":
                        self.titanium_scan = True
                elif len(user_data) == 12:
                    self.enemy_encounter_scan = True
                    self.titanium_scan = True

                self.print_animation(self.GAME_LOAD)
                self.print_animation(f"\nWelcome back, commander {self.player_name}!")
                self.update_hub()
                self.play()

        elif player_choice == "2":
            if save_slots[1] == "empty":
                self.print_animation("Empty slot!\n\n")
                self.load()
            else:
                user_data = save_slots[1].split()
                self.player_name = user_data[0]
                self.titanium = int(user_data[2])
                self.robots = int(user_data[4])

                if len(user_data) == 11:
                    if user_data[10] == "enemy_info":
                        self.enemy_encounter_scan = True
                    elif user_data[10] == "titanium_scan":
                        self.titanium_scan = True
                elif len(user_data) == 12:
                    self.enemy_encounter_scan = True
                    self.titanium_scan = True

                self.print_animation(self.GAME_LOAD)
                self.print_animation(f"\nWelcome back, commander {self.player_name}!")
                self.update_hub()
                self.play()

        elif player_choice == "3":
            if save_slots[2] == "empty":
                self.print_animation("Empty slot!\n\n")
                self.load()
            else:
                user_data = save_slots[2].split()
                self.player_name = user_data[0]
                self.titanium = int(user_data[2])
                self.robots = int(user_data[4])

                if len(user_data) == 11:
                    if user_data[10] == "enemy_info":
                        self.enemy_encounter_scan = True
                    elif user_data[10] == "titanium_scan":
                        self.titanium_scan = True
                elif len(user_data) == 12:
                    self.enemy_encounter_scan = True
                    self.titanium_scan = True

                self.print_animation(self.GAME_LOAD)
                self.print_animation(f"\nWelcome back, commander {self.player_name}!")
                self.update_hub()
                self.play()

        elif player_choice == "back":
            self.welcome_screen()

    def play(self):
        self.print_animation("\n" + self.GAME_HUB)
        condition = True

        while condition:
            self.print_animation("\nYour command:")
            player_choice = input().lower()

            if player_choice == "m":
                self.print_animation("\n" + self.GAME_MENU)

                self.print_animation("\nYour command:")
                player_choice = input().lower()

                if player_choice == "back":
                    self.play()
                    condition = False

                elif player_choice == "main":
                    self.welcome_screen()
                    condition = False

                elif player_choice == "save":
                    self.save(save_exit=True)
                    condition = False

                elif player_choice == "exit":
                    self.print_animation("\nThanks for playing, bye!")
                    condition = False

            elif player_choice == "ex":
                self.explore()
                condition = False

            elif player_choice == "up":
                self.upgrade()
                condition = False

            elif player_choice == "save":
                self.save()
                condition = False

            else:
                self.print_animation("\nInvalid input\n")

    def explore(self):
        location_num_to_explore = random.randint(1, 9)
        location_titanium = dict()
        encounter_rates = dict()
        loop = True

        while loop:
            condition = True

            if len(self.location_options) < location_num_to_explore:
                self.print_animation("Searching...", wait="long")
                self.location_options.append(random.choice(self.locations))
                location_titanium[len(self.location_options)] = random.randint(10, 100)
                encounter_rates[len(self.location_options)] = random.random()

            elif len(self.location_options) == location_num_to_explore:
                self.print_animation("\nNothing more in sight.")
                self.print_animation("\n\t[Back]")
                condition = False

                print()

            if condition:
                for i in range(len(self.location_options)):
                    if self.titanium_scan and self.enemy_encounter_scan:
                        self.print_animation(f"\n[{i + 1}] {self.location_options[i]} Titanium: {location_titanium[i + 1]} Encounter rate: {round(encounter_rates[i + 1], 2) * 100}%")

                    elif self.titanium_scan and self.enemy_encounter_scan is False:
                        self.print_animation(f"\n[{i + 1}] {self.location_options[i]} Titanium: {location_titanium[i + 1]}")
                    elif self.titanium_scan is False and self.enemy_encounter_scan:
                        self.print_animation(f"\n[{i + 1}] {self.location_options[i]} Encounter rate: {round(encounter_rates[i + 1], 2) * 100}%")
                    else:
                        self.print_animation(f"\n[{i + 1}] {self.location_options[i]}")

                print()

                self.print_animation("\n[S] to continue searching")

                print()

            while True:
                player_choice = input("\nYour command:").lower()

                if player_choice == "s":
                    break

                elif player_choice == "back":
                    self.location_options.clear()
                    self.play()
                    loop = False
                    break

                try:
                    int(player_choice)

                except ValueError:
                    self.print_animation("\nInvalid input.")
                    continue

                else:
                    if int(player_choice) - 1 in range(location_num_to_explore) and int(player_choice) <= len(self.location_options):
                        self.print_animation("Deploying robots...")
                        player_encounter_rate = random.random()

                        if player_encounter_rate > encounter_rates[int(player_choice)]:
                            self.print_animation(f"\n{self.location_options[int(player_choice) - 1]} explored successfully, with no damage taken.")
                            self.titanium += location_titanium[int(player_choice)]
                            self.location_options.clear()
                            self.update_hub()
                            self.print_animation(f"\nAcquired {location_titanium[int(player_choice)]} lumps of titanium")
                            self.play()

                        else:
                            if self.robots > 1:
                                self.titanium += location_titanium[int(player_choice)]
                                self.enemy_encounter()
                                self.print_animation(f"\n{self.location_options[int(player_choice) - 1]} explored successfully, 1 robot lost")
                                self.location_options.clear()
                                self.print_animation(f"\nAcquired {location_titanium[int(player_choice)]} lumps of titanium")
                                self.play()

                            elif self.robots == 1:
                                self.enemy_encounter()
                                self.location_options.clear()
                                self.welcome_screen()
                        loop = False
                        break
                    else:
                        self.print_animation("\nInvalid input")

    def enemy_encounter(self):
        self.print_animation("\nEnemy encounter!!!")
        self.robots -= 1

        if self.robots > 0:
            self.update_hub()

        elif self.robots == 0:
            self.print_animation("\nMission aborted, the last robot lost...")
            self.print_animation(f"\n{self.GAME_OVER}")

            with open("high_scores.txt", "r") as file:
                lines = file.readlines()

            if len(lines) < 10:
                with open("high_scores.txt", "a") as file:
                    if len(lines) == 0:
                        file.write(f"{self.player_name} {self.titanium}")
                    else:
                        file.write(f"\n{self.player_name} {self.titanium}")

            else:
                new_lines = list()
                for line in lines:
                    user_data = line.split()
                    if self.titanium > int(user_data[1]):
                        new_lines.append(f"{self.player_name} {self.titanium}")
                    else:
                        new_lines.append(line)

                with open("high_scores.txt", "w") as file:
                    for i in range(len(new_lines) - 1):
                        file.write(f"{new_lines[i]}\n")
                    file.write(f"{new_lines[len(new_lines) - 1]}")

            self.titanium = 0
            self.robots = 3
            self.titanium_scan = False
            self.enemy_encounter_scan = False
            self.update_hub()

    def upgrade(self):
        print()
        self.print_animation(self.UPGRADE)

        print()

        while True:
            player_choice = input("\nYour command:").lower()

            if player_choice == "1" and self.titanium >= 250:
                self.titanium -= 250
                self.titanium_scan = True
                self.update_hub()
                self.print_animation("\nPurchase successful. You can now see how much titanium you can get from each found location.")
                self.play()
                break

            elif player_choice == "1" and self.titanium < 250:
                self.print_animation("\nNot enough titanium!")

            elif player_choice == "2" and self.titanium >= 500:
                self.titanium -= 500
                self.enemy_encounter_scan = True
                self.update_hub()
                self.print_animation("\nPurchase successful. You will now see how likely you will encounter an enemy at each found location.")
                self.play()
                break

            elif player_choice == "2" and self.titanium < 500:
                self.print_animation("\nNot enough titanium!")

            elif player_choice == "3" and self.titanium >= 1000:
                self.robots += 1
                self.titanium -= 1000
                self.update_hub()
                self.print_animation("\nPurchase successful. You now have an additional robot")
                self.play()
                break

            elif player_choice == "3" and self.titanium < 1000:
                self.print_animation("\nNot enough titanium!")

            elif player_choice == "back":
                self.play()
                break

            else:
                self.play()
                break

    def save(self, save_exit=False):
        self.print_animation("\tSelect save slot:")
        save_slots = list()

        print()

        self.update_file_lines()

        for idx, slot in enumerate(self.file_lines):
            self.print_animation(f"\t\t[{idx + 1}] {slot}")
            save_slots.append(slot.strip("\n"))

        print("\n")

        player_choice = input("Your command:").lower()

        if player_choice == "1" or player_choice == 1:
            if self.titanium_scan and self.enemy_encounter_scan:
                save_slots[0] = f"{self.player_name} Titanium: {self.titanium} Robots: {self.robots} Last save: {datetime.datetime.now()} Upgrades: enemy_info titanium_scan"
            elif self.titanium_scan and self.enemy_encounter_scan is False:
                save_slots[0] = f"{self.player_name} Titanium: {self.titanium} Robots: {self.robots} Last save: {datetime.datetime.now()} Upgrades: titanium_scan"
            elif self.titanium_scan is False and self.enemy_encounter_scan:
                save_slots[0] = f"{self.player_name} Titanium: {self.titanium} Robots: {self.robots} Last save: {datetime.datetime.now()} Upgrades: enemy_info"
            else:
                save_slots[0] = f"{self.player_name} Titanium: {self.titanium} Robots: {self.robots} Last save: {datetime.datetime.now()}"

        if player_choice == "2" or player_choice == 2:
            if self.titanium_scan and self.enemy_encounter_scan:
                save_slots[1] = f"{self.player_name} Titanium: {self.titanium} Robots: {self.robots} Last save: {datetime.datetime.now()} Upgrades: enemy_info titanium_scan"
            elif self.titanium_scan \
                    and self.enemy_encounter_scan is False:
                save_slots[1] = f"{self.player_name} Titanium: {self.titanium} Robots: {self.robots} Last save: {datetime.datetime.now()} Upgrades: titanium_scan"
            elif self.titanium_scan is False and self.enemy_encounter_scan:
                save_slots[1] = f"{self.player_name} Titanium: {self.titanium} Robots: {self.robots} Last save: {datetime.datetime.now()} Upgrades: enemy_info"
            else:
                save_slots[1] = f"{self.player_name} Titanium: {self.titanium} Robots: {self.robots} Last save: {datetime.datetime.now()}"

        if player_choice == "3" or player_choice == 3:
            if self.titanium_scan and self.enemy_encounter_scan:
                save_slots[2] = f"{self.player_name} Titanium: {self.titanium} Robots: {self.robots} Last save: {datetime.datetime.now()} Upgrades: enemy_info titanium_scan"
            elif self.titanium_scan and self.enemy_encounter_scan is False:
                save_slots[2] = f"{self.player_name} Titanium: {self.titanium} Robots: {self.robots} Last save: {datetime.datetime.now()} Upgrades: titanium_scan"
            elif self.titanium_scan is False and self.enemy_encounter_scan:
                save_slots[2] = f"{self.player_name} Titanium: {self.titanium} Robots: {self.robots} Last save: {datetime.datetime.now()} Upgrades: enemy_info"
            else:
                save_slots[2] = f"{self.player_name} Titanium: {self.titanium} Robots: {self.robots} Last save: {datetime.datetime.now()}"

        with open("save_file.txt", "w") as file:
            if len(save_slots) == 1:
                file.write(save_slots[0])

            else:
                for i in range(len(save_slots) - 1):
                    file.write(save_slots[i] + "\n")
                file.write(save_slots[len(save_slots) - 1])

        self.update_file_lines()
        self.print_animation(self.GAME_SAVE)

        if save_exit is False:
            self.play()

    def high_scores(self):
        self.print_animation("\n\n\tHIGH SCORES")

        print()

        with open("high_scores.txt", "r") as file:
            lines = file.readlines()

        scores = list()

        for line in lines:
            user_data = line.split()
            score = int(user_data[1].replace("\n", ""))
            scores.append(score)
        scores.sort(reverse=True)

        final_lines = list()

        for score in scores:
            for line in lines:
                if str(score) or str(score) + "\n" in line:
                    final_lines.append(line)

        for i in range(len(final_lines)):
            self.print_animation(f"\n({i + 1}) {final_lines[i]}")
        self.print_animation("\n\n\t[Back]")

        print()

        self.print_animation("\nYour command:")
        player_choice = input().lower()

        print()

        while player_choice != "back":
            self.print_animation("\nEnter a valid command!")
            self.print_animation("\nYour command:")
            player_choice = input().lower()

            print()
        self.welcome_screen()

    def help(self):
        self.print_animation("\nHello commander! Your goal is to find titanium as much as possible before you lose all of your robots.")
        self.print_animation("\nYou can give commands by input to explore locations and collect titanium from those locations.")
        self.print_animation("\nHave a good luck on titainum hunt!")

    def update_hub(self):
        robots = self.robots * "╬   ╬╬╬╬╬╬╬   ╬     " + "\n" \
                 + self.robots * "╬╬╬╬╬     ╬╬╬╬╬     " + "\n" \
                 + self.robots * "    ╬╬╬╬╬╬╬         " + "\n" \
                 + self.robots * "   ╬╬╬   ╬╬╬        " + "\n" \
                 + self.robots * "   ╬       ╬        " + "\n" \
                 + self.robots * "   ╬       ╬        " + "\n" \
                 + self.robots * "   ╬       ╬        "

        self.GAME_HUB = f"""\
║════════════════════════════════════════════════════════════════════════════════║
{robots}
   Titanium: {self.titanium}
║════════════════════════════════════════════════════════════════════════════════║
║                  [Ex]plore                          [Up]grade                  ║
║                  [Save]                             [M]enu                     ║
║════════════════════════════════════════════════════════════════════════════════║
                          """

    def update_file_lines(self):
        with open("save_file.txt", "r") as file:
            self.file_lines = file.readlines()


create_file()
game = Excavators()
random.seed(game.seed)
game.welcome_screen()

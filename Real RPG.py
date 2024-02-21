import random
import time

class Player:
    def __init__(self, name, health, attack, defense, coins, World=1, level=1, experience=0):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.coins = coins
        self.World = World
        self.level = level
        self.experience = experience

    def attack_enemy(self):
        return random.randint(1, self.attack)

    def take_damage(self, damage):
        self.health -= max(0, damage - self.defense)

    def heal(self):
        if self.health <= 0:
            print(f"{self.name} is defeated. Can't heal.")
        elif self.coins >= 10:
            self.health = min(100, self.health + 20)
            self.coins -= 10  # Corrected from 20 to 10
            print(f"{self.name} healed for 20 health.")
        else:
            print("Not enough coins to heal.")

    def level_up(self):
        level_up_experience = 100 + self.level * 50  
        if self.experience >= level_up_experience:
            self.level += 1
            self.health += 10
            self.attack += 5
            self.defense += 2

            # Apply buff when leveling up
            self.attack += 5
            self.health += 2

            print(f'{self.name} leveled up to level {self.level}!')
            print(f'Attack and health increased! Attack: {self.attack}, Health: {self.health}')
        else:
            print("Not enough experience points to level up.")

            self.World_Level()

    def World_Level(self):
        while self.experience >= 500 * (2 ** (self.World - 1)):
            self.World += 1
            print(f"{self.name} World level is increased. New World level: {self.World}")

    def respawn(self):
        self.health = 100
        print(f"{self.name} respawned with full health!")

    def rename(self, new_name):
        print(f"{self.name} changed name to {new_name}.")
        self.name = new_name

    def earn_coins(self, amount):
        self.coins += amount
        print(f"{self.name} earned {amount} coins!")

def battle(player):
    enemy_health = random.randint(50, 100)
    print(f"\nYou encountered an enemy with {enemy_health} health!")

    while enemy_health > 0 and player.health > 0:
        player_damage = player.attack_enemy()
        enemy_damage = random.randint(1, 15)

        enemy_health -= player_damage
        player.take_damage(enemy_damage)

        print(f"You dealt {player_damage} damage to the enemy.")
        print(f"The enemy dealt {enemy_damage} damage to you.")

        print(f"\nYour health: {player.health}")
        print(f"Enemy health: {enemy_health}")

    if player.health > 0:
        coins_earned = random.randint(1, 120)
        player.earn_coins(coins_earned)
        player.experience += random.randint(1, 50)
        print("You defeated the enemy and gained 50 experience points!")
        print(f"Total experience: {player.experience}")
        print(f"Total Coins: {player.coins}")

        player.level_up()

def main():
    player_name = input("Enter your character's name: ")
    my_player = Player(name=player_name, health=100, attack=10, defense=5, coins=0)
    
    battle_cooldown = 15  # Set the cooldown duration in seconds
    last_battle_time = 0  # Initialize the last battle time

    heal_cooldown = 15 
    last_heal_time = 0 

    while True:
        print("\n1. Battle")
        print("2. Check Status")
        print("3. Heal")
        print("4. Check Coins")
        print("5. Rename")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if my_player.health <= 0:
            print("\nYou are defeated.")
            respawn_choice = input("Do you want to respawn? (yes/no): ").lower()
            if respawn_choice == 'yes':
                my_player.respawn()
            else:
                print("Exiting the game. Goodbye!")
                break

        if choice == '1':
            current_time = time.time()
            if current_time - last_battle_time < battle_cooldown:
                remaining_cooldown = battle_cooldown - (current_time - last_battle_time)
                print(f"You need to wait {remaining_cooldown:.2f} seconds before battling again.")
            else:
                battle(my_player)
                last_battle_time = time.time()  # Update the last battle time

        elif choice == '2':
            print(f"\nName: {my_player.name}")
            print(f"Level: {my_player.level}")
            print(f"Health: {my_player.health}")
            print(f"Attack: {my_player.attack}")
            print(f"Defense: {my_player.defense}")
            print(f"Experience: {my_player.experience}")

        elif choice == '3':
            current_time = time.time()
            if current_time - last_heal_time < heal_cooldown:
                remaining_cooldown = heal_cooldown - (current_time - last_heal_time)
                print(f"You need to wait {remaining_cooldown:.2f} seconds before healing again.")
            else:
                my_player.heal()
                last_heal_time = time.time()  # Update the last battle time
            

        elif choice == '4':
            print(f"\nCoins: {my_player.coins}")

        elif choice == '5':
            new_name = input("Enter your new name: ")
            my_player.rename(new_name)

        elif choice == '6':
            print("Quitting the game. Goodbye!")
            break

        else:
            print("Kamu Milih apa sih")

if __name__ == "__main__":
    main()
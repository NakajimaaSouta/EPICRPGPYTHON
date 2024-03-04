import random
import time

class Player:
    def __init__(self, name, health, attack, defense, coins, World=1, level=1, experience=0):
        self.name = name
        self.health = health
        self.max_health = health  # Initialize max_health
        self.attack = attack
        self.defense = defense
        self.coins = coins
        self.World = World
        self.level = level
        self.experience = experience
        self.last_battle_time = 0  # Track last battle time
        self.last_heal_time = 0  # Track last heal time
        self.battle_cooldown = 0  # Set battle cooldown duration in seconds
        self.heal_cooldown = 0  # Set heal cooldown duration in seconds

    def attack_enemy(self):
        return random.randint(1, self.attack)

    def take_damage(self, damage):
        self.health -= max(0, damage - self.defense)

    def heal(self):
        current_time = time.time()
        if current_time - self.last_heal_time < self.heal_cooldown:
            remaining_cooldown = int(self.heal_cooldown - (current_time - self.last_heal_time))
            print(f"I am already healed wait for {remaining_cooldown} seconds to heal again.")
        else:
            if self.health <= 0:
                print(f"{self.name} is defeated. Can't heal.")
            elif self.coins >= 10:
                self.health = min(self.max_health, self.health + 20)  # Ensure health doesn't exceed max_health
                self.coins -= 10
                print(f"{self.name} healed for 20 health.")
                self.last_heal_time = current_time  # Update last heal time
            else:
                print("Not enough coins to heal.")

    def level_up(self):
        level_up_experience = 10 * self.level * 50 * self.level
        if self.experience >= level_up_experience:
            self.level += 1
            self.max_health += 10  
            self.attack += 15
            self.defense += 2 + self.level * self.level

            # Adjust the experience required for the next level
            self.experience -= level_up_experience

            # Apply additional buffs based on the level
            self.attack += 5 + self.level
            self.health += 2 + self.level
            self.max_health += 10 + self.level

            print(f'{self.name} leveled up to level {self.level}!')
            print()
            print(f'Attack and health increased! Attack: {self.attack}, Health: {self.health}')
        else:
            print()
            print("Not enough experience points to level up.")

            self.World_Level()

    def World_Level(self):
        while self.experience >= 2500 *  (4 ** (self.World - 1)):
            self.World += 1
            print(f"{self.name} World level is increased. New World level: {self.World}")

    def respawn(self):
        self.health = self.max_health  # Set health to max_health when respawning
        print(f"{self.name} respawned with full health!")

    def rename(self, new_name):
        print(f"{self.name} changed name to {new_name}.")
        self.name = new_name

    def earn_coins(self, amount):
        self.coins += amount
        print(f"{self.name} earned {amount} coins!")

    def can_battle(self):
        current_time = time.time()
        if current_time - self.last_battle_time < self.battle_cooldown:
            remaining_cooldown = int(self.battle_cooldown - (current_time - self.last_battle_time))
            print(f"I am tired, i am gonna rest for {remaining_cooldown} second ")
            return False
        else:
            return True

    def update_last_battle_time(self):
        self.last_battle_time = time.time()

class Monster:
    def __init__(self, name, max_hp, attack, gold):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.attack = attack
        self.gold = gold

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0  # Ensure that hp doesn't go below 0

def battle(player):
    while True:
        monsters = [
            Monster("Goblin", 30, 10, 1),
            Monster("Ork", 50, 15, 3),
            Monster("Troll", 56, 10, 7),
            Monster("Zombie", 100, 15, 5),
            Monster("Reyno", 150, 30, 10)
        ]
        enemy = random.choice(monsters)
        print(f"\nYou encountered a {enemy.name} with {enemy.max_hp} health!")

        while enemy.is_alive() and player.health > 0:
            print("Player health:", player.health)
            print("Enemy health:", enemy.hp)
            print()  # Add an empty print statement for space

            # Player's turn
            player_damage = player.attack_enemy()
            print(f"You attacked the {enemy.name} and dealt {player_damage} damage!")
            enemy.take_damage(player_damage)
            if not enemy.is_alive():
                print(f"You defeated the {enemy.name} and earned {enemy.gold} gold!")
                player.earn_coins(enemy.gold)
                player.experience += random.randint(1, 25)
                print("You Gained Experience Points")
                return  # Exit battle function

            # Enemy's turn
            enemy_damage = enemy.attack - player.defense
            print(f"The {enemy.name} attacked you and dealt {enemy_damage} damage!")
            player.take_damage(enemy_damage)

            if player.health <= 0:
                print("\nYou are defeated.")
                respawn_choice = input("Do you want to respawn? (yes/no): ").lower()
                if respawn_choice == 'yes':
                    player.respawn()
                    return  # Exit battle function
                else:
                    print("Exiting the game. Goodbye!")
                    exit()
            
            if player.health > 0:
                coins_earned = random.randint(1, 15)
                player.earn_coins(coins_earned)
                player.experience += 50 
                print(f"Total experience: {player.experience}")

                player.level_up()

def main():
    player_name = input("Enter your character's name: ")
    my_player = Player(name=player_name, health=100, attack=20, defense=5, coins=0)

    while True:  # pengulangan
        print("\n1. Battle")
        print("2. Check Status")
        print("3. Heal")
        print("4. Rename")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            if my_player.can_battle():
                my_player.update_last_battle_time()  # Update last battle time
                battle(my_player)
            else:
                print()

        elif choice == '2':
            print(f"\nName: {my_player.name}")
            print(f"Level: {my_player.level}")
            print(f"World: {my_player.World}")
            print(f"Health: {my_player.health}/{my_player.max_health}")  # Show current and max health
            print(f"Attack: {my_player.attack}")
            print(f"Defense: {my_player.defense}")
            print(f"Experience: {my_player.experience}")
            print(f"Total Coins: {my_player.coins}")

        elif choice == '3':
            my_player.heal()

        elif choice == '4':
            new_name = input("Enter your new name: ")
            my_player.rename(new_name)

        elif choice == '5':
            print("Quitting the game. Goodbye!")
            exit()

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

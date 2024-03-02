import random

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
            self.coins -= 10
            print(f"{self.name} healed for 20 health.")
        else:
            print("Not enough coins to heal.")

    def level_up(self):
        level_up_experience = 10 + self.level * 1  
        if self.experience >= level_up_experience:
            self.level += 1
            self.health += 10
            self.attack += 5
            self.defense += 2

            # Adjust the experience required for the next level
            self.experience -= level_up_experience

            # Apply additional buffs based on the level
            self.attack += 5 + self.level
            self.health += 2 + self.level

            print(f'{self.name} leveled up to level {self.level}!')
            print(f'Attack and health increased! Attack: {self.attack}, Health: {self.health}')
        else:
            print("Not enough experience points to level up.")

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
            Monster("Goblin", 30, 10, 20),
            Monster("Ork", 50, 15, 30),
            Monster("Troll", 80, 20, 50),
            Monster("Zombie", 100, 15, 70),
            Monster("Reyno", 300, 15, 100)
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
            enemy_damage = enemy.attack
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


def main():
    player_name = input("Enter your character's name: ")
    my_player = Player(name=player_name, health=100, attack=10, defense=5, coins=0)

    while True:  # Main loop for the game
        print("\n1. Battle")
        print("2. Check Status")
        print("3. Heal")
        print("4. Check Coins")
        print("5. Rename")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            battle(my_player)  # Call the battle function directly

        elif choice == '2':
            print(f"\nName: {my_player.name}")
            print(f"Level: {my_player.level}")
            print(f"World: {my_player.World}")
            print(f"Health: {my_player.health}")
            print(f"Attack: {my_player.attack}")
            print(f"Defense: {my_player.defense}")
            print(f"Experience: {my_player.experience}")

        elif choice == '3':
            my_player.heal()

        elif choice == '4':
            print(f"\nCoins: {my_player.coins}")

        elif choice == '5':
            new_name = input("Enter your new name: ")
            my_player.rename(new_name)

        elif choice == '6':
            print("Quitting the game. Goodbye!")
            exit()

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

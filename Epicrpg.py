import random

class Player:
    def __init__(self, name, health, attack, defense, coins):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.coins = coins
        self.level = 1
        self.experience = 0

    def attack_enemy(self):
        return random.randint(1, self.attack)

    def take_damage(self, damage):
        self.health -= max(0, damage - self.defense)

    def heal(self):
        if self.health <= 0:
            print(f"{self.name} is defeated. Can't heal.")
        elif self.experience >= 10:
            self.health = min(100, self.health + 20)
            self.experience -= 20
            print(f"{self.name} healed for 20 health.")
        else:
            print("Not enough experience points to heal.")

    def earn_coins(self, amount):
        self.coins += amount
        print(f"{self.name} earned {amount} coins!")

    def level_up(self):
        level_up_experience = 100 + self.level * 50  # Adjust the experience requirement
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

    def respawn(self):
        self.health = 100
        print(f"{self.name} respawned with full health!")

    def rename(self, new_name):
        print(f"{self.name} changed name to {new_name}.")
        self.name = new_name

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
        coins_earned = random.randint(1, 15)
        player.earn_coins(coins_earned)
        player.experience += 50
        print("You defeated the enemy and gained 50 experience points!")
        print(f"Total experience: {player.experience}")

        player.level_up()

def main():
    player_name = input("Enter your character's name: ")
    player = Player(name=player_name, health=100, attack=10, defense=5, coins=0)

    while True:
        print("\n1. Battle")
        print("2. Check Status")
        print("3. Heal")
        print("4. Check Coins")
        print("5. Rename")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if player.health <= 0:
            print("\nYou are defeated.")
            respawn_choice = input("Do you want to respawn? (yes/no): ").lower()
            if respawn_choice == 'yes':
                player.respawn()
            else:
                print("Exiting the game. Goodbye!")
                break

        if choice == '1':
            battle(player)

        elif choice == '2':
            print(f"\nName: {player.name}")
            print(f"Level: {player.level}")
            print(f"Health: {player.health}")
            print(f"Attack: {player.attack}")
            print(f"Defense: {player.defense}")
            print(f"Experience: {player.experience}")

        elif choice == '3':
            player.heal()

        elif choice == '4':
            print(f"\nCoins: {player.coins}")

        elif choice == '5':
            new_name = input("Enter your new name: ")
            player.rename(new_name)

        elif choice == '6':
            print("Quitting the game. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

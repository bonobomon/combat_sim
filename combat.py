# combat.py
import random
from attacks import attacks

def enemy_attack(n, player_health=50, enemy_health=45, player_status=None):
    if n <= 0 or player_health <= 0:
        if player_health <= 0:
            print("You died")
        else:
            print("You survived")
        return
    
    if player_status is None:
        player_status = []
    
    for status in player_status[:]:
        if status[0] == "poisoned":
            player_health -= 1
            status[1] -= 1
            print(f"Poison ticks! Deals 1 damage. Player health: {player_health}")
            if status[1] <= 0:
                player_status.remove(status)
                print("Poison wears off!")
        elif status[0] == "burned":
            player_health -= 1
            status[1] -= 1
            print(f"Burn ticks! Deals 1 damage. Player health: {player_health}")
            if status[1] <= 0:
                player_status.remove(status)
                print("Burn wears off!")
    
    # Enemy AI tweak
    if enemy_health < 15:
        attack = "parry"  # Defensive when weak
    else:
        attack = random.choice(list(attacks.keys()))
    damage = attacks[attack]
    player_health -= damage
    print(f"Enemy uses {attack}! Deals {damage} damage. Player health: {player_health}")
    
    if attack == "acid spit" and player_health > 0:
        player_status.append(["poisoned", 3])
        print("You’re poisoned!")
    if attack == "magic sword" and player_health > 0:
        player_status.append(["burned", 2])
        print("You’re burned!")
    
    if player_health > 0:
        while True:
            try:
                print("Choose attack power (0-10): ")
                player_damage = int(input())
                if 0 <= player_damage <= 10:
                    break
                print("Please enter a number between 0 and 10!")
            except ValueError:
                print("Enter a valid number!")
        
        enemy_health -= player_damage
        print(f"Player hits back! Deals {player_damage} damage. Enemy health: {enemy_health}")
        
        if enemy_health <= 0:
            print("Enemy defeated!")
            return
    
    enemy_attack(n - 1, player_health, enemy_health, player_status)
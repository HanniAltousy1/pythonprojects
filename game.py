import random


def play_game():
    # Set the initial state of the game
    health = 100
    enemy_health = 100
    enemy_damage = random.randint(10, 20)

    # Start the game loop
    while health > 0 and enemy_health > 0:
        # Print the current state of the game
        print("Your health:", health)
        print("Enemy health:", enemy_health)

        # Get player input
        player_action = input("What would you like to do? (attack/heal) ")

        if player_action == "attack":
            enemy_health -= random.randint(10, 20)
            if enemy_health <= 0:
                print("You defeated the enemy!")
                break
            health -= enemy_damage
            print("The enemy deals", enemy_damage, "damage to you.")
        elif player_action == "heal":
            heal_amount = random.randint(10, 30)
            health += heal_amount
            print("You heal", heal_amount, "points of health.")
        else:
            print("Invalid action, please try again.")

    if health <= 0:
        print("You have been defeated.")
    else:
        print("You have won the game!")


play_game()
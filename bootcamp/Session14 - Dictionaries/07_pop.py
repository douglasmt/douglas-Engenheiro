#DO NOT TOUCH game_properties!
game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notifications", "achievements"] 

# Use the game_properties list and dict.fromkeys() to generate a dictionary with all values set to 0. Save the result to a variable called initial_game_state
initial_game_state = {}.fromkeys([])
initial_game_state = {}.fromkeys(list(game_properties),0)
print("\n VALUES in the beginning \n")
print(initial_game_state)

initial_game_state.pop("current_score")
print("\n VALUES in the after pop \n")
print(initial_game_state)
print("\n END \n")

initial_game_state.pop()
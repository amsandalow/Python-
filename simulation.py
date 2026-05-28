import random

# Procedure to run one race
def run_race():
    t_pos = 0
    h_pos = 0
    finish_line = 100

    # Loop until someone wins
    while t_pos < finish_line and h_pos < finish_line:
        # Tortoise is slow but always moves
        t_pos = t_pos + 2

        # Hare is fast but usually sleeps
        # random.random() gives a number between 0 and 1
        # 0.95 means he sleeps 95% of the time
        if random.random() < 0.05:
            h_pos = h_pos + 20
        else:
            h_pos = h_pos + 0

    if t_pos >= finish_line:
        return "tortoise"
    else:
        return "hare"

# --- Main Program ---
# A student would likely just start the variables and loop here
t_wins = 0
h_wins = 0

for i in range(100):
    winner = run_race()
    if winner == "tortoise":
        t_wins = t_wins + 1
    else:
        h_wins = h_wins + 1

# Simple print statements
print("Tortoise Wins:")
print(t_wins)
print("Hare Wins:")
print(h_wins)

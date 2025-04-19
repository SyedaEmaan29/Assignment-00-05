"""
Program: dicesimulator
----------------------
Simulate rolling two dice, three times.  Prints
the results of each die roll.  This program is used
to show how variable scope works.
"""

# Import the random library which lets us simulate random things like dice!
import random

# Number of sides on each die to roll
NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and prints their total
    """
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)
    total: int = die1 + die2
    print("Total of two dice:", total)

def main():
    die1: int = 10 # main()'s die1 is 10 (unchanged by roll_dice()).
    print("die1 in main() starts as: " + str(die1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("die1 in main() is: " + str(die1)) #main()'s die1 is still 10, proving it was never modified.

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()

#     Real-world Analogy

# Think of main()'s die1 as a notebook on your desk.

# roll_dice()'s die1 is a notebook in a drawer.

# Writing in one does not change the other, even if both are named "die1."
# Here, die1 = 10 is used to demonstrate variable scope—specifically, that:

# Variables with the same name in different functions are independent.

# The die1 in main() (set to 10) is completely separate from the die1 in roll_dice() (a random dice roll).

# Changing one does not affect the other.

# Local variables stay inside their function.

# Even though roll_dice() also has a die1, it does not modify main()'s die1.

# After calling roll_dice() three times, main()'s die1 remains 10.

# What This Program Shows
# Scope Isolation

# main()'s die1 and roll_dice()'s die1 are different variables.

# They just happen to share the same name but exist in separate scopes.
    
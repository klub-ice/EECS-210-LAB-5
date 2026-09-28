# Name: Zoey Spies
# KUID: 3136594
# LAB Session (Day/Time): Monday 11 AM
# LAB Assignment: Lab 5
# Description:
#
#
#
# Collaborators/Sources: 268 notes, geeksforgeeks, stackoverflow
import re

def get_input_list(prompt="Enter numbers (use spaces and/or commas): ") -> list[int]:
    user_input = input(prompt)
    # Split on commas or spaces (one or more of them)
    tokens = re.split(r"[,\s]+", user_input.strip())
    # Convert to integers, ignoring empty strings
    return [int(t) for t in tokens if t]

# Your Code Here


# Example usage
def main():
    L1 = get_input_list()
    print(f"Got: {L1}")

    
main()
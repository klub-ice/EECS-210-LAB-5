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
def merge(L1: list[int], L2: list[int]) -> list[int]:  # Merges two sorted lists into a single sorted list
    merged_list = []  # Initialize the merged list
    i, j = 0, 0  # Initialize pointers for L1 and L2

    while i < len(L1) and j < len(L2):  # Loop until we reach the end of either list
        if L1[i] < L2[j]:  # If the current element in L1 is smaller, append it to the merged list
            merged_list.append(L1[i])  # Increment the pointer for L1
            i += 1  # increment the pointer for L1
        else:  # If the current element in L2 is smaller or equal, append it to the merged list
            merged_list.append(L2[j])
            j += 1

    while i < len(L1):  # Append remaining elements from L1
        merged_list.append(L1[i])  # append the current element from L1 to the merged list
        i += 1  # increment the pointer for L1

    while j < len(L2):  # Append remaining elements from L2
        merged_list.append(L2[j])  # append the current element from L2 to the merged list
        j += 1  # increment the pointer for L2

    return merged_list  # Return the merged list

def merge_sort(L: list[int]) -> list[int]:  # Sorts a list using the merge sort algorithm
    if len(L) <= 1:  # Base case: a list of length 0 or 1 is already sorted
        return L

    mid = len(L) // 2  # Find the midpoint of the list
    left_half = merge_sort(L[:mid])  # Recursively sort the left half
    right_half = merge_sort(L[mid:])  # Recursively sort the right half

    return merge(left_half, right_half)  # Merge the sorted halves

# Example usage
def main():
    numbers = get_input_list()  # Get the list of numbers from the user
    sorted_numbers = merge_sort(numbers)  # Sort the list using merge sort
    print("Sorted numbers:", sorted_numbers)  # Print the sorted list

main()

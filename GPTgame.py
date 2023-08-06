# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 20:33:02 2023

@author: ChatGPT
"""

import random

def binary_search_game():
    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    attempts = 0
    guess = 0
    
    print("Welcome to the Binary Search Game!")
    print("Try to guess the number between 1 and 100.")
    
    # Loop until the player guesses the correct number
    while guess != target_number:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        # Check if the guess is too low, too high, or correct
        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
    
    print(f"Congratulations! You guessed the number {target_number} in {attempts} attempts.")
    
# Start the game
binary_search_game()

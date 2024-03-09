#!/usr/bin/python3 venv
# v1.0 - GEMatria
# CompSci Tool for Gematria  
# Linguistics [ english, hebrew, greek ]
#

# libraries / modules imported
import os
import sys
import datetime

learn_101 = """
 █████                                                              
░░███                                                               
 ░███         ██████   ██████   ████████  ████████                  
 ░███        ███░░███ ░░░░░███ ░░███░░███░░███░░███                 
 ░███       ░███████   ███████  ░███ ░░░  ░███ ░███                 
 ░███      █░███░░░   ███░░███  ░███      ░███ ░███                 
 ███████████░░██████ ░░████████ █████     ████ █████                
░░░░░░░░░░░  ░░░░░░   ░░░░░░░░ ░░░░░     ░░░░ ░░░░░                 
                                                                    
                                                                    
                                                                    
 █████   █████          █████                                       
░░███   ░░███          ░░███                                        
 ░███    ░███   ██████  ░███████  ████████   ██████  █████ ███ █████
 ░███████████  ███░░███ ░███░░███░░███░░███ ███░░███░░███ ░███░░███ 
 ░███░░░░░███ ░███████  ░███ ░███ ░███ ░░░ ░███████  ░███ ░███ ░███ 
 ░███    ░███ ░███░░░   ░███ ░███ ░███     ░███░░░   ░░███████████  
 █████   █████░░██████  ████████  █████    ░░██████   ░░████░████   
░░░░░   ░░░░░  ░░░░░░  ░░░░░░░░  ░░░░░      ░░░░░░     ░░░░ ░░░░    
                                                                    
 """
print("\n")
txt_details = """
 by: al3bet
 git: github.com/al3fbet
 profile: al3fbet.github.io/
 date: 2024
                                                                
"""

print(learn_101)
print(txt_details)

current_datetime = datetime.datetime.now()
formatted_datetime_english = current_datetime.strftime("%A, %B %d, %Y %H:%M:%S")
print("Current date and time:", formatted_datetime_english)
print("\n")



# Gematria function of the program
def calculate_gematria(word, alphabet):
    gematria = {}
    if alphabet == "english":
        # English alphabet gematria values
        english_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i, letter in enumerate(english_alphabet, 1):
            gematria[letter] = i
    elif alphabet == "hebrew":
        # Hebrew alphabet gematria values
        hebrew_alphabet = "אבגדהוזחטיכלמנסעפצקרשתךםןףץ"
        values = [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 50, 40, 70, 80, 90,
        ]
        for i, letter in enumerate(hebrew_alphabet):
            gematria[letter] = values[i]
    elif alphabet == "greek":
        # Greek alphabet gematria values
        greek_alphabet = "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"
        for i, letter in enumerate(greek_alphabet, 1):
            gematria[letter] = i if i <= 24 else i + 300
    
    total_value = sum(gematria.get(char.upper(), 0) for char in word)
    return total_value

def main():
    print("Choose an alphabet: English, Hebrew, or Greek")
    alphabet_choice = input("Enter 'english', 'hebrew', or 'greek': ").lower()

    if alphabet_choice not in ['english', 'hebrew', 'greek']:
        print("Invalid choice.")
        return

    word = input(f"Enter a word in {alphabet_choice.capitalize()}: ")
    gematria_value = calculate_gematria(word, alphabet_choice)
    
    print(f"The gematria value of '{word}' in {alphabet_choice.capitalize()} is: {gematria_value}")

if __name__ == "__main__":
    main()


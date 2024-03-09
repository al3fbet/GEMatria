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

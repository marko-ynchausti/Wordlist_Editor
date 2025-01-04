# This program allows a user to make modifications to an existing wordlist file.
# The user gets to choose what modifications they make from a menu with a list of most common modifications for a wordlist.
# Each time the user makes a modification, a new file is outputted with the changes made.
# The user can continue to make modifications without the program ending, since the main logic of the program is on a loop.
# The purpose of this program is to streamline the repetetiveness of modifying existing wordlists for password cracking capture the flag challenges.

# imports module sys to terminate program
import sys

# This function is used to terminate the program
def exit_tool():
  print("Terminating tool.")
  sys.exit()

# This variable is used to create a divider between the outputted wordlist and the edits menu
newline = "\n-------------------------------------"

# This function is the menu of commands the user can choose from
def potential_edits():
  print("\nHere are the potential edits:", newline)
  print("nospace - deletes spaces")
  print("dash - replaces space with a dash")
  print("underscore - replaces space with a underscore")
  print("upper - uppercases beginning of word")
  print("lower - lowercases beginning of word")
  print("end - ends program", newline)

# Stores the wordlist file in wordlist variable
wordlist = "wordlist.txt"

# This tries to check if the wordlist file is present, if it is, then it opens it. 
try:
  file = open('wordlist.txt', 'r')
  print("Beginning of the wordlist:", newline)
  
  # This loops through the first 5 lines of the wordlist file and outputs it. 
  # This is the counter
  i = 0 
  # For every line in the file
  for line in file: 
    # Prints the current line in the file
    print(line, end="") 
    # Increments counter by 1
    i += 1 
    # Ends loop if the counter reaches 5
    if i == 5: 
        break

#The except is here to handle the error given when the wordlist.txt file is not found.
except FileNotFoundError:
  print(f"Could not find {wordlist} file.")
  exit_tool()
  
# This function deletes all the spaces in every line of the initial wordlist file, and appends the changes made to a new file.
def nospace():
  # Creates an empty list
  words=[] 
  # Opens the wordlist file
  rfile = open('wordlist.txt','r')
  # For every line in the file
  for line in rfile:
    # Replace space with no space. Essentially, it removes spaces
    line = line.replace(" ", "") 
    # Appends the change to the emtpy words list created earlier
    words.append(line)
  # Opens a new file
  wfile = open("nospace.txt", "w")
  # Loops through every item in the now populated words list, and writes the content to the new file
  for item in words:
    wfile.write(item)

# This function replaces all the spaces in every line of the initial wordlist file with dashes, and appends the changes made to a new file.
def dash():
  words=[]
  rfile = open('wordlist.txt','r')
  for line in rfile:
    # Replaces a space with a dash
    line = line.replace(" ", "-") 
    words.append(line)
  wfile = open("dash.txt", "w")
  for item in words:
    wfile.write(item)

# This function replaces all the spaces in every line of the initial wordlist file with underscores, and appends the changes made to a new file.
def underscore():
  words=[]
  rfile = open('wordlist.txt','r')
  for line in rfile:
    # Replaces a space with an underscore
    line = line.replace(" ", "_") 
    words.append(line)
  wfile = open("underscore.txt", "w")
  for item in words:
    wfile.write(item)

# This function capitlizes the beginning of every word in every line of the initial wordlist file, and appends the changes made to a new file
def uppercase():
  words=[]
  rfile = open('wordlist.txt','r')
  for line in rfile:
    # Capitlizes the beginning of every word
    line = line.title() 
    words.append(line)
  wfile = open("uppercase.txt", "w")
  for item in words:
    wfile.write(item)

# This function lowercases every word in every line of the initial wordlist file, and appends the changes made to a new file
def lowercase():
  words=[]
  rfile = open('wordlist.txt','r')
  for line in rfile:
    # Lowercases every word
    line = line.lower() 
    words.append(line)
  wfile = open("lowercase.txt", "w")
  for item in words:
    wfile.write(item)
    
# Counter for edits made set to 0
edits_made=0

# This is the main logic of the program. It is on a while loop that never stops unless the user ends it. Within the loop lies if and else statements, which determine what to do depending on what the user inputted.
while True:
  # This if statement shows the menu depending if the user already entered a command.
  if edits_made == 0:
    potential_edits()
  
  edits = input("\nWhat do you want to do?")

  # If the user inputted nospace, then the function nospace is called
  if edits == "nospace":
    edits_made=+1 # Adds one to the edits_made counter at the top of the loop to keep track of the edits made
    nospace()
    
  elif edits == "dash":
    edits_made=+1
    dash()
    
  elif edits == "underscore":
    edits_made=+1
    underscore()
    
  elif edits == "upper":
    edits_made=+1
    uppercase()
    
  elif edits == "lower":
    edits_made=+1
    lowercase()

  # If user inputted end, the program breaks out of the loop and ends.
  elif edits == "end":
    print("Ending tool...")
    break
  # If the user does not input a valid command, then "enter a valid command" is outputted
  else: 
    print("Enter valid command")

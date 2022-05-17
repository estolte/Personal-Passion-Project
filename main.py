import random
from colorama import init, Fore, Back, Style
from os import system, name
from time import sleep
from second import pr_char
guessCheck = True
init()
#code used from https://www.geeksforgeeks.org/clear-screen-python/ to clear the display
tota_wins = 0
total_guesses = 0
total_games = 0
total_wins = 0
winstreak = 0
highest_streak = 0
def averages():
  try:
    total_guesses/total_wins
  except ZeroDivisionError:
    pass
    
def win_percentage():
  try:
    total_wins/total_games
  except ZeroDivisionError:
    pass
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    else:
        _ = system('clear')

#main game loop
loop = True
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
f = open('wordlist.txt', 'r')
wordlist = f.readlines()
num = len(wordlist)
validguess = open('validguesses.txt', 'r')




#want to make it so it has each guess on top of each other, no letter list inbetween and one letter list at the bottom for each guess

#ideas: sys.clear after each guess, store each guess to a var guess 1-6, rewrite over each guess after the game is over.
#this would be perfect for getting the text back up there, but not sure how it would work to get the colors back.




while loop:
  check_w = False
  output2 = []
  #print(alphabet)
  print(Back.WHITE + Fore.BLACK + "Start a new game? (y/quit/stats)" + Style.RESET_ALL)
  
  command = input()
  #COMMAND CENTER
  
  if command == 'quit':
    loop = False
  
  if command == 'stats':
    try:
      average = total_guesses / tota_wins
      wp = (tota_wins / total_games) * 100
      print('Total wins: ' + str(tota_wins))
      #average guesses
      print('Average guesses per win: ' + str(average))
      #win percentage
      print('Win Percentage: ' + str(wp) + '%')
      #print(total_guesses)
      print("Current Winstreak of " + str(winstreak))
      print("Highest Winstreak: " + str(highest_streak) )
    except ZeroDivisionError:
      print("No stats to display, play then try again")
      pass
  
  elif command == 'y':
    total_games = total_games + 1
    random_word = wordlist[random.randint(0, num - 1)]
    
    guess = 0
    
    print(Back.WHITE + Fore.BLACK + "Enter a word" + Style.RESET_ALL)
    
    
    while guess < 6:
      attempt = input()
      if attempt not in validguess:
        print("Guess not in valid word list. Try again.")
      #ELITE HAXOR
      #print(random_word)
      # game logic
        
      output = ""
      for i in range(5):

        if attempt[i] == random_word[i]:
          output = output + Back.GREEN + attempt[i] + Back.RESET

        elif attempt[i] in random_word:
          output = output + Back.YELLOW + attempt[i] + Back.RESET

        else:
          output = output + attempt[i] + Back.RESET
        
      print(output)

      guess += 1 
      #check for win
      def check_win():
        if attempt in random_word:
          if guess <= 3:
            print("wow ur insane bro gj u got it in %s" % guess)
            
          if guess == 4:
            print("You got it in %s" % guess)
            
          if guess >= 5:
            print("You took %s to get it." % guess)
            
      if attempt in random_word:
        check_w = True
        total_guesses = total_guesses + guess
        winstreak = winstreak + 1
        
      check_win()
      
      # resets game
      if check_w == True:
        guess += 6
        
        

      # adds total wins

      if check_w == True:
        tota_wins = tota_wins + 1

      #once done resets letter list
      if guess > 5:
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

        
      #letter list
      if guess < 6:
        if attempt not in random_word:
          for letter in attempt:
            try:
              del alphabet[alphabet.index(letter)]

            except ValueError:
              pass
          a = ""
          for i in alphabet:
            a += f"{i} "
          print(Back.WHITE + Fore.BLACK  + a + Style.RESET_ALL)

      
      # shows used letters, not working, M doesn't appear, won't store to the next guess
  
      '''asdfs = list(attempt)'''
      '''letter_guesses.append(attempt)
      print(letter_guesses)
      for z in range(26):
        
        for j in range(5):
          
          if alphabet[z] not in output2:
            
            for list in letter_guesses:
              
              if alphabet[z] not in list:  
                
                output2.append(alphabet[z])
            '''
              
      
      #thorn = ''.join(output2)
      #print(thorn)
      #output2.clear()

      #lose logic
      if attempt not in random_word and guess >= 6:
        print("nice try but you lost")
        winstreak = 0
        
    else:
      print("The word was: " + random_word, end ="") 
      print("Try again? y/n")
      end_screen_input = input()
      if end_screen_input == "y":
        command = 'y'
        clear()
      elif end_screen_input == "n":
        break
    if winstreak > highest_streak:
      highest_streak = winstreak
      
      

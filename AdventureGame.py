'''This is a short adventure game using multiple if statements. The inputs use one letter to choose your direction that you are going. To play click the run button or Ctrl + Enter.'''
'''Made by Awnsh'''
'''
     @@@@@@                               @@@@@@  
    @@@@@@@@@                          @@@@@@@@@  
    @@@@@@@@@@@         @@@@#        @@@@@@@@@@@  
    @@@@@@@@@@@@@     @@@@@@@@      @@@@@@ @@@@@  
    @@@@@@  @@@@@@   @@@@@@@@@@@  @@@@@@@  @@@@@  
    @@@@@@   @@@@@@@@@@@@@ @@@@@@@@@@@@    @@@@@  
    @@@@@@     @@@@@@@@@    @@@@@@/@@@     @@@@@  
    @@@@@@      @@@@@@@       @@@@@@       @@@@@  
     @@@@@@  @@@@@@@@          *@@@@@@@@@@@@@@@@  
      @@@@@@@@@@@@@              @@@@@@@@@@@@@@   
         @@@@@@                      @@@@@@@      
'''

import os
import time
import random

#Takes name of player
namereg = input("What is your name explorer?: ")
#capitalizes first letter
name = namereg.capitalize()
print("Alright " + name + ", lets get exploring!")
time.sleep(2)
os.system('clear')

#makes a random chance to fall into a river whenever encountered
riverfall = random.randint(1,8)

#random chance that you win the bear fight whne encountered
bearfight = random.randint(1,3)

#allows to loop back to the start
def start():
  print("You have found your way into a forest and got lost.")
  print()
  time.sleep(1.2)
  out = input("Do you think your can find your way out? (y/n): ")
  os.system('clear')

  #allows to loop back to paths
  def lrfb():
    if out == "y":
      print("You see four paths. Left, Right, Forward, and Backwards.")
      print()
      time.sleep(1.2)
      pathreg = input("Which path do you want to take? (l/r/f/b): ")
      path = pathreg.lower()
      os.system('clear')
      
    elif out == "n":
      print("Ok " + name + ", Goodbye.")
      quit()

    else:
      print("Please input y or n")
      time.sleep(2)
      os.system('clear')
      start()

    
    #allows to loop back to entered path
    def enter():
      if path == "left" or path == "l":
        print("You have encountered a wall")
        print()
        time.sleep(1.2)
        climbreg = input("Do you want to climb it or go back? (c/b): ")
        climb = climbreg.lower()
        os.system('clear')
      
        if climb == "b":
          print("Ok!")
          time.sleep(2)
          os.system('clear')
          lrfb()
          
        elif climb == "c":
          print("You have encountered a fallen down tree")
          print()
          time.sleep(1.2)
          treereg = input("Do you want to climb over it or go back? (c/b): ")
          tree = treereg.lower()
          os.system('clear')


          if tree == "c":
            print("You are at a waterfall")
            print()
            time.sleep(1.2)
            waterfallreg = input("Do you want to go under it or keep going forward? (u/f): ")
            waterfall = waterfallreg.lower()
            os.system('clear')

            if waterfall == "u":
              print("There is nothing")
              time.sleep(2)
              os.system('clear')
              quit()

            elif waterfall == "f":
              print("You encounter a river")
              print()
              time.sleep(1.2)
              river1reg = input("Do you want to cross it or go around it? (c/a): ")
              river1 = river1reg.lower()
              os.system('clear')

              if river1 == "c" and not riverfall == 2:
                print("You found an exit to the forest!")
                time.sleep(2)
                os.system('clear')
                quit()

              elif river1 == "c" and riverfall == 2:
                print("You fell into the river")
                time.sleep(2)
                os.system('clear')
                quit()

              elif river1 == "a":
                print("You tried to go around it but fell in")
                time.sleep(2)
                os.system('clear')
                quit()

              else:
                print("I do not understand that yet.")
                time.sleep(2)
                os.system('clear')
                quit()
                
          
            
          elif tree == "b":
            print("Ok!")
            time.sleep(2)
            os.system('clear')
            enter()

          else:
            print("I do not understand that yet")
            time.sleep(2)
            os.system('clear')
            quit()
          
    #done
      elif path == "backwards" or path == "b":
        print("You left the forest, Goodbye " + name + "!")
        time.sleep(2)
        os.system('clear')
        quit()
    

      #done
      elif path == "right" or path == "r":
        print("There is a fork in the road. Left and Right")
        print()
        time.sleep(1.2)
        forkreg = input("Which side do you want to go? (l/r): ")
        fork = forkreg.lower()
        os.system('clear')

        if fork == "l":
          print("You encounter a bear.")
          time.sleep(1.2)
          print()
          bearreg = input("Do you want to run or fight it? (r/f): ") 
          bear = bearreg.lower()
          os.system('clear')
      
          if bear == "f" and bearfight == 2:
            print("You won")
            time.sleep(2)
            os.system('clear')
            print("You found a new part of the forest")
            print()
            time.sleep(1.2)
            fork1reg = input("Do you want to go left or right? (l/r): ")
            fork1 = fork1reg.lower()
            os.system('clear')

            if fork1 == "l":
              print("You found an exit to the forest!")
              time.sleep(2)
              os.system('clear')
              quit()

            elif fork1 == "r":
              print("You fell into a hole")
              time.sleep(2)
              os.system('clear')
              quit()

            else:
              print("I do not understand that yet")
              time.sleep(2)
              os.system('clear')
              quit()
            
          elif bear == "f" and bearfight == 1:
            print("The bear won")
            time.sleep(2)
            os.system('clear')
            quit()
            
          elif bear == "f" and bearfight == 3:
            print("The bear won")
            time.sleep(2)
            os.system('clear')
            quit()
          
          elif bear == "r":
            print("You ran to a new part of the forest. There is two paths, Left and right")
            time.sleep(1.2)
            print()
            path1reg = input("Which side are you going? (l/r): ")
            path1 = path1reg.lower()
            os.system('clear')

          else:
            print("I do not understand that yet")
            time.sleep(2)
            os.system('clear')
            quit()
            
            if path1 == "l":
                print("You found an exit to the forest!")
                quit()

            elif path1 == "r":
              print("You fell into a hole")
              quit()

            else:
              print("I do not understand that yet")
              time.sleep(2)
              os.system('clear')
              quit()
    
        elif fork == "r":
          print("There is a dead end")
          time.sleep(2)
          os.system('clear')
          quit()

        else:
          print("I do not understand that yet")
          time.sleep(2)
          os.system('clear')
          quit()
        
    #done
      elif path == "forward" or path == "f":
        print("There is a river")
        print()
        time.sleep(1.2)
        riverreg = input("Do you want to cross the bridge it or go back? (c/b): ")
        river = riverreg.lower()
        os.system('clear')

        if river == "c" and not riverfall == 1:
          print("There is two paths")
          print()
          time.sleep(1.2)
          path2reg = input("Do you want to go left or right (l/r): ")
          path2 = path2reg.lower()
          os.system('clear')

          if path2 == "l":
            print("You found an exit to the forest")
            time.sleep(2)
            os.system('clear')
            quit()

          elif path2 == "r":
            print("You found a staircase in the middle of the forest")
            print()
            time.sleep(1.2)
            stairsreg = input("Do you want to go down or keep going? (d/g): ")
            stairs = stairsreg.lower()
            os.system('clear')

            if stairs == "d":
              print("There was nothing, but you are stuck")
              print()
              time.sleep(2)
              os.system('clear')
              quit()

            elif stairs == "g":
              print("There is a waterfall")
              print()
              time.sleep(1.2)
              waterfall1reg = input("Do you want to go under it or around it? (u/a): ")
              waterfall1 = waterfall1reg.lower()
              os.system('clear')

              if waterfall1 == "u":
                print("There was nothing under the waterfall")
                time.sleep(2)
                os.system('clear')
                quit()

              elif waterfall1 == "a":
                print("You found an exit to the forest!")
                time.sleep(2)
                os.system('clear')
                quit()

              else:
                print("I do not understand that yet")
                time.sleep(2)
                os.system('clear')
                enter()
                
            else: 
              print("I do not understand that yet")
              time.sleep(2)
              os.system('clear')
              enter()
              
          else:
            print("I do not understand that yet")
            time.sleep(2)
            os.system('clear')
            enter()
          
        elif river == "c" and riverfall == 1:
          print("You fell into the river")
          time.sleep(2)
          os.system('clear')
          quit()

        elif river == "b":
          os.system('clear')
          print("Ok!")
          time.sleep(2)
          os.system('clear')
          lrfb()

        else:
          print("Please input c or b")
          time.sleep(2)
          os.system('clear')
          enter()
          

      else:
        print("Please input l, r, f, b")
        time.sleep(2)
        os.system('clear')
        lrfb()

      
    #runs the enter funtion
    enter()
    #runs the lrfb funtion
  lrfb()
  #runs the start fuction
start()
import random
import wikipedia as wiki
import pywhatkit

def options(): # Prints all the options
  print("")
  print("========================")
  print('''Options:
  1) Simple Calculator
  2) Caculator Functions
  3) Password Generator
  4) Random Number Generator 
  5) Rubiks Cube Menu
  6) Echo
  7) Web Search
  8) Search YouTube
  ?) Sign Out
  0) Power Off
  ''')
  print("========================")

def calculator(): # Simple addition, subtraction etc.
    calculatoranswer = eval(input("What is the calculation? > "))
    print(f"That equals to {calculatoranswer}")

def welcome(): # Entering Password to sign in
  print("================================================================================================")
  print("Welcome to SwestBot V2! I am a new iteration of a chatbot/smart assistant the_swest made a few years ago")
  if input("Password (777) > ") == password:
    print("Authorised.")
  else:
    print("Incorrect.")
    welcome()

def passwordgen(): # Generates a password
    chars = "abcdefghijklmnopqrstuvqxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789"
    passnum = int(input("Number of passwords? > "))
    passlen = int(input("Length of passwords? > "))
    print("")
    if passnum == 1:
        print("Here is your password:")
        print("")
    else:
        print("Here are your passwords:")
        print("")
    for i in range(passnum):
        password = ""
        for c in range(passlen):
            password += random.choice(chars)
        print(password)

def calcpower(x,y): # Calculates the powers of two numbers
    print(f"{x} to the power of {y} is {x**y}")

def cuboidmenu(): # Menu of the cuboid functions
    print('''Options:
    1) Volume
    2) Surface Area
    ''')
    cuboidchoice = input("Cuboid Functiom > ")
    if cuboidchoice == "1":
        print("")
        cuboidl = int(input("What is the length of the cuboid? > "))
        cuboidw = int(input("What is the width of the cuboid? > "))
        cuboidh = int(input("What is the height of the cuboid? > "))
        print("")
        print(f"The volume of the cuboid is {cuboidl*cuboidh*cuboidw}")
        print("")
    elif cuboidchoice == "2":
        print("")
        cuboidl = int(input("What is the length of the cuboid? > "))
        cuboidw = int(input("What is the width of the cuboid? > "))
        cuboidh = int(input("What is the height of the cuboid? > "))
        print("")
        print(f"The surface area of the cuboid is {2*((cuboidl*cuboidw)+(cuboidw*cuboidh)+(cuboidl*cuboidh))}")
        print("")
    else:
        print("Invalid Choice")

def cylindermenu(): # Menu of the cylinder functions
    print('''Options:
    1) Volume
    2) Surface Area
    ''')
    cylinderchoice = input("Cylinder Function > ")
    if cylinderchoice == "1":
        print("")
        cylinderr = int(input("What is the radius of the cylinder? > "))
        cylinderh = int(input("What is the height of the cylinder? > "))
        print("")
        cylcalc = pi*(cylinderr**2)*cylinderh
        print(f"The volume of the cylinder is {round(cylcalc,2)}")
        print("")
    elif cylinderchoice == "2":
        print("")
        cylinderr = int(input("What is the radius of the cylinder? > "))
        cylinderh = int(input("What is the height of the cylinder? > "))
        print("")
        cycalc = (2*pi*cylinderr*cylinderh)+(2*pi*(cylinderr**2))
        print(f"The surface area of the cuboid is {round(cycalc,2)}")
        print("")
    else:
        print("Invalid Choice")

def spheremenu(): # Menu of the sphere functions
    print('''Options:
    1) Volume
    2) Surface Area
    ''')
    spherechoice = input("Sphere Functiom > ")
    if spherechoice == "1":
        print("")
        spherer = int(input("What is the radius of the sphere? > "))
        print("")
        spherecalc = (4/3)*pi*(spherer**3)
        print(f"The volume of the sphere is {round(spherecalc,2)}")
        print("")
    elif spherechoice == "2":
        print("")
        spherer = int(input("What is the radius of the sphere? > "))
        print("")
        spherecalc = 4*pi*(spherer**2)
        print(f"The surface area of the sphere is {round(spherecalc,2)}")
        print("")
    else:
        print("Invalid Choice")

def calcmenu(): # Menu for the calculator functions
    print('''Functions:
    1) Power
    2) Average
    3) Cuboid Menu
    4) Cylinder Menu
    5) Sphere Menu
    ''')
    calcchoice = input("Calculator Function > ")
    if calcchoice == "1":
        print("")
        powernum = int(input("What number should be underneath the power? > "))
        powertop = int(input("What is the power? > "))
        calcpower(powernum,powertop)
    elif calcchoice == "2":
        print("")
        avgcount = int(input("How many numbers? > "))
        total = 0
        for i in range(avgcount):
            avgnumber = input(f"Enter number {str(i+1)} > ")
            total = total + int(avgnumber)
        result = total / avgcount
        print("")
        print(f"The average is {str(round(result,2))}")
    elif calcchoice == "3":
        cuboidmenu()
    elif calcchoice == "4":
        cylindermenu()
    elif calcchoice == "5":
        spheremenu()
    else:
        print("Invalid Choice")

def randnum(): # Random Number Generator
    randlb = int(input("What is the lower bound? > "))
    randhb = int(input("What is the upper bound? > "))
    if randlb < randhb:
        print(f"The number is {random.randint(randlb,randhb)}")
    else:
        print("Error: Higher Bound is less than Lower Bound.")

def rubiksscramble():
    moves = ["R", "F", "U", "L", "B", "D", "R'", "F'", "U'", "L'", "B'", "D'", "R2", "F2", "U2", "L2", "B2", "D2"]
    scramblenum = int(input("Number of scrambles? > "))
    scramblelen = int(input("Length of scrambles? > "))
    print("")
    if scramblenum == 1:
        print("Here is your scramble:")
        print("")
    else:
        print("Here are your scrambles:")
        print("")
    for i in range(scramblenum):
        scramble = ""
        for c in range(scramblelen):
            scramble += random.choice(moves)
            scramble += " "
        print("")
        print(scramble)

def rubiksaverage():
    solves = []
    solves.append(float(input("1st Solve > ")))
    solves.append(float(input("2nd Solve > ")))
    solves.append(float(input("3rd Solve > ")))
    solves.append(float(input("4th Solve > ")))
    solves.append(float(input("5th Solve > ")))
    solves.sort()
    solves.pop(0)
    solves.pop(-1)
    cubeavg = (solves[0]+solves[1]+solves[2])/3
    print(f"The average of those solves is {round(cubeavg,2)}")

def cubemenu():
    print('''Options:
    1) Scrambler
    2) Average Calculator
    ''')
    rubikschoice = input("Cube Function > ")
    if rubikschoice == "1":
        rubiksscramble()
    elif rubikschoice == "2":
        rubiksaverage()
    else:
        print("Invalid Choice")

def echo():
    print("I will copy you! Say 'stop' to end.")
    echo1=input("Say something! > ")
    while echo1 != "stop":
        echo1 = input(f"Echo: {echo1}!  > ")

def pywiki():
    searchterm = input("Thing to search > ")
    searchlen = input("How many sentences should the result be? > ")
    wikiresult = wiki.summary(searchterm, sentences = searchlen)
    print("")
    print(wikiresult)

def youtube():
    videoterm = input("What do you want to watch? > ")
    pywhatkit.playonyt(videoterm)

password = "777"
pi = 3.141592653589793
welcome()
while True:
    options()
    choice = input("Option > ")
    if choice == "1":
        print("")
        calculator()
    elif choice == "2":
        print("")
        calcmenu()
    elif choice == "3":
        print("")
        passwordgen()
    elif choice == "4":
        print("")
        randnum()
    elif choice == "5":
        print("")
        cubemenu()
    elif choice == "6":
        echo()
    elif choice == "7":
        pywiki()
    elif choice == "8":
        youtube()
    elif choice == "?":
        print("")
        welcome()
    elif choice == "0":
        print("")
        print("Powering Off")
        exit()
    else:
        print("Invalid choice.")
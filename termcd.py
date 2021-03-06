#!/usr/bin/env python3

from sys import argv, stderr
import sys, os
import time
import math

def printUsageAndExit(code=1):
    stderr.write("Usage: python3 "+sys.argv[0]+" [OPTION]... [TIME]\n\
    TIME                      The time to count down from, specified in the MM:SS format. Minutes can be omitted if 0.\n\
    -n        --no-colors     Don't color the output.\n\
    -h        --help          Print help message.\n\
")
    sys.exit(code)

if len(argv) < 2:
    printUsageAndExit()

USE_COLORS = True
COUNT_DOWN_FROM = 0
for arg in argv[1:]:
    if arg == "-h" or arg == "--help":
        printUsageAndExit(0)
    elif arg == "-n" or arg == "--no-colors":
        USE_COLORS = False
    else:
        try:
            values = tuple(int(x) for x in arg.split(":"))
            if len(values) == 2:
                minutes, seconds = values
            elif len(values) == 1:
                minutes = 0
                seconds = values[0]
            else:
                printUsageAndExit()

            COUNT_DOWN_FROM = minutes*60+seconds
        except:
            printUsageAndExit()
if COUNT_DOWN_FROM < 1:
    printUsageAndExit()

DIGITS = {
"0":
"""
     000000000     
   00:::::::::00   
 00:::::::::::::00 
0:::::::000:::::::0
0::::::0   0::::::0
0:::::0     0:::::0
0:::::0     0:::::0
0:::::0 000 0:::::0
0:::::0 000 0:::::0
0:::::0     0:::::0
0:::::0     0:::::0
0::::::0   0::::::0
0:::::::000:::::::0
 00:::::::::::::00 
   00:::::::::00   
     000000000     
""",
"1":
"""
  1111111   
 1::::::1   
1:::::::1   
111:::::1   
   1::::1   
   1::::1   
   1::::1   
   1::::l   
   1::::l   
   1::::l   
   1::::l   
   1::::l   
111::::::111
1::::::::::1
1::::::::::1
111111111111\
""",
"2":
"""
 222222222222222    
2:::::::::::::::22  
2::::::222222:::::2 
2222222     2:::::2 
            2:::::2 
            2:::::2 
         2222::::2  
    22222::::::22   
  22::::::::222     
 2:::::22222        
2:::::2             
2:::::2             
2:::::2       222222
2::::::2222222:::::2
2::::::::::::::::::2
22222222222222222222\
""",
"3":
"""
 333333333333333   
3:::::::::::::::33 
3::::::33333::::::3
3333333     3:::::3
            3:::::3
            3:::::3
    33333333:::::3 
    3:::::::::::3  
    33333333:::::3 
            3:::::3
            3:::::3
            3:::::3
3333333     3:::::3
3::::::33333::::::3
3:::::::::::::::33 
 333333333333333   \
""",
"4":
"""
       444444444  
      4::::::::4  
     4:::::::::4  
    4::::44::::4  
   4::::4 4::::4  
  4::::4  4::::4  
 4::::4   4::::4  
4::::444444::::444
4::::::::::::::::4
4444444444:::::444
          4::::4  
          4::::4  
          4::::4  
        44::::::44
        4::::::::4
        4444444444\
""",
"5":
"""
555555555555555555 
5::::::::::::::::5 
5::::::::::::::::5 
5:::::555555555555 
5:::::5            
5:::::5            
5:::::5555555555   
5:::::::::::::::5  
555555555555:::::5 
            5:::::5
            5:::::5
5555555     5:::::5
5::::::55555::::::5
 55:::::::::::::55 
   55:::::::::55   
     555555555     \
""",
"6":
"""
        66666666   
       6::::::6    
      6::::::6     
     6::::::6      
    6::::::6       
   6::::::6        
  6::::::6         
 6::::::::66666    
6::::::::::::::66  
6::::::66666:::::6 
6:::::6     6:::::6
6:::::6     6:::::6
6::::::66666::::::6
 66:::::::::::::66 
   66:::::::::66   
     666666666     \
""",
"7":
"""
77777777777777777777
7::::::::::::::::::7
7::::::::::::::::::7
777777777777:::::::7
           7::::::7 
          7::::::7  
         7::::::7   
        7::::::7    
       7::::::7     
      7::::::7      
     7::::::7       
    7::::::7        
   7::::::7         
  7::::::7          
 7::::::7           
77777777            \
""",
"8":
"""
     888888888     
   88:::::::::88   
 88:::::::::::::88 
8::::::88888::::::8
8:::::8     8:::::8
8:::::8     8:::::8
 8:::::88888:::::8 
  8:::::::::::::8  
 8:::::88888:::::8 
8:::::8     8:::::8
8:::::8     8:::::8
8:::::8     8:::::8
8::::::88888::::::8
 88:::::::::::::88 
   88:::::::::88   
     888888888     \
""",
"9":
"""
     999999999     
   99:::::::::99   
 99:::::::::::::99 
9::::::99999::::::9
9:::::9     9:::::9
9:::::9     9:::::9
 9:::::99999::::::9
  99::::::::::::::9
    99999::::::::9 
         9::::::9  
        9::::::9   
       9::::::9    
      9::::::9     
     9::::::9      
    9::::::9       
   99999999        \
""",
":":
"""
      
      
      
::::::
::::::
::::::
      
      
      
::::::
::::::
::::::
      
      
      
      \
"""
}

DIGIT_HEIGHT = len(DIGITS["0"].splitlines())
for digitK, digit in DIGITS.items():
    if len(digit.splitlines()) != DIGIT_HEIGHT:
        sys.stderr.write("Digit "+digitK+" is not padded\n")
        sys.exit(1)

def printDigits(digits: str):
    for i in range(DIGIT_HEIGHT):
        for digit in digits:
            print(" "+DIGITS[digit].splitlines(False)[i], end=" ")
        print()

def clearScreen():
    if os.getenv("TERM", None):
        if os.system("clear"):
            if os.system("cls"):
                print("\n"*500)
    else:
        print("\n"*500)
 

START_TIME = time.time()

print("\033[?25l") # Hide cursor
while True:
    try:
        remainingTime = max(int(COUNT_DOWN_FROM-(time.time()-START_TIME)+1), 0)
 
        clearScreen()
        if USE_COLORS:
            r, g, b = abs(math.sin(time.time()/10)), abs(math.cos(time.time()/10)), 1-abs(math.sin(time.time()/3))
            print("\033[38;2;{};{};{}m".format(int(r*255), int(g*255), int(b*255)))

        formattedRemainingTime = str(remainingTime//60).zfill(2)+":"+str(remainingTime%60).zfill(2)
        printDigits(formattedRemainingTime)
        
        if time.time() - START_TIME > COUNT_DOWN_FROM:
            print("\a")
        
        time.sleep(0.1)
    except KeyboardInterrupt:
        clearScreen()
        print("\033[?25h") # Show cursor
        sys.exit(0)


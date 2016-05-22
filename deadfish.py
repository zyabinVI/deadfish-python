import sys
try:
    sys.ps1
except NameError:
    sys.ps1 = '>>> '

# Initialisation
x = 0

while True:
    # Get user input
    cmd = raw_input(sys.ps1)
    if x == 256 or x == -1:
        # Overflow, reset accumulator
        x = 0
    # Process input
    if cmd == "i" or cmd == "x":
        x += 1 # Increment
    elif cmd == "d":
        x -= 1 # Decrement
    elif cmd == "s" or cmd == "k":
        x **= 2 # Square
    elif cmd == "o" or cmd == "c":
        print x # Output
    elif cmd == "h":
        break # Halt
    else:
        print "Unrecognized command."


# Initialisation
x = 0

while True:
    # Get user input
    cmd = raw_input(">> ")
    if x == 256 or x == -1:
        # Overflow, reset accumulator
        x = 0
    # Process input
    if cmd == "i" or cmd == "x":
        x = x + 1 # Increment
    elif cmd == "d":
        x = x - 1 # Decrement
    elif cmd == "s" or cmd == "k":
        x = x * x # Square
    elif cmd == "o" or cmd == "c":
        print x # Output
    elif cmd == "h":
        break # Halt
    else:
        print "Unrecognized command."

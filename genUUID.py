#!/usr/bin/env python3

# Generate UUID version 1 or version 4

# Imports
import uuid
import sys
import time


# Printer
def printer(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    print()


# UUID version 1 generator
def generate_uuid_1():
    generated_uuid = uuid.uuid1()
    return f"Version1 UUID: \033[2;32m{str(generated_uuid)}\033[m\n"


# UUID version 4 generator
def generate_uuid_4():
    generated_uuid = uuid.uuid4()
    return f"Version4 UUID: \033[2;32m{str(generated_uuid)}\033[m\n"


# Takes arguments
arguments = sys.argv


# Help message
help_message = """
Help: python getUUID.py [[-h] [-v1] [-v4]]
    -h  : Show this message and exit.
    -v1 : Generate version 1 UUID
    -v4 : Generate version 4 UUID

* What is a Version 1 UUID?
    A Version 1 UUID is a universally unique identifier that 
    is generated using a timestamp and the MAC address of 
    the computer on which it was generated.

* What is a version 4 UUID?
    A Version 4 UUID is a universally unique identifier that 
    is generated using random numbers.using a secure random 
    number generator.
"""


# Run the program
if __name__ == "__main__":
    if "-h" in arguments:
        print(help_message)
        sys.exit()

    if "-v1" in arguments:
        printer("\033[2;34m* Generating UUID version 1 for you...\033[m")
        printer(generate_uuid_1())

    if "-v4" in arguments:
        printer("\033[2;34m* Generating UUID version 4 for you...\033[m")
        printer(generate_uuid_4())

    if len(sys.argv) == 1:
        print("\033[2;31mError: no argument found! Use -h\033[m")

# EOF

import sys

def print_to_stderr(message):
    sys.stderr.write(message + '\n')

print_to_stderr("This is an error message")
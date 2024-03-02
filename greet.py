import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Print a greeting message.')

# Add an argument for the name
parser.add_argument('name', type=str, help='The name to greet')

# Parse the command-line arguments
args = parser.parse_args()

# Print the greeting message
print(f'Hello, {args.name}!')

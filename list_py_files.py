import os

# List all .py files and their sizes
for filename in os.listdir('.'):
    if filename.endswith('.py'):
        size = os.path.getsize(filename)
        print(f"{filename} - {size} bytes")

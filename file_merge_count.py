# Merge two files and count lines, words, and characters

# Create two sample text files
with open('file1.txt', 'w') as f:
    f.write("Hello World\nThis is file 1.\nPython is fun!")
with open('file2.txt', 'w') as f:
    f.write("File 2 here.\nLearning File Handling in Python.")

# Merge files
with open('merged.txt', 'w') as merged:
    for filename in ['file1.txt', 'file2.txt']:
        with open(filename) as f:
            merged.write(f.read() + "\n")

# Count lines, words, and characters in merged file
with open('merged.txt') as f:
    content = f.read()
    lines = content.strip().split("\n")
    words = content.split()
    chars = len(content)

print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", chars)

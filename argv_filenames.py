import sys

if len(sys.argv) < 2:
    print("Usage: python argv_filenames.py <file1> <file2> ...")
else:
    for filename in sys.argv[1:]:
        print(f"Filename from argv: {filename}")

import os
print(lambda f: "File content:\n" + f.read() if not f is None else "Error: File not found.")(lambda n: open(n, "r") if os.path.isfile(n) else None)(input("Enter the file name:\n"))
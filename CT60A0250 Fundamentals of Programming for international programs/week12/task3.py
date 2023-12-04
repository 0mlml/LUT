reverse_string = lambda s: s if len(s) == 0 else reverse_string(s[1:]) + s[0]

print((lambda s: f"Original String: {s}\nReversed String: {reverse_string(s)}")(input("Give a string to reverse:\n")))
ascii_chr = 65
for i in range(0, 6):
    for j in range(0, i+1):
        char = chr(ascii_chr)
        print(char, end='')
        ascii_chr += 1
    print()

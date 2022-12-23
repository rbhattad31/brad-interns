def checkRotation(s1, s2):

    if len(s1) != len(s2):
        return False
    temp = s1 + s2

    if s2 in temp:
        return True
    else:
        return False
s1 = "HELLO"
s2 = "OLLEH"

if checkRotation(s1, s2):
    print("Given Strings are rotations of each other.")
else:
    print("Given Strings are not rotations of each other.")

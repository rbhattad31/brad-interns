try:
    print(eval("hello world"))
except SyntaxError as se:
    print("Syntax error %s (%s %s): %s" %(se.filename, se.lineno, se.offset, se.text))
    print(se)

site = "facebook"     #  indentation error
if site == "facebook":
    print("logging on to facebook")
else:
    print("retype the url")
print("all set")


secret = "secretcode"
print "You get 3 chances to get this right"
for i in range(0,3):
    password = raw_input("Please enter your password: ")
    if password == secret:
        print "You're in!"
        break
if password != secret:
    print "Sorry you've lost your chance, it's too late now"


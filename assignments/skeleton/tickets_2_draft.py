num_tickets = 100

print "There are %d tickets available" % (num_tickets)
print "Get your tickets before we sell out!"

tickets_wanted = raw_input("How many tickets would you like?\n")

tickets_wanted = int(tickets_wanted)

#Check that the number of tickets available is less than
#the number of tickets wanted
if tickets_wanted > num_tickets:
    #Output to the screen a message saying we don't have
    #that many tickets available
    print "Sorry we don't have that many tickets available"
else:
    #Calculate the number of tickets left

    #Output to the screen a message showing how many tickets were bought
    #For example: You bought 3 tickets(3)

    #Output to the screen a message showing how many tickets
    #are left
    print "There are %d ticket(s) left" % (num_tickets)






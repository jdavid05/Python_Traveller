#========================================================================
# Task 1: Cities visited by a person
#========================================================================
#------------------------------------------------------------------------
# Create the list of people
#------------------------------------------------------------------------

Ans = "Y"
while Ans.upper() == "Y":
    print "\n"
    print "1. List the cities for a traveler"
    print "2. Add to the list"
    print "3. Exit"
    
    Ans = raw_input("\nPlease select an option (1, 2, or 3):")

    if int(Ans) > 3:
        print "\nThat is not a good answer. Please enter 1, 2 or 3:"
        Ans = "Y"
        

    while Ans == "1":
        # Open the travel.txt file
        infile = open ('travel.txt', 'r')
        # read a line of data
        line = infile.readline()
        # Start an empty list of people
        listf = []
        lista = []
        # Loop:
        while line != "":
            # get the three values from the line
            l, f, c = line.split (',')
            l = l.strip('"')
            f = f.strip('"')
            c = c.rstrip('\n')
            c = c.strip('"')
            
            
            # if the person's name isn't in the list of people:
            there=False
            form = l + " " + f
            for name in listf:
            #add it to the list.
                if form.upper() == name.upper():
                    there = True
                    break
            if not there:
                listf.append(form)

            # if the city name isn't in the list of cities:
            there=False
            form = c
            for name in lista:
            #add it to the list.
                if form.upper() == name.upper():
                    there = True
                    break
            if not there:
                lista.append(form)
                
            # Read the next line
            line = infile.readline()
        # Close the file
        infile.close


        # Sort the list --> listname.sort()
        listf.sort()
        # Loop to display each name in the list
        print "      Traveller Names"
        print "============================="
        for l in listf:
            print "      %s" % l

        # Ask for a name to list the cities travelled to.
        name = raw_input("Enter a name to list cities:\n")

        #------------------------------------------------------------------------
        # Look through the file to find the pets owned.
        #------------------------------------------------------------------------
        # Open the file:
        infile = open ('travel.txt', 'r')
        # Read a line
        line = infile.readline()
        # print heading " Cities travelled to:"
        print "\nVisited List:"
        print "------------------------"
        # Loop:
        lista = []
        while line != "":
            # Get the three fields:
            l,f,c = line.split(',')
            # Clean the values
            l=l.strip('"')
            f=f.strip('"')
            c=c.rstrip('\n')
            c=c.strip('"')

            form = l + " " + f
##
##            notthere = False
##            form = l + " " + f
##            # If the value from the file matches the name entered:
##            for name in lista:
##                if form.upper() == name.upper():
##                    lista.append(c)
##                    notthere = True
            # Print the city that was visited
            if form.upper() == name.upper():
                print "%s has travelled to %s" % (name, c)
                
            # Read the next line
            line = infile.readline()
            
        for i in lista:
            print i
        # Close the file
        infile.close()
        Ans = raw_input("\n\n\tProcess another file? (Y/N) : ")
        if len(Ans) == 0:
            Ans = "Y"
        

    #========================================================================
    # Task 2: Append to the file
    #========================================================================
    while Ans == "2":
        # Prompt for the three values. Repeat prompt until something is entered.
        one = raw_input('\nplease enter a last name to add to the file:')
        two = raw_input('\nplease enter a first name to add to the file:')
        three = raw_input('\nplease enter the city they travelled to to add it to the file:')
        # Open file, write values, close file.
        afile = open('travel.txt','a')
        print '"%s","%s","%s"'% (two, one, three)
        afile.write('"%s","%s","%s"\n'% (two, one, three))
        afile.close()
        Ans = raw_input("\nProcess another file? (Y/N) : ")
        if len(Ans) == 0:
            Ans = "Y"
        


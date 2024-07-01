import mysql.connector

#The menu for all event interactions
def eventMenu():

    exit = False
    #Menu
    while not exit:
        print("What would you like to find")
        print("1) Concerts")
        print("2) Conventions")
        print("3) Festivals")
        print("4) Show All events")
        print("5) Back")

        eventInput = input()

        if (eventInput == '1'):
            concerts()

        elif (eventInput == '2'):
            conventions()

        elif (eventInput == '3'):
            festivals()

        elif (eventInput == '4'):
            showAllEvent()

        elif (eventInput == '5'):
            exit = True
            print("Returning to Main Menu")
    
        else:
            print("Invalid input please try again")


#Show all Concerts
def concerts():
    #Show only the esential data from the event,location, and concert
    print("ID, Performer, Genres, Total amount of Tickets, Tickets left, Start time and date, End time and Date, Address, City")
    cursor.execute("SELECT  public_events.event_id,artist,genre,total_tickets,ticket_left, start_date,end_date,address,city FROM concert JOIN public_events ON concert.event_id = public_events.event_id JOIN location ON location.location_id = public_events.location_id;")
    for i in cursor:
        print(i)
    print()


#Show only Cconventions
def conventions():
    #Show only the esential data from the event,location, and conventions
    print("ID, Name, Theme, Open to puvlic, Start time and date, End time and Date, Address, City")
    cursor.execute("SELECT  public_events.event_id,`name`,theme,open_to_public, start_date,end_date,address,city FROM convention JOIN public_events ON convention.event_id = public_events.event_id JOIN location ON location.location_id = public_events.location_id;")
    for i in cursor:
        print(i)
    print()


#Show only festivals
def festivals():
    print("ID, Name, Celebrating, Start time and date, End time and Date, Address, City")
    cursor.execute("SELECT  public_events.event_id ,`name`, celebration, start_date,end_date,address,city FROM festival JOIN public_events ON festival.event_id = public_events.event_id JOIN location ON location.location_id = public_events.location_id;")
    for i in cursor:
        print(i)
    print()


#Show all the events
def showAllEvent():
    concerts()
    conventions()
    festivals()


#Create a new event
def createEvent():

    cursor.execute("SELECT * FROM location WHERE is_open = TRUE")
    openLocation= cursor.fetchall()

    #See if any location is open
    if openLocation == []:
        print("Can not create event due to no open location")
        return
    else:
        print("Id, Address, City, Capacity, is_avaliable (1 = Yes, 0 = no), Owner_id")
        cursor.execute("SELECT * FROM location WHERE is_open = TRUE")
        for i in cursor:
            print(i)

    locationID = input("Select the location where the event will be held")
    startDateHour = input("What time and date does it start (YYYY-MM-DD HH:MM::SS)")
    endDateHour = input("What time and date does it end (YYYY-MM-DD HH:MM::SS)")


    #If valid input add it if not crash
    try:
        cursor.execute("INSERT INTO public_events (start_date, end_date, location_id) VALUES ('%s','%s',%s)" % (startDateHour, endDateHour,locationID))
        #Change the location so it is not open for a new event
        cursor.execute("UPDATE location SET is_open = %s WHERE location_id = %s" , (False, locationID))

    except:
        db.rollback()
        print("Error \n Returning")
        return

    eventType = input("What kind of event is it \n1) Concert \n2) Convention \n3) Festival")
    

    #Create a concert
    if eventType == "1":
        artist = input("Who is performing")
        genre = input("What kind of music do they play")
        totalTickets = input("How many tickets are avaliable")

        #If valid input add it if not crash
        try:
            cursor.execute("INSERT INTO concert (event_id, artist,genre,total_tickets,ticket_left) VALUES (LAST_INSERT_ID(),%s,%s,%s,%s);",(artist,genre,totalTickets,totalTickets))
        except:
            db.rollback()
            print("Error \nReturning")
            return
    


    #Create a convention
    elif eventType == '2':
        name = input("What is the name of the convention")
        theme = input("What is the theme of the convention")
        isOpen = input("Can anyone walk in at anytime (T/F)")

        if isOpen == "T" or isOpen == 't':
            isOpen = True
        elif isOpen == "F" or isOpen == 'f':
            isOpen = False


        #If valid input add it if not crash
        try:
            cursor.execute("INSERT INTO convention (event_id, name, theme, open_to_public) VALUES (LAST_INSERT_ID(),'%s','%s',%s);" % (name,theme,isOpen))
        except:
            db.rollback()
            print("Error \nReturning")
            return



    #Create a festival    
    elif eventType == '3':
        festivalName = input("What is the name of the festival")
        celebration = input("What is it celebrating")

        #If valid input add it if not crash
        try:
            cursor.execute("INSERT INTO festival (event_id,name,celebration) VALUES (LAST_INSERT_ID(), %s,%s);",(festivalName,celebration))
        except:
            db.rollback()
            print("Error \nReturning")
            return

    #The user enter an invalid input
    else:
        print("Error \nReturning")
        return

        
#Delete an event
def deleteEvent():
    #Show all the events
    showAllEvent()

    #Ask for which one to delete
    eventID = input("What is the id of the event that you want to delete")

    #If valid input add it if not crash
    try:
        cursor.execute("DELETE FROM public_events WHERE event_id = %s;"% eventID)
    except:
        db.rollback()
        print("Error \nReturning")  
        return


#Show all the locations
def locations():
    #Show the owner their contact information along side the detail of the location they own
    print("ID, Address, City, Capacity, Availability(1 = Is avaliable , 0 = Not avaliable), Owner Name, Email, Phone Number ")
    cursor.execute("SELECT location_id,address ,city ,capacity , is_open, owner_name, email, phoneNO FROM location JOIN owners ON location.owner_id = owners.owner_id;")
    for i in cursor:
        print(i)
    print()


#Create a new location
def createLocation():
    #Ask if the new location have an existing owner
    ownerExist = input("Is the owner already in the databse? (Y/N)")

    #If Not create a new owner
    if (ownerExist == 'n' or ownerExist == 'N'):
        ownerName = input("What is their name?")
        ownerEmail = input("What is their email?")
        ownerPhone = input("What is their phone number?")


    #If valid input add it if not crash
        try:
            cursor.execute("INSERT INTO owners (owner_name, email, phoneNO ) VALUES (%s, %s,%s );",(ownerName,ownerEmail,ownerPhone))
        except:
            db.rollback()
            print("Error \n Returning")     
            return   
        
        address = input("What is the location's address?")
        city = input("What city is it located in?")
        capacity = input("What is the capacity?")


        #If valid input add it if not crash
        try:
            cursor.execute("INSERT INTO location (address, city, capacity, is_open, owner_id) VALUES (%s,%s,%s,TRUE, LAST_INSERT_ID());",(address,city,capacity))
        except:
            db.rollback()
            print("Error \n Returning")   
            return
        

    elif (ownerExist == 'y' or ownerExist == "Y"):

        #Take in information
        owners()
        ownerId = input("What is there ID?")
        address = input("What is the location's address?")
        city = input("What city is it located in?")
        capacity = input("What is the capacity?")

        #If valid input add it if not crash
        try:
            cursor.execute("INSERT INTO location (address, city, capacity, owner_id, is_open) VALUES (%s, %s,%s,%s,TRUE);",(address,city,capacity,ownerId))
        except:
            db.rollback()
            print("Error \n Returning")  
            return       

    else:
        print("Invalid input\nReturning")
        return


def deleteLocation():
    #Show all locations
    locations()

    locationID = input("What is the id of the location that you want to delete")

    #If valid input add it if not crash
    try:
        cursor.execute("DELETE FROM location WHERE location_id = %s;"% locationID)
    except:
        db.rollback()
        print("Error \n Returning")  

#Show the largest capacity from all locations
def largestLocation():
    cursor.execute("SELECT MAX(capacity) FROM location;")
    for i in cursor:
        print(i)

#Change the amount of ticket avaliable for a concert
def changeTicketAmount():
    concerts()
    concertID = input("Which concert are we changing?")
    ticketsLeft = input("How many tickets are left over now?")

    cursor.execute("UPDATE concert SET ticket_left = %s WHERE event_id = %s;", (ticketsLeft,concertID))

def owners():
    cursor.execute("SELECT * FROM owners")
    for i in cursor:
        print(i)


if __name__ == "__main__":
    #Connect to database
    db = mysql.connector.connect(host = "localhost", user = 'one_cool_dude', passwd = "passwerd", database = 'whats_happening')

    cursor = db.cursor()

    quit = False
    
    #Menu
    while not quit:
        print("------------OPTIONS------------")
        print("1) Find Events")
        print("2) Create Event")
        print("3) Delete Event")
        print("4) See Locations")
        print("5) Create Location")
        print("6) Delete Location")
        print("7) Largest Capacity")
        print("8) Change Ticket Avaliable for Concert")
        print("9) Quit")

        userInput = input()

        if (userInput == '1'):
            eventMenu()

        elif (userInput == '2'):
            createEvent()

        elif (userInput == '3'):
            deleteEvent()

        elif (userInput == '4'):
            locations()

        elif (userInput == '5'):
            createLocation()

        elif (userInput == '6'):
            deleteLocation()

        elif (userInput == '7'):
            largestLocation()

        elif (userInput == '8'):
            changeTicketAmount()

        elif (userInput == '9'):
            print("Exiting")
            quit = True

        else:
            print("Invalid input please try again")

        db.commit()


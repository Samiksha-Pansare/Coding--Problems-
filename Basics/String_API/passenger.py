#lex_auth_0127382193364008961449

#Sample ticket list - ticket format: "flight_no:source:destination:ticket_no"
#Note: flight_no has the following format - "airline_name followed by three digit number

#Global variable
import re


ticket_list=['AI101:MUM:LON:001', 'AI101:MUM:LON:002', 'SI456:MUM:SIN:145', 'EM456:MUM:DUB:098', 'SI456:MUM:SIN:050', 'SI456:MUM:SIN:051']
print("Length: ",len(ticket_list))

def find_passengers_flight(airline_name="AI"):
    #This function finds and returns the number of passengers travelling in the specified airline.
    count=0
    for i in ticket_list:
        string_list=i.split(":")
        if(string_list[0].startswith(airline_name)):
            count+=1
    return count

def find_passengers_destination(destination):
    c=0
    for ticket in ticket_list:
        info_list=ticket.split(":")
        if info_list[2]==destination:
            c=c+1
    return c

def find_passengers_per_flight():
    '''Write the logic to find and return a list having number of passengers traveling per flight based on the details in the ticket_list
    In the list, details should be provided in the format:
    [flight_no:no_of_passengers, flight_no:no_of_passengers, etc.].'''
    flightnamelist=[]
    flight_count=[]
    for ticket in ticket_list:
        info_list=ticket.split(":")
        flight_name=info_list[0]
        flight_name=flight_name

        # print("Ticket:", flight_name)
        if flight_name not in flightnamelist:
            flightnamelist.append(flight_name)
            flight_count.append(1)
        else:
            flight_count[flightnamelist.index(flight_name)]=flight_count[flightnamelist.index(flight_name)]+1
    # print(flight_count)
    result=[]

    # print("Flight Count: ",flight_count)
    # print("Flight Name: ",flightnamelist)
    for i in range(0,len(flight_count)):
        #print("i: ",i)
        result.append(flightnamelist[i]+":"+str(flight_count[i]))
    return result
    

def sort_passenger_list():
    #Write the logic to sort the list returned from find_passengers_per_flight() function in the descending order of number of passengers
    list_passenger_per_flight = find_passengers_per_flight()
    dict1 = {}
    print(list_passenger_per_flight)
    for i in list_passenger_per_flight:
        string_list=i.split(":")
        dict1[string_list[0]] = int(string_list[1])
    dict2 = []
    for key, value in sorted(dict1.items(), key=lambda item: item[1], reverse = True):
        dict2.append(str(key)+":"+str(value))
    return dict2
    #Remove pass and write your logic here


#Provide different values for airline_name and destination and test your program.
print(find_passengers_flight("AI"))
print(find_passengers_destination("LON"))
print(sort_passenger_list())
print(find_passengers_per_flight())
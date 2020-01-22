'''
Akash and Vishal are quite fond of travelling. They mostly travel by railways. They were travelling in a train one day and they got interested in the seating arrangement of their compartment. The compartment looked something like


So they got interested to know the seat number facing them and the seat type facing them. The seats are denoted as follows :

Window Seat : WS
Middle Seat : MS
Aisle Seat : AS

You will be given a seat number, find out the seat number facing you and the seat type, i.e. WS, MS or AS.

INPUT
First line of input will consist of a single integer T denoting number of test-cases. Each test-case consists of a single integer N denoting the seat-number.

OUTPUT
For each test case, print the facing seat-number and the seat-type, separated by a single space in a new line.

'''

n = int(input("No. of inputs: "))
seats = []
for i in range(n):
    x = int(input("Enter seat number: "))
    seats.append(x)

for j in range(len(seats)):
    if seats[j] % 12 in (1,6,7,0):
        print("WS")
        if seats[j] % 12 == 1:
            print("opposite seat is: {}{}".format(seats[j]+11, " WS"))
        elif seats[j] % 12 == 6:
            print("opposite seat is: {}{}".format(seats[j]+1, " WS"))
        elif seats[j] % 12 == 7:
            print("opposite seat is: {}{}".format(seats[j]-1, " WS"))
        elif seats[j] % 12 == 0:
            print("opposite seat is: {}{}".format(seats[j]-11, " WS"))
        else:
            print("Invalid WS")
            
    elif seats[j] % 12 in (2,5,8,11):
        print("MS")
        if seats[j] % 12 == 2:
            print("opposite seat is: {}{}".format(seats[j]+9, " MS"))
        elif seats[j] % 12 == 5:
            print("opposite seat is: {}{}".format(seats[j]+3, " MS"))
        elif seats[j] % 12 == 8:
            print("opposite seat is: {}{}".format(seats[j]-3, " MS"))
        elif seats[j] % 12 == 11:
            print("opposite seat is: {}{}".format(seats[j]-9, " MS"))
        else:
            print("Invalid MS")
            
    elif seats[j] % 12 in (3,4,9,10):
        print("AS")
        if seats[j] % 12 == 3:
            print("opposite seat is: {}{}".format(seats[j]+7, " AS"))
        elif seats[j] % 12 == 4:
            print("opposite seat is: {}{}".format(seats[j]+5, " AS"))
        elif seats[j] % 12 == 9:
            print("opposite seat is: {}{}".format(seats[j]-5, " AS"))
        elif seats[j] % 12 == 10:
            print("opposite seat is: {}{}".format(seats[j]-7, " AS"))
        else:
            print("Invalid AS")
    else:
        print("Invalid seat number")

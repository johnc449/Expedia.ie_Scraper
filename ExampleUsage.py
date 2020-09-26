#example usage
from main import Main
import time

day=27   #date of departure, automatically sets return 2 days later
month=9

with open("EuropeanAirportCodes.txt", "r") as airportList:      #opens list of IATA codes 
    for line in airportList:    #loops over list of IATA codes
        stripped_line= line.strip()    #cleans the line up
        for price in Main.price("DUB",stripped_line,[str(day),str(month),"2020"],[str(int(day)+3),str(month),"2020"],"1"):   #loops over returned prices
            print(price)       
            if(price.isdigit()==True and float(price)<30):   #ignores prices over £1000, because who wants to pay over £1000 for a flight? I'll fix this later
                                                           #sends email if price is below 30 Euros 
                Main.sendEmailToMyself(price+"    "+str(day)+
                                       " "+str(month) ,"Good Price "
                                       +stripped_line,"recieverEmail@gmail.com",
                                       "senderEmail@gmail.com","password")  #substitute emails here, sends email with date and price
        time.sleep(Main.waitingTime)
           

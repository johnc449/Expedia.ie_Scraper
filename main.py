from selenium import webdriver        #importing necessary modules
from selenium.webdriver.common.keys import Keys
import time        #using time.sleep to avoid detection by website
from selenium.webdriver.chrome.options import Options
options = Options()


class Main:
    loadingTime=15  #time it waits for pages to load
    
                #there is probably a more elegant way to do this
    
    waitingTime=60   #time it waits before having another go at site
    def price(departDestination,
              arrivalDestination,
              departDate,
              returnDate,
              numberAdults):
        #departDestination= IATA code for depart airport
        #arrivalDestintation=IATA code for arrival airport
        #departDate= Date of departure
        #returnDate= Date of return
        #numberAdults= Number of adults leaving, I haven't implemented kids pricing yet
        #date format day: arrivalDate[0] DD     month: arrivalDate[1] MM     year: arrivalDate[2] YY

        driver = webdriver.Chrome("./chromedriver.exe", chrome_options=options)   #opens chromedriver, has to have window as it is hard to avoid detection
        
        driver.get("https://www.expedia.ie/Flights-Search?flight-type=on&mode=search&trip=roundtrip&leg1=from%3A%28"+
                   departDestination+"%29%2Cto%3A%28"+arrivalDestination+"%29%2Cdeparture%3A"+departDate[0]+"%2F"+
                   departDate[1]+"%2F"+departDate[2]+"TANYT&options=cabinclass%3Aeconomy&leg2=from%3A%28"+arrivalDestination+
                   "%29%2Cto%3A+%28"+departDestination+"%29%2Cdeparture%3A"+returnDate[0]+"%2F"+returnDate[1]+"%2F"+
                   returnDate[2]+"TANYT&passengers=children%3A0%2Cadults%3A"+numberAdults+
                   "%2Cseniors%3A0%2Cinfantinlap%3AY&fromDate="+departDate[0]+"%2F"+departDate[1]+"%2F"+departDate[2]+
                   "&toDate="+returnDate[0]+"%2F"+returnDate[1]+"%2F"+returnDate[2]+"&d1="+departDate[2]+
                   "-"+departDate[1]+"-"+departDate[0]+"&d2="+returnDate[2]+"-"+returnDate[1]+"-"+returnDate[2])   
        #was complex to reverse engineer and is difficult to understand, probably best not to touch this 

        time.sleep(Main.loadingTime)    #time waited for page to load

        results= driver.find_element_by_id("flightModuleList")   #dismantles page as necessary 
        results= results.find_elements_by_tag_name('li')
        prices=[]
        for result in results:   #loops over results and ignores ads/gaps
            try:
                prices.append(result.find_element_by_tag_name('h3').text.split("€")[1])  
        
            except:
                pass

        driver.quit()   # Closes window
        return(prices)  # Returns prices in array
    
    def sendEmailToMyself(text,
                          subject,
                          recieverEmail,
                          senderEmail,
                          password):
        import smtplib, time
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart

        # creates SMTP session 
        s = smtplib.SMTP("smtp.gmail.com", 587) 
 
        # start TLS for security 
        s.starttls()
 
        # Authentication 
        s.login(senderEmail, password)
 
        # Instance of MIMEMultipart 
        msg = MIMEMultipart("alternative")
 
        # Write the subject
        msg["Subject"]= subject
 
        msg["From"]=senderEmail
        msg["To"]=recieverEmail
 
        # Plain text body of the mail
        text = text
 
        # Attach the Plain body with the msg instance
        msg.attach(MIMEText(text, "plain"))
 
        # HTML body of the mail
        html ="<h2>"+text+"</h2>"
 
        # Attach the HTML body with the msg instance
        msg.attach(MIMEText(html, "html"))
 
        # Sending the mail
        s.sendmail(senderEmail, recieverEmail, msg.as_string())
        s.quit()
        print('Email Sent')

        

        
       




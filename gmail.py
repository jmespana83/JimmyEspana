import smtplib
import time
import imaplib
import email
import time
import robin_stocks as r
import shutil

# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------


ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "baldis.basics" + ORG_EMAIL
FROM_PWD    = "_123"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993

lst = []
saidDelimiter = "kdslk8732872mcmc7474irir"
#saidDelimiter = "Alert: "
thecounterhelper = 0



def read_email_from_gmail():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')

        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]

        id_list = mail_ids.split()  
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])


        for i in range(latest_email_id,first_email_id, -1):
            typ, data = mail.fetch(str(i).encode(), '(RFC822)' )

            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(str(response_part[1]))
                    #msg = print(msg)
                    #print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
                    
                    #print(msg)
                    ##### WRITE IT TO SOME TXT FILE
                    ##
                    ##
                    #msg.as_string()
                    f = open("sometextfile.txt", "a")
                    #print(msg, file=f)
                    f.write(str(msg))
                    f.close()
                    ##
                    ##
                    #####
                    ##print(msg)
                    #email_subject = msg['subject']
                    #email_from = msg['from']
                    #print('From : ' + email_from + '\n')
                    #print('Subject : ' + email_subject + '\n')

    except Exception as e:
        print(str(e))




def parse_alerts_and_determine_new_ones_to_handle():
    #saidDelimiter = "kdslk8732872mcmc7474irir"
    try:
        file1 = open('sometextfile.txt', 'r')
        Lines = file1.readlines()
        #count = 0
        # Strips the newline character
        for line in Lines:
            if saidDelimiter in line:
                brokenUpParts = line.split(saidDelimiter)
                with open('myfile.txt') as myfile:
                    #print(brokenUpParts[1])
                    if brokenUpParts[1] in myfile.read() or brokenUpParts[1] in lst:
                        #print('Blahblah')
                        pass
                    else:
                        lst.append(brokenUpParts[1])
                        print("added to alerts to process")
                        print(lst)
                        print("ABOVE called from parseAlertsDetermine")
                #

    except Exception as e:
        print(str(e))
 
 


def go_ahead_and_handle():
    #saidDelimiter = "kdslk8732872mcmc7474irir"
    try:
        for item in lst:
            place_the_trade(item)
            update_file_with_new_entry(item)
            lst.remove(item)
            print(lst)
            print("ABOVE called from goAheadAndHandle")
                #

    except Exception as e:
        print(str(e))




def place_the_trade(i):
    #saidDelimiter = "kdslk8732872mcmc7474irir"
    #
    #
    ##     TV sytnax in alert should look like this:    
    #
    #    kdslk8732872mcmc7474irir{{timenow}} {{strategy.order.action}} {{strategy.order.contracts}} {{ticker}}kdslk8732872mcmc7474irir
    #
    #
    try:
        #
        #
        login = r.login("jim@gmail.com","23!") #################################################################
        #
        #
        tradeDetails = i.split()
        print(tradeDetails[0]) # time alert got triggered
        print(tradeDetails[1]) # buy or sell
        action = tradeDetails[1]
        print(tradeDetails[2]) # number of contracts
        numOfContracts = tradeDetails[2]
        print(tradeDetails[3]) # ticker symbol
        tickerSymb = tradeDetails[3]
        #
        #
        ############Buy 10 shares of Apple at market price  #################################################################
         #################################################################r.order_buy_market('AAPL',10)  #################################################################
        #
        if "buy" in action:
            print("we're making a Buy")
            r.order_buy_market(tickerSymb,int(numOfContracts))
        elif "sell" in action:
            print("we're making a Sell")
            r.order_sell_market(tickerSymb,int(numOfContracts))
        else:
            print("that is strange, we didnt get a buy or sell action")
        #
        print("made a trade")
                #

    except Exception as e:
        print(str(e))



def print_contents_of_LST():
    #saidDelimiter = "kdslk8732872mcmc7474irir"
    try:
        print(lst)
        print("ABOVE called from printContetnsLST")
                #

    except Exception as e:
        print(str(e))



def update_file_with_new_entry(i):
    #saidDelimiter = "kdslk8732872mcmc7474irir"
    try:
        # Append-adds at last
        file1 = open("myfile.txt", "a")  # append mode
        file1.write(i + "\n" + "\n")
        #file1.write("\n")
        file1.close()
                #

    except Exception as e:
        print(str(e))



def clean_up_file_sometextfile_txt():
    #saidDelimiter = "kdslk8732872mcmc7474irir"
    try:
        #original = r'.\sometextfile.txt'
        #target = r'.\sometextfile-temp.txt'
        #shutil.copyfile(original, target)
        f = open("sometextfile.txt", "w")
        #print(msg, file=f)
        f.write(" ")
        f.close()
                #

    except Exception as e:
        print(str(e))


while (True):

    #
    time.sleep(1)
    #
    read_email_from_gmail()
    #
    #
    time.sleep(1)
    #
    parse_alerts_and_determine_new_ones_to_handle()
    #
    time.sleep(1)
    #
    go_ahead_and_handle()
    #
    time.sleep(1)
    #
    print_contents_of_LST()
    #
    #
    if thecounterhelper > 10:
        clean_up_file_sometextfile_txt()
        thecounterhelper = 0
    else:
        #thecounterhelper = 0
        thecounterhelper = thecounterhelper + 1
    print(thecounterhelper)
    #
    #
    time.sleep(1)
    #

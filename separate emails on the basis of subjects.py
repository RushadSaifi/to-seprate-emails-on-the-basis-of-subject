import imaplib
import email
from email.header import decode_header
N = 100 #Let us assume user apply for 100 no. jobs so that N = 100.

# Mail account credentials
username = "mustafadocument786@gmail.com"
password = "xxxxxxxx"

# create an IMAP4 class with SSL
imap = imaplib.IMAP4_SSL("imap.gmail.com")
# authenticate
imap.login(username, password)

#Select Inbox from all the mailboxes.
status, messages = imap.select("INBOX")

#Check total no. of mails
messages = int(messages[0])

#Empty list for containing Seprated Mails
filter=[]

#Use for Loop over each email to seprate
for i in range(messages, messages-N, -1):
    res, msg = imap.fetch(str(i), "(RFC822)")
    for response in msg:
        if isinstance(response, tuple):
            msg1 = email.message_from_bytes(response[1])
            subject = decode_header(msg1["Subject"])[0][0]
            if subject == "Thank you for applying":
                filter.append(msg)
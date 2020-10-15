1. Use the built-in imaplib module to list and read your emails in Python, we gonna need the help of IMAP protocol.

2. so that, import imaplib & email.

3. decode_header is used to decode the the emails because imported mails using imaplib is in the form of byte code.

4. now, account credentials is used to login in the mail account of which we want to seprate mails.

5. and then, we gonna need to connect to the IMAP server.

6. login using account credentials.

7. status, messages = imap.select("INBOX")   #this code is used to choose inbox over all mail boxe i.e..(spam, sent, etc)
   status contains the status that it is done or not. (ok/no)

8. Now, find the total no of mails in the inbox using messages = int(messages[0]).

9. Make Empty List to containing seprated mails.

10. Now, use for loop over each email to check the subject is "Thank you for applying".

11. The first thing to notice is we've used range(messages, messages-N, -1), which means going from the top to the bottom,
    the newest email messages got the highest id number, the first email message has an ID of 1.

12. Second, we used the imap.fetch() method, which fetches the email message by ID using the standard format
    specified in RFC 822.

13. After that, we parse the bytes returned by the fetch() method to a proper Message object, and used decode_header() 
    function from email.header module to decode the subject of the email address to human readable unicode.

14. if subject contains "Thank you for applying" then the main is append in filter list and get seprated.
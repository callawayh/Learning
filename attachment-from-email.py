import imaplib, email, os

user = "<email>"
password = "<Password>"
imap_url = 'imap.gmail.com' # for gmail
attachment_dir = '<path of where attachments should go>'

def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None,True)
    
def get_attachments(msg):
    for part in msg.walk():
        if part.get_content_maintype()=='multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        fileName = part.get_filename()
        #return fileName
        if bool(fileName):
            filePath = os.path.join(attachment_dir, fileName)
            with open(filePath,'wb') as f:
                f.write(part.get_payload(decode=True))
    
def search(key,value,con):
    result, data  = con.search(None,key,'"{}"'.format(value))
    return data

# this relates to the list of emails from search 
def get_emails(result_bytes): 
    msgs = []
    for num in result_bytes[0].split():
        typ, data = con.fetch(num, '(RFC822)')
        msgs.append(data)
    return msgs
    
con  = imaplib.IMAP4_SSL(imap_url)
con.login(user, password)
con.select("INBOX") # or whatever folder you want

result, data = con.fetch(b'2', '(RFC822)') #b2 refers to the location of the email in chronological order
raw = email.message_from_bytes(data[0][1])
get_attachments(raw)

# using some of the functions
# print body
print(get_body(raw))

# search for messages from a sender, returns list 
search("FROM","<an email>",con)

# get emails 
msgs = get_emails(search('FROM','<an email>',con))

for msg in msgs:
    print(get_body(email.message_from_bytes(msg[0][1]))
  

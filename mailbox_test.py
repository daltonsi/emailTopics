import mailbox
import json
import time


# CODE Reference: http://stackoverflow.com/questions/7166922/extracting-the-body-of-an-email-from-mbox-file-decoding-it-to-plain-text-regard

def getcharsets(msg):
    charsets = set({})
    for c in msg.get_charsets():
        if c is not None:
            charsets.update([c])
    return charsets

def handleerror(errmsg, emailmsg,cs):
    print()
    print(errmsg)
    print("This error occurred while decoding with ",cs," charset.")
    print("These charsets were found in the one email.",getcharsets(emailmsg))
    print("This is the subject:",emailmsg['subject'])
    print("This is the sender:",emailmsg['From'])

def getbodyfromemail(msg):
    body = None
    if msg.is_multipart():
        for part in msg.walk():
            if part.is_multipart():
                for subpart in part.walk():
                    if subpart.get_content_type() == 'text/plain':
                        body = subpart.get_payload(decode=True)
            elif part.get_content_type() == 'text/plain':
                body = part.get_payload(decode=True)
    elif msg.get_content_type() == 'text/plain':
        body = msg.get_payload(decode=True)
    """for charset in getcharsets(msg):
        try:
            body = body.decode(charset)
        except UnicodeDecodeError:
            handleerror("UnicodeDecodeError: encountered.",msg,charset)
            pass
        except AttributeError:
            handleerror("AttributeError: encountered" ,msg,charset)
            pass"""
    return body


if __name__ == '__main__':
    time.clock()
    list_of_email_dicts = []
    for thisemail in mailbox.mbox('UMSI-Open.mbox'):

        new_dict = {}
        body = getbodyfromemail(thisemail)
        print thisemail['subject']
        print thisemail['To']
        print thisemail['From']
        print body
        #if themail['body'] == None:
        new_dict["body"] = body.encode('utf-8')
        #else:
    #        new_dict["body"] = body.encode('utf-8')

        new_dict["subject"] = thisemail['subject'].encode('utf-8')
        new_dict["To"] = thisemail['To'].encode('utf-8')
        new_dict['From'] = thisemail['From'].encode('utf-8')
        list_of_email_dicts.append(new_dict)

    with open('emails_result.json', 'w') as fp:
        json.dump(list_of_email_dicts, fp)
    time.clock()

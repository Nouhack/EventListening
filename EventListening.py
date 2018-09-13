# -*- coding: utf-8 -*-

import subprocess
import smtplib
import time

while True:
        time.sleep(10)
        out=subprocess.check_output('powershell -command "Get-EventLog -LogName System -After (get-date).AddMinutes(-5)| format-table source,Timegenerated,Message -wrap"',shell=True)
        out=str(out)
        out=list(out)
        for i in range(len(out)):
                if (out[i]=="\\") and(out[i+1]=="n") and (out[i-1]=="r")and ((out[i-2]=="\\")):
                    out[i]="\n"
                    out[i-1]=''
                    out[i+1]=''
                    out[i-2]==''

        for i in range(len(out)):
                if (out[i]=='\\') and (out[i+1]=='x') and (out[i+2]=='8') and ((out[i+3]=='2') or (out[i+3]=='8')):
                        out[i]="e"
                        out[i+1]=""
                        out[i+2]=""
                        out[i+3]=""
                if (out[i]=="?"):
                        out[i]="'"
                if (out[i]=='\\') and (out[i+1]=='x') and (out[i+2]=='f') and (out[i+3]=='f'):
                        out[i]=""
                        out[i+1]=""
                        out[i+2]=""
                        out[i+3]=""
                if (out[i]=='\\') and (out[i+1]=='x') and (out[i+2]=='8') and (out[i+3]=='5'):
                        out[i]="a"
                        out[i+1]=""
                        out[i+2]=""
                        out[i+3]=""
        out="".join(out)
        try:
                ss=smtplib.SMTP("smtp.gmail.com",587)
                ss.starttls()
                ss.login("your email","your password")
                ss.sendmail("your email","second email",out)
                ss.quit()

        except:
                None
        



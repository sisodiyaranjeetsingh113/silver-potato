import smtplib
server=smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("satyamevjayate113@gmail.com","baba@007sisodiya")

toSend="patilanamika02@gmail.com"
fromSend="satyamevjayate113@gmail.com"
msg="Hi behna.... kesi h.... i miss you alot....Goodnight"
try:
    server.sendmail(fromSend,toSend,msg)
except Exception as e:
    print(e)
else:
    print("mail is sending....")
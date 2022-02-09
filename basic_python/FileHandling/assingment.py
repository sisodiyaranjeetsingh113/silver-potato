import os
fname="baba.txt"
f=open(fname,"w")
f.write('''"student_name":"kamal sharma"
date_of_birth":"1/2/2005"
"science":90
"social_science":80
"mathematics":75
"hindi":95
"english":70
"sanskrit":80''')
f.close()
f=open(fname,"r")
name=(f.readline())
f.close()





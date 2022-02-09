import goslate
txt=input("Enter your text:")
gs=goslate.Goslate()

tr=gs.translate(txt,'hi')

#print(tr)

#मेरा नाम रणजीत सिंह है


f=open("trn.txt","w",encoding='utf8')
f.write(tr)
print("file is created...!")

f.close()
import add_author 
from add_author import AddIntoAuthorList 
class MainClass():
        
    dict1=dict()
    def set_id(self,id):
        self.id=id        
    def set_name(self,name):
        self.name=name    
    def set_book(self,book):
        self.book=book   
    def get_book(self):
           return book
    def get_name(self):
           return name
    def get_list(self):
        return self.dict1
    def set_list(self,dict1):
        self.dict1=dict1







print("-------------------------------------------------------")
print("----------------------Welcome to you-------------------")
n=1
while(n!=0):
    print("-------------------------------------------------------") 
    n=int(input("Enter a choice(1 to 4) : \n1   => ADD AUTHOR  \n2   => UPDATE AUTHOR BOOK  \n3   => DELETE AUTHOR  \n4    => LIST OF AUTHORS  \n5    => Exit  \n-------------------------------------------------------\nType here   :"))
    obj_m_c=MainClass()
    if(n==1):
        id=input("Enter a author id :")
        name=input("Enter a author name :")
        book=input("Enter a author book :")       
        authorlist=obj_m_c.dict1

        obj_Add=add_author.AddIntoAuthorList(id,name,book,authorlist)  
        obj_m_c.dict1=obj_Add.Add()
        print("added....!")

    elif(n==2):
        name=input("Enter a author name :")
        
        book=input("Enter a author book :")
       
    elif(n==3):
       pass
    elif(n==4):
        f=open("AFHList.txt","r+")
        
        target=len(f.read())
        print(target)
        x=0
        
        while(x<=target):
            a=f.readline()    
            l1=0
            vid=""
            vvalue=""
            for i in a:
                x=x+1
                if(i==':'):
                    break
                l1=l1+1
                vid=vid+i             
                for i in a:
                    if(l1<0):
                        x=x+1
                        vvalue=vvalue+i
                        if(i=="}"):
                            break    
                    l1=l1-1

            print(vid,"      ",vvalue)
            x=x+1
        


    else:
        n=0
        print("-------------------------------------------------------")
        print("-----------------------Thank you-----------------------")
        print("------------------------------------------------------- \n \n")
else:

    print("----------------------------Visit Again---------------------------------")
        




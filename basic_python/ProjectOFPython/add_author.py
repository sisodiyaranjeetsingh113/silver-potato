import os
class AddIntoAuthorList():
    def __init__(self,id,name,book,dict1):
        self.id=id
        self.name=name
        self.book=book
        self.AuthorList=dict1
        
    def Add(self):    
        self.AuthorList[self.id]={"author_name":self.name,"author_book":self.book}
        AuthorFHList="AFHList.txt"
        
        f=open(AuthorFHList,"a+")      
        F=self.id+':{"author_name":'+self.name+',"author_book":'+self.book+'}\n'
        f.write(F)
        
        f.close()
        print(self.AuthorList)
        return self.AuthorList 
        
         
      
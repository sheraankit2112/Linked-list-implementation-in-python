class node:
    def __init__(self,data):
        self.data=data
        self.nextval=None
class link:
    def __init__(self):
        self.headval=None
    def insert_front(self):
        value=input("Enter the value:")
        if self.headval==None:
            self.headval=node(value)
        else:
            c=self.headval 
            self.headval==None
            self.headval=node(value)
            self.headval.nextval=c
    def insert_any(self):
        ptr=1
        f=self.headval
        if self.headval==None:
            print("list is empty,the element is inserted at 0 position")
            val=input("Enter the value:")
            self.headval=node(val)
        else:
            m=0
            val=input("Enter the value:")
            pos=int(input("Enter the position you want to insert:"))
            if pos==0:
                self.insert_front(val)


            while f.nextval:
                store=f.nextval
                if pos==ptr:
                    f.nextval=node(val)
                    f.nextval.nextval=store

                f=f.nextval
                ptr=ptr+1
            
            
    def delete(self):
        if self.headval==None:
            print("list is empty")
        else:
            ele=input("Enter the value which you want to delete:")
            a=self.headval
            
            z=self.headval
            b=self.headval.data
            c=self.headval.nextval
            e=c.data
            if ele==b:
                self.headval=self.headval.nextval
            elif ele==e:
                self.headval.nextval=self.headval.nextval.nextval
            else:
                while a.nextval:
                    if ele==c.data:
                        a.nextval=a.nextval.nextval
                        break
                    c=c.nextval
                    a=a.nextval


    def insert_end(self):
        valu=input("Enter the value:")
        if self.headval==None:
            self.headval=node(valu)
        b=self.headval
        while b.nextval:
            b=b.nextval
            
        b.nextval=node(valu)
    def traverse(self):
        a=self.headval
        while a is not None:
            print(a.data)
            a=a.nextval
        


obj=link()

print("1.insert_front\n2.insert_end\n3.insert_any\n4.delete\n5.display\n6.exit")
while True:
    c=int(input("Enter your choice:"))
    if c==1:
        obj.insert_front()
    if c==2:
        obj.insert_end()
    if c==3:
        obj.insert_any()
    if c==5:
        obj.traverse()
    if c==4:
        obj.delete()
    if c==6:
        break




'''
Main File
==========

'''
def validate_mob(x):
    if x.isdigit() and len(x)==10:
        return 1
    else:
        return 0

def create_contact():
       fp=open('data.txt','a')
       n=input("Enter Name:")
       mn=input("Enter mobile number:")
       res=validate_mob(mn)
       #print(res)
       if res==1:
           a,b=searchmob(mn)
           if b==1:
               print("Number Already Exist:")
               
           else:    
               d=n+":"+mn+"\n"
               fp.write(d)
               fp.close()
               print("Contact created successfully!!")

       else:
              print("please enter valid mobile number")


def display():
    fp=open('data.txt','r')
    d=fp.read()
    print("=========Contact Directory===========")
    print()
    print(d)
    print("=========================================")
              
def searchmob(n):
    fp=open('data.txt','r')
    data=fp.readlines()
    for x in data:
          l=x.split(":")
          if int(n)==int(l[1]):
              #print("Contact Found")
              #print(x)

              return x,1
    else:
              return '',0

def searchname():
     print("Search contact number by name")
     ns=input("Enter Name:")
     fp=open('data.txt','r')
     data=fp.readlines()
     print(data)
     flag=0
     for x in data:
          l=x.split(":")
          if ns.upper()==l[0].upper():
              print(x)
              flag=1
     if flag==0:
           print("Contact Not Found!!!")
     fp.close()
       
   
    
    
print("Welcome to contact directory console application:")

print()
while True:

    print()
    print("1.Create contact")
    print("2.View cotacts")
    print("3.Search ny Name")
    print("4.Search by Mobile Number")
    print("5.Exit")
    ch=int(input("Enter your choice:"))

    if ch==1:
       create_contact()
       
    elif ch==2:
       display()
       
    elif ch==3:
        searchname()
        
    elif ch==4:
      ms=input("Enter mobile number to be searched")  
      a,b=searchmob(ms)
      #print(a)
      #print(b)
      if b==1:
          print("Contact Found:")
          print(a)
      else:
          print("NOT FOUND")
      
    elif ch==5:
      break

    else:
         print("please enter valid option!!!")

print("Thank you for using application")


    

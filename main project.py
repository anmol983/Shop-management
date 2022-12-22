import pymysql as x
import random

username=input("Enter Mysql username:    ")
password=input("Enter MySQL password:    ")
print("")
print("\t\t\t\t\tWELCOME TO EMART")

def machine_independance():
    try:
        db=x.connect(host='localhost',user=username,passwd=password,db='q')
        cur=db.cursor()
        try:
           r=cur.execute("desc LOGIN_DETAILS")
           
        except:
           
           cur.execute("create table LOGIN_DETAILS(First_Name char(15) not null,Last_Name char(15) default 'null',Phone_no bigint not null unique check(Phone_no>=1000000000 and Phone_no<=9999999999),Username char(35) primary key,Password char(20) not null,Address char(30),Status char(20) default 'user' not null)")
           cur.execute("insert into LOGIN_DETAILS values('Malaika','null',9885536785,'malaika@gmail.com','M@l@ik@1','Dwarka sec-9','Admin')")
           cur.execute("insert into LOGIN_DETAILS(First_Name,Last_Name,Phone_no,Username,Password,Address) values('Aarav','Preet',8965648955,'aarav.aarav@gmail.com','Aarav123','Noida')")
           cur.execute("insert into LOGIN_DETAILS(First_Name,Last_Name,Phone_no,Username,Password,Address) values('Monica','Manjoosha',7985707686,'monica.manjoosha@gmail.com','@1992Monica','Dwarka Mor')")
           db.commit()
           
        cur.close()
        db.close()
    except:
        
        try:
            db=x.connect(host='localhost',user=username,passwd=password)
            cur=db.cursor()
        
            cur.execute("create database q")
            cur.execute("use q")
            cur.execute("create table LOGIN_DETAILS(First_Name char(15) not null,Last_Name char(15) default 'null',Phone_no bigint not null unique check(Phone_no>=1000000000 and Phone_no<=9999999999),Username char(35) primary key,Password char(20) not null,Address char(30),Status char(20) default 'user' not null)")
            cur.execute("insert into LOGIN_DETAILS values('Malaika','null',9885536785,'malaika@gmail.com','M@l@ik@1','Dwarka sec-9','Admin')")
            cur.execute("insert into LOGIN_DETAILS(First_Name,Last_Name,Phone_no,Username,Password,Address) values('Aarav','Preet',8965648955,'aarav.aarav@gmail.com','Aarav123','Noida')")
            cur.execute("insert into LOGIN_DETAILS(First_Name,Last_Name,Phone_no,Username,Password,Address) values('Monica','Manjoosha',7985707686,'monica.manjoosha@gmail.com','@1992Monica','Dwarka Mor')")
            db.commit()
        except:
            print("some error please check")
        cur.close()
        db.close()




def Password():
    import sys
    global rp
    global pwvalid
    lowercount=0
    uppercount=0
    digitcount=0
    p=input("Enter password(Password must contain alteast 8 character,one uppercase,one lowercase,one digit):    ")
    print("")
    z=True
    while z:
        if len(p)<8:
            print("Password too short")
            print("")
            pwvalid='invalid'
            break
        elif len(p)>18:
            print("Password too long")
            print("")
            pwvalid='invalid'
            break
        for i in p:
            if i.islower():
                lowercount+=1
            elif i.isupper():
                 uppercount+=1
            elif i.isdigit:
                 digitcount+=1
                 
        else:
            if lowercount==0:
                    print("Please enter a lowercase letter in password")
                    print("")
                    pwvalid='invalid'
                    break
            
            elif uppercount==0:
                    print("Please enter an uppercase letter in password")
                    print("")
                    pwvalid='invalid'
                    break
            
            elif digitcount==0:
                    print("Please enter a digit in password")
                    print("")
                    pwvalid='invalid'
                    break
            else:
                print("\t\t\tYour Password is:",p)
                print("")
                pwvalid='valid'
                return(p)
                break
    if z:
        print("Not a Valid Password")
        print("")
        c=input("do you want to enter again y or n:    ")
        print("")
        while True:
            
         if c=="y":
             p=Password()
             break
         else:
           pwvalid='invalid'
           break
         break
    return(p)       

#password creation code
def f_name():
       global fvalid
       fname=input("Enter First Name:    ")
       print("")
       if fname=='':
           print("invalid first name")
           print("")
           c=input("do you want to enter again y or n:    ")
           print("")
           while True:
            if c=="y":
               
                     fname=f_name()
                     break
            else:
                     fvalid='invalid'
                     break
            break    
           
       else:
           x1=fname.isalpha()
           if x1==True:
               fvalid='valid'
           else:
               print("invalid first name")
               print("")
               c=input("do you want to enter again y or n:    ")
               print("")
               fvalid='invalid'
               while True:
                if c=="y":
                   
                     fname=f_name()
                     break
                else:
                     fvalid='invalid'
                     break
                break 
               
       return(fname)



def u_name():
       global uname
       global uvalid
       uname=input("Enter Username:    ")
       print("")
       if uname=='':
           print("invalid Username")
           print("")
           c=input("do you want to enter again y or n:    ")
           print("")
           while True:
            if c=="y":
                     uname=u_name()
                     break
            else:
                     uvalid='invalid'
                     break
            break
           
       else:
           x1=uname.isdigit()
           if x1==True:
               uvalid='invalid'
               print("invalid Username")
               print("")
               c=input("do you want to enter again y or n:    ")
               print("")
               while True:
                 if c=="y":
                     uname=u_name()
                     break
                 else:
                     uvalid='invalid'
                     break
                 break
           else:
               uvalid='valid'
               
           
       return(uname)


def add_n():
       global avalid
       add=input("Enter Address:    ")
       print("")
       if add=='':
           print("invalid Address")
           print("")
           c=input("do you want to enter again y or n:    ")
           print("")
           while True:
            if c=="y":
                     add=add_n()
                     break
            else:
                     avalid='invalid'
                     break
            break
         
       else:
           x1=add.isalnum()
           if x1==True:
               avalid='valid'
           else:
               print("invalid Address")
               print("")
               c=input("do you want to enter again y or n:    ")
               print("")
               avalid='invalid'
               while True:
                if c=="y":
                     add=add_n()
                     break
                else:
                     avalid='invalid'
                     break
                break
           
       return(add)


def l_name():
       global lvalid
       lname=input("Enter last Name:    ")
       print("")
       if lname=='':
           lvalid='valid'
       else:
           x1=lname.isalpha()
           if x1==True:
               lvalid='valid'
            
           else:
               print("invalid last name")
               print("")
               c=input("do you want to enter again y or n:    ")
               print("")
               lvalid='invalid'
               while True:
                if c=="y":
                     lname=l_name()
                     break
                else:
                     lvalid='invalid'
                     break
                break
           
       return(lname)

    
def p_no():
     global pvalid
     try:
       pno=int(input("Enter Phone number:    "))
       print("")
       if pno>1000000000 and pno<9999999999:
                   pvalid='valid'
       else:
                   print("invalid phone number")
                   print("")
                   c=input("do you want to enter again y or n:    ")
                   print("")
                   pvalid='invalid'
                   while True:
                    if c=="y":
                     pno=p_no()
                     break
                    else:
                     pvalid='invalid'
                     break
                    break
           
     except: 
               print("invalid phone number")
               print("")
               c=input("do you want to enter again y or n:    ")
               print("")
               pvalid='invalid'
               while True:
                if c=="y":
                    pno=p_no()
                    break
                else:
                     pvalid='invalid'
                     break
                break
           
     return(pno)          



def sign_up():
  
       db=x.connect(host='localhost',user=username,passwd=password,db='q')
       cur=db.cursor()
       fname=f_name()
       lname=l_name()
       pno=p_no()
       add=add_n()
       uname=u_name()
       pword=Password()
       q1="insert into LOGIN_DETAILS(First_Name,Last_Name,Phone_no,Username,Password,Address) values('%s','%s',%s,'%s','%s','%s')"%(fname,lname,pno,uname,pword,add)
       cur.execute(q1)
       db.commit()
       cur.close()
       db.close()
 
#code for user sign_up


def login():
    import sys
    global uname
    global oldun
    db=x.connect(host='localhost',user=username,passwd=password,db='q')
    cur=db.cursor()
    
    uname=input("enter Username:    ")
    oldun=username
    print("")
    q1="select * from LOGIN_DETAILS"
    cur.execute(q1)
    r1=cur.fetchall()
    for j in range(0,len(r1)):
     for k in range(0,len(r1)):
      if uname in r1[k]:
     
       q2="select * from LOGIN_DETAILS where Username='%s'"%(uname)
    
       r=cur.execute(q2)
       rr=cur.fetchall()
       for i in rr:
         p=i[4]
         x2=input("Enter Password:    ")
         if x2==p:
             
            print("\t\t\t\tHELLO ",i[0])
            sub_menu()
         else:
            print("invalid username or password ")
            print("")
            c=input("do you want to enter again y or n:    ")
            print("")
            if c=="y":
                     login()
            else:
                     menu()
                     pass    
    else:
            print("invalid username or password ")
            print("")
            c=input("do you want to enter again y or n:    ")
            print("")
            if c=="y":
                     login()
            else:
                     menu()
                     pass   
         
    
  


def groceries():
    
        db=x.connect(host='localhost',user=username,passwd=password,db='q')
        cur=db.cursor()
        try:
           r=cur.execute("desc GROCERIES")
        except:
           cur.execute("create table GROCERIES(Product_ID char(5) primary key,Product_Name varchar(50),Amount char(7),Price int,Type char(30))")
           cur.execute("insert into GROCERIES values('P001','Cadbury Dairy Milk(Oreo)','70g',80,'Snacks')")
           cur.execute("insert into GROCERIES values('P002','Sunfeast Dark Fantasy','24packs',150,'Snacks')")
           cur.execute("insert into GROCERIES values('P003','Rajdhani Toor Dal','1kg',125,'Staples')")
           cur.execute("insert into GROCERIES values('P004','Rajdhani Rajma','1kg',100,'Staples')")
           cur.execute("insert into GROCERIES values('P005','Olive Oil','500ml',200,'Staples')")
           cur.execute("insert into GROCERIES values('P006','Dhara Mustard Oil','500ml',100,'Staples')")
           cur.execute("insert into GROCERIES values('P007','Ananda Ghee','1Litre',600,'Staples')")
           cur.execute("insert into GROCERIES values('P008','Ashirvaad Atta','10kg',450,'Staples')")
           cur.execute("insert into GROCERIES values('P009','Refined flour','1kg',70,'Staples')")
           cur.execute("insert into GROCERIES values('P010','Charminar Rice','5kg',289,'Staples')")
           cur.execute("insert into GROCERIES values('P011','Dhampura Sugar','1kg',60,'Staples')")
           cur.execute("insert into GROCERIES values('P012','Tata Salt','1kg',30,'Staples')")
           cur.execute("insert into GROCERIES values('P013','Almond','1kg',700,'Staples')")
           cur.execute("insert into GROCERIES values('P014','Walnut','500g',650,'Staples')")
           cur.execute("insert into GROCERIES values('P015','Lays(Cream and Onion)','52g',20,'Snacks')")
           cur.execute("insert into GROCERIES values('P016','Kurkure(Masala)','60g',25,'Snacks')")
           cur.execute("insert into GROCERIES values('P017','Uncle chips','55g',20,'Snacks')")
           cur.execute("insert into GROCERIES values('P018','Lipton green tea','25bags',156,'Beverages')")
           cur.execute("insert into GROCERIES values('P019','Tata tea ','250g',96,'Beverages')")
           cur.execute("insert into GROCERIES values('P020','Nescafe','100g',290,'Beverages')")
           cur.execute("insert into GROCERIES values('P021','Maggie','560g',91,'Snacks')")
           cur.execute("insert into GROCERIES values('P022','Fusilli Pasta','500g',100,'Snacks')")
           cur.execute("insert into GROCERIES values('P023','Kissan Ketchup','950g',110,'Packaged food')")
           cur.execute("insert into GROCERIES values('P024','Nutella Ferrero','350g',342,'Packaged food')")
           cur.execute("insert into GROCERIES values('P025','Fun Food Mayonnaise','500g',107,'Packaged food')")
           cur.execute("insert into GROCERIES values('P026','Kissan Jam(Mango)','700g',205,'Packaged food')")
           cur.execute("insert into GROCERIES values('P027','Apis Honey','500g',206,'Packaged food')")
           cur.execute("insert into GROCERIES values('P028','Knorr soup(Manchow)','43g',50,'Packaged food')")
           cur.execute("insert into GROCERIES values('P029','Dettol Soap(Original)','125g',40,'Personal care')")
           cur.execute("insert into GROCERIES values('P030','Lifeboy Handwash','200ml',172,'Personal care')")
           cur.execute("insert into GROCERIES values('P031','Parachute Coconut oil','600ml',218,'Personal care')")
           cur.execute("insert into GROCERIES values('P032','Dettol Sanitizer','60ml',55,'Personal care')")
           cur.execute("insert into GROCERIES values('P033','Colgate Toothpaste','200g',95,'Personal care')")
           cur.execute("insert into GROCERIES values('P034','Colgate Toothbrush','6Piece',85,'Personal care')")
           cur.execute("insert into GROCERIES values('P035','Fogg Deodorant(Men)','150ml',115,'Personal care')")
           cur.execute("insert into GROCERIES values('P036','Nivea lotion(Cocoa)','200ml',247,'Personal care')")
           cur.execute("insert into GROCERIES values('P037','Dabur Gulabari','250ml',65,'Personal care')")
           cur.execute("insert into GROCERIES values('P038','Tide Detergent Powder','3kg',372,'Household care')")
           cur.execute("insert into GROCERIES values('P039','Ezee Liquid Detergent','2Litre',304,'Household care')")
           cur.execute("insert into GROCERIES values('P040','Vim Dish Wash','750ml',140,'Household care')")
           cur.execute("insert into GROCERIES values('P041','Veggie Wash','200ml',100,'Household care')")
           cur.execute("insert into GROCERIES values('P042','Kiwi Dranex','50g',25,'Household care')")
           cur.execute("insert into GROCERIES values('P043','Lizol KItchen Cleaner','450ml',115,'Household care')")
           cur.execute("insert into GROCERIES values('P044','Hit Spray','700ml',260,'Household care')")
           cur.execute("insert into GROCERIES values('P045','Odonil Fragrance Block','150g',125,'Household care')")
           db.commit()
           cur.close()
           db.close()
   
           #print("Incorrect Username or Password")






        
def view_cart():
    try:
        db=x.connect(host='localhost',user=username,passwd=password,db='q')
        cur=db.cursor()
        q="select * from Cart"
        cur.execute(q)
        items=cur.fetchall()
        count=cur.rowcount
        if count>0:
          print("_"*120)
          print("{0:<5}{1:^50}{2:^10}{3:^10}{4:^10}{5:^30}"\
              .format('P_ID','Product_Name','Amount','Quantity','Price','Type'))
          print("_"*120)
          for i in items:
                print("{0:<5}{1:^50}{2:^10}{3:^10}{4:^10}{5:^30}"\
                  .format(i[0],i[1],i[2],i[3],i[4],i[5]))
                print("_"*120)  
                
        else:
            print("cart empty")
        q1="select sum(Price) from Cart"
        cur.execute(q1)
        pp=cur.fetchall()
        for i in pp:
             total=pp[0][0]
             print("")
             print("\t\t\tTotal Amount is:",total)
        cur.close()
        db.close()
    except:
        print("Cart empty")



def view_GROCERIES():
    try:
        db=x.connect(host='localhost',user=username,passwd=password,db='q')
        cur=db.cursor()
        q="select * from GROCERIES"
        cur.execute(q)
        items=cur.fetchall()
        count=cur.rowcount
        print("_"*105)
        print("{0:<5}{1:^50}{2:^10}{3:^10}{4:^30}"\
              .format('P_ID','Product_Name','Amount','Price','Type'))
        print("_"*105)
        if count>0:
            for i in items:
                print("{0:<5}{1:^50}{2:^10}{3:^10}{4:^30}"\
                  .format(i[0],i[1],i[2],i[3],i[4]))
                print("_"*105) 
                
        else:
            print("No item found")
        cur.close()
        db.close()
    except:
        print("some error please check")



def del_from_cart():
 try: 
   db=x.connect(host='localhost',user=username,passwd=password,db='q')
   cur=db.cursor()
   cur.execute("select * from Cart")
   rr=cur.fetchall()
   count=cur.rowcount
   if count>0:
    r=input("Enter product id to be deleted:    ")
    print("")
    for j in range(0,len(rr)):
     for k in range(0,len(rr)):
      if r in rr[k]:
       while True:
            q="delete from cart where Product_ID='%s'"%(r)
            r=cur.execute(q)
            db.commit()
      
            c=input("do you want to delete more y or n:    ")
            print("")
            if c=="y":
              del_from_cart()
            else:
              view_cart()
              break
            break

            
      else:
           print('Product not in cart')
           c=input("do you want to enter again y or n")
           print("")
           if c=="y":
                             del_from_cart()
                             break
           else:
                             view_cart()
                             break 
           break
      break
   else:
       print("cart empty")
   cur.close()
   db.close()
 except:
   print("Cart empty")



def modify_cart1():

    try:  
      db=x.connect(host='localhost',user=username,passwd=password,db='q')
      cur=db.cursor()
      cur.execute("select * from cart")
      rr=cur.fetchall()
      count=cur.rowcount
      P_IDm=input("Enter Product Id of product to be modified")
      print("")
      if count>0:
          for j in range(0,len(rr)):
            for k in range(0,len(rr)):
              if P_IDm in rr[k]:
                 while True:
                     
                     
                     s="select Price from GROCERIES where Product_ID='%s'"%(P_IDm)
                     t=cur.execute(s)
                     l=cur.fetchall()
                     for i in l:
                          Qutm=int(input("Enter new quantity of product"))
                          print("")
                          pr=int(i[0])*Qutm
                          q="update Cart set Price=%s where Product_ID='%s'"%(pr,P_IDm)
                          r=cur.execute(q)
                          q1="update Cart set Quantity=%s where Product_ID='%s'"%(Qutm,P_IDm)
                          r1=cur.execute(q1)
                          db.commit()
                          
                          c=input("do you want to modify more y or n")
                          print("")
                          if c=="y":
                             modify_cart1()
                          else:
                             view_cart()
                             break 
                          break
                     break 
              else:
                  print("Product not in cart")
                  c=input("do you want to enter again y or n")
                  print("")
                  if c=="y":
                             modify_cart1()
                  else:
                             view_cart()
                             break 
                  break
              break
      else:
          print("cart empty")
         
      cur.close()
      db.close()
    except:
      print("cart empty")












def add_to_cart2():
    try:
        db=x.connect(host='localhost',user=username,passwd=password,db='q')
        cur=db.cursor()
        try:
            q="desc Cart"
            cur.execute(q)
            P=input("enter product id:    ")
            try:
               q1="select * from groceries where Product_ID='%s'"%(P)
               cur.execute(q1)
               s=cur.fetchall()
               for i in s:
                   p_id=i[0]
                   Name=i[1]
                   Amt=i[2]
                   Qut=int(input("Enter the Quantity:    "))
                   print("")
                   price=i[3]*Qut
                   typ=i[4]
                   q="insert into Cart values('%s','%s','%s','%d','%d','%s')"%(p_id,Name,Amt,Qut,price,typ)
                   cur.execute(q)
                   db.commit()
               c=input("do you want to add more y or n:    ")
               print("")
               if c=="y":
                     add_to_cart2()
               else:
                     view_cart()
                     pass     
            except:
                print("invalid input or product already in cart")
        except:
            cur.execute("create table Cart(Product_ID char(5) primary key,Product_Name varchar(50),Amount char(7),Quantity char(6),Price int,Type char(30))")
            P=input("enter product id:    ")
            try:
               q1="select * from groceries where Product_ID='%s'"%(P)
               cur.execute(q1)
               s=cur.fetchall()
               for i in s:
                   p_id=i[0]
                   Name=i[1]
                   Amt=i[2]
                   Qut=int(input("Enter the Quantity:    "))
                   print("")
                   price=i[3]*Qut
                   typ=i[4]
                   q="insert into Cart values('%s','%s','%s','%d','%d','%s')"%(p_id,Name,Amt,Qut,price,typ)
                   cur.execute(q)
                   db.commit()
               c=input("do you want to add more y or n:    ")
               print("")
               if c=="y":
                     add_to_cart2()
               else:
                     view_cart()
                     pass                        
            except:
                print("invalid input or product already in cart")
        
    except:
        print("some error")


def display_user_record():
    try:
        db=x.connect(host='localhost',user=username,passwd=password,db='q')
        cur=db.cursor()
        
        q="select * from LOGIN_DETAILS where Username='%s'"%(uname)
        r=cur.execute(q)
        if r>0:
            rr=cur.fetchall()
            print("_"*120)
            print("{0:<15}{1:^15}{2:^10}{3:^20}{4:^20}{5:^30}{6:^5}"\
              .format('First_name','Last_name','Phone_no','Username','Password','Address','Status'))
            print("_"*120)
            l=len(rr)
            for i in rr:
                print("{0:<15}{1:^15}{2:^10}{3:^20}{4:^20}{5:^30}{6:^5}"\
                  .format(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
                print("_"*120) 
        else:
            print("No Record Found")
        cur.close()
        db.close()
    except: 
        print("error in code")



def update_details_first_name():
  try:
        db=x.connect(host='localhost',user=username,passwd=password,db='q')
        cur=db.cursor()
        fn=f_name()
        if fvalid=='valid':
           q1="update login_details set First_Name='%s' where Username='%s'"%(fn,uname)
           r1=cur.execute(q1)
           db.commit()
           print('\t\t\t\t'"Details Updated")
           print("")
           display_user_record()
           cur.close()
           db.close()
        else:
        
            pass
  except:
        print("some  error please check")



def update_details_last_name():
    try:
        db=x.connect(host='localhost',user=username,passwd=password,db='q')
        cur=db.cursor()
        ln=l_name()
        if lvalid=='valid':
          q1="update login_details set Last_Name='%s' where Username='%s'"%(ln,uname)
          r1=cur.execute(q1)
          db.commit()
          print('\t\t\t\t'"Details Updated")
          print("")
          display_user_record()
          cur.close()
          db.close()
        else:
            pass
    except:
        print("some  error please check")


def update_details_Phone_no():
    try:
        db=x.connect(host='localhost',user=username,passwd=password,db='q')
        cur=db.cursor()
        phno=p_no()
        if pvalid=='valid':
          q1="update login_details set Phone_No=%s where Username='%s'"%(phno,uname)
          r1=cur.execute(q1)
          db.commit()
          print('\t\t\t\t'"Details Updated")
          print("")
          display_user_record()
          cur.close()
          db.close()
        else:
            pass
    except:
        print("some  error please check")

def update_details_password():
    try:
        db=x.connect(host='localhost',user=username,passwd=password,db='q')
        cur=db.cursor()
        p=Password()
        if pwvalid=='valid':
          q1="update login_details set Password='%s' where Username='%s'"%(p,uname)
          r1=cur.execute(q1)
          db.commit()
          print('\t\t\t\t'"Details Updated")
          print("")
          display_user_record()
          cur.close()
          db.close()
        else:
            pass
    except:
        print("some  error please check")


def update_details_Address():
    try:
        db=x.connect(host='localhost',user=username,passwd=password,db='q')
        cur=db.cursor()
        add=add_n()
        if avalid=='valid':
          q1="update login_details set Address='%s' where Username='%s'"%(add,uname)
          r1=cur.execute(q1)
          db.commit()
          print('\t\t\t\t'"Details Updated")
          print("")
          display_user_record()
          cur.close()
          db.close()
        else:
            pass
    except:
        print("some error please check")


def del_account():
    try:
        db=x.connect(host='localhost',user=username,passwd=password,db='q')
        cur=db.cursor()
        q="delete from login_details where Username='%s'"%(uname)
        r=cur.execute(q)
        db.commit()
        print("your acoount has been deleted")
        print("")
        cur.close()
        db.close()
    except:
        print("error in code")



def delivery_charges():
    
        db=x.connect(host='localhost',user=username,passwd=password,db='q')
        cur=db.cursor()
        q1="select sum(Price) from Cart"
        cur.execute(q1)
        pp=cur.fetchall()
        for i in pp:
             total=pp[0][0]
        if total<1000:
            dil=50
        else:
            dil=0
        print("\t\t\tdelivery charges:",dil)
        print("")


def order_preview():

    print('\t\t\t\t'"ORDER PREVIEW")
    print("")
    try:
        db=x.connect(host='localhost',user=username,passwd=password,db='q')
        cur=db.cursor()
        q="select * from Cart"
        cur.execute(q)
        items=cur.fetchall()
        count=cur.rowcount
        print("_"*120)
        print("{0:<5}{1:^50}{2:^10}{3:^10}{4:^10}{5:^30}"\
              .format('P_ID','Product_Name','Amount','Quantity','Price','Type'))
        print("_"*120)
        if count>0:
            for i in items:
                print("{0:<5}{1:^50}{2:^10}{3:^10}{4:^10}{5:^30}"\
                  .format(i[0],i[1],i[2],i[3],i[4],i[5]))
                print("_"*120)
                
        else:
            print("cart empty")
            print("")
        q1="select sum(Price) from Cart"
        cur.execute(q1)
        pp=cur.fetchall()
        for i in pp:
             total=pp[0][0]
             print("\t\t\tTotal Amount is:",total)
             print("")
        cur.close()
        db.close()

        db=x.connect(host='localhost',user=username,passwd=password,db='q')
        cur=db.cursor()
        q1="select sum(Price) from Cart"
        cur.execute(q1)
        pp=cur.fetchall()
        for i in pp:
             total=pp[0][0]
        if total<1000:
            dil=50
        else:
            dil=0
        print("Free delivery for order above 1000")
        print("")
        print('\t\t\tDelivery Chrage is:',dil)
        print("")
        print('\t\t\tTotal Amount Payable:',dil+total)
        print("")

        
    except:
        print("some error please ")



def expected_delivery():
  try:
    db=x.connect(host='localhost',user=username,passwd=password,db='q')
    cur=db.cursor()
    q="SELECT DATE_ADD(CURDATE(), INTERVAL 5 DAY)"
    cur.execute(q)
    f=cur.fetchall()
    for i in f:
         print("\t\t\tExpected deliver by:",(i)[0])
         print("")
         print("\t\t**Due to Covid 19 it may take longer than usual to deliver**")
         print("")
    cur.close()
    db.close()
  except:
      ("some error please check")

def Payment():
    print("\t\t\t\tPAYMENT")
    print("")
    print("Sorry at the moment only cash on delivery is avalable")
    print("")
    expected_delivery()



def clear_cart():
  try:
    db=x.connect(host='localhost',user=username,passwd=password,db='q')
    cur=db.cursor()
    q="Drop table Cart"
    cur.execute(q)
    cur.close()
    db.close()
  except:
      print("some error please check")




def captcha():
    x=random.randint(10000,99999)
    print("\t\t\t-------")
    print('\t\t\t',x)
    print("\t\t\t-------")
    y=int(input("Enter Captcha:    "))
    print("")
    if x==y:
        print("\t\t\t\t\tOrder placed")
        print("")
        print("\t\t\t\tTHANK YOU FOR SHOPPING AT EMART")
        print("")
        clear_cart()
    
    else:
        print("Wrong Captcha")
        print("")
        print("Do you want to enter again:y or n")
        print("")
        c=input("enter choice:    ")
        print("")
        if c=='y':
            captcha()
        else:
            pass
    

def current_datetime():
     db=x.connect(host='localhost',user=username,passwd=password,db='q')
     cur=db.cursor()
     q="select NOW()"
     cur.execute(q)
     f=cur.fetchall()
     for i in f:
         print((i)[0])
     cur.close()
     db.close()
    

def bill():
  try:
    db=x.connect(host='localhost',user=username,passwd=password,db='q')
    cur=db.cursor()

    q2="select * from LOGIN_DETAILS where Username='%s'"%(uname)
    r=cur.execute(q2)
    rr=cur.fetchall()
    for i in rr:
         fn=i[0]
         ln=i[1]
         ph=i[2]
         ad=i[5]
         
    print("\t\t\t\t\t\tBILL")
    print("_"*105)
    print("First name:",fn,"\t\t\t\t\t\tLast name:",ln)
    print("")
    print("Phone:",ph,"\t\t\t\tAddress:",ad)
    print("")
    print('Date and Time: ',end='')
    print("")
    current_datetime()
    
    try:
        
        q="select * from Cart"
        cur.execute(q)
        items=cur.fetchall()
        count=cur.rowcount
        print("_"*120)
        print("{0:<5}{1:^50}{2:^10}{3:^10}{4:^10}{5:^30}"\
              .format('P_ID','Product_Name','Amount','Quantity','Price','Type'))
        print("_"*120)
        if count>0:
            for i in items:
                print("{0:<5}{1:^50}{2:^10}{3:^10}{4:^10}{5:^30}"\
                  .format(i[0],i[1],i[2],i[3],i[4],i[5]))
                print("_"*120)  
                
                
        else:
            print("cart empty")
            print("")
        q1="select sum(Price) from Cart"
        cur.execute(q1)
        pp=cur.fetchall()
        for i in pp:
             total=pp[0][0]
             print("\t\t\t\t\tTotal Amount is:",total)
             print("")
        cur.close()
        db.close()

        db=x.connect(host='localhost',user=username,passwd=password,db='q')
        cur=db.cursor()
        q1="select sum(Price) from Cart"
        cur.execute(q1)
        pp=cur.fetchall()
        for i in pp:
             total=pp[0][0]
        if total<1000:
            dil=50
        else:
            dil=0
        print('\t\t\t\t\tDelivery Chrage is',dil)
        print("")
        print('\t\t\t\t\tTotal Amount Payable:',dil+total)
        print("")
        print("\t\t\t\t\tTHANK YOU FOR SHOPPING")
        print("")
        
    except:
        print("some error please check")
  except:
      print("some error please check")
       


def Sort():
  try:
    db=x.connect(host='localhost',user=username,passwd=password,db='q')
    cur=db.cursor()
    print("1.Price(Low to High)")
    print("2.Price(High to Low)")
    print("")
    c=int(input("Enter choice:    "))
    print("")
    if c==1:
        q="select * from groceries order by Price"
        cur.execute(q)
        items=cur.fetchall()
        count=cur.rowcount
        print("_"*120)
        print("{0:<5}{1:^50}{2:^10}{3:^10}{4:^30}"\
              .format('P_ID','Product_Name','Amount','Price','Type'))
        print("_"*120)
        if count>0:
            for i in items:
                print("{0:<5}{1:^50}{2:^10}{3:^10}{4:^30}"\
                  .format(i[0],i[1],i[2],i[3],i[4]))
                print("_"*120) 
                
        else:
            print("No item found")
            print("")
        cur.close()
        db.close()
    elif c==2:
        q="select * from groceries order by Price desc"
        cur.execute(q)
        items=cur.fetchall()
        count=cur.rowcount
        print("_"*105)
        print("{0:<5}{1:^50}{2:^10}{3:^10}{4:^30}"\
              .format('P_ID','Product_Name','Amount','Price','Type'))
        print("_"*105)
        if count>0:
            for i in items:
                print("{0:<5}{1:^50}{2:^10}{3:^10}{4:^30}"\
                  .format(i[0],i[1],i[2],i[3],i[4]))
                print("_"*105) 
                
        else:
            print("No item found")
            print("")
        cur.close()
        db.close()
    else:
        print("Invalid input do you want to enter again")
        print("")
        d=input("enter choice y or n:    ")
        print("")
        if d=='y':
            Sort()
        else:
           pass
  except:
      print("some error please check")


def filters():
  try:
    db=x.connect(host='localhost',user=username,passwd=password,db='q')
    cur=db.cursor()
    print("1.Filter by Price")
    print("2.Filter by Type")
    print("")
    c=int(input("enter choice:    "))
    print("")
    if c==1:
        y=int(input("enter min amount:    "))
        print("")
        z=int(input("enter max amount:    "))
        print("")
        q="select * from groceries where Price between '%d' and '%d'"%(y,z)
        cur.execute(q)
        items=cur.fetchall()
        count=cur.rowcount
        print("_"*105)
        print("{0:<5}{1:^50}{2:^10}{3:^10}{4:^30}"\
              .format('P_ID','Product_Name','Amount','Price','Type'))
        print("_"*105)
        if count>0:
            for i in items:
                print("{0:<5}{1:^50}{2:^10}{3:^10}{4:^30}"\
                  .format(i[0],i[1],i[2],i[3],i[4]))
                print("_"*105) 
                
        else:
            print("No item found")
        cur.close()
        db.close()
    elif c==2:
        print("enter type from:")
        print("")
        print("Snacks")
        print("Staples")
        print("Beverages")
        print("Packaged food")
        print("Personal care")
        print("Household care")
        print("")
        c1=input("enter choice:    ")
        print("")
        q="select * from groceries where Type='%s'"%(c1)
        cur.execute(q)
        items=cur.fetchall()
        count=cur.rowcount
        print("_"*105)
        print("{0:<5}{1:^50}{2:^10}{3:^10}{4:^30}"\
              .format('P_ID','Product_Name','Amount','Price','Type'))
        print("_"*105)
        if count>0:
            for i in items:
                print("{0:<5}{1:^50}{2:^10}{3:^10}{4:^30}"\
                  .format(i[0],i[1],i[2],i[3],i[4]))
                print("_"*105) 
                
        else:
            print("No item found")
            print("")
        cur.close()
        db.close()
    else:
        print("Invalid input do you want to enter again")
        print("")
        d=input("enter choice y or n:    ")
        print("")
        if d=='y':
            filters()
        else:
           pass
  except:
      print("some error please check")





def search_groceries():
  try:
    db=x.connect(host='localhost',user=username,passwd=password,db='q')
    cur=db.cursor()
    print("")
    c=int(input("enter name of product:    "))
    print("")
    q="select * from groceries where Product_Name like '%s'% "%(c)
    cur.execute(q)
    items=cur.fetchall()
    count=cur.rowcount
    print("_"*105)
    print("{0:<5}{1:^50}{2:^10}{3:^10}{4:^30}"\
              .format('P_ID','Product_Name','Amount','Price','Type'))
    print("_"*105)
    if count>0:
        for i in items:
            print("{0:<5}{1:^50}{2:^10}{3:^10}{4:^30}"\
                  .format(i[0],i[1],i[2],i[3],i[4]))
            print("_"*105) 
    print("Do you want to search again")
    print("")
    d=input("enter choice y or n:    ")
    print("")
    if d=='y':
             search_groceries()
    else:
           pass
  except:
      print("some error please check")



def menu_view_groceries():
   while True:
        print("")
        print("\t\t\t1. View All Products")
        print("\t\t\t2. Search Groceries")
        print("\t\t\t3. Sort Groceries")
        print("\t\t\t4. Filter Groceries")
        print("\t\t\t5. Return to previous menu")
        print("")
        c=int(input("Enter Choice:    "))
        print("")
        if c==1:
            view_GROCERIES()
        elif c==2:
             search_groceries()
        elif c==3:
            Sort()
        elif c==4:
            filters()
        else:
            break




def menu_update():
    while True:
        print("")
        print("\t\t\t1. Update First Name")
        print("\t\t\t2. Update Last Name")
        print("\t\t\t3. Update Phone Number")
        print("\t\t\t4. Update Password")
        #print("\t\t\t5. Update Username")
        print("\t\t\t5. Update Address")
        print("\t\t\t6. Return to previous menu")
        print("")
        c=int(input("Enter Choice:    "))
        print("")
        if c==1:
            update_details_first_name()
        elif c==2:
            update_details_last_name()
        elif c==3:
            update_details_Phone_no()
        elif c==4:
            update_details_password()
        elif c==5:
            update_details_Address()
            
        else:
            break




def menu_account():
    while True:
        print("\t\t\t\t\tMY ACCOUNT")
        print("")
        print("\t\t\t1. My Record")
        print("\t\t\t2. Update details")
        print("\t\t\t3. Del Account")
        print("\t\t\t4. Return to previous menu")
        print("")
        c=int(input("Enter Choice:    "))
        print("")
        if c==1:
            display_user_record()
        elif c==2:
            menu_update()
        elif c==3:
            del_account()
        else:
            break





def menu_cart():
    while True:
        print("")
        print("\t\t\t1. View Cart")
        print("\t\t\t2. Add to Cart")
        print("\t\t\t3. Delete Product from Cart")
        print("\t\t\t4. Modify Cart")
        print("\t\t\t5. Return to previous menu")
        print("")
        c=int(input("Enter Choice:    "))
        print("")
        if c==1:
            view_cart()
        elif c==2:
            add_to_cart2()
        elif c==3:
            del_from_cart()
        elif c==4:
            modify_cart1()
        else:
            break



def place_order():
  
  try:
    db=x.connect(host='localhost',user=username,passwd=password,db='q')
    cur=db.cursor()
    cur.execute("desc Cart")
    while True:
      cur.execute("select * from Cart")
      rrr=cur.fetchall()
      count=cur.rowcount
      if count>0:
        print("")
        print("\t\t\t1. Proceed")
        print("\t\t\t2. Return to previous menu")
        print("")
        c=int(input("Enter Choice:    "))
        print("")
        if c==1:
            order_preview()
            print("\t\t\t1. Proceed")
            print("\t\t\t2. Return to previous menu")
            print("")
            c1=int(input("Enter Choice:    "))
            print("")
            if c1==1:
                Payment()
                print("\t\t\t1. Proceed")
                print("\t\t\t2. Return to previous menu")
                print("")
                c2=int(input("Enter Choice:    "))
                print("")
                if c2==1:
                    bill()

                    print("\t\t\t1. Proceed")
                    print("\t\t\t2. Print Bill")
                    print("\t\t\t3. Return to previous menu")
                    print("")
                    c3=int(input("Enter Choice:    "))
                    print("")
                    if c3==1:
                        captcha()
                        break
                    
                    else:
                        break
        
                    
                else:
                    break
                
            else:
                break
            
        else:
            break
        
      else:
          print("Cart is empty")
          break
  except:
      print("cart empty")
                 




def sub_menu():
    while True:
        print("")
        print("\t\t\t1. View Groceries")
        print("\t\t\t2. Cart")
        print("\t\t\t3. My Account")
        print("\t\t\t4. Place Order")
        print("\t\t\t5. Sign Out")
        print("")
        c=int(input("Enter Choice:    "))
        print("")
        if c==1:
            menu_view_groceries()
        elif c==2:
            menu_cart()
        elif c==3:
            menu_account()
        elif c==4:
            place_order()
        else:
            menu()





def menu():
    while True:
        print()
        print("\t\t\t1. LOGIN")
        print("\t\t\t2. SIGN UP")
        print("\t\t\t3. Exit")
        print("")
        c=int(input("Enter Choice:    "))
        print("")
        if c==1:
            machine_independance()
            groceries()
            login()
            
        elif c==2:
            machine_independance()
            groceries()
            sign_up()
            sub_menu()
        else:
            break


menu()

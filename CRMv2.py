import sqlite3
import sys
import os
from prettytable import PrettyTable
import re
import textwrap


path='customerdetailsdb.db'
db=sqlite3.connect(path)
cursor=db.cursor()

def create_db() :
    cursor.execute(''' create table if not exists cusdatadb(
                                                        order_no varchar(20) PRIMARY KEY,
                                                        name varchar(50),
                                                        product varchar(100),
                                                        invoice_no varchar(30),
                                                        quantity integer,
                                                        e_mail varchar(100),
                                                        address varchar(200),
                                                        order_date varchar(20),
                                                        delivery_date varchar(20),
                                                        price integer,
                                                        amountpr integer,
                                                        status_ord varchar(50))''')

def insert_db(*argumentofdb):
    listofarg = argumentofdb
    cursor.execute('''insert into cusdatadb values (?,?,?,?,?,?,?,?,?,?,?,?)''',(list(listofarg)))
    db.commit()
    print "Customer detail inserted Successfully!\n"

def check_ord(val):
    matchobj=re.match(r'^\w+$',val)
    return matchobj

def check_only_dig(val):
    matchobj=re.match(r'^[0-9]*$',val)
    return matchobj

def check_only_char(val):
    matchobj=re.match(r'([^0-9][A-Za-z\.]+\s?)+',val)
    return matchobj

def check_email(value):
    matchobje=re.match(r'[^@]+@[^@]+\.[^@]+',value)
    return matchobje

def check_date(val):
    matchobj=re.match(r'^[0-9][0-9]+[.-/][0-1][0-9]+[.-/][0-9][0-9][0-9][0-9]$',val)
    return matchobj


def load_details():
            print "Load customer details! "
            matchobj=False
            while(not matchobj):
                order_id=raw_input("Order No. : ")
                if order_id != '':
                    matchobj=check_ord(order_id)
                else:
                    matchobj=True
                    
            matchobj=False
            while(not matchobj):
                cus_name=raw_input("Name : ")
                if cus_name != '':
                    matchobj=check_only_char(cus_name)
                else:
                    matchobj=True
                    
            product_name=raw_input("Product : ")
            invoice_no=raw_input("Invoice No. : ")
            matchobj=False
            while(not matchobj):
                quantity=raw_input("Quantity : ")
                if quantity != '':
                    matchobj=check_only_dig(quantity)
                else:
                    matchobj=True
                    
            matchobj=False
            while(not matchobj):
                e_mail=raw_input("E-mail : ")
                if e_mail != '':
                    matchobj=check_email(e_mail)
                else:
                    matchobj=True
                    
            address=raw_input("Address : ")
            matchobj=False
            while (not matchobj):
                order_date=raw_input("Order Date : ")
                if order_date != '':
                    matchobj=check_date(order_date)
                else:
                    matchobj=True
                    
            matchobj=False
            while (not matchobj):
                delivery_date=raw_input("Delivery Date : ")
                if delivery_date != '':
                    matchobj=check_date(delivery_date)
                else:
                    matchobj=True
                    
            matchobj=False
            while(not matchobj):
                price=raw_input("Price of one item : ")
                if price != '':
                    matchobj=check_only_dig(price)
                else:
                    matchobj=True
                    
            if quantity=='':
                quantity=0
            if price ==  '' or price.isalpha():
                price = 0
            if quantity!=0 and price!=0:
                price=int(price)
                quantity=int(quantity)
                amount=price*quantity
            else :
                amount=0
            matchobj=False
            while(not matchobj):
                statusord=raw_input("Status of the order : ")
                if statusord != '':
                    matchobj=check_only_char(statusord)
                else:
                    matchobj=True
                    
            insert_db(order_id,cus_name,product_name,invoice_no,quantity,e_mail,address,order_date,delivery_date,price,amount,statusord)
            
def retrive_all():
    cursor.execute('''select * from cusdatadb''')
    all_rows=cursor.fetchall()
    display_rows(all_rows)

def display_rows(all_rows):
    t = PrettyTable(['ORDER NO.','NAME', 'PRODUCT','INVOICE NO.','QUANTITY','E-MAIL','ADDRESS','ORDER DATE','DELIVERY DATE','PRICE','AMOUNT','STATUS'])
    t.hrules=True
    for rows in all_rows:
        addrows=[textwrap.fill(rows[0]),textwrap.fill(rows[1],14),textwrap.fill(rows[2],10),textwrap.fill(rows[3]),textwrap.fill(str(rows[4])),textwrap.fill(rows[5],15),textwrap.fill(rows[6],15),textwrap.fill(rows[7]),textwrap.fill(rows[8]),textwrap.fill(str(rows[9])),textwrap.fill(str(rows[10])),textwrap.fill(rows[11])]
        t.add_row(addrows)
        #print 'Order No. : {0} \nName : {1} \nProduct : {2} \nInvoice No. : {3}\nQuantity : {4}\nE-mail : {5}\nAddress : {6}\nOrder Date : {7}\nDelivery Date : {8}\nPrice : {9}\nAmount : {10}\nStatus :{11}\n'.format(rows[0],rows[1],rows[2],rows[3],rows[4],rows[5],rows[6],rows[7],rows[8],rows[9],rows[10],rows[11])
    print t
    print '\n'
    
def delete_all():
    print 'Are you sure ? , You decided to delete all the customer details. Once deleted all your data will be lost. \n Enter your option : y - Yes \t n - No \n '
    opt=raw_input("your option : ")
    print '\n'
    if opt=='y':
        cursor.execute('''delete from cusdatadb''')
        print "All the customer details are deleted succcessfully!\n"
        db.commit()
        
def retrive_fn():
    optionret=int(raw_input("Retrive by :\n1.Order No. \n2.Name \n3.Product \n4.Invoice No. \n5.E-mail \n6:Order Date \n7.Delivery Date \n8.Status \nAny Other Number :Back\nEnter your option "))
    print '\n'
    if optionret>8: return
    if optionret==1:
        retopt=raw_input("Order No. : ")
        cursor.execute('''select * from cusdatadb where order_no=?''',(retopt,))
    elif optionret==2:
        retopt=raw_input("Name : ")
        cursor.execute('''select * from cusdatadb where name=?''',(retopt,))
    elif optionret==3:
        retopt=raw_input("Product : ")
        cursor.execute('''select * from cusdatadb where product=?''',(retopt,))
    elif optionret==4:
        retopt=raw_input("Invoice No. : ")
        cursor.execute('''select * from cusdatadb where invoice_no=?''',(retopt,))
    elif optionret==5:
        retopt=raw_input("E-mail : ")
        cursor.execute('''select * from cusdatadb where e_mail=?''',(retopt,))
    elif optionret==6:
        retopt=raw_input("Order Date. : ")
        cursor.execute('''select * from cusdatadb where order_date=?''',(retopt,))
    elif optionret==7:
        retopt=raw_input("Delivery Date : ")
        cursor.execute('''select * from cusdatadb where delivery_date=?''',(retopt,))
    elif optionret==8:
        retopt=raw_input("Order Status : ")
        cursor.execute('''select * from cusdatadb where status_ord=?''',(retopt,))
    all_rows=cursor.fetchall()
    if len(all_rows) == 0:
        print "The value "+str(retopt)+" doesn't exist in the customer database"
        return
    display_rows(all_rows)

def is_in_db(optionret,retopt):
    if optionret==1:
        cursor.execute('''select * from cusdatadb where order_no=?''',(retopt,))
    elif optionret==2:
        cursor.execute('''select * from cusdatadb where name=?''',(retopt,))
    elif optionret==3:
        cursor.execute('''select * from cusdatadb where product=?''',(retopt,))
    elif optionret==4:
        cursor.execute('''select * from cusdatadb where invoice_no=?''',(retopt,))
    elif optionret==5:
        cursor.execute('''select * from cusdatadb where e_mail=?''',(retopt,))
    elif optionret==6:
        cursor.execute('''select * from cusdatadb where order_date=?''',(retopt,))
    elif optionret==7:
        cursor.execute('''select * from cusdatadb where delivery_date=?''',(retopt,))
    elif optionret==8:
        cursor.execute('''select * from cusdatadb where status_ord=?''',(retopt,))
    all_rows=cursor.fetchall()
    if len(all_rows) == 0:
        print "The value "+str(retopt)+" doesn't exist in the customer database"
        return False
    return True
    

def delete_fn():
    print 'Are you sure ? , You decided to delete some of the customer details. Once deleted all your data will be lost. \n Enter your option : y - Yes \t n - No \n'
    opt=raw_input("your option : ")
    print '\n'
    if opt=='y':
        optionret=int(raw_input("Delete by: \n1.Order No. \n2.Name \n3.Product \n4.Invoice No. \n5.E-mail \n6.Order Date \n7.Delivery Date \n8.Status \nAny Other Number:Back\nEnter your option: "))
        if optionret>8: return
        if optionret==1:
            ordofcus=raw_input("Order No. : ")
            if not is_in_db(optionret,ordofcus):return
            cursor.execute('''delete from cusdatadb where order_no=?''',(ordofcus,))
        elif optionret==2:
            namofcus=raw_input("Name : ")
            if not is_in_db(optionret,namofcus):return
            cursor.execute('''delete from cusdatadb where name=?''',(namofcus,))
        elif optionret==3:
            prodofcus=raw_input("Product : ")
            if not is_in_db(optionret,prodofcus):return
            cursor.execute('''delete from cusdatadb where product=?''',(prodofcus,))
        elif optionret==4:
            invnoofcus=raw_input("Invoice No. : ")
            if not is_in_db(optionret,invnoofcus):return
            cursor.execute('''delete from cusdatadb where invoice_no=?''',(invnoofcus,))
        elif optionret==5:
            emailofcus=raw_input("E-mail : ")
            if not is_in_db(optionret,emailofcus):return
            cursor.execute('''delete from cusdatadb where e_mail=?''',(emailofcus,))
        elif optionret==6:
            orddateofcus=raw_input("Order Date. : ")
            if not is_in_db(optionret,orddateofcus):return
            cursor.execute('''delete from cusdatadb where order_date=?''',(orddateofcus,))
        elif optionret==7:
            deldateofcus=raw_input("Delivery Date : ")
            if not is_in_db(optionret,deldateofcus):return
            cursor.execute('''delete from cusdatadb where delivery_date=?''',(deldateofcus,))
        elif optionret==8:
            stateoford=raw_input("Order Status : ")
            if not is_in_db(optionret,stateoford):return
            cursor.execute('''delete from cusdatadb where status_ord=?''',(stateoford,))
        db.commit()
        print "The customer data deleted Successfully!"

def update_fn():
    optionret=int(raw_input("Update by: \n1.Order No. \n2.Name \n3.Product \n4.Invoice No. \n5.E-mail \n6.Order Date \n7.Delivery Date \n8.Status \nAny Other Number:Back \nEnter your option: "))
    if optionret>8: return
    whereopt=raw_input("Enter the order No. for which the change has to be implemented: ")
    print '\n'
    if not is_in_db(1,whereopt):return
    if optionret==1:
        ordofcus=raw_input("Order No. : ")
        cursor.execute('''update cusdatadb set order_no= ? where order_no = ?''',(ordofcus,whereopt))
    elif optionret==2:
        namofcus=raw_input("Name : ")
        cursor.execute('''update cusdatadb set name= ? where order_no = ?''',(namofcus,whereopt))
    elif optionret==3:
        prodofcus=raw_input("Product : ")
        cursor.execute('''update cusdatadb set product=? where order_no = ?''',(prodofcus,whereopt))
    elif optionret==4:
        invnoofcus=raw_input("Invoice No. : ")
        cursor.execute('''update cusdatadb set invoice_no=? where order_no = ?''',(invnoofcus,whereopt))
    elif optionret==5:
        emailofcus=raw_input("E-mail : ")
        cursor.execute('''update cusdatadb set e_mail=? where order_no = ?''',(emailofcus,whereopt))
    elif optionret==6:
        orddateofcus=raw_input("Order Date : ")
        cursor.execute('''update cusdatadb set order_date=? where order_no = ?''',(orddateofcus,whereopt))
    elif optionret==7:
        deldateofcus=raw_input("Delivery Date : ")
        cursor.execute('''update cusdatadb set delivery_date=? where order_no = ?''',(deldateofcus,whereopt))
    elif optionret==8:
            stateoford=raw_input("Order Status : ")
            cursor.execute('''update cusdatadb set status_ord=? where order_no = ?''',(stateoford,whereopt))
    db.commit()
    print "Customer Detail updated successfully!\n"
    
    
def get_options() :
    while(True):
        option=raw_input("\n1.Insert \n2.Retrieve \n3.Retrive All \n4.Update \n5.Delete \n6.Delete All \n7.Exit \nEnter your option: ")
        print '\n'
        if option == '1':
            load_details()
        elif option == '2':
            retrive_fn()
        elif option == '3':
            retrive_all()
        elif option == '4':
            update_fn()
        elif option == '5':
            delete_fn()
        elif option == '6':
            delete_all()
        elif option == '7':
            quit()
        else:
            print "Re-enter your option"
        print '\n'

        
if __name__.endswith('__main__'):
    try:
        
        cmpname="CRM"
        print "=" * 167 + "\n" + cmpname.center(175," ") + "\n" + "=" * 167
       # path='customerdetailsnew.db'
       # db=sqlite3.connect(path)
       # cursor=db.cursor()
        create_db()
        get_options()        
    except sqlite3.IntegrityError:
        print 'Oops! Order Number already exist! Try Another Number!'
        raw_input("Hit enter to exit the Application!\n")
    except ValueError:
        print 'Oops! Enter Valid Value'
        raw_input("Hit enter to exit the Application!\n")
    except:
        print "Application Interrupted : An Error Occured\n"
    finally:
        db.commit()
        db.close()

import sqlite3

userid = int(input("Enter ID:"))
username = input("Enter Name:")
con = sqlite3.connect(r"C:\Users\pdc2b-training.pdc2b\myape.db")

cr = con.cursor()
result = cr.execute("select * from Test where eid = ? and ename=?",(userid,username))
# cr.execute("insert into test values(?,?)",(4,"Hare"))
# con.commit();
if len(cr.fetchall())>0:
    print("Welcome "+username)
else:
    print("Invlaid Login")
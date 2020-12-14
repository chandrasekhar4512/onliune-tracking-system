import sqlite3
c=sqlite3.connect("consignment.db")
'''c.execute(create table consignment
            (c_number int primary key NOT NULL,
             NAME  TEXT NOT NULL,
             TO_ AddressCHAR(50) NOT NULL,
             F_address CHAR(50) NOT NULL,
             R_DATE CHAR(15),
             D_DATE CHAR(15)))'''0
#c.execute("INSERT INTO consignment(c_number,NAME,TO_Address,F_address,R_DATE,D_DATE)VALUES(1,'TAMAN','HYD','PGW','10/10/18','18/10/18'")
#c.commit()
data=c.execute("SELECT * FROM consignment")
for row in data:
    print("c_number",row[0])
    print("name",row[1])
    print("to",row[2])
    print("from",row[3])
    print("R_Date",row[3])
    print("D_Date",row[3],"\n")
print("table created sucessfully")
c.close()

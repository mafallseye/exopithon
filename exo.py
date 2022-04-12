"""
cursorSel.rowcount
cursorSel.lastrowid
"""
import mysql.connector as MC

try:
    conn=MC.connect(host='localhost',database='mydb',user='root',password='admin')
    cursorSel=conn.cursor()
    req ='INSERT INTO user(userid,firstname,lastname) VALUES(%s,%s,%S)'
    infos=(cursorSel.lastrowid, 'maguette', 'seye')
    cursorSel.execute(req, infos)
    conn.commit()
    req='SELECT * FROM user'
    cursorSel.execute(req)
    userlist=cursorSel.fetchall()
    for i in userlist:
        print('prenom:{}'.format(i[1]))

except MC.Error as err:
       print(err)

finally:
    if(conn.is_connected()):
        cursorSel.close()
        conn.close()
"""
cursorSel.rowcount
cursorSel.lastrowid
"""
import mysql.connector as MC

try:
    conn=MC.connect(host='localhost',database='mydb',user='root',password='admin')
    cursorSel=conn.cursor()
    req ='INSERT INTO user(userid,firstname,lastname) VALUES(%s, %s, %s)'
    infos=(cursorSel.lastrowid, 'maguette', 'seye')

    cursorSel.execute(req, infos)
    conn.commit()

    req='UPDATE user SET firstname=%s WHERE firstname=%s'
    value=('Mansour', 'maguette')
    cursorSel.execute(req, value)
    conn.commit()
    print(cursorSel.rowcount,'ligne modifier')

    req='DELETE FROM user WHERE firstname=%s'
    sup=('mansour',)
    cursorSel.execute(req, sup)
    conn.commit()
    print(cursorSel.rowcount,'ligne supprimer')

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
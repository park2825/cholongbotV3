import time, sqlite3, discord

conn = sqlite3.connect('db')
cur = conn.cursor()

def rank():
    cur.execute('SELECT * FROM users ORDER BY money DESC')
    l = cur.fetchall()
    e = discord.Embed(title='부자 5명', dsecription='부자 5명을 호명하겠다.', color=0xffc0cb)
    for i in range(0, 5):
        e.add_field(name =str(i+1)+'위', value='<@%s>\n%d원'%(l[i][1],l[i][0]))
    return e

def money(uid):
    cur.execute('SELECT * FROM users WHERE id=?', [uid])
    l = cur.fetchone()
    m=""
    if l is None:
        m = "5000"

        cur.execute('INSERT INTO users VALUES(?,?,?);', (m,uid,time.time()))
        conn.commit()
        cur.execute('SELECT * FROM users WHERE id=?', [uid])
        l = cur.fetchone()
    elif l[2]+300 <= time.time():
        m = str(int(l[0])+5000)
        cur.execute('UPDATE users SET money = ?, time=? WHERE id = ?',(m,time.time(),uid))
        conn.commit()
    
    if m=="":
        e = discord.Embed(title='돈이 지급되지 않았습니다.', description='돈은 5분에 한번씩 지급합니다.\n'+str(int((l[2]+300)-time.time()))+'초 남았습니다.', color=0xff0000)
    else:
        e = discord.Embed(title = '돈이 지급되었습니다.', description='회원님의 돈은 '+m+'원 있습니다.', color=0xffc0cb)
    return e


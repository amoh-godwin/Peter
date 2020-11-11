import sqlite3

conn = sqlite3.connect('settings.db')
cursor = conn.cursor()

def select():
    sql = """SELECT * FROM Servers"""
    cursor.execute(sql)
    al = cursor.fetchall()
    info = {}
    servers = []
    for server in al:
        print(server)
        info['id'] = int(server[0])
        info['name'] = server[2]
        info['default_port'] = int(server[4])
        info['port'] = int(server[5])
        info['status'] = server[6]
        servers.append(info)

    print(info)
    print(servers)

def update():
    sql = """UPDATE Databases SET id=0"""
    cursor.execute(sql)
    conn.commit()

conn.close()

import sqlite3

conn = sqlite3.connect('settings.db')
cursor = conn.cursor()

sql = """SELECT * FROM Databases"""
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

conn.close()

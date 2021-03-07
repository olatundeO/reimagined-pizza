import sqlite3
import socket
import json  #javascript object notation(json)


toppings = []
prices = {"medium":0, "large":0, "xlarge":0, "m_toppings":0, "l_toppings":0, "x_toppings":0}


conn = sqlite3.connect('pizza.db')
cursor = conn.cursor()

for row in cursor.execute('SELECT * FROM Prices'):
    prices[row[0]] = row[1]

for row in cursor.execute('SELECT * FROM Toppings order by topping'):
    toppings.append(row[0])

price_list = str.encode(json.dumps(prices))
topping_list = str.encode(json.dumps(toppings))
conn.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 8008
server.bind((host, port))
server.listen(5)

while True:  #keep connection open
    print('Listening for a client...')
    client, addr = server.accept()
    client.send(str.encode('Welcome to my server!'))

    while True:
        data = client.recv(1024)
        command = bytes.decode(data)

        if command == 'toppings':
            client.send(topping_list)
        elif command == 'price':
            client.send(price_list)
        elif command == 'exit':
            break
        else:
            client.send(str.encode('Invalid Command!'))

    client.close()

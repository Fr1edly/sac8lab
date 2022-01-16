import lxml.etree as ET
import threading
import tornado.websocket
import tornado.web
import tornado.ioloop
import datetime
import json 

date = datetime.datetime.now()

dom = ET.parse("file.xml")
xslt = ET.parse("file.xslt")
transform = ET.XSLT(xslt)
newhtml = transform(dom)
strfile = ET.tostring(newhtml)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print('Get')
        self.render("mypage.html")
        self.write(strfile)


# обработчик событий  вебсоккетов
class EchoWebSocket(tornado.websocket.WebSocketHandler):
    clients = []  # массив клиентов
    fl = True
    index = 0

    # проверяются и даются права на действия с соккетом, здесь права даются всем
    def check_origin(self, origin):
        return True

    # обработка события открытия соединения
    def open(self):
        print("Client open")
        # добавляем клиента в список
        self.clients.append(self)
        self.fl = True
        # запускаем поток отправки сообщение клиенту
        #loop = tornado.ioloop.PeriodicCallback(self.go, 1000)
        #loop.start()

    # обработка прихода события от сервера
    def on_message(self, message):
        print("Client message " + message)
        self.go(json.loads(message))

    # обработка события закрытия соккета клиента
    def on_close(self):
        self.fl = False
        # удаляем клинта из списка
        self.clients.remove(self)
        print("WebSocket closed")

    # процедура отправки сообщения клиенту 
    
    def go(self, message):
        print('ok')
        if self.fl:
            #s = '{"type": "chat", "data": "' + datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S") + '"}'
            s = '{"type": "chat", "data": "' + message['data'] + '"}'
            # посылаем сообщение клиенту
            print(s)
            self.write_message(s)
            print("send message : " + s)
            # запускаем таймер который будет вызывать функцию go с аргументом client каждые 3 сек
            # t = threading.Timer(3.0, self.go, [self.clients[0]])
            # t.start()


# создаем приложение tornado с обработчиком вебсоккетов и http сервером
if __name__ == "__main__":
    app = tornado.web.Application([(r"/data", EchoWebSocket), (r'/', MainHandler)])
    app.listen(10556)
    print("Start Server")
    tornado.ioloop.IOLoop.instance().start()

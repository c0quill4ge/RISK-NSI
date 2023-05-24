import websockets


class User:
    def __init__(self, websocket: websockets.WebSocketServerProtocol, id: int):
        self.__websocket = websocket
        self.__id = id

    def __str__(self):
        return f"User {self.__id} : {self.__websocket}"

    def get_id(self):
        return self.__id

    def get_websocket(self):
        return self.__websocket
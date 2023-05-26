import json

import websockets

from web_socket_server.database.database import Database
from web_socket_server.utils.action import Action


class User:
    def __init__(self, websocket: websockets.WebSocketServerProtocol, id: int):
        self.__websocket = websocket
        self.__id = int(id)
        self.__database = Database()
        self.__username = self.__database.recupere_bdd("joueurs", "pseudo", {"id_joueur": ("=", self.__id)})[0][0]

    def __str__(self):
        return f"User<username:{self.__username},id:{self.__id},websocket:{str(self.__websocket)}>"

    def get_id(self):
        return self.__id

    def get_websocket(self):
        return self.__websocket

    def get_pseudo(self):
        return self.__username

    async def send_message(self, message: str):
        await self.__websocket.send(json.dumps({"message": message}))

    def send_action(self, action: Action, data: dict):
        self.__websocket.send(json.dumps({"action": action, "data": data}))

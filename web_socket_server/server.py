#!/usr/bin/env python

import asyncio
import json

from websockets.server import serve

from web_socket_server.database.database import Database
from web_socket_server.utils.user import User


class WebServer:
    def __init__(self, host: str|int, port: int):
        self.__host = host
        self.__port = int(port)
        self.__database = Database()
        self.__clients = dict()
        self.__clients_list = list()

    async def main(self):
        async with serve(self.gestion, host=self.__host, port=self.__port):
            await asyncio.Future()  # boucle infinie qui ne gène pas l'exécution du reste du programme

    async def gestion(self, websocket):
        connecte = False
        async for message in websocket:
            if not connecte:
                conn = self.connection(websocket, message)
                connecte = conn[0]
                user = User(websocket, conn[1])

                self.register_user(user)
                await self.action(user)

    def connection(self, websocket, message):

        json_dict = json.loads(message)

        if len(json_dict) != 1:
            return False
        if len(json_dict["token"]) != 256:
            return False
        return self.__database.find_token(json_dict["token"])  # (True, id_joueur) si le token existe et le compte aussi, (False, None) sinon

    async def action(self, user: User):
        print(str(user) + " connecté")
        await user.send_message("ok")

    def register_user(self, user: User):
        self.__clients[user.get_pseudo()] = user
        self.__clients_list.append(user)



server = WebServer("localhost", 8765)
asyncio.run(server.main())

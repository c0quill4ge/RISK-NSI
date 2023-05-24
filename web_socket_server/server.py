#!/usr/bin/env python

import asyncio
import json

from websockets.server import serve

from web_socket_server.database.database import Database
from web_socket_server.utils.user import User

bdd = Database()


async def gestion(websocket):
    connecte = False
    async for message in websocket:
        if not connecte:
            conn = connection(websocket, message)
            connecte = conn[0]
            user = User(websocket, conn[1])
        else:
            # on est connecté
            await action(websocket, message)


def connection(websocket, message):
    global bdd

    json_dict = json.loads(message)

    if len(json_dict) != 1:
        return False
    if len(json_dict["token"]) != 256:  # à modifier en fonction du token généré par le php
        return False
    return bdd.find_token(json_dict["token"])  # (True, id_joueur) si le token existe et le compte aussi, (False, None) sinon


async def action(websocket, message):
    print("action en cours")


async def main():
    async with serve(gestion, host="localhost", port=8765):
        await asyncio.Future()  # boucle infinie qui ne gène pas l'exécution du reste du programme


asyncio.run(main())

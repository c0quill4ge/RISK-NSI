#!/usr/bin/env python

import asyncio
import json


from websockets.server import serve

from web_socket_server.database.database import Database

bdd = Database()


async def gestion(websocket):
    connecte = False
    async for message in websocket:
        if not connecte:
            connecte = connection(websocket, message)
        else:
            # on est connecté
            await action(websocket, message)


def connection(websocket, message):
    global bdd

    json_dict = json.loads(message)

    if len(json_dict) != 1:
        return False
    if len(json_dict["token"]) != 256:  # faudra ptet modifier après en fonction de la vraie valeur attendue
        return False
    


async def action(websocket, message):
    print("action en cours")


async def main():
    async with serve(gestion, host="localhost", port=8765):
        await asyncio.Future()  # boucle infinie qui ne gène pas l'exécution du reste du programme


asyncio.run(main())
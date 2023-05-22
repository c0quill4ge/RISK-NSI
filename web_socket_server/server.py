#!/usr/bin/env python

import asyncio

from websockets.server import serve


async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)


async def gestion(websocket):
    connecte = False
    async for message in websocket:
        if not connecte:
            connecte = connection(websocket, message)
        else:
            # on est connecté
            await action(websocket, message)


def connection(websocket, message):
    print("Message reçu :", message)  # je fais des tests ici
    print("user connecté")

    # print(str(websocket.remote_address) + " s'est connecté")


async def action(websocket, message):
    print("action en cours")


async def main():
    async with serve(gestion, host="localhost", port=8765):
        await asyncio.Future()  # boucle infinie qui ne gène pas l'exécution du reste du programme


asyncio.run(main())
import asyncio

async def hola(texto):
    await asyncio.sleep(1)
    print(f'{texto} is gay 😭😭😭')
    await bye(texto) # se llama con await

async def bye(texto):
    await asyncio.sleep(2)
    print(f'\nBYE {texto} BYE')

asyncio.run(hola(input('Nombre: ')))
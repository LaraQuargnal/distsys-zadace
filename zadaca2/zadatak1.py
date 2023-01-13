import nest_asyncio
nest_asyncio.apply()
import asyncio
import os

async def afun1(lista_datoteka):
    await asyncio.sleep(0.2)
    return [{"naziv": datoteka, "velicina": os.path.getsize(datoteka)} for datoteka in lista_datoteka]

def fun2(lista_datoteka):
    for datoteka in lista_datoteka:
        with open(datoteka, 'w') as d:
            d.write('\n'.join(str(i) for i in range(1, 10001)))

async def main():
   lista_datoteka = ["datoteka{}.txt".format(i) for i in range(1, 4)]
   for naziv_datoteke in lista_datoteka:
       open(naziv_datoteke, 'a').close()
   fun2(lista_datoteka)
   rez = await afun1(lista_datoteka)
   print(rez)


if __name__ == "__main__":
    asyncio.run(main())



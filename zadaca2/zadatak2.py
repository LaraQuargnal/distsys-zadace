import numpy as np
import psutil
import asyncio

async def afunc1():
    for i in range(10):
        np.random.normal(loc=0, scale=1, size=1000000)
        await asyncio.sleep(0.9)

async def afunc2():
    return psutil.cpu_percent(10)

async def main():
    await asyncio.gather(afunc1(), afunc2())
    cpu = await afunc2()
    print(f'Iskorištenost CPU u 10 sekundi iznosi: {cpu}')
 
if __name__ == "__main__":
    asyncio.create_task(main())
 

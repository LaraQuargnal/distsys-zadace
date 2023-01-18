import asyncio

NODES = 5   # simulirano slanje sa 5 nodova
sequences = [0] * NODES
buffer = {}


async def handler(reader, writer):
    print("Someone is here")

    while data := await reader.readline():
        try:
            ldata = data.decode("utf8").split('/', maxsplit=2)          # zarez ovdje ne smije biti separator!!!
            if len(ldata) != 3:
                raise Exception("Error: krivi input format.")
            # sender=int, deps= dependencies =  tuple odvojen "," , message = string
            sender, deps, msg = int(ldata[0]), tuple(map(int, ldata[1].split(','))), ldata[2].strip()
            print("Received:", sender, deps, msg)
            buffer[sender, deps] = msg

            def deliver():
                print(f"Status: {'-'.join(map(str, sequences))}")  # f-string
                for (n, x), msg in buffer.items():  # prolazi kroz items u buffer dict
                    # if true: za svaki node ukoliko je sequnces >= od dependencies na tom indexu
                    if all(sequences[i] >= x[i] for i in range(NODES)):
                    
                        print("*** Delivering", n, x, msg) 
                        del buffer[n, x]
                        sequences[n] += 1
                        return True

            while deliver():
                pass

        except Exception as e:
            print(e)


async def main():
    server = await asyncio.start_server(handler, "127.0.0.1", 9000)     # funkcija prima 3 parametra
    print(server.sockets)
    async with server:
        print("Server started!")
        await server.serve_forever()

asyncio.run(main())

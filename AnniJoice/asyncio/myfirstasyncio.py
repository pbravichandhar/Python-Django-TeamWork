import asyncio
import time

async def myWork():
    print("Starting Work")
    time.sleep(5)
    print("Finishing Work")

loop = asyncio.get_event_loop()
loop.run_until_complete(myWork())


async def mycouroutine():
    print("My Frist Coroutine")
try:
    loop.run_until_complete(mycouroutine())
finally:
    loop.close()









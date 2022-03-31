'''
Tasks run Concurrently
======================

In the last example, the coroutines ran serially.  To get them run in parallel you need to create tasks and
then await the tasks.
'''

import asyncio

# this is a new style coroutine
async def coroutineA():
    print('I am coroutineA')
    await asyncio.sleep(1)                # yield control
    print('I am coroutineA')

async def coroutineB():
    print('I am coroutineB')
    await asyncio.sleep(1)                # yield control
    print('I am coroutineB')


async def main():
    taskA = asyncio.create_task(coroutineA()) #ONLY NEW ADDITIONS
    taskB = asyncio.create_task(coroutineB()) #ONLY NEW ADDITION

    await taskA
    await taskB

asyncio.run(main())      

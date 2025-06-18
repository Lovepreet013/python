# To write async code in Python, you can use the `asyncio` library.

#Asyncio has 3 main components:
# -> coroutines : A coroutine is the result of an asynchronous function which can be declared using the keyword async before def.

# -> event loop : The event loop is the object which executes our asynchronous code and decides how to switch between async functions. After creating an event loop we can add multiple coroutines to it; these coroutines will all be running concurrently when run_until_complete or run_forever is called.

# -> future : A future is an object that works as a placeholder for the output of an asynchronous function, and it gives us information about the function state. A future is created when we add a coroutine to an event loop.

import asyncio

#When we declare a function using the async keyword the function is not executed; instead, a coroutine object is returned.
async def my_function(arg):
    print("I am async coroutine with arg: ", arg)


#To call coroutine, first method :
my_coroutine = my_function(1)

#There are two ways to read the output of an async function from a coroutine. The first way is to use the await keyword, which is only possible inside async functions and will wait for the coroutine to terminate and return the result.
# result = await my_function()

#Second Method is to call event loop and run the coroutine using run_until_complete method.

loop = asyncio.new_event_loop() #create loop

future = loop.create_task(my_coroutine) #add coroutine to loop, This is future

loop.run_until_complete(future) # add coroutine to the loop concurrently
loop.close() #close the loop
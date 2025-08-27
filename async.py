# To write async code in Python, you can use the `asyncio` library.

#Asyncio has 3 main components:
# -> coroutines : A coroutine is the result of an asynchronous function which can be declared using the keyword async before def.

# -> event loop : The event loop is the object which executes our asynchronous code and decides how to switch between async functions. After creating an event loop we can add multiple coroutines to it; these coroutines will all be running concurrently when run_until_complete or run_forever is called.

# -> future : A future is an object that works as a placeholder for the output of an asynchronous function, and it gives us information about the function state. A future is created when we add a coroutine to an event loop.

import asyncio

#When we declare a function using the async keyword the function is not executed; instead, a coroutine object is returned.
async def my_function(arg):
    # print("I am async coroutine with arg: ", arg)
    return
    


#To call coroutine, first method :
my_coroutine = my_function(1)

#There are two ways to read the output of an async function from a coroutine. The first way is to use the await keyword, which is only possible inside async functions and will wait for the coroutine to terminate and return the result.
# result = await my_function()

#Second Method is to call event loop and run the coroutine using run_until_complete method.

loop = asyncio.new_event_loop() #create loop

future = loop.create_task(my_coroutine) #add coroutine to loop, This is future

loop.run_until_complete(future) # add coroutine to the loop concurrently
loop.close() #close the loop


async def function_name(arg):
    await asyncio.sleep(1)  # Simulate an asynchronous operation
    return

#Consider the following asynchronous function that squares a number and sleeps for one second before returning.
async def square(x):
    # print("Square", x)
    await asyncio.sleep(1)
    # print("End Square", x)
    return x * x

results = asyncio.run(square(8)) # In Newer version we do not need to manually create or manage the event loop
# print(results)

#other example to execute Multiple Tasks:

#stimualte delay and returns the square of a number
async def compute_square(x):
    await asyncio.sleep(11)  # Simulate a delay
    return x * x

#Print a message and call compute_square
async def square_of_number(x):
    print('Square', x)
    res = await compute_square(x)
    print('End square', x)
    return res

#Collects and print the results as each task completed
async def when_done(tasks):
    for res in asyncio.as_completed(tasks):
        result = await res
        print("Result : ", result)

#Cleaner way to run async code 
async def main():
    await when_done([
        square_of_number(1),
        square_of_number(2),
        square_of_number(3),
    ])

#Run the main function
asyncio.run(main())


async def sum(n1, n2):
    print("Sum", n1, n2)
    await asyncio.sleep(1)  # Simulate a delay
    return n1 + n2

# asyncio.run(sum(1, 2))  # This will run the sum coroutine and print the result

async def main_sum():
    tasks = [sum(1,2), sum(2,3)]
    for coro in asyncio.as_completed(tasks):
        results = await coro
        print("Result:", results)

asyncio.run(main_sum())
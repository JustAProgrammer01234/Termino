import random
from jishaku.functools import executor_function

@executor_function 
async def generate_random_number(num1, num2):
    return random.randint(num1, num2)

@executor_function 
async def random_choice(iterable):
    return random.choice(iterable)
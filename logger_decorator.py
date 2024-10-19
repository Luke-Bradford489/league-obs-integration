import functools

class LogArgsKwargs:
    def __init__(self, func):
        self.func = func
        functools.update_wrapper(self, func)

    async def __call__(self, *args, **kwargs):
        # Log the positional arguments
        formatted_args = ", ".join([repr(a) for a in args]) if args else "None"
        
        # Log the keyword arguments
        formatted_kwargs = ", ".join([f"{k}={repr(v)}" for k, v in kwargs.items()]) if kwargs else "None"

        print(f"Calling {self.func.__name__} with:\n  Args: {formatted_args}\n  Kwargs: {formatted_kwargs}")
        
        # Call the original async function and await the result
        result = await self.func(*args, **kwargs)
        
        # Optionally, log the result
        print(f"{self.func.__name__} returned: {repr(result)}\n")
        
        return result
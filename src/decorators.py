# def log(file_name=""):
#     def log_wrap(func):
#         def wrapper(*args, **kwargs):
#             print(f"Вызов функции: {func.__name__}")
#             result = func(*args, **kwargs)
#             print(result)
#             return result
#         return wrapper
#     return log_wrap

def log(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов функции: {func.__name__}")
        result = func(*args, **kwargs)
        return result
    return wrapper

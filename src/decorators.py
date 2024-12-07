# def log(file_name=""):
#     def log_wrap(func):
#         def wrapper(*args, **kwargs):
#             print(f"Вызов функции: {func.__name__}")
#             result = func(*args, **kwargs)
#             print(result)
#             return result
#         return wrapper
#     return log_wrap

def log(file_name=None):
    def log_wrap(func):
        def wrapper(*args, **kwargs):
            log_message = f"{func.__name__} ok\n"
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                log_message = f"{func.__name__} error: {e}. Inputs: {args}\n"
                # Если произошла ошибка, всё равно логируем её и пробрасываем дальше
                if file_name:
                    with open(file_name, "a") as log_file:
                        log_file.write(log_message)
                else:
                    print(log_message)
                raise

            # Если указано имя файла, записываем лог в файл
            if file_name:
                with open(file_name, "a") as log_file:
                    log_file.write(log_message)
            else:
                # Если имя файла не указано, выводим в консоль
                print(log_message)

            return result

        return wrapper
    return log_wrap


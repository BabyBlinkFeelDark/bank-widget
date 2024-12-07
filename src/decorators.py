import os, time, inspect
from xmlrpc.client import boolean


def log(isLogs=False):
    def log_wrap(func):
        def wrapper(*args, **kwargs):
            log_message = f"{time.ctime()}: {func.__name__} ok"
            if isLogs:
                file_path = file_creater(func, isLogs, dir="logs")
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                log_message = f"{time.ctime()}: {func.__name__} error: {e}. Inputs: {args}\n"
                if isLogs:
                    with open(file_path, "a") as log_file:
                        log_file.write(log_message)
                        log_file.write("\n")
                else:
                    print(log_message)
                    print("")
                return None

            if isLogs:
                with open(file_path, "a") as log_file:
                    log_file.write(log_message)
                    log_file.write("\n")
            else:
                print(log_message)
                print("")

            return result

        return wrapper

    return log_wrap

def file_creater(current_func, cfile=None, dir = ""):
    stack = inspect.stack()
    caller_frame = stack[1]
    caller_module = inspect.getmodule(caller_frame[0])
    dir_path = os.path.join(os.getcwd()[:-4], dir)
    if dir_path and not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_name = f"log_{os.path.basename(caller_module.__file__).replace('.py', '')}"
    file_path = str(dir_path + "/" + file_name + ".txt")
    return str(file_path)

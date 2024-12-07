import os, time
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
    dir_path = os.path.join(os.getcwd()[:-4], dir)
    if dir_path and not os.path.exists(dir_path):
        os.makedirs(dir_path)
    if not isinstance(cfile, str):
        file_name = f"log_{str(current_func.__name__)}"
        file_path = str(dir_path + "/" + file_name + ".txt")
    elif not isinstance(cfile, boolean):
        file_name = f"log_{current_func.__name__}"
        file_path = str(dir_path + "/" + file_name + ".txt")
        print(file_path)
    return str(file_path)

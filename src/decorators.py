import os, time
from xmlrpc.client import boolean


def log(isLogs=False):
    def log_wrap(func):
        def wrapper(*args, **kwargs):
            log_message = f"{time.ctime()}: {func.__name__} ok"
            dir_path = os.path.join(os.getcwd()[:-4], "log")
            if dir_path and not os.path.exists(dir_path):
                os.makedirs(dir_path)

            if not isinstance(isLogs, str):
                file_name = f"log_{func.__name__}"
                file_path=str(dir_path +"/"+ file_name + ".txt")
            elif not isinstance(isLogs, boolean):
                file_name = f"log_{isLogs}"
                file_path = str(dir_path + "/" + file_name + ".txt")

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



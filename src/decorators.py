import os, time

def log(file_name=None):
    def log_wrap(func):
        def wrapper(*args, **kwargs):
            log_message = f"{time.ctime()}: {func.__name__} ok"

            if file_name:
                dir_path=os.path.join(os.getcwd()[:-4],"log")
                file_path=str(dir_path +"/"+ file_name + ".txt")
                if dir_path and not os.path.exists(dir_path):
                    os.makedirs(dir_path)

            try:
                result = func(*args, **kwargs)
            except Exception as e:
                log_message = f"{time.ctime()}: {func.__name__} error: {e}. Inputs: {args}\n"
                if file_name:
                    with open(file_path, "a") as log_file:
                        log_file.write(log_message)
                        log_file.write("\n")
                else:
                    print(log_message)
                    print("")
                return None

            if file_name:
                with open(file_path, "a") as log_file:
                    log_file.write(log_message)
                    log_file.write("\n")
            else:
                print(log_message)
                print("")

            return result

        return wrapper

    return log_wrap



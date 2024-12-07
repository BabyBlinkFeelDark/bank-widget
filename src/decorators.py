import inspect
import os
import time
from typing import Any, Callable, Optional


def log(isLogs: bool = False) -> Callable:
    def log_wrap(func: Callable[..., str]) -> Callable[..., Optional[str]]:
        def wrapper(*args: Any, **kwargs: Any) -> Optional[str]:
            log_message: str = f"{time.ctime()}: {func.__name__} ok"
            if isLogs:
                file_path: str = file_creater(dir="logs")
            try:
                result: str = func(*args, **kwargs)
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


def file_creater(dir: str = "") -> str:
    stack = inspect.stack()
    caller_frame = stack[1]
    caller_module = inspect.getmodule(caller_frame[0])
    dir_path: str = os.path.join(os.getcwd()[:-4], dir)
    if dir_path and not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_name: str = f"log_{os.path.basename(caller_module.__file__).replace('.py', '')}"
    file_path: str = str(dir_path + "/" + file_name + ".txt")
    return file_path

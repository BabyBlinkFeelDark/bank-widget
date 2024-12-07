import inspect
import os
import time
from typing import Any, Callable, Optional


def log(isLogs: bool = False) -> Callable:
    """
    Декоратор для логирования выполнения функций.

    При включении логирования (isLogs=True) декоратор будет записывать информацию
    о каждом вызове функции в лог-файл. В случае ошибки также будет записан
    стек ошибки. Если isLogs=False, информация будет выводиться в консоль.

    :param isLogs: Флаг, указывающий, нужно ли вести логирование в файл. По умолчанию False.
    :return: Декорированная функция, которая либо логирует выполнение в файл, либо выводит в консоль.
    """

    def log_wrap(func: Callable[..., str]) -> Callable[..., Optional[str]]:
        """
        Оборачивает целевую функцию для добавления логирования.

        Логирование включает запись в файл или вывод в консоль, в зависимости
        от параметра isLogs. Также ловит исключения, записывая их в лог или выводя
        в консоль.

        :param func: Функция, которую нужно обернуть.
        :return: Обернутая функция с логированием.
        """

        def wrapper(*args: Any, **kwargs: Any) -> Optional[str]:
            """
            Функция-обертка, которая выполняет логирование и обработку ошибок.

            Выполняет саму целевую функцию, записывает успешный результат в лог-файл
            или выводит в консоль, а также ловит исключения и записывает их в лог.

            :param args: Позиционные аргументы для функции.
            :param kwargs: Ключевые аргументы для функции.
            :return: Результат выполнения целевой функции или None в случае ошибки.
            """
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
    """
    Создает лог-файл в указанной директории. Если директория не существует,
    она будет создана. Имя файла будет основано на имени модуля, из которого
    был вызван лог.

    :param dir: Директория, в которой должен быть создан файл (по умолчанию - "logs").
    :return: Путь к созданному лог-файлу.
    """
    stack = inspect.stack()
    caller_frame = stack[1]
    caller_module = inspect.getmodule(caller_frame[0])
    dir_path: str = os.path.join(os.getcwd()[:-4], dir)
    if dir_path and not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_name: str = f"log_{os.path.basename(caller_module.__file__).replace('.py', '')}"
    file_path: str = str(dir_path + "/" + file_name + ".txt")
    return file_path

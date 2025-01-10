import time
from typing import Any, Callable, Optional


def log(filename: str = "") -> Callable:
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
            try:
                result: str = func(*args, **kwargs)
            except Exception as e:
                log_message = f"{time.ctime()}: {func.__name__} error: {e}. Inputs: {args}\n"
                if filename != "":
                    with open(filename, "a") as log_file:
                        log_file.write(log_message)
                        log_file.write("\n")
                else:
                    print(log_message)
                    print("")
                raise e

            if filename != "":
                with open(filename, "a") as log_file:
                    log_file.write(log_message)
                    log_file.write("\n")
            else:
                print(log_message)
                print("")

            return result

        return wrapper

    return log_wrap

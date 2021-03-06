"""

    Объект сообщения

        Сообщение, формируемое и выводимое средсвами диагностики Django, представляется
        в виде экземпляра класса LogRecord из стандартного Python модуля logging.

        Аттрибуты:
            message - текст сообщения
            levelname - Уровень сообщения (строка)
            levelno - Уровень сообщения (число)
            pathname - пульный путь выполняемого сейчас файла
            filename - имя выполняемого сейчас файлв
            module - имя выполняемого модуля
            lineno - порядковый номер выполняемой строки
            funcName - имя выполняемой в данный момент функции
            acttime - дата и время создания соощения в виде строки
            created - дата и время создания соощения в виде вещественного числа (кол-во секнд с 01.01.1970)
            msecs - Миллисекунды из времени создания сообщени в виде целого числа
            relativeCreated - кол-во миллисекунд, прошедших между запуском регистратора и созд. тек. сообщ.
            exc_info - кортеж (ссылка на класс искл, объект искл и объект, хранящий стек вызовов)
            stack_info - объект, хранязий стек вызовов
            process - ID процесса в виде цлого числа
            processName - Имя процесса в виде строки
            thread - ID потока
            threadName - Имя потока
            name - имя регистратора, оставившего это сообщение

"""
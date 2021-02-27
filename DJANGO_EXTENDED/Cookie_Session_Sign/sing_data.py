"""

    Подписывание данных (цифровая подпись)

    Виды:
        1) Для строк
        2) Для ругих значений

    (1) Для строк

        Используется класс Signer из django.core.signing

        Signer([key=None][,][sep=':'][,][salt=None])

            key - ключ, на основе которого будет генерироваться цифровая подпись
                  (по умолчвнию беертся из параметра SECRET_KEY)
            sep - символ разделения (подпись:подписанное значение)

        Методы класса:
            sign(<подписанное значение>) - подписывает значение и возвращает результат
            unsign(<подписанное значение>) - извлекает значение (если оно подделано-ошибка)

            Примеры:
            signer = Signer()
            val = signer.sign('Django')
            print(val)
            print(signer.unsign(val))
            print(signer.unsign(val+'c'))


        Класс TimestampSigner - цифровая подпись с ограничение по времени
            signer = TimestampSigner()
            val = signer.sign('Python')
            print(val)
            print(signer.unsign(val)) # Ьудет работать как Signer()
            print(signer.unsign(val, max_age=timedelta(minutes=30)))
            print(signer.unsign(val, max_age=timedelta(seconds=30)))


    (2) Если подписывается значенеи отличное от строки

        Используется функцями из модуля django.core.signing:

        dumps(<значение>[, key=None][, salt='django.core.signing'][, compress=False])

            Подписывает значение с применением класса TimestampSigner и возвращает результат
            в виде строки.
            Сжатие будет давать более заметный результат при подписывание данных большого размера.

        loads(<подписанное начение>[, key=None][, salt='django.core.signing'][, max_age=None])

            Извлекает из подписаного значения оригинальную веичину


        Пример:

            s1 = dumps(12345678)
            s2 = dumps([1,2,3,4])
            s3 = dumps[[1,2,3,4], compress=True]

            loads(s1)
            loads(s2)
            loads(s3, max_age=10)
"""
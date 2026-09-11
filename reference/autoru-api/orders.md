---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/orders.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# API заказа полного отчета

Получение отчета состоит из двух этапов:
1. [Создание заказа](https://yandex.ru/dev/autoru/doc/ru/reference/carfax-orders/create.md).
    Возвращает уникальный идентификатор заказа (`id`), необходимый для получения результата.
1. [Результат заказа](https://yandex.ru/dev/autoru/doc/ru/reference/carfax-orders/result.md).
    Возвращает результат заказа по его `id`. Заказ становится доступен по мере готовности, полная готовность заказа зависит от работоспособности партнеров и может быть непредсказуемой в случае аварий.

Для получения отчета необходимо [аутентифицироваться](https://yandex.ru/dev/autoru/doc/ru/reference/auth-login.md) с помощью токена `x-authorization` и получить `session_id`.

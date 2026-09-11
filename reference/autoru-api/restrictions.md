---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/concepts/restrictions.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# Ограничения по использованию ресурсов API

При использовании API Авто.ру действует ограничение: не более 300 запросов в минуту.

В случае превышения ограничений дальнейшие действия пользователя временно блокируются. Блокировка длится несколько минут. При этом API возвращает ответ с HTTP-статусом 429 Too Many Requests.


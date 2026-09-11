---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/concepts/response-codes.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# Коды ответа

По коду ответа можно узнать результат выполнения операции. В таблице приведен список кодов, которые поддерживаются в API Авто.ру.

#|
||
**Код**
|
**Причина**
|
**Описание**
||
 || 200 | OK | Успешный запрос. || 
 || 400 | BAD_REQUEST | Синтаксическая ошибка в запросе. || 
 || 401 | AUTH_ERROR | Неверный логин / пароль. || 
 || 401 | NO_AUTH | Не удалось авторизовать пользователя по переданным данным. || 
 || 402 | NOT_ENOUGH_FUNDS_ON_ACCOUNT | Недостаточно средств для оплаты. || 
 || 403 | CODE_AUTH_REQUIRED
PASSWORD_EXPIRED | Не удается аутентифицироваться. || 
 || 403 | CUSTOMER_ACCESS_FORBIDDEN | Доступ для данного пользователя запрещен. || 
 || 403 | AGENT_ACCESS_FORBIDDEN | Доступ для данного пользователя запрещен. || 
 || 404 | OFFER_NOT_FOUND | Объявление не найдено. || 
 || 404 | CLIENT_NOT_FOUND | Клиент не найден. || 
 || 409 | NO_PHONE | Не указан телефон продавца. || 
 || 422 | UNPROCESSABLE_ENTITY | Невозможно получить ответ из-за логической ошибки. || 
||
429
|
TOO MANY REQUESTS
|
Превышено ограничение по использованию ресурсов. Подробнее смотрите в разделе [Ограничения по использованию ресурсов API](https://yandex.ru/dev/autoru/doc/ru/concepts/restrictions.md).
||
 || 500 | INTERNAL SERVER ERROR | Внутренняя ошибка сервера. || 
 || 500 | INTERNAL SERVER ERROR
UNKNOWN_ERROR | Внутренняя ошибка сервера. || 

|#

Если запрос был обработан без ошибок, API отвечает кодом `200 OK` и возвращает статус операции `SUCCESS` в теле ответа.

```json
{
  "status":"SUCCESS"
}
```

Если во время выполнения запроса произошла ошибка, API отвечает одним из кодов (таблица кодов приведена выше), возвращает статус операции `ERROR` в теле ответа и имеет следующий формат:

```json
{
  "error":"{string}",
  "status":"ERROR",
  "detailed_error":"{string}"
}
```

#|
||
**Параметр**
|
**Описание**
||
||
`error`
|
Текстовый код ошибки.
||
||
`status`
|
Статус выполнения операции. В случае ошибки значение всегда `ERROR`.
||
||
`detailed_error`
|
Детальное описание ошибки.
||

|#


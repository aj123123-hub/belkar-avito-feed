---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/concepts/access.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# Доступ к API

Хост для всех запросов к API: 

```http
https://apiauto.ru/X.X
```
где X.X — [номер версии](https://yandex.ru/dev/autoru/doc/ru/concepts/versions.md) API. Текущая версия — 1.0.

Для работы с API Авто.ру необходим авторизационный токен. Чтобы получить токен, обратитесь к своему менеджеру в Авто.ру.

Токен следует передавать при каждом запросе к API в значении HTTP-заголовка `x-authorization`: 

```http
curl -i -X GET 'GET https://apiauto.ru/1.0/dealer/account' -H 'x-authorization: fefernrjkgnerkj3453445...'
```

## Формат взаимодействия {#formats}

Взаимодействие ведется по протоколу HTTP с использованием SSL/TLS-шифрования.

Поддерживаемые HTTP-методы: GET, POST, PUT, DELETE.

Ответ сервиса содержит данные в формате JSON.

Список операций приведен в разделе [Операции с ресурсами API](https://yandex.ru/dev/autoru/doc/ru/reference/all-resources.md).

### Заголовки запроса {#formats}

#|
||
**Заголовок**
|
**Описание**
|
**Область применения**
||
||
`x-authorization`
|
Авторизационный токен.
|
Общий заголовок, используется во всех операциях.
||
||
`Accept`
|
Формат выходных данных для ресурса. Допустимые значения: 
- application/octet-stream;
- application/json.
|
Общий заголовок. Может использоваться во всех операциях.
||
||
`Content-Type`
|
Формат входных данных для ресурса. Допустимые значения: 
- text/json, application/json.
|
Общий заголовок, используется в операциях с http-методами POST и PUT.
||
||
`x-session-id`
|
Идентификатор сессии пользователя.
|
Специализированный заголовок. Подробности использования описаны в конкретных операциях.
||
||
`x-dealer-id`
|
Идентификатор дилера.
|
Специализированный заголовок. Подробности использования описаны в конкретных операциях.
||

|#


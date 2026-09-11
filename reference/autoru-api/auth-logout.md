---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/auth-logout.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# POST /auth/logout

Завершает пользовательскую сессию.

## Формат запроса {#input}

```
POST https://apiauto.ru/1.0/auth/logout
```

### Заголовки запроса {#headers}

#|
||
**Заголовок**
|
**Описание**
||
 || `x-dealer-id` | Идентификатор клиента. Используется для работы под учетной записью агентства. || 
 || `x-session-id` | Идентификатор сессии пользователя. Значение можно получить с помощью операции [POST /auth/login](https://yandex.ru/dev/autoru/doc/ru/reference/auth-login.md). || 

|#

### Формат тела запроса {#structure-in}

Тело запроса отсутствует.

Общая структура ответа приведена ниже. Порядок следования элементов не гарантируется. В структуре могут присутствовать служебные параметры, которые не описаны в таблице.

## Формат ответа {#output-structure}

```json
{  
  "session": {
    "id": "{string}",
    "creation_timestamp": "{string}",
    "expire_timestamp": "{string}",
    "ttl_sec": {integer}
  }
}
```

<div class="params-table">

{% include notitle [session](../_includes/params/auth-logout-dee48011df57.md#session) %}

 
:   {% include notitle [id](../_includes/params/auth-logout-dee48011df57.md#id) %}

    {% include notitle [creation_timestamp](../_includes/params/auth-logout-dee48011df57.md#creation_timestamp) %}

    {% include notitle [expire_timestamp](../_includes/params/auth-logout-dee48011df57.md#expire_timestamp) %}

    {% include notitle [ttl_sec](../_includes/params/auth-logout-dee48011df57.md#ttl_sec) %}

</div>

## Коды ответа {#response-codes}

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
 || 500 | INTERNAL SERVER ERROR | Внутренняя ошибка сервера. || 

|#

## Пример {#example-JSON}

> Запрос:
> 
> 
> ```http
> curl -i -X POST 'https://apiauto.ru/1.0/auth/logout' -H 'x-authorization: 2dtrer432...' -H 'Accept: application/json' -H 'Content-Type: application/json'
> ```
> 
> 
> Ответ:
> 
> 
> ```json
> {
>   "session": {
>     "id": "11112233|152...019.777..0.oWEL...JwyqRHw...",
>     "creation_timestamp": "2018-05-28T14:33:39.697Z",
>     "expire_timestamp": "2018-08-26T14:33:39.697Z",
>     "ttl_sec": 7776000
>   }
> }
> ```


{% include [table-style](../_includes/table-style-border-none-2a2aa0c324bf.md) %}

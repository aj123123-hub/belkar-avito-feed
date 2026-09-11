---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/calltracking-call-record.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# POST /calltracking/call/record

Возвращает ссылку на запись звонка.

## Формат запроса {#input}

```
POST https://apiauto.ru/1.0/calltracking/call/record
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

```json
{
  "call_id": {integer},
  "external_id":
    {
      "id": {string},
      "service": {string}
    }
}
```

<div class="params-table">

{% include notitle [call_id](../_includes/params/calltracking-call-record-6e3b17e6444e.md#call_id) %}

{% include notitle [external_id](../_includes/params/calltracking-call-record-6e3b17e6444e.md#external_id) %}

 
:   {% include notitle [id](../_includes/params/calltracking-call-record-6e3b17e6444e.md#id) %}

    {% include notitle [service](../_includes/params/calltracking-call-record-6e3b17e6444e.md#service) %}

</div>

Общая структура ответа приведена ниже. Порядок следования элементов не гарантируется. В структуре могут присутствовать служебные параметры, которые не описаны в таблице.

## Формат ответа {#output-structure}

```json
{
  "url": {string},
  "headers": {object},
  "expire_timestamp": {string},
  "error": {string},
  "status": {string},
  "detailed_error": {string}
}
```

<div class="params-table">

{% include notitle [url](../_includes/params/calltracking-call-record-6e3b17e6444e.md#url) %}

{% include notitle [headers](../_includes/params/calltracking-call-record-6e3b17e6444e.md#headers) %}

{% include notitle [expire_timestamp](../_includes/params/calltracking-call-record-6e3b17e6444e.md#expire_timestamp) %}

{% include notitle [error](../_includes/params/calltracking-call-record-6e3b17e6444e.md#error) %}

{% include notitle [status](../_includes/params/calltracking-call-record-6e3b17e6444e.md#status) %}

{% include notitle [detailed_error](../_includes/params/calltracking-call-record-6e3b17e6444e.md#detailed_error) %}

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
 || 401 | NO_AUTH | Не удалось авторизовать пользователя по переданным данным. || 
 || 500 | INTERNAL SERVER ERROR | Внутренняя ошибка сервера. || 

|#

## Пример {#example-JSON}

> Запрос:
> 
> 
> ```http
> curl -i -X POST 'https://apiauto.ru/1.0/calltracking/call/record' \ 
> -H 'x-dealer-id: 2dtrer432...' \
> -H 'x-session-id: 112_aoR02Tpv...' \
> -H 'Accept: application/json' \
> -d '{
>       "call_id":0,
>       "external_id": {
>         "id":"string",
>         "service":"TELEPONY"
>       }
>     }'
> ```
> 
> 
> Ответ:
> 
> 
> ```json
> HTTP/1.1 200 OK
> Server: nginx
> Date: Tue, 24 Jul 2018 15:19:41 GMT
> Content-Type: application/json
> Connection: keep-alive
> 
> {
>   "url": "string",
>   "headers": {},
>   "expire_timestamp": "2020-06-17T17:20:58.502Z",
>   "status": "SUCCESS"
> }
> ```


{% include [table-style](../_includes/table-style-border-none-2a2aa0c324bf.md) %}

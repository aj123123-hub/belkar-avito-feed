---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/delete-calltracking-call-tag.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# DELETE /calltracking/call/tag

Удаляет указанные теги звонка.

## Формат запроса {#input}

```
DELETE https://apiauto.ru/1.0/calltracking/call/tag
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
  "tags": [
    {
      "value": {string}
    }
  ],
  "call_id": {integer}
}
```

<div class="params-table">

{% include notitle [tags](../_includes/params/put-calltracking-call-tag-514b9cf0162f.md#tags_delete) %}

 
:   {% include notitle [value](../_includes/params/put-calltracking-call-tag-514b9cf0162f.md#value) %}

{% include notitle [call_id](../_includes/params/put-calltracking-call-tag-514b9cf0162f.md#call_id) %}

</div>

Общая структура ответа приведена ниже. Порядок следования элементов не гарантируется. В структуре могут присутствовать служебные параметры, которые не описаны в таблице.

## Формат ответа {#output-structure}

```json
{
  "request": {
    "tags": [
      {
        "value": {string}
      }
    ],
    "call_id": {integer}
  },
  "error": {string},
  "status": {string},
  "detailed_error": {string}
}
```

<div class="params-table">

{% include notitle [request](../_includes/params/put-calltracking-call-tag-514b9cf0162f.md#request) %}

 
:   {% include notitle [tags](../_includes/params/put-calltracking-call-tag-514b9cf0162f.md#tags_delete) %}
    
     
    :   {% include notitle [value](../_includes/params/put-calltracking-call-tag-514b9cf0162f.md#value) %}

    {% include notitle [call_id](../_includes/params/put-calltracking-call-tag-514b9cf0162f.md#call_id) %}

{% include notitle [error](../_includes/params/put-calltracking-call-tag-514b9cf0162f.md#error) %}

{% include notitle [status](../_includes/params/put-calltracking-call-tag-514b9cf0162f.md#status) %}

{% include notitle [detailed_error](../_includes/params/put-calltracking-call-tag-514b9cf0162f.md#detailed_error) %}

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
> curl -i -X DELETE 'https://apiauto.ru/1.0/calltracking/call/tag' \ 
> -H 'x-dealer-id: 2dtrer432...' \
> -H 'x-session-id: 112_aoR02Tpv...' \
> -H 'Accept: application/json' \
> -d '{
>       "tags": [
>         {
>           "value": "string"
>         }
>       ],
>       "call_id": 0
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
>   "request": {
>     "tags": [
>       {
>         "value": "string"
>       }
>     ],
>     "call_id": 0
>   },
>   "status": "SUCCESS"
> }                                    
>                 
> ```

{% include [table-style](../_includes/table-style-border-none-2a2aa0c324bf.md) %}

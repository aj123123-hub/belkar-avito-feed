---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/calltracking-call-complaint.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# POST /calltracking/call/complaint

Отправляет жалобу на платный звонок.

## Формат запроса {#input}

```
POST https://apiauto.ru/1.0/calltracking/call/complaint
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
  "text": {string},
  "email": {string}
}
```
<div class="params-table">

#|
||
##call_id##
|
Идентификатор звонка в трекере звонков.
||
|#

<br>

#|
||
##text##
|
Текст заявки.
||
|#

<br>

#|
||
##email##
|
Почта заявителя.
||
|#

</div>

Общая структура ответа приведена ниже. Порядок следования элементов не гарантируется. В структуре могут присутствовать служебные параметры, которые не описаны в таблице.

## Формат ответа {#output-structure}

```json
{
  "status": {string}
}
```

<div class="params-table">

#|
||
##status##
|
Статус запроса.

{% cut "Допустимые значения:" %}

- `SUCCESS` — успешный запрос;
- `ERROR` — ошибка.

{% endcut %}

||
|#

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
> curl -i -X POST 'https://apiauto.ru/1.0/calltracking/call/complaint' \ 
> -H 'x-dealer-id: 2dtrer432...' \
> -H 'x-session-id: 112_aoR02Tpv...' \
> -H 'Accept: application/json' \
> -d '{
>       "call_id": 0,
>       "text": "string",
>       "email": "string"
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
>   "status": "SUCCESS"
> }                                    
>                 
> ```

{% include [table-style](../_includes/table-style-border-none-2a2aa0c324bf.md) %}

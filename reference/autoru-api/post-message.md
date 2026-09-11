---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/chats/additional/post-message.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# POST /chat/message

Метод позволяет отправить сообщения чат-рума.

## Формат запроса {#input}

```
POST https://apiauto.ru/1.0/chat/message

```

### Заголовки запроса {#headers}

{% include notitle [request-header](../../../_includes/reference/chats/additional/request-header-36116fd5e6e8.md) %}

### Формат тела запроса {#structure-in}

```json
{
  "room_id": {string},
  "payload": {
    "content_type": {string},
    "value": {string}
  },
  "provided_id": {string},
}

```

<div class="params-table">

#|
|| ##room_id##[*](*req) | Идентификатор чата, в который отправляется сообщение ||
|#

#|
|| ##payload##[*](*req) | Объект, содержащий тип контента и само сообщение ||
|#

 
:   {% include notitle [POST_payload_content_type](../../../_includes/params/chats-room-ef391d198a80.md#POST_payload_content_type) %}

    {% include notitle [payload_value](../../../_includes/params/chats-room-ef391d198a80.md#payload_value) %}

{% include notitle [provided_id](../../../_includes/params/chats-room-ef391d198a80.md#provided_id) %}


</div>

{% include notitle [req](../../../_includes/popups-00286d1be377.md#req) %}

Общая структура ответа приведена ниже. Порядок следования элементов не гарантируется. В структуре могут присутствовать служебные параметры, которые не описаны в таблице.

## Формат ответа {#output-structure}

```json
{
  "message": {
    "id": {string},
    "room_id": {string},
    "author": {string},
    "created": {string},
    "payload": {
      "content_type": {string},
      "value": {string}
    },
    "provided_id": {string}, 
    "me": {boolean},
  },
  "error": {string},
  "status": {string},
  "detailed_error": {string}
}

```

<div class="params-table">


{% include notitle [message](../../../_includes/params/chats-room-ef391d198a80.md#message) %}

 
:   {% include notitle [message_id](../../../_includes/params/chats-room-ef391d198a80.md#message_id) %}

    {% include notitle [room_id](../../../_includes/params/chats-room-ef391d198a80.md#room_id) %}

    {% include notitle [author](../../../_includes/params/chats-room-ef391d198a80.md#author) %}

    {% include notitle [created](../../../_includes/params/chats-room-ef391d198a80.md#created) %}

    {% include notitle [payload](../../../_includes/params/chats-room-ef391d198a80.md#payload) %}

     
    :   {% include notitle [payload_content_type](../../../_includes/params/chats-room-ef391d198a80.md#payload_content_type) %}

        {% include notitle [payload_value](../../../_includes/params/chats-room-ef391d198a80.md#payload_value) %}

    {% include notitle [provided_id](../../../_includes/params/chats-room-ef391d198a80.md#provided_id) %}

    {% include notitle [message_me](../../../_includes/params/chats-room-ef391d198a80.md#message_me) %}

{% include notitle [error](../../../_includes/params/chats-room-ef391d198a80.md#error) %}

{% include notitle [status](../../../_includes/params/chats-room-ef391d198a80.md#status) %}

{% include notitle [detailed_error](../../../_includes/params/chats-room-ef391d198a80.md#detailed_error) %}


</div>

## Коды ответа {#response-codes}

{% include notitle [response-codes](../../../_includes/reference/chats/additional/response-codes-b8134368c2f0.md) %}

## Пример {#example-JSON}

> Запрос:
> 
> ```http
> curl -X 'POST' \
>  'https://apiauto.ru/1.0/chat/message' \
>  -H 'accept: application/json' \
>  -H 'x-session: ...' \
>  -H 'x-authorization: ...' \
>  -H 'Content-Type: application/json' \
>  -d '{
>  "room_id": "5fc79a5859760e3b424ee9ccfce96dd5",
>  "payload": {
>    "content_type": "TEXT_PLAIN",
>    "value": "Привет"
>  }
> }'
> ```
> 
> 
> Ответ:
> 
> 
> ```json
> HTTP/1.1 200 OK
> Server: nginx
> Date: Fri, 12 Jul 2018 13:30:59 GMT
> Content-Type: application/json
> Connection: keep-alive
> 
> {
>   "status": "SUCCESS"
> }                                     
> ```

{% include [table-style](../../../_includes/table-style-border-none-2a2aa0c324bf.md) %}

[*req]: {% include notitle [req](../../../_includes/popups-00286d1be377.md#req) %}


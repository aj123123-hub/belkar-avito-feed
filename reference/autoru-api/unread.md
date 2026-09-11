---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/chats/additional/unread.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# GET /chat/message/unread

Метод позволяет узнавать, есть ли непрочитанные сообщения.

## Формат запроса {#input}

```
GET https://apiauto.ru/1.0/chat/message/unread/
```

### Заголовки запроса {#headers}

{% include notitle [request-header](../../../_includes/reference/chats/additional/request-header-36116fd5e6e8.md) %}

## Формат ответа {#output-structure}

```json
{
  "has_unread": true,
  "unread_counter": 2,
  "status": "SUCCESS"
}
```


<div class="params-table">

{% include notitle [has_unread](../../../_includes/params/chats-room-ef391d198a80.md#has_unread) %}

{% include notitle [unread_counter](../../../_includes/params/chats-room-ef391d198a80.md#unread_counter) %}

{% include notitle [status](../../../_includes/params/chats-room-ef391d198a80.md#status) %}

</div>


## Коды ответа {#response-codes}

{% include notitle [response-codes](../../../_includes/reference/chats/additional/response-codes-b8134368c2f0.md) %}

## Пример {#example-JSON}

> Запрос:
> 
> 
> ```
> curl -X 'GET' \
>  'https://apiauto.ru/1.0/chat/message/unread' \
>  -H 'accept: application/json' \
>  -H 'x-session: ...' \
>  -H 'x-authorization: ...' 
> ```
> 
> 
> Ответ:
> 
> ```json
> {
>  "has_unread": true,
>  "unread_counter": 2,
>  "status": "SUCCESS"
> }
> ```

{% include [table-style](../../../_includes/table-style-border-none-2a2aa0c324bf.md) %}


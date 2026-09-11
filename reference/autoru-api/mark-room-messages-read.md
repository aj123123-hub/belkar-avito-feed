---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/chats/additional/mark-room-messages-read.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# DELETE /chat/message/unread 

Метод позволяет отметить чат-рум как прочитанный.

## Формат запроса {#input}

```
DELETE https://apiauto.ru/1.0/chat/message/unread

? [room_id](*room_id)=<string>
```

<div class="params-table">

#|
|| ##room_id##[*](*req) | ID чат-рума ||
|#

</div>

{% include notitle [req](../../../_includes/popups-00286d1be377.md#req) %}


### Заголовки запроса {#headers}

{% include notitle [request-header](../../../_includes/reference/chats/additional/request-header-36116fd5e6e8.md) %}

## Формат ответа {#output-structure}

```json
{
  "status": "SUCCESS"
}
```

<div class="params-table">

{% include notitle [status](../../../_includes/params/chats-room-ef391d198a80.md#status) %}

</div>


## Коды ответа {#response-codes}

{% include notitle [response-codes](../../../_includes/reference/chats/additional/response-codes-b8134368c2f0.md) %}

## Пример {#example-JSON}

> Запрос:
> 
> 
> ```
> curl -X 'DELETE' \
>  'https://apiauto.ru/1.0/chat/message/unread?room_id=...' \
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
>  "status": "SUCCESS"
> }
> ```

{% include [table-style](../../../_includes/table-style-border-none-2a2aa0c324bf.md) %}

[*req]: {% include notitle [req](../../../_includes/popups-00286d1be377.md#req) %}

[*room_id]: {% include notitle [only_unread](../../../_includes/popups-00286d1be377.md#room_id) %}

---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/chats/additional/get-message.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# GET /chat/message

Метод позволяет получить сообщения чат-рума.

## Формат запроса {#input}

```
GET https://apiauto.ru/1.0/chat/message/

? [room_id](*room_id)=<string>
& [from](*message_from)=<string> 
& [[count](*count)=<integer>]
& [[asc](*asc)=<boolean>]
```

<div class="params-table">

#|
|| ##room_id##[*](*req) | ID чат-рума ||
|| ##from## | ID сообщения, начиная с которого нужно возвращать сообщения в ответе ||
|| ##count## | Количество сообщений ||
|| ##asc## | Возвращать сообщения по возрастанию или по убыванию номера идентификатора ||
|#

</div>

{% include notitle [req](../../../_includes/popups-00286d1be377.md#req) %}


### Заголовки запроса {#headers}

{% include notitle [request-header](../../../_includes/reference/chats/additional/request-header-36116fd5e6e8.md) %}

## Формат ответа {#output-structure}

```json
 {
  "messages": [
    {
      "id": {string},
      "room_id": {string},
      "author": {string},
      "created": {string},
      "payload": {
        "content_type": {string},
        "value": {string}
      },
      "attachments": [
        {
          "image": {
            "sizes": {
              "additionalProp1": {string},
              "additionalProp2": {string},
              "additionalProp3": {string}
            }
          },
        }
      ],
      "me": {boolean},
    }
  ],
  "error": {string},
  "status": {string},
  "detailed_error": {string}
}
```


<div class="params-table">

{% include notitle [messages](../../../_includes/params/chats-room-ef391d198a80.md#messages) %}

 
:   {% include notitle [messages_id](../../../_includes/params/chats-room-ef391d198a80.md#messages_id) %}

    {% include notitle [room_id](../../../_includes/params/chats-room-ef391d198a80.md#room_id) %}

    {% include notitle [author](../../../_includes/params/chats-room-ef391d198a80.md#author) %}

    {% include notitle [created](../../../_includes/params/chats-room-ef391d198a80.md#created) %}

    {% include notitle [payload](../../../_includes/params/chats-room-ef391d198a80.md#payload) %}

     
    :   {% include notitle [payload_content_type](../../../_includes/params/chats-room-ef391d198a80.md#payload_content_type) %}

        {% include notitle [payload_value](../../../_includes/params/chats-room-ef391d198a80.md#payload_value) %}

    {% include notitle [attachments](../../../_includes/params/chats-room-ef391d198a80.md#attachments) %}

     
    :   {% include notitle [attachments_image](../../../_includes/params/chats-room-ef391d198a80.md#attachments_image) %}

    {% include notitle [messages_me](../../../_includes/params/chats-room-ef391d198a80.md#messages_me) %}

{% include notitle [error](../../../_includes/params/chats-room-ef391d198a80.md#error) %}

{% include notitle [status](../../../_includes/params/chats-room-ef391d198a80.md#status) %}

{% include notitle [detailed_error](../../../_includes/params/chats-room-ef391d198a80.md#detailed_error) %}

</div>


## Коды ответа {#response-codes}

{% include notitle [response-codes](../../../_includes/reference/chats/additional/response-codes-b8134368c2f0.md) %}

## Пример {#example-JSON}

> Запрос:  
> 
> ```
> curl -X 'GET' \
>  'https://apiauto.ru/1.0/chat/message?room_id=d7bf06f7c895a30403cb6732d61ecdc8&count=100&asc=true' \
>  -H 'accept: application/json'\
>  -H 'x-session: ...' \
>  -H 'x-authorization: ...' 
>
> ```
> 
> 
> Ответ:
> 
> ```json
> {
>   "messages": [
>     {
>       "id": "11f04e2a9a42fe00a95b6bf174b85f15",
>       "room_id": "d7bf06f7c895a30403cb6732d61ecdc8",
>       "author": "O5zY3TPD_4iQ4IniT8iczUKZlKPQ7EUnvTguP7MjY-u_S4soqCyFK4vKNj0whsWP",
>       "created": "2025-06-20T23:02:13.216Z",
>       "payload": {
>         "content_type": "TEXT_HTML",
>         "value": "\nНе упустите это предложение — напишите или позвоните продавцу сегодня!<br>\nА мы подарим вам Отчёт Авто.ру, чтобы было легче принять решение о покупке.<br>\n<a href=\"https://auto.ru/promo/free-report-rules/\">Как получить отчёт</a>\n"
>       },
>     },
>     {
>       "id": "11f04e2b0cbabbd0ab841f2854e64edd",
>       "room_id": "d7bf06f7c895a30403cb6732d61ecdc8",
>       "author": "O5zY3TPD_4iQ4IniT8iczUKZlKPQ7EUnvTguP7MjY-u_S4soqCyFK4vKNj0whsWP",
>       "created": "2025-06-20T23:05:25.261Z",
>       "payload": {
>         "content_type": "TEXT_HTML",
>         "value": "\nНе упустите это предложение — напишите или позвоните продавцу сегодня!<br>\nА мы подарим вам Отчёт Авто.ру, чтобы было легче принять решение о покупке.<br>\n<a href=\"https://auto.ru/promo/free-report-rules/\">Как получить отчёт</a>\n"
>       },
>     },
>     {
>       "id": "11f060d561c0a100ac686bc64ab9f84e",
>       "room_id": "d7bf06f7c895a30403cb6732d61ecdc8",
>       "author": "O5zY3TPD_4iQ4IniT8iczUKZlKPQ7EUnvTguP7MjY-u_S4soqCyFK4vKNj0whsWP",
>       "created": "2025-07-14T17:10:03.280Z",
>       "payload": {
>         "content_type": "TEXT_HTML",
>         "value": "<b style=\"font-weight: 500; margin-bottom: 2px; display: block;\">Поздравляем с покупкой!</b><div>Машина уже в Гараже. А вместе с ней — чек-лист, чтобы не забыть важное при покупке. Заходите в Гараж почаще: сможете хранить историю обслуживания и получать напоминания о ТО.</div><a href=\"http://ya.ru\" style=\"margin-top: 12px; display: inline-block;\">Ссылка на Чек-лист</a>"
>       },
>     },
>     {
>       "id": "11f060d5c99151d0a9f40d9806816e8c",
>       "room_id": "d7bf06f7c895a30403cb6732d61ecdc8",
>       "author": "O5zY3TPD_4iQ4IniT8iczUKZlKPQ7EUnvTguP7MjY-u_S4soqCyFK4vKNj0whsWP",
>       "created": "2025-07-14T17:12:57.453Z",
>       "payload": {
>         "content_type": "TEXT_HTML",
>         "value": "<div style=\"margin-bottom: 8px;\">Вы недавно контактировали с продавцом <a data-action=\"open_reseller_offer\" href=\"http://ya.ru\">[марка-модель-цена]</a>. Как всё прошло? 🚗</div><div>Пожалуйста, расскажите, чем закончилось ваше общение, и поставьте оценку. Ваш отзыв повлияет на рейтинг продавца и поможет другим покупателям сделать правильный выбор!</div><a style=\"display: inline-flex; margin-top: 12px; border-radius: 8px; background: black; padding: 0 16px; height: 32px; text-decoration: none; color: white; font-weight: 500; font-size: 13px; line-height: 16px; align-items: center;\" data-action=\"open_feedback_on_reseller_for\" href=\"http://ya.ru\">Поставить оценку</a>"
>       },
>     }
>   ],
>   "status": "SUCCESS"
> } 
> ```

{% include [table-style](../../../_includes/table-style-border-none-2a2aa0c324bf.md) %}

[*req]: {% include notitle [req](../../../_includes/popups-00286d1be377.md#req) %}

[*room_id]: {% include notitle [only_unread](../../../_includes/popups-00286d1be377.md#room_id) %}

[*message_from]: {% include notitle [only_unread](../../../_includes/popups-00286d1be377.md#message_from) %}

[*count]: {% include notitle [only_unread](../../../_includes/popups-00286d1be377.md#count) %}

[*asc]: {% include notitle [only_unread](../../../_includes/popups-00286d1be377.md#asc) %}


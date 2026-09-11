---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/chats/additional/room-by-id.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# GET /chat/room/by-id

Метод позволяет получить список чат-румов по ID.

## Формат запроса {#input}

```
GET https://apiauto.ru/1.0/chat/room/by-id

? [id](*id)=<string>
```

<div class="params-table">

#|
|| ##id##[*](*req) | ID чат-рума ||
|#

</div>

{% include notitle [req](../../../_includes/popups-00286d1be377.md#req) %}


### Заголовки запроса {#headers}

{% include notitle [request-header](../../../_includes/reference/chats/additional/request-header-36116fd5e6e8.md) %}

## Формат ответа {#output-structure}

```json
{
  "rooms": [
    {
      "id": {string},
      "created": {string},
      "updated": {string},
      "users": [
        {
          "id": {string},
          "blocked_room": {boolean},
          "average_reply_delay_minutes": {integer},
          "last_seen": {string},
          "description": {string},
          "room_last_read": {string}
        }
      ],
      "me": {string},
      "subject": {
        "offer": {
          "source": {
            "category": {string},
            "id": {string}
          },
          "value": {модель оффера}
        },
        "title": {string},
        "title_v2": {string},
        "image": {
          "additionalProp1": {string},
          "additionalProp2": {string},
          "additionalProp3": {string}
        }
      },
      "last_message": {
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
      },
    }
  ],
  "error": {string},
  "status": {string},
  "detailed_error": {string}
}
```


<div class="params-table">

{% include notitle [rooms](../../../_includes/params/chats-room-ef391d198a80.md#rooms) %}

 
:   {% include notitle [id](../../../_includes/params/chats-room-ef391d198a80.md#id) %}

    {% include notitle [created](../../../_includes/params/chats-room-ef391d198a80.md#created) %}

    {% include notitle [updated](../../../_includes/params/chats-room-ef391d198a80.md#updated) %}

    {% include notitle [users](../../../_includes/params/chats-room-ef391d198a80.md#users) %}

     
    :   {% include notitle [users_id](../../../_includes/params/chats-room-ef391d198a80.md#users_id) %}

        {% include notitle [users_blocked_room](../../../_includes/params/chats-room-ef391d198a80.md#users_blocked_room) %}

        {% include notitle [users_average_reply_delay_minutes](../../../_includes/params/chats-room-ef391d198a80.md#users_average_reply_delay_minutes) %}

        {% include notitle [users_last_seen](../../../_includes/params/chats-room-ef391d198a80.md#users_last_seen) %}

        {% include notitle [users_description](../../../_includes/params/chats-room-ef391d198a80.md#users_description) %}

        {% include notitle [users_room_last_read](../../../_includes/params/chats-room-ef391d198a80.md#users_room_last_read) %}

    {% include notitle [me](../../../_includes/params/chats-room-ef391d198a80.md#me) %}

    {% include notitle [subject](../../../_includes/params/chats-room-ef391d198a80.md#subject) %}

     
    :   #|
        || ##offer## | Данные объявления на Авто.ру. Модель предложения см. в разделе [GET /feeds/history/{task_id}](../../feeds-history-taskId.md) в массиве `offers` ||
        |#

        {% include notitle [subject_title](../../../_includes/params/chats-room-ef391d198a80.md#subject_title) %}

        {% include notitle [subject_title_v2](../../../_includes/params/chats-room-ef391d198a80.md#subject_title_v2) %}

        {% include notitle [subject_image](../../../_includes/params/chats-room-ef391d198a80.md#subject_image) %}

    {% include notitle [last_message](../../../_includes/params/chats-room-ef391d198a80.md#last_message) %}

     
    :   {% include notitle [last_message_id](../../../_includes/params/chats-room-ef391d198a80.md#last_message_id) %}

        {% include notitle [last_message_room_id](../../../_includes/params/chats-room-ef391d198a80.md#last_message_room_id) %}

        {% include notitle [last_message_author](../../../_includes/params/chats-room-ef391d198a80.md#last_message_author) %}

        {% include notitle [last_message_created](../../../_includes/params/chats-room-ef391d198a80.md#last_message_created) %}

        {% include notitle [payload](../../../_includes/params/chats-room-ef391d198a80.md#payload) %}

         
        :   {% include notitle [payload_content_type](../../../_includes/params/chats-room-ef391d198a80.md#payload_content_type) %}

            {% include notitle [payload_value](../../../_includes/params/chats-room-ef391d198a80.md#payload_value) %}

        {% include notitle [attachments](../../../_includes/params/chats-room-ef391d198a80.md#attachments) %}

         
        :   {% include notitle [attachments_image](../../../_includes/params/chats-room-ef391d198a80.md#attachments_image) %}

             
            :   {% include notitle [attachments_image_sizes](../../../_includes/params/chats-room-ef391d198a80.md#attachments_image_sizes) %}

        {% include notitle [last_message_me](../../../_includes/params/chats-room-ef391d198a80.md#last_message_me) %}

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
>  'https://apiauto.ru/1.0/chat/room/by-id?id=d7bf06f7c895a30403cb6732d61ecdc8' \
>  -H 'accept: application/json' 
>  -H 'x-session: ...' \
>  -H 'x-authorization: ...'  
> ```
> 
> 
> Ответ:
> 
> ```json
> {
>   "rooms": [
>     {
>       "id": "d7bf06f7c895a30403cb6732d61ecdc8",
>       "created": "2025-06-20T23:02:13.034Z",
>       "updated": "2025-07-18T14:56:29.523Z",
>       "users": [
>         {
>           "id": "Btl1Z7Bm0jtPoJSQvkmoxUulXrL0cUQczsM2FarmYay7fv4k1bk1gQ",
>           "room_last_read": "2025-07-18T14:56:29.525Z"
>         },
>         {
>           "id": "MtOslS-_yRyQ4IniT8iczUKZlKPQ7EUnvTguP7MjY-u_S4soqCyFK4vKNj0whsWP",
>         }
>       ],
>       "me": "Btl1Z7Bm0jtPoJSQvkmoxUulXrL0cUQczsM2FarmYay7fv4k1bk1gQ",
>       "subject": {
>         "offer": {
>           "source": {
>             "category": "cars",
>             "id": "1128547367-53ec285d"
>           },
>           "value": {модель оффера}
>         },
>         "title": "Валерий",
>         "image": {
>           "thumb_m": "//images.mds-proxy.test.avto.ru/get-autoru-vos/2074086/91522721e78a2c6d8c6f7be9ec3cda3a/thumb_m",
>           "832x624": "//images.mds-proxy.test.avto.ru/get-autoru-vos/2074086/91522721e78a2c6d8c6f7be9ec3cda3a/832x624",
>           "456x342n": "//images.mds-proxy.test.avto.ru/get-autoru-vos/2074086/91522721e78a2c6d8c6f7be9ec3cda3a/456x342n",
>           "full": "//images.mds-proxy.test.avto.ru/get-autoru-vos/2074086/91522721e78a2c6d8c6f7be9ec3cda3a/full",
>           "1200x900": "//images.mds-proxy.test.avto.ru/get-autoru-vos/2074086/91522721e78a2c6d8c6f7be9ec3cda3a/1200x900",
>           "small": "//images.mds-proxy.test.avto.ru/get-autoru-vos/2074086/91522721e78a2c6d8c6f7be9ec3cda3a/small",
>           "584x438": "//images.mds-proxy.test.avto.ru/get-autoru-vos/2074086/91522721e78a2c6d8c6f7be9ec3cda3a/584x438"
>         },
>         "title_v2": "Chevrolet Aveo I, 2007"
>       },
>       "last_message": {
>         "id": "11f060d5c99151d0a9f40d9806816e8c",
>         "room_id": "d7bf06f7c895a30403cb6732d61ecdc8",
>         "author": "O5zY3TPD_4iQ4IniT8iczUKZlKPQ7EUnvTguP7MjY-u_S4soqCyFK4vKNj0whsWP",
>         "created": "2025-07-14T17:12:57.453Z",
>         "payload": {
>           "content_type": "TEXT_HTML",
>           "value": "<div style=\"margin-bottom: 8px;\">Вы недавно контактировали с продавцом <a data-action=\"open_reseller_offer\" href=\"http://ya.ru\">[марка-модель-цена]</a>. Как всё прошло? 🚗</div><div>Пожалуйста, расскажите, чем закончилось ваше общение, и поставьте оценку. Ваш отзыв повлияет на рейтинг продавца и поможет другим покупателям сделать правильный выбор!</div><a style=\"display: inline-flex; margin-top: 12px; border-radius: 8px; background: black; padding: 0 16px; height: 32px; text-decoration: none; color: white; font-weight: 500; font-size: 13px; line-height: 16px; align-items: center;\" data-action=\"open_feedback_on_reseller_for\" href=\"http://ya.ru\">Поставить оценку</a>"
>         },
>       },
>     }
>   ],
>   "status": "SUCCESS"
> } 
> ```

{% include [table-style](../../../_includes/table-style-border-none-2a2aa0c324bf.md) %}

[*req]: {% include notitle [req](../../../_includes/popups-00286d1be377.md#req) %}

[*id]: {% include notitle [only_unread](../../../_includes/popups-00286d1be377.md#id) %}

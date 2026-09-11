---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/chats/additional/room-light.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# GET /chat/room/light

Метод позволяет получить список чат-румов.

## Формат запроса {#input}

```
GET https://apiauto.ru/1.0/chat/room/light

? [[only_unread](*only_unread)=<boolean>]
```

<div class="params-table">

#|
|| ##only_unread## | Признак. Добавлять в ответ только непрочитанные чаты. 

{% cut "Допустимые значения:" %}

- `true` — будут добавлены только непрочитанные чаты; 
- `false` — будут добавлены прочитанные и непрочитанные чаты

{% endcut %}

||
|#

</div>

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
> 'https://apiauto.ru/1.0/chat/room/light' \
>  -H 'x-session: ...' \
>  -H 'x-authorization: ...' 
> ```
> 
> 
> Ответ: 
> 
> ```json
>  {
>    "rooms": [
>    {
>        "id": "8dd0aa64a684dec3b88047e4c1ca6a78",
>        "created": "2019-02-25T11:49:34.883Z",
>        "updated": "2025-08-20T14:35:23.337Z",
>        "users": [
>          {
>            "id": "fb491ecdde6a556e",
>            "room_last_read": "2025-08-20T14:40:18.320Z"
>          },
>          {
>            "id": "tHFSUBR3HJjvFNpF16b7M_eK2NBuutJTLsoBzDB3b85EG1wtyv9X3A",
>            "room_last_read": "2025-08-20T14:35:23.355Z"
>          }
>        ],
>        "me": "tHFSUBR3HJjvFNpF16b7M_eK2NBuutJTLsoBzDB3b85EG1wtyv9X3A",
>        "subject": {
>          "title": "Чат с поддержкой",
>         "image": {
>           "1200x900": "//avatars.mds.yandex.net/get-autoru-all/1336268/techSupportAutoru/1200x900",
>           "180x135": "//avatars.mds.yandex.net/get-autoru-all/1336268/techSupportAutoru/180x135",
>           "248x186": "//avatars.mds.yandex.net/get-autoru-all/1336268/techSupportAutoru/248x186",
>           "small": "//vertis-frontend.s3.yandex.net/auto/frontend/chat-logo/icon-166x124.png",
>           "thumb_l": "//avatars.mds.yandex.net/get-autoru-all/1336268/techSupportAutoru/thumb_l",
>           "thumb_l_2x": "//avatars.mds.yandex.net/get-autoru-all/1336268/techSupportAutoru/thumb_l_2x"
>         },
>         "title_v2": "Чат с поддержкой"
>       },
>       "last_message": {
>         "id": "11f07dd2e3e894c0ab302f0b38f5b353",
>         "room_id": "8dd0aa64a684dec3b88047e4c1ca6a78",
>         "author": "fb491ecdde6a556e",
>         "created": "2025-08-20T14:35:16.876Z",
>         "payload": {
>           "content_type": "TEXT_HTML",
>           "value": "Привет! С вами бот 🤖 С чем нужна помощь?"
>         },
>       },
>     },
>     {
>       "id": "8879709c92e3aa528c68b903687c0e0e",
>       "created": "2024-10-15T13:33:58.040Z",
>       "updated": "2025-08-20T14:33:00.477Z",
>       "users": [
>         {
>           "id": "d18e891cd0d56f3e",
>           "room_last_read": "2024-10-16T09:08:20.924Z"
>         },
>         {
>           "id": "pddQI0dT6aybIi0SBV2wdPN0TUwq2Ca2gg0y3nUcEEZ_6O81WOo0Xg",
>           "room_last_read": "2024-10-29T12:52:34.194Z"
>         }
>       ],
>       "me": "pddQI0dT6aybIi0SBV2wdPN0TUwq2Ca2gg0y3nUcEEZ_6O81WOo0Xg",
>       "subject": {
>         "offer": {
>           "source": {
>             "category": "cars",
>             "id": "1125455382-414bd07f"
>           },
>         },
>         "title": "Чат",
>         "title_v2": "Чат"
>       },
>       "last_message": {
>         "id": "11ef8bca4402e5f0b8854ff40ed84c79",
>         "room_id": "8879709c92e3aa528c68b903687c0e0e",
>         "author": "d18e891cd0d56f3e",
>         "created": "2024-10-16T14:23:51.247Z",
>         "payload": {
>           "content_type": "TEXT_PLAIN"
>         },
>         "attachments": [
>           {
>             "image": {
>               "sizes": {
>                 "320x320": "//custodian-download.test.vertis.yandex-team.ru/download/ZBBT_0b6fyISK1pfToDy37ZCT25Q5UIZf9oG6vdWG4vzK1TDz4XbPd0kPZt3axgxkMU8x4EEfOqyn4qlJJBqWW3b2ElGsGXgblGbXvB4w7tavmlZNGDGYqtUd-vvJpyQhCN2CFflkfg/320x320",
>                 "460x460": "//custodian-download.test.vertis.yandex-team.ru/download/ZBBT_0b6fyISK1pfToDy37ZCT25Q5UIZf9oG6vdWG4vzK1TDz4XbPd0kPZt3axgxkMU8x4EEfOqyn4qlJJBqWW3b2ElGsGXgblGbXvB4w7tavmlZNGDGYqtUd-vvJpyQhCN2CFflkfg/460x460",
>                 "1200x1200": "//custodian-download.test.vertis.yandex-team.ru/download/ZBBT_0b6fyISK1pfToDy37ZCT25Q5UIZf9oG6vdWG4vzK1TDz4XbPd0kPZt3axgxkMU8x4EEfOqyn4qlJJBqWW3b2ElGsGXgblGbXvB4w7tavmlZNGDGYqtUd-vvJpyQhCN2CFflkfg/1200x1200"
>               }
>             }
>           }
>         ],
>       },
>     },
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
>         },
>         "title": "Чат",
>         "title_v2": "Чат"
>       },
>       "last_message": {
>         "id": "11f060d5c99151d0a9f40d9806816e8c",
>         "room_id": "d7bf06f7c895a30403cb6732d61ecdc8",
>         "author": "O5zY3TPD_4iQ4IniT8iczUKZlKPQ7EUnvTguP7MjY-u_S4soqCyFK4vKNj0whsWP",
>         "created": "2025-07-14T17:12:57.453Z",
>         "payload": {
>           "content_type": "TEXT_HTML",
>           "value": "<div style=\"margin-bottom: 8px;\"Вы недавно контактировали с продавцом <a data-action=\"open_reseller_offer\" href=\"http://ya.ru\"[марка-модель-цена]</a. Как всё прошло? 🚗</div<divПожалуйста, расскажите, чем закончилось ваше общение, и поставьте оценку. Ваш отзыв повлияет на рейтинг продавца и поможет другим покупателям сделать правильный выбор!</div<a style=\"display: inline-flex; margin-top: 12px; border-radius: 8px; background: black; padding: 0 16px; height: 32px; text-decoration: none; color: white; font-weight: 500; font-size: 13px; line-height: 16px; align-items: center;\" data-action=\"open_feedback_on_reseller_for\" href=\"http://ya.ru\"Поставить оценку</a"
>         },
>       },
>     },
>   ],
>   "status": "SUCCESS"
> }
> ```

{% include [table-style](../../../_includes/table-style-border-none-2a2aa0c324bf.md) %}

[*only_unread]: {% include notitle [only_unread](../../../_includes/popups-00286d1be377.md#only_unread) %}


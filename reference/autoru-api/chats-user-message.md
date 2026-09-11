---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/chats/basic/chats-user-message.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# POST Сообщение пользователя

Позволяет передавать сообщение пользователя Авто.ру на сервер внешней системы.

## Формат запроса {#input}

{% note warning %}

Запрос отправляется на URL, указанный в личном кабинете дилера.

{% endnote %}

```
POST https://api.example.com/
? [chat_id](*chat_id)=<string>
```

<div class="params-table">

#|
|| ##chat_id##[*](*req) | Внешний идентификатор чата. 

Задается в личном кабинете дилера в поле ChatId при подключении приложения. Должен уникальным образом идентифицировать одного клиента Авто.ру, для которого выполняются запросы. ||
|#

</div>

{% include notitle [req](../../../_includes/popups-00286d1be377.md#req) %}

### Формат тела запроса {#structure-in}

```json
{
  "sender": {
    "id": {string},
    "name": {string},
    "photo": {string},
    "url": {string},
    "title": {string}
  },
  "message" : {
    "type": {string},
    "id": {string},
    "text": {string},
    "file": {string},
    "thumb": {string}
  }
}
```

<div class="params-table">

{% include notitle [sender](../../../_includes/params/chats-user-message-24c98b864439.md#sender) %}

 
:   {% include notitle [id](../../../_includes/params/chats-user-message-24c98b864439.md#id1) %}

    {% include notitle [name](../../../_includes/params/chats-user-message-24c98b864439.md#name) %}

    {% include notitle [photo](../../../_includes/params/chats-user-message-24c98b864439.md#photo) %}

    {% include notitle [url](../../../_includes/params/chats-user-message-24c98b864439.md#url) %}

    {% include notitle [title](../../../_includes/params/chats-user-message-24c98b864439.md#title) %}

{% include notitle [message](../../../_includes/params/chats-user-message-24c98b864439.md#message) %}

 
:   {% include notitle [type](../../../_includes/params/chats-user-message-24c98b864439.md#type) %}

    {% include notitle [id](../../../_includes/params/chats-user-message-24c98b864439.md#id2) %}

    {% include notitle [text](../../../_includes/params/chats-user-message-24c98b864439.md#text) %}

    {% include notitle [file](../../../_includes/params/chats-user-message-24c98b864439.md#file) %}

    {% include notitle [thumb](../../../_includes/params/chats-user-message-24c98b864439.md#thumb) %}

</div>

{% include notitle [req](../../../_includes/popups-00286d1be377.md#req) %}

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
> curl -i -X POST 'https://api.example.com/?chat_id=fh5GkT67' \
> -H 'Accept: application/json' \
> -d {
>      "sender" : {
>        "id" : "a3bc21...",
>        "name" : "ivanivanov",
>        "photo" : "https://avatars.mds.yandex.net/.../1200x900n",
>        "url" : "https://auto.ru/cars/.../1097255222-276b1ca9",
>        "title" : "Mercedes-Benz E-Класс V (W213, S213, C238), 1670000 руб"
>      },
>      "message": {
>        "type": "text",
>        "id": "2b17a38c...",
>        "text": "Здравствуйте! Еще продается?"
>      }
>    }
> ```
> 
> 
> Ответ:
> 
> 
> ```json
> HTTP/1.1 200 OK
> Server: nginx
> Date: Mon, 14 Sep 2020 14:34:59 GMT
> Connection: keep-alive
> ```

{% include [table-style](../../../_includes/table-style-border-none-2a2aa0c324bf.md) %}


[*req]: {% include notitle [req](../../../_includes/popups-00286d1be377.md#req) %}

[*chat_id]: Внешний идентификатор чата. Задается в личном кабинете дилера в поле ChatId при подключении приложения. Должен уникальным образом идентифицировать одного клиента Авто.ру, для которого выполняются запросы.

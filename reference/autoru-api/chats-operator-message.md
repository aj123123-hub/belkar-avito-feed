---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/chats/basic/chats-operator-message.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# POST /aggregators/auto/hook

Позволяет передавать сообщение оператора из внешней системы пользователю Авто.ру.

## Формат запроса {#input}

```
POST https://apiauto.ru/1.0/aggregators/auto/hook
? [token](*token)=<string>
```

<div class="params-table">

#|
||
##token##[*](*req)
|
Внешний идентификатор чата. Задается в личном кабинете дилера в поле ChatId при подключении приложения. Должен уникальным образом идентифицировать одного клиента Авто.ру, для которого выполняются запросы.
||
|#

</div>

{% include notitle [req](../../../_includes/popups-00286d1be377.md#req) %}

### Формат тела запроса {#structure-in}

```json
{
  "sender": {
    "name": {string},
    "photo": {string},
    "email": {string}
  },
  "recipient": {
    "id": {string}
  },
  "message" : {
    "type": {string},
    "id": {string},
    "text": {string},
    "file": {string}
  }
}
```

<div class="params-table">

{% include notitle [sender](../../../_includes/params/chats-operator-message-4a6852be1121.md#sender) %}

 
:   {% include notitle [name](../../../_includes/params/chats-operator-message-4a6852be1121.md#name) %}

    {% include notitle [photo](../../../_includes/params/chats-operator-message-4a6852be1121.md#photo) %}

    {% include notitle [email](../../../_includes/params/chats-operator-message-4a6852be1121.md#email) %}

{% include notitle [recipient](../../../_includes/params/chats-operator-message-4a6852be1121.md#recipient) %}

 
:   {% include notitle [id1](../../../_includes/params/chats-operator-message-4a6852be1121.md#id1) %}

{% include notitle [message](../../../_includes/params/chats-operator-message-4a6852be1121.md#message) %}

 
:   {% include notitle [type](../../../_includes/params/chats-operator-message-4a6852be1121.md#type) %}

    {% include notitle [id2](../../../_includes/params/chats-operator-message-4a6852be1121.md#id2) %}

    {% include notitle [text](../../../_includes/params/chats-operator-message-4a6852be1121.md#text) %}

    {% include notitle [file](../../../_includes/params/chats-operator-message-4a6852be1121.md#file) %}


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
> curl -i -X POST 'https://chat-api-ext.vertis.yandex.net/api/1.x/aggregators/auto/hook?token=Vj72x3B9NT' \
> -H 'Accept: application/json' \
> -d {
>      "sender": {
>        "name": "Alex"
>      },
>      "recipient": {
>        "id": "a3bc21...",
>      },
>      "message": {
>        "type": "text",
>        "id": "4568...",
>        "text": "Здравствуйте! Да, продается."
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

[*token]: Внешний идентификатор чата. Задается в личном кабинете дилера в поле ChatId при подключении приложения. Должен уникальным образом идентифицировать одного клиента Авто.ру, для которого выполняются запросы.

[*req]: {% include notitle [req](../../../_includes/popups-00286d1be377.md#req) %}

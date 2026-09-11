---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/dealer/chats/campaigns/preview.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# POST dealer/chats/campaigns/preview

Предпросмотр рассылки.

## Формат запроса {#input}

```json

{
  "offer_ids": "1128253634-637c343c",
  "category": "CARS",
  "section": "USED"
}
```


<div class="params-table">

{% include notitle [offer_ids](../../../../_includes/params/campaigns-435f0a37c701.md#offer_ids) %}

{% include notitle [category](../../../../_includes/params/campaigns-435f0a37c701.md#category) %}

{% include notitle [section](../../../../_includes/params/campaigns-435f0a37c701.md#section) %}

</div>

### Заголовки запроса {#headers}

| Заголовок  | Описание  |
| ----------- | ----------- |
| `x-dealer-id`| Идентификатор клиента. Используется для работы под учетной записью агентства.|
| `x-session-id`| Идентификатор сессии пользователя. Значение можно получить с помощью операции [POST /auth/login](../../../auth-login.md).|

## Формат ответа {#output-structure}

```json
{
  "templates": [
    {
      "id": 0,
      "text": "А ещё в подарок: {gifts}",
      "required_fields": "gifts",
      "category": "cars"
    }
  ],
  "gifts": [
    {
      "id": 0,
      "name": "Шины",
      "image_url": "string"
    }
  ],
  "messages_limit": 0,
  "message_price_kopecks": 0,
  "offer_id_messages_limit": {
    "additionalProp1": 0,
    "additionalProp2": 0,
    "additionalProp3": 0
  }
}

```

<div class="params-table">

{% include notitle [templates](../../../../_includes/params/campaigns-435f0a37c701.md#templates) %}

 
:   {% include notitle [id](../../../../_includes/params/campaigns-435f0a37c701.md#templates_id) %}
    
    {% include notitle [text](../../../../_includes/params/campaigns-435f0a37c701.md#text) %}

    {% include notitle [required_fields](../../../../_includes/params/campaigns-435f0a37c701.md#required_fields) %}

    {% include notitle [category](../../../../_includes/params/campaigns-435f0a37c701.md#category) %}

{% include notitle [gifts](../../../../_includes/params/campaigns-435f0a37c701.md#gifts) %}

 
:   {% include notitle [id](../../../../_includes/params/campaigns-435f0a37c701.md#id) %}
    
    {% include notitle [name](../../../../_includes/params/campaigns-435f0a37c701.md#gift_name) %}

    {% include notitle [image_url](../../../../_includes/params/campaigns-435f0a37c701.md#gift_image_url) %}

{% include notitle [messages_limit](../../../../_includes/params/campaigns-435f0a37c701.md#messages_limit) %}

{% include notitle [message_price_kopecks](../../../../_includes/params/campaigns-435f0a37c701.md#message_price_kopecks) %}

{% include notitle [offer_id_messages_limit](../../../../_includes/params/campaigns-435f0a37c701.md#offer_id_messages_limit) %}

</div>


## Коды ответа {#response-codes}

#|
||**Код**|**Причина**|**Описание**||
 || 200 | OK | Успешный запрос. || 
 || 400 | BAD_REQUEST | Синтаксическая ошибка в запросе. || 
 || 401 | NO_AUTH | Не удалось авторизовать пользователя по переданным данным. || 
 || 403 | CODE_AUTH_REQUIRED
PASSWORD_EXPIRED | Не удается аутентифицироваться. || 
 || 500 | INTERNAL SERVER ERROR | Внутренняя ошибка сервера. || 

|#

{% include [table-style](../../../../_includes/table-style-border-none-2a2aa0c324bf.md) %}

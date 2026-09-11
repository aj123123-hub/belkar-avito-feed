---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/dealer/chats/campaigns/list-offers.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# POST dealer/chats/campaigns/list-offers

Позволяет получить статистику по каждому офферу в групповой рассылке.

## Формат запроса {#input}

```json
{
  "campaign_id": "string",
  "sorting": {
    "sorting_field": "CREATED_TIME",
    "sorting_type": "DESCENDING"
  }
}
```

<div class="params-table">

{% include notitle [campaign_id](../../../../_includes/params/campaigns-435f0a37c701.md#campaign_id) %}

{% include notitle [sorting](../../../../_includes/params/campaigns-435f0a37c701.md#sorting) %}

 
:   {% include notitle [sorting_field](../../../../_includes/params/campaigns-435f0a37c701.md#sorting_field) %}

    {% include notitle [sorting_type](../../../../_includes/params/campaigns-435f0a37c701.md#sorting_type) %}

</div>

### Заголовки запроса {#headers}

| Заголовок  | Описание  |
| ----------- | ----------- |
| `x-dealer-id`| Идентификатор клиента. Используется для работы под учетной записью агентства.|
| `x-session-id`| Идентификатор сессии пользователя. Значение можно получить с помощью операции [POST /auth/login](../../../auth-login.md).|

## Формат ответа {#output-structure}

```json
{
  "campaign_offers": [
    {
      "campaign_id": {string},
      "offer": { модель оффера },
      "stats": {
        "campaign_id": {string},
        "messages_sent_count": {integer},
        "messages_read_count": {integer},
        "messages_ignore_count": {integer},
        "messages_contacts_count": {integer},
        "messages_chats_count": {integer},
        "messages_callback_count": {integer},
        "chats_count": {integer},
        "calls_count": {integer},
        "chats_relevant_count": {integer},
        "calls_relevant_count": {integer},
        "campaign_message_send_price_kopecks": {integer},
        "price_kopecks_per_message": {integer},
        "chats_price_kopecks": {integer},
        "calls_price_kopecks": {integer}
      }
    }
  ]
}
```

<div class="params-table">

{% include notitle [campaign_offers](../../../../_includes/params/campaigns-435f0a37c701.md#campaign_offers) %}

 
:   {% include notitle [campaign_id](../../../../_includes/params/campaigns-435f0a37c701.md#campaign_id) %}

    {% include notitle [offer](../../../../_includes/params/campaigns-435f0a37c701.md#offer) %}

    {% include notitle [stats](../../../../_includes/params/campaigns-435f0a37c701.md#stats) %}

     
    :   {% include notitle [campaign_id](../../../../_includes/params/campaigns-435f0a37c701.md#campaign_id) %}

        {% include notitle [messages_sent_count](../../../../_includes/params/campaigns-435f0a37c701.md#messages_sent_count) %}

        {% include notitle [messages_read_count](../../../../_includes/params/campaigns-435f0a37c701.md#messages_read_count) %}

        {% include notitle [messages_ignore_count](../../../../_includes/params/campaigns-435f0a37c701.md#messages_ignore_count) %}

        {% include notitle [messages_contacts_count](../../../../_includes/params/campaigns-435f0a37c701.md#messages_contacts_count) %}

        {% include notitle [messages_callback_count](../../../../_includes/params/campaigns-435f0a37c701.md#messages_callback_count) %}

        {% include notitle [chats_count](../../../../_includes/params/campaigns-435f0a37c701.md#chats_count) %}

        {% include notitle [calls_count](../../../../_includes/params/campaigns-435f0a37c701.md#calls_count) %}

        {% include notitle [chats_relevant_count](../../../../_includes/params/campaigns-435f0a37c701.md#chats_relevant_count) %}

        {% include notitle [calls_relevant_count](../../../../_includes/params/campaigns-435f0a37c701.md#calls_relevant_count) %}

        {% include notitle [campaign_message_send_price_kopecks](../../../../_includes/params/campaigns-435f0a37c701.md#campaign_message_send_price_kopecks) %}

        {% include notitle [price_kopecks_per_message](../../../../_includes/params/campaigns-435f0a37c701.md#price_kopecks_per_message) %}

        {% include notitle [chats_price_kopecks](../../../../_includes/params/campaigns-435f0a37c701.md#chats_price_kopecks) %}

        {% include notitle [calls_price_kopecks](../../../../_includes/params/campaigns-435f0a37c701.md#calls_price_kopecks) %}

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

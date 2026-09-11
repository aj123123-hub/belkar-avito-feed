---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/dealer/chats/campaigns-get.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# GET dealer/chats/campaigns

Позволяет получить последнюю рассылку по избранному для указанного объявления.

## Формат запроса {#input}

```
GET https://apiauto.ru/1.0/dealer/chats/campaigns
? [[campaign_id](*campaign_id)=<integer>]
& [[offer_id](*offer_id)=<array[string]>]
```

<div class="params-table">

{% include notitle [campaign_id](../../../_includes/params/campaigns-435f0a37c701.md#campaign_id) %}

{% include notitle [offer_id](../../../_includes/params/campaigns-435f0a37c701.md#offer_id) %}

</div>

### Заголовки запроса {#headers}

| Заголовок  | Описание  |
| ----------- | ----------- |
| `x-dealer-id`| Идентификатор клиента. Используется для работы под учетной записью агентства.|
| `x-session-id`| Идентификатор сессии пользователя. Значение можно получить с помощью операции [POST /auth/login](../../auth-login.md).|


## Формат ответа {#output-structure}

```json

{
  "campaign": {
    "id": "string",
    "campaign_type": "MANUAL",
    "campaign_status": "DRAFT",
    "multi_campaign": true,
    "all_offers_count": 0,
    "offers": [
      {модель оффера}
    ],
    "created_at": "2026-03-25T19:19:30.140Z",
    "active_from": "2026-03-25T19:19:30.140Z",
    "active_to": "2026-03-25T19:19:30.140Z",
    "send_from": "2026-03-25T19:19:30.140Z",
    "send_to": "2026-03-25T19:19:30.140Z",
    "template": {
      "id": 0,
      "text": "А ещё в подарок: {gifts}",
      "required_fields": "gifts",
      "category": "cars"
    },
    "promocode": "string",
    "promocode_valid_to": "2026-03-25T19:19:30.140Z",
    "percentage": 0,
    "kopeck": 0,
    "verba": {
      "verba": [
        {
          "id": 0,
          "name": "Шины",
          "image_url": "string"
        }
      ]
    },
    "custom": "string",
    "stats": {
      "campaign_id": "string",
      "messages_sent_count": 0,
      "messages_read_count": 0,
      "messages_ignore_count": 0,
      "messages_contacts_count": 0,
      "messages_chats_count": 0,
      "messages_callback_count": 0,
      "chats_count": 0,
      "calls_count": 0,
      "chats_relevant_count": 0,
      "calls_relevant_count": 0,
      "campaign_message_send_price_kopecks": 0,
      "price_kopecks_per_message": 0,
      "chats_price_kopecks": 0,
      "calls_price_kopecks": 0
    }
  },
  "campaign_offer": {
    "campaign_id": "string",
    "offer": {модель оффера},
    "stats": {
      "campaign_id": "string",
      "messages_sent_count": 0,
      "messages_read_count": 0,
      "messages_ignore_count": 0,
      "messages_contacts_count": 0,
      "messages_chats_count": 0,
      "messages_callback_count": 0,
      "chats_count": 0,
      "calls_count": 0,
      "chats_relevant_count": 0,
      "calls_relevant_count": 0,
      "campaign_message_send_price_kopecks": 0,
      "price_kopecks_per_message": 0,
      "chats_price_kopecks": 0,
      "calls_price_kopecks": 0
    }
  }
}

```

<div class="params-table">

{% include notitle [campaign](../../../_includes/params/campaigns-435f0a37c701.md#campaign) %}

 
:   {% include notitle [id](../../../_includes/params/campaigns-435f0a37c701.md#id) %}
    
    {% include notitle [campaign_type](../../../_includes/params/campaigns-435f0a37c701.md#campaign_type) %}

    {% include notitle [campaign_status](../../../_includes/params/campaigns-435f0a37c701.md#campaign_status) %}

    {% include notitle [multi_campaign](../../../_includes/params/campaigns-435f0a37c701.md#multi_campaign) %}

    {% include notitle [all_offers_count](../../../_includes/params/campaigns-435f0a37c701.md#all_offers_count) %}

    {% include notitle [offers](../../../_includes/params/campaigns-435f0a37c701.md#offers) %}

    {% include notitle [created_at](../../../_includes/params/campaigns-435f0a37c701.md#created_at) %}

    {% include notitle [active_from](../../../_includes/params/campaigns-435f0a37c701.md#active_from) %}

    {% include notitle [active_to](../../../_includes/params/campaigns-435f0a37c701.md#active_to) %}

    {% include notitle [send_from](../../../_includes/params/campaigns-435f0a37c701.md#send_from) %}

    {% include notitle [send_to](../../../_includes/params/campaigns-435f0a37c701.md#send_to) %}

    {% include notitle [template](../../../_includes/params/campaigns-435f0a37c701.md#template) %}
    
    {% include notitle [promocode](../../../_includes/params/campaigns-435f0a37c701.md#promocode) %}

    {% include notitle [promocode_valid_to](../../../_includes/params/campaigns-435f0a37c701.md#promocode_valid_to) %}

    {% include notitle [percentage](../../../_includes/params/campaigns-435f0a37c701.md#percentage) %}

    {% include notitle [kopeck](../../../_includes/params/campaigns-435f0a37c701.md#kopeck) %}

    {% include notitle [verba](../../../_includes/params/campaigns-435f0a37c701.md#verba) %}

    {% include notitle [custom](../../../_includes/params/campaigns-435f0a37c701.md#custom) %}

    {% include notitle [stats](../../../_includes/params/campaigns-435f0a37c701.md#stats) %}

     
    :   {% include notitle [campaign_id](../../../_includes/params/campaigns-435f0a37c701.md#stats_campaign_id) %}

        {% include notitle [messages_sent_count](../../../_includes/params/campaigns-435f0a37c701.md#messages_sent_count) %}

        {% include notitle [messages_read_count](../../../_includes/params/campaigns-435f0a37c701.md#messages_read_count) %}

        {% include notitle [messages_ignore_count](../../../_includes/params/campaigns-435f0a37c701.md#messages_ignore_count) %}

        {% include notitle [messages_contacts_count](../../../_includes/params/campaigns-435f0a37c701.md#messages_contacts_count) %}

        {% include notitle [messages_chats_count](../../../_includes/params/campaigns-435f0a37c701.md#messages_chats_count) %}

        {% include notitle [messages_callback_count](../../../_includes/params/campaigns-435f0a37c701.md#messages_callback_count) %}

        {% include notitle [chats_count](../../../_includes/params/campaigns-435f0a37c701.md#chats_count) %}

        {% include notitle [calls_count](../../../_includes/params/campaigns-435f0a37c701.md#calls_count) %}

        {% include notitle [chats_relevant_count](../../../_includes/params/campaigns-435f0a37c701.md#chats_relevant_count) %}

        {% include notitle [calls_relevant_count](../../../_includes/params/campaigns-435f0a37c701.md#calls_relevant_count) %}

        {% include notitle [campaign_message_send_price_kopecks](../../../_includes/params/campaigns-435f0a37c701.md#campaign_message_send_price_kopecks) %}

        {% include notitle [price_kopecks_per_message](../../../_includes/params/campaigns-435f0a37c701.md#price_kopecks_per_message) %}

        {% include notitle [chats_price_kopecks](../../../_includes/params/campaigns-435f0a37c701.md#chats_price_kopecks) %}

        {% include notitle [calls_price_kopecks](../../../_includes/params/campaigns-435f0a37c701.md#calls_price_kopecks) %}

    {% include notitle [campaign_offer](../../../_includes/params/campaigns-435f0a37c701.md#campaign_offer) %}

     
    :   {% include notitle [campaign_id](../../../_includes/params/campaigns-435f0a37c701.md#campaign_id) %}

        {% include notitle [offer](../../../_includes/params/campaigns-435f0a37c701.md#offer) %}

        {% include notitle [stats](../../../_includes/params/campaigns-435f0a37c701.md#stats) %}

         
        :   {% include notitle [campaign_id](../../../_includes/params/campaigns-435f0a37c701.md#stats_campaign_id) %}

            {% include notitle [messages_sent_count](../../../_includes/params/campaigns-435f0a37c701.md#messages_sent_count) %}

            {% include notitle [messages_read_count](../../../_includes/params/campaigns-435f0a37c701.md#messages_read_count) %}

            {% include notitle [messages_ignore_count](../../../_includes/params/campaigns-435f0a37c701.md#messages_ignore_count) %}

            {% include notitle [messages_contacts_count](../../../_includes/params/campaigns-435f0a37c701.md#messages_contacts_count) %}

            {% include notitle [messages_chats_count](../../../_includes/params/campaigns-435f0a37c701.md#messages_chats_count) %}

            {% include notitle [messages_callback_count](../../../_includes/params/campaigns-435f0a37c701.md#messages_callback_count) %}

            {% include notitle [chats_count](../../../_includes/params/campaigns-435f0a37c701.md#chats_count) %}

            {% include notitle [calls_count](../../../_includes/params/campaigns-435f0a37c701.md#calls_count) %}

            {% include notitle [chats_relevant_count](../../../_includes/params/campaigns-435f0a37c701.md#chats_relevant_count) %}

            {% include notitle [calls_relevant_count](../../../_includes/params/campaigns-435f0a37c701.md#calls_relevant_count) %}

            {% include notitle [campaign_message_send_price_kopecks](../../../_includes/params/campaigns-435f0a37c701.md#campaign_message_send_price_kopecks) %}

            {% include notitle [price_kopecks_per_message](../../../_includes/params/campaigns-435f0a37c701.md#price_kopecks_per_message) %}

            {% include notitle [chats_price_kopecks](../../../_includes/params/campaigns-435f0a37c701.md#chats_price_kopecks) %}

            {% include notitle [calls_price_kopecks](../../../_includes/params/campaigns-435f0a37c701.md#calls_price_kopecks) %}

</div>



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
 || 401 | NO_AUTH | Не удалось авторизовать пользователя по переданным данным. || 
 || 403 | CODE_AUTH_REQUIRED
PASSWORD_EXPIRED | Не удается аутентифицироваться. || 
 || 500 | INTERNAL SERVER ERROR | Внутренняя ошибка сервера. || 

|#

{% include [table-style](../../../_includes/table-style-border-none-2a2aa0c324bf.md) %}

[*campaign_id]: {% include notitle [campaign_id](../../../_includes/popups-00286d1be377.md#campaign_id) %}

[*offer_id]: {% include notitle [offer_id](../../../_includes/popups-00286d1be377.md#offer_id) %}

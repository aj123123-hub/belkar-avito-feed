---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/dealer/chats/campaigns-post.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# POST dealer/chats/campaigns

Позволяет создать рассылку по избранным объявлениям.

{% note warning %}

Если в личном кабинете дилера не работают чаты, отправка рассылок будет недоступна.

{% endnote %}

## Формат запроса {#input}

```

POST https://apiauto.ru/1.0/dealer/chats/campaigns

```

### Заголовки запроса {#headers}

| Заголовок  | Описание  |
| ----------- | ----------- |
| `x-session-id`| Идентификатор сессии пользователя. Значение можно получить с помощью операции [POST /auth/login](../../auth-login.md).|
|`x-authorization`| Авторизационный токен. См. подробнее [Доступ к API](../../../concepts/access.md).|

### Формат тела запроса {#structure-in}

```json
{
  "campaign_type": {string},
  "offer_ids": [ 
    {string} 
  ],
  "category": {string},
  "section": {string},
  "messages_limit": {integer},
  "promocode": {string},
  "promocode_valid_hours": {integer},
  "percentage": {integer},
  "kopeck": {integer},
  "verba": {
    "gift_ids": [
      {integer}
    ]
  },
  "custom": {string}
}

```

<div class="params-table">

{% include notitle [campaign_type](../../../_includes/params/campaigns-435f0a37c701.md#campaign_type) %}

{% include notitle [offer_ids](../../../_includes/params/campaigns-435f0a37c701.md#offer_ids) %}

{% include notitle [category](../../../_includes/params/campaigns-435f0a37c701.md#category) %}

{% include notitle [section](../../../_includes/params/campaigns-435f0a37c701.md#section) %}

{% include notitle [messages_limit](../../../_includes/params/campaigns-435f0a37c701.md#messages_limit) %}

{% include notitle [promocode](../../../_includes/params/campaigns-435f0a37c701.md#promocode) %}

{% include notitle [promocode_valid_hours](../../../_includes/params/campaigns-435f0a37c701.md#promocode_valid_hours) %}

{% note alert %}

Обязательно укажите скидку (`percentage` или `kopeck`) или подарок (`verba` или `custom`). Иначе вы не сможете отправить рассылку.

{% endnote %}

{% include notitle [percentage](../../../_includes/params/campaigns-435f0a37c701.md#percentage) %}

{% include notitle [kopeck](../../../_includes/params/campaigns-435f0a37c701.md#kopeck) %}

{% include notitle [verba](../../../_includes/params/campaigns-435f0a37c701.md#verba) %}

 
:   {% include notitle [gift_ids](../../../_includes/params/campaigns-435f0a37c701.md#gift_ids) %}

{% include notitle [custom](../../../_includes/params/campaigns-435f0a37c701.md#custom) %}

</div>

## Формат ответа {#output-structure}

```
{
  "campaign_id": {string}
}
```

<div class="params-table">

{% include notitle [campaign_id](../../../_includes/params/campaigns-435f0a37c701.md#campaign_id) %}

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

## Пример {#example-JSON}

```
{
  "campaign_id": "019ae8ab-80e4-7554-8200-ff13a4c92db4"
}
```

{% include [table-style](../../../_includes/table-style-border-none-2a2aa0c324bf.md) %}

---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/auction-cars-used-promo-campaign-activate.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# PUT /dealer/auction/cars/used/promo-campaign/{campaign_id}/activate

Позволяет запустить временно приостановленную рекламную кампанию.

## Формат запроса {#input}

```
PUT https://apiauto.ru/1.0/dealer/auction/cars/used/promo-campaign/{[campaign_id](*campaign_id)}/activate
```

<div class="params-table">

#|
||
##campaign_id##
|
{% include notitle [campaign_id](../_includes/popups-00286d1be377.md#campaign_id) %}
||
|#

</div>

### Заголовки запроса {#headers}

#|
||
**Заголовок**
|
**Описание**
||
 || `x-dealer-id` | Идентификатор клиента. Используется для работы под учетной записью агентства. || 
 || `x-session-id` | Идентификатор сессии пользователя. Значение можно получить с помощью операции [POST /auth/login](https://yandex.ru/dev/autoru/doc/ru/reference/auth-login.md). || 

|#

Общая структура ответа приведена ниже. Порядок следования элементов не гарантируется. В структуре могут присутствовать служебные параметры, которые не описаны в таблице.

## Формат ответа {#output-structure}

```json
{
  "status": {string}
}
```

<div class="params-table">

#|
||
##status##
|
Статус ответа.
||
|#

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
 || 403 | AGENT_ACCESS_FORBIDDEN | Доступ для данного пользователя запрещен. || 

|#

## Пример {#example-JSON}

> Запрос:
> 
> 
> ```http
> curl -X 'PUT' \
> 'http://apiauto.ru/1.0/dealer/auction/cars/used/promo-campaign/1/activate' \
> -H 'accept: application/json' \
> -H 'x-authorization: xxxxxxxxxxxx'
> ```
> 
> 
> Ответ:
> 
> 
> ```json
> {
>   "status": "SUCCESS"
> }
> ```

{% include [table-style](../_includes/table-style-border-none-2a2aa0c324bf.md) %}

[*campaign_id]: {% include notitle [campaign_id](../_includes/popups-00286d1be377.md#campaign_id) %}

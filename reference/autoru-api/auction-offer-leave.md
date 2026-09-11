---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/auction-offer-leave.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# POST /dealer/auction/offer/{offer_id}/leave

Выводит объявление из аукциона.

## Формат запроса {#input}

```
GET https://apiauto.ru/1.0/dealer/auction/offer/{[offer_id](*offer_id)}/leave
```

<div class="params-table">

#|
||
##offer_id##
|
{% include notitle [offer_id](../_includes/popups-00286d1be377.md#offer_id) %}
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

### Формат тела запроса {#structure-in}

```json
{
  "previous_bid": {integer}
}
```

<div class="params-table">

#|
||
##previous_bid##
|
Предыдущая ставка аукциона в копейках.
||
|#

</div>

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
 || 401 | NO_AUTH | Не удалось авторизовать пользователя по переданным данным. || 
 || 403 | AGENT_ACCESS_FORBIDDEN | Доступ для данного пользователя запрещен. || 
 || 500 | INTERNAL SERVER ERROR
UNKNOWN_ERROR | Внутренняя ошибка сервера. || 

|#

## Пример {#example-JSON}

> Запрос:
> 
> 
> ```http
> curl -X POST
> --header 'x-session-id: 14090654|1622...' 
> --header 'x-dealer-id: 16269' 
> -d '{ \ 
>  "previous_bid": 210000
>  }' 'https://apiauto.ru/1.0/dealer/auction/offer/{offer_id}/leave'
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

[*offer_id]: {% include notitle [offer_id](../_includes/popups-00286d1be377.md#offer_id) %}


---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/auction-offer-current-state.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# GET /dealer/auction/offer/{offer_id}/current_state

Возвращает состояние аукциона по объявлению.

## Формат запроса {#input}

```
GET https://apiauto.ru/1.0/dealer/auction/offer/{[offer_id](*offer_id)}/current-state
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

Общая структура ответа приведена ниже. Порядок следования элементов не гарантируется. В структуре могут присутствовать служебные параметры, которые не описаны в таблице.

## Формат ответа {#output-structure}

```json
{
  "state": {
    "current_bid": {integer},
    "base_price": {integer},
    "min_bid": {integer},
    "max_bid": {integer},
    "one_step": {integer},
    "limit_exceeded": {boolean}
  },
  "segments": [
    {
      "percent": {integer},
      "min_bid": {integer},
      "max_bid": {integer},
      "current": {boolean}
    }
  ]
}
```

<div class="params-table">

{% include notitle [state](../_includes/params/auction-offer-current-state-fb4175c1a94e.md#state) %}

 
:   {% include notitle [current_bid](../_includes/params/auction-offer-current-state-fb4175c1a94e.md#current_bid) %}

    {% include notitle [base_price](../_includes/params/auction-offer-current-state-fb4175c1a94e.md#base_price) %}

    {% include notitle [min_bid](../_includes/params/auction-offer-current-state-fb4175c1a94e.md#min_bid) %}

    {% include notitle [max_bid](../_includes/params/auction-offer-current-state-fb4175c1a94e.md#max_bid) %}

    {% include notitle [one_step](../_includes/params/auction-offer-current-state-fb4175c1a94e.md#one_step) %}

    {% include notitle [limit_exceeded](../_includes/params/auction-offer-current-state-fb4175c1a94e.md#limit_exceeded) %}

{% include notitle [segments](../_includes/params/auction-offer-current-state-fb4175c1a94e.md#segments) %}

 
:   {% include notitle [percent](../_includes/params/auction-offer-current-state-fb4175c1a94e.md#percent) %}

    {% include notitle [min_bid](../_includes/params/auction-offer-current-state-fb4175c1a94e.md#min_bid_2) %}

    {% include notitle [max_bid](../_includes/params/auction-offer-current-state-fb4175c1a94e.md#max_bid_2) %}

    {% include notitle [current](../_includes/params/auction-offer-current-state-fb4175c1a94e.md#current) %}

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
 || 403 | CUSTOMER_ACCESS_FORBIDDEN | Доступ для данного пользователя запрещен. || 
 || 500 | INTERNAL SERVER ERROR | Внутренняя ошибка сервера. || 

|#

## Пример {#example-JSON}

> Запрос:
> 
> 
> ```http
> curl -i -X GET
> --header 'Accept: application/json'
> --header 'x-session-id: 14090654|1622...' 
> 'https://apiauto.ru/1.0/dealer/auction/offer/{offer_id}/current-state'
> ```
> 
> 
> Ответ:
> 
> 
> ```json
> {
>   "state": {
>     "current_bid": 100000,
>     "base_price": 100,
>     "min_bid": 10000,
>     "max_bid": 1290000,
>     "one_step": 10000,
>     "limit_exceeded": false
>   },
>   "segments": [
>     {
>       "percent": 5,
>       "min_bid": 100,
>       "max_bid": 50000,
>       "current": true
>     }
>   ]
> }      
> ```

{% include [table-style](../_includes/table-style-border-none-2a2aa0c324bf.md) %}

[*offer_id]: {% include notitle [offer_id](../_includes/popups-00286d1be377.md#offer_id) %}



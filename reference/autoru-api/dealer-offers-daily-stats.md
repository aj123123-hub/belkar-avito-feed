---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/dealer-offers-daily-stats.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# GET /dealer/offers-daily-stats

Возвращает статистику показов объявлений с разбиением по дням.

## Формат запроса {#input}

```
GET https://apiauto.ru/1.0/dealer/offers-daily-stats
? [from_date](*from_date)=<date>
? [[to_date](*to_date)=<date>]
```
<div class="params-table">

{% include notitle [from_date](../_includes/params/dealer-offers-daily-stats-8d19fd08bd32.md#from_date) %}

{% include notitle [to_date](../_includes/params/dealer-offers-daily-stats-8d19fd08bd32.md#to_date) %}

</div>

{% include notitle [req](../_includes/popups-00286d1be377.md#req) %}

### Заголовки запроса {#headers}

#|
|| **Заголовок** | **Описание** ||
|| `x-dealer-id` | Идентификатор клиента. Используется для работы под учетной записью агентства. ||
|| `x-session-id` | Идентификатор сессии пользователя. Значение можно получить с помощью операции [POST /auth/login](https://yandex.ru/dev/autoru/doc/ru/reference/auth-login.md). ||
|#

Общая структура ответа приведена ниже. Порядок следования элементов не гарантируется. В структуре могут присутствовать служебные параметры, которые не описаны в таблице.

## Формат ответа {#output-structure}

```json
{
  "days": [
    {
      "date": {string},
      "card_view": {integer},
      "phone_show": {integer}
    }
  ],
  "error": {string},
  "status": {string}
}          
```

<div class="params-table">

{% include notitle [days](../_includes/params/dealer-offers-daily-stats-8d19fd08bd32.md#days) %}

 
:   {% include notitle [date](../_includes/params/dealer-offers-daily-stats-8d19fd08bd32.md#date) %}

    {% include notitle [card_view](../_includes/params/dealer-offers-daily-stats-8d19fd08bd32.md#card_view) %}

    {% include notitle [phone_show](../_includes/params/dealer-offers-daily-stats-8d19fd08bd32.md#phone_show) %}

{% include notitle [error](../_includes/params/dealer-offers-daily-stats-8d19fd08bd32.md#error) %}

{% include notitle [status](../_includes/params/dealer-offers-daily-stats-8d19fd08bd32.md#status) %}

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

 || 500 | INTERNAL SERVER ERROR | Внутренняя ошибка сервера. || 
||
|#

## Пример {#example-JSON}

> Запрос:
> 
> 
> ```http
> curl -i -X GET 'https://apiauto.ru/1.0/dealer/offers-daily-stats' -H 'x-authorization: 2dtrer432...' -H 'x-session-id: 112_aoR02Tpv...'
> ```
> 
> 
> Ответ:
> 
> 
> ```json
> HTTP/1.1 200 OK
> Server: nginx
> Date: Fri, 15 Jun 2018 13:30:59 GMT
> Content-Type: application/json
> Connection: keep-alive
>                     
> {
>   "days": [
>     {
>       "date": "2019-03-13",
>       "card_view": 0,
>       "phone_show": 0
>     }
>   ],
>   "status": "SUCCESS"
> }         
> ```


{% include [table-style](../_includes/table-style-border-none-2a2aa0c324bf.md) %}


[*from_date]: {% include notitle [from_date](../_includes/popups-00286d1be377.md#from_date) %}

[*to_date]: {% include notitle [to_date](../_includes/popups-00286d1be377.md#to_date) %}

[*req]: {% include notitle [req](../_includes/popups-00286d1be377.md#req) %}

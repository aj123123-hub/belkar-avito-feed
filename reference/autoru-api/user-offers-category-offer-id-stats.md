---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/user-offers-category-offer-id-stats.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# GET /user/offers/{category}/{offerID}/stats

Возвращает статистику просмотров по указанному объявлению.

## Формат запроса {#input}

```
POST https://apiauto.ru/1.0/user/offers/{[category](*category)}/{[offerID](*offerID)}/stats
? [from](*from)=<string>
& [to](*to)=<string>
```

<div class="params-table">

#|
||
##category##
|
Название категории ТС. Допустимые значения:

- `cars` — легковые автомобили;
- `moto` — мототранспорт;
- `trucks` — коммерческий транспорт;
- `all` — все категории ТС.

||
|#

#|
|| ##offerID## | Идентификатор объявления, для которого необходимо получить статистику просмотров. ||
|#

#|
|| ##from##[*](*req) | Дата начала отсчета в формате YYYY-MM-DDдля получения статистики по дням. ||
|#

#|
|| ##to##[*](*req) | Дата окончания отсчета в формате YYYY-MM-DDдля получения статистики по дням. ||
|#


</div>

\* Обязательный параметр

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
  "items": [
    {
      "offer_id": "{string}",
      "counters": [
        {
          "date": "{string}",
          "views": {integer},
          "phone_views": {integer}
        }
      ]
    }
  ],
  "status": "{string}"
}
```

<div class="params-table">

{% include notitle [items](../_includes/params/user-offers-category-offer-id-stats-55b54a275354.md#items) %}

 
:   {% include notitle [offer_id](../_includes/params/user-offers-category-offer-id-stats-55b54a275354.md#offer_id) %}

    {% include notitle [counters](../_includes/params/user-offers-category-offer-id-stats-55b54a275354.md#counters) %}
    
     
    :   {% include notitle [date](../_includes/params/user-offers-category-offer-id-stats-55b54a275354.md#date) %}

        {% include notitle [views](../_includes/params/user-offers-category-offer-id-stats-55b54a275354.md#views) %}

        {% include notitle [phone_views](../_includes/params/user-offers-category-offer-id-stats-55b54a275354.md#phone_views) %}

{% include notitle [status](../_includes/params/user-offers-category-offer-id-stats-55b54a275354.md#status) %}

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
 || 404 | OFFER_NOT_FOUND | Объявление не найдено. || 
 || 500 | INTERNAL SERVER ERROR | Внутренняя ошибка сервера. || 

|#

## Пример {#example-JSON}

> Запрос:
> 
> 
> ```http
> curl -i -X GET 'https://apiauto.ru/1.0/user/offers/trucks/15304953-96189649/stats?from=2018-06-25&to=2018-06-30' -H 'x-authorization: 2dtrer432...' -H 'Accept: application/json' -H 'x-session-id: 112_aoR02Tpv...'
> ```
> 
> 
> Ответ:
> 
> 
> ```json
> HTTP/1.1 200 OK
> Server: nginx
> Date: Tue, 10 Jul 2018 15:19:41 GMT
> Content-Type: application/json
> Connection: keep-alive
>                     
> {
>   "items": [
>     {
>       "offer_id": "15304953-96189649",
>       "counters": [
>         {
>           "date": "2018-06-25",
>           "views": 0,
>           "phone_views": 0,
>           "phone_calls": 0
>         },
>         {
>           "date": "2018-06-26",
>           "views": 0,
>           "phone_views": 0,
>           "phone_calls": 0
>         },
>         {
>           "date": "2018-06-27",
>           "views": 0,
>           "phone_views": 0,
>           "phone_calls": 0
>         },
>         {
>           "date": "2018-06-28",
>           "views": 1,
>           "phone_views": 0,
>           "phone_calls": 0
>         },
>         {
>           "date": "2018-06-29",
>           "views": 2,
>           "phone_views": 0,
>           "phone_calls": 0
>         },
>         {
>           "date": "2018-06-30",
>           "views": 0,
>           "phone_views": 0,
>           "phone_calls": 0
>         }
>       ]
>     }
>   ]
> }
> ```

{% include [table-style](../_includes/table-style-border-none-2a2aa0c324bf.md) %}

[*category]: {% include notitle [req](../_includes/popups-00286d1be377.md#category) %}

[*offerID]: Идентификатор объявления, для которого необходимо получить статистику просмотров.

[*req]: {% include notitle [req](../_includes/popups-00286d1be377.md#req) %}

[*from]: {% include notitle [from](../_includes/popups-00286d1be377.md#from-date) %}

[*to]: {% include notitle [to](../_includes/popups-00286d1be377.md#to-date) %}


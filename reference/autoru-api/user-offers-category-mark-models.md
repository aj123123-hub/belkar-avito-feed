---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/user-offers-category-mark-models.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# GET /user/offers/{category}/mark-models

Возвращает список марок/моделей и количество объявлений для каждой марки/модели, которые удовлетворяют заданным условиям.

## Формат запроса {#input}

```
GET https://apiauto.ru/1.0/user/offers/{[category](*category)}/mark-models
? [[truck_category](*truck_category)=<string>]
& [[moto_category](*moto_category)=<string>]
& [[status](*status)=<array[string]>]
& [[service](*service)=<array[string]>]
& [[vin](*vin)=<array[string]>]
& [[mark_model](*mark_model)=<array[string]>]
& [[price_from](*price_from)=<integer>]
& [[price_to](*price_to)=<integer>]
& [[section](*section)=<string>]
& [[create_date_from](*create_date_from)=<string>]
& [[create_date_to](*create_date_to)=<string>]
& [[no_active_services](*no_active_services)=<boolean>]
& [[ban_reason](*ban_reason)=<array[string]>]
```

<div class="params-table">

{% include notitle [category](../_includes/params/user-offers-category-request-550dd7264ccb.md#category) %}

{% include notitle [truck_category](../_includes/params/user-offers-category-request-550dd7264ccb.md#truck_category) %}

{% include notitle [moto_category](../_includes/params/user-offers-category-request-550dd7264ccb.md#moto_category) %}

{% include notitle [status](../_includes/params/user-offers-category-request-550dd7264ccb.md#status) %}

{% include notitle [service](../_includes/params/user-offers-category-request-550dd7264ccb.md#service) %}

{% include notitle [vin](../_includes/params/user-offers-category-request-550dd7264ccb.md#vin) %}

{% include notitle [mark_model](../_includes/params/user-offers-category-request-550dd7264ccb.md#mark_model) %}

{% include notitle [price_from](../_includes/params/user-offers-category-request-550dd7264ccb.md#price_from) %}

{% include notitle [price_to](../_includes/params/user-offers-category-request-550dd7264ccb.md#price_to) %}

{% include notitle [section](../_includes/params/user-offers-category-request-550dd7264ccb.md#section) %}

{% include notitle [create_date_from](../_includes/params/user-offers-category-request-550dd7264ccb.md#create_date_from) %}

{% include notitle [create_date_to](../_includes/params/user-offers-category-request-550dd7264ccb.md#create_date_to) %}

{% include notitle [no_active_services](../_includes/params/user-offers-category-request-550dd7264ccb.md#no_active_services) %}

{% include notitle [ban_reason](../_includes/params/user-offers-category-request-550dd7264ccb.md#ban_reason) %}

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
  "mark_models": [
    {
      "mark": "{string}",
      "models": [
        {
          "model": "{string}",
          "offers_count": {integer},
          "human_name": "{string}",
          "category": "{string}"
        }
      ],
      "offers_count": {integer},
      "human_name": "{string}"
    },
    {
      "mark": "{string}",
      "models": [
        {
          "model": "{string}",
          "offers_count": {integer},
          "human_name": "{string}",
          "category": "{string}"
        }
      ],
      "offers_count": {integer},
      "human_name": "{string}"
    }
  ],
  "status": "{string}"
}
```

<div class="params-table">

{% include notitle [mark_models](../_includes/params/user-offers-category-mark-models-043d9a7514f5.md#mark_models) %}

 
:   {% include notitle [mark](../_includes/params/user-offers-category-mark-models-043d9a7514f5.md#mark) %}

    {% include notitle [human_name](../_includes/params/user-offers-category-mark-models-043d9a7514f5.md#human_name) %}

    {% include notitle [models](../_includes/params/user-offers-category-mark-models-043d9a7514f5.md#models) %}
    
     
    :   {% include notitle [model](../_includes/params/user-offers-category-mark-models-043d9a7514f5.md#model) %}

        {% include notitle [human_name](../_includes/params/user-offers-category-mark-models-043d9a7514f5.md#human_name) %}

        {% include notitle [category](../_includes/params/user-offers-category-mark-models-043d9a7514f5.md#category) %}

        {% include notitle [offers_count](../_includes/params/user-offers-category-mark-models-043d9a7514f5.md#offers_count) %}

    {% include notitle [offers_count](../_includes/params/user-offers-category-mark-models-043d9a7514f5.md#offers_count) %}

{% include notitle [status](../_includes/params/user-offers-category-mark-models-043d9a7514f5.md#status) %}

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

|#

## Пример {#example-JSON}

> Запрос:
> 
> 
> ```http
> curl -i -X GET 'https://apiauto.ru/1.0/user/offers/moto/mark-models?create_date_from=2015-07-08T11%3A29%3A16%2B03%3A00&create_date_to=2018-07-08T11%3A29%3A16%2B03%3A00&no_active_services=false' -H 'x-authorization: 2dtr...er432' -H 'x-session-id: 112_ao...R02Tpv'
> ```
> 
> 
> Ответ:
> 
> 
> ```json
> HTTP/1.1 200 OK
> Server: nginx
> Date: Fri, 12 Jul 2018 13:30:59 GMT
> Content-Type: application/json
> Connection: keep-alive
> 
> {
>   "mark_models": [
>     {
>       "mark": "BULTACO",
>       "models": [
>         {
>           "model": "ASTRO_50",
>           "offers_count": 1,
>           "human_name": "Astro 50",
>           "category": "MOTO"
>         }
>       ],
>       "offers_count": 1,
>       "human_name": "Bultaco"
>     },
>     {
>       "mark": "BMW",
>       "models": [
>         {
>           "model": "F_800_ST",
>           "offers_count": 1,
>           "human_name": "F 800 ST",
>           "category": "MOTO"
>         }
>       ],
>       "offers_count": 1,
>       "human_name": "BMW"
>     },
>     {
>       "mark": "APRILIA",
>       "models": [
>         {
>           "model": "DORSODURO",
>           "offers_count": 1,
>           "human_name": "Dorsoduro 750",
>           "category": "MOTO"
>         }
>       ],
>       "offers_count": 1,
>       "human_name": "Aprilia"
>     }
>   ],
>   "status": "SUCCESS"
> }
> ```

{% include [table-style](../_includes/table-style-border-none-2a2aa0c324bf.md) %}

[*category]: {% include notitle [category](../_includes/popups-00286d1be377.md#category) %}

[*truck_category]: {% include notitle [truck_category](../_includes/popups-00286d1be377.md#truck_category) %}

[*moto_category]: {% include notitle [moto_category](../_includes/popups-00286d1be377.md#moto_category) %}

[*status]: {% include notitle [status](../_includes/popups-00286d1be377.md#status) %}

[*service]: {% include notitle [service](../_includes/popups-00286d1be377.md#service) %}

[*vin]: {% include notitle [vin](../_includes/popups-00286d1be377.md#vin) %}

[*mark_model]: {% include notitle [mark_model](../_includes/popups-00286d1be377.md#mark_model) %}

[*price_from]: {% include notitle [price_from](../_includes/popups-00286d1be377.md#price_from-description) %}

[*price_to]: {% include notitle [price_to](../_includes/popups-00286d1be377.md#price_to-description) %}

[*section]: {% include notitle [section](../_includes/popups-00286d1be377.md#section) %}

[*create_date_from]: {% include notitle [create_date_from](../_includes/popups-00286d1be377.md#create_date_from) %}

[*create_date_to]: {% include notitle [create_date_to](../_includes/popups-00286d1be377.md#create_date_to) %}

[*no_active_services]: {% include notitle [no_active_services](../_includes/popups-00286d1be377.md#no_active_services) %}

[*ban_reason]: {% include notitle [ban_reason](../_includes/popups-00286d1be377.md#ban_reason) %}



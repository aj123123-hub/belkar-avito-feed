---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/auction-cars-used-promo-campaign-put.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# PUT /dealer/auction/cars/used/promo-campaign/{campaign_id}

Позволяет изменить параметры рекламной кампании.

## Формат запроса {#input}

```
PUT https://apiauto.ru/1.0/dealer/auction/cars/used/promo-campaign/{[campaign_id](*campaign_id)}
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

### Формат тела запроса {#structure-in}

```json
{
  "promo_campaign_params": {
    "name": "{string}",
    "period": {
      "from": "date",
      "to": "date"
    },
    "filters": {
      "in_stock": "{string}",
      "year_from": {integer},
      "year_to": {integer},
      "price_from": {integer},
      "price_to": {integer},
      "catalog_filter": [
        {
          "mark": "{string}",
          "model": "{string}",
          "generation": {string},
        }
      ],
      "vin_codes": [
        "{string}"
      ],
      "vin_report_statuses": [
        "{string}"
      ],
    },
    "max_offer_daily_calls": {integer},
    "bidding_algorithm": {
      "max_position_for_price": {
        "max_bid": {integer}
      }
    },
    "description": "{string}",
    "days_on_stock": {
      "from": {integer},
      "to": {integer}
    },
    "days_without_calls": {
      "from": {integer},
      "to": {integer}
    }
  }
}
```

<div class="params-table">

{% include notitle [promo_campaign_params](../_includes/params/auction-cars-used-promo-campaign-put-0874d0e8450c.md#promo_campaign_params) %}

{% include notitle [name](../_includes/params/auction-cars-used-promo-campaign-put-0874d0e8450c.md#name) %}

{% include notitle [period](../_includes/params/auction-cars-used-promo-campaign-put-0874d0e8450c.md#period) %}

{% include notitle [filters](../_includes/params/auction-cars-used-promo-campaign-put-0874d0e8450c.md#filters) %}

 
:   {% include notitle [in_stock](../_includes/params/auction-cars-used-promo-campaign-put-0874d0e8450c.md#in_stock) %}

    {% include notitle [year_from](../_includes/params/auction-cars-used-promo-campaign-put-0874d0e8450c.md#year_from) %}

    {% include notitle [year_to](../_includes/params/auction-cars-used-promo-campaign-put-0874d0e8450c.md#year_to) %}

    {% include notitle [price_from](../_includes/params/auction-cars-used-promo-campaign-put-0874d0e8450c.md#price_from) %}

    {% include notitle [price_to](../_includes/params/auction-cars-used-promo-campaign-put-0874d0e8450c.md#price_to) %}

    {% include notitle [catalog_filter](../_includes/params/auction-cars-used-promo-campaign-put-0874d0e8450c.md#catalog_filter) %}

     
    :   {% include notitle [mark](../_includes/params/auction-cars-used-promo-campaign-put-0874d0e8450c.md#mark) %}

        {% include notitle [model](../_includes/params/auction-cars-used-promo-campaign-put-0874d0e8450c.md#model) %}

        {% include notitle [generation](../_includes/params/auction-cars-used-promo-campaign-put-0874d0e8450c.md#generation) %}

    {% include notitle [vin_codes](../_includes/params/auction-cars-used-promo-campaign-put-0874d0e8450c.md#vin_codes) %}

    {% include notitle [vin_report_statuses](../_includes/params/auction-cars-used-promo-campaign-put-0874d0e8450c.md#vin_report_statuses) %}

{% include notitle [max_offer_daily_calls](../_includes/params/auction-cars-used-promo-campaign-put-0874d0e8450c.md#max_offer_daily_calls) %}

{% include notitle [bidding_algorithm](../_includes/params/auction-cars-used-promo-campaign-put-0874d0e8450c.md#bidding_algorithm) %}

 
:   {% include notitle [max_position_for_price](../_includes/params/auction-cars-used-promo-campaign-put-0874d0e8450c.md#max_position_for_price) %}

    {% include notitle [max_bid](../_includes/params/auction-cars-used-promo-campaign-put-0874d0e8450c.md#max_bid) %}

{% include notitle [status](../_includes/params/auction-cars-used-promo-campaign-put-0874d0e8450c.md#status) %}

{% include notitle [offers_count](../_includes/params/auction-cars-used-promo-campaign-put-0874d0e8450c.md#offers_count) %}

{% include notitle [description](../_includes/params/auction-cars-used-promo-campaign-put-0874d0e8450c.md#description) %}

{% include notitle [change_at](../_includes/params/auction-cars-used-promo-campaign-put-0874d0e8450c.md#change_at) %}

{% include notitle [days_on_stock](../_includes/params/auction-cars-used-promo-campaign-put-0874d0e8450c.md#days_on_stock) %}

 
:   {% include notitle [from](../_includes/params/auction-cars-used-promo-campaign-put-0874d0e8450c.md#from) %}

    {% include notitle [to](../_includes/params/auction-cars-used-promo-campaign-put-0874d0e8450c.md#to) %}

{% include notitle [days_without_calls](../_includes/params/auction-cars-used-promo-campaign-put-0874d0e8450c.md#days_without_calls) %}

 
:   {% include notitle [from](../_includes/params/auction-cars-used-promo-campaign-put-0874d0e8450c.md#from) %}

    {% include notitle [to](../_includes/params/auction-cars-used-promo-campaign-put-0874d0e8450c.md#to) %}

</div>

Общая структура ответа приведена ниже. Порядок следования элементов не гарантируется. В структуре могут присутствовать служебные параметры, которые не описаны в таблице.

## Формат ответа {#output-structure}

```json
{
  "campaign": {
  "id": {string},
  "name": "{string}",
    "period": {
      "from": "date",
      "to": "date"
    },
    "filters": {
      "in_stock": "{string}",
      "year_from": {integer},
      "year_to": {integer},
      "price_from": {integer},
      "price_to": {integer},
      "catalog_filter": [
        {
          "mark": "{string}",
          "model": "{string}",
          "generation": {string},
      "vin_codes": [
        "{string}"
      ],
      "vin_report_statuses": [
        "{string}"
      ],
    },
    "max_offer_daily_calls": {integer},
    "bidding_algorithm": {
      "max_position_for_price": {
        "max_bid": {integer}
      }
    },
    "status": "{string}",
    "market_indicator": {
      "ordered_segments": [
        {
          "offers_count": {integer}
        }
      ]
    },
    "description": "{string}",
    "change_at": "date",
    "days_on_stock": {
      "from": {integer},
      "to": {integer}
    },
    "days_without_calls": {
      "from": {integer},
      "to": {integer}
    }
  }
}
```

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
> 'http://apiauto.ru/1.0/dealer/auction/cars/used/promo-campaign/1' \
> -H 'accept: application/json' \
> -H 'x-authorization: xxxxxxxxxxxx' \
> -H 'Content-Type: application/json' \
> -d '
> {
>   "promo_campaign_params": {
>     "name": "string",
>     "period": {
>       "from": "2022-09-01T11:29:55.030Z",
>       "to": "2022-09-01T11:29:55.030Z"
>     },
>     "filters": {
>       "in_stock": "ANY_STOCK",
>       "year_from": 0,
>       "year_to": 0,
>       "price_from": 0,
>       "price_to": 0,
>       "catalog_filter": [
>         {
>           "mark": "BMW",
>           "model": "X1",
>           "generation": 8246645,
>         }
>       ],
>       "vin_codes": [
>         "string"
>       ],
>       "vin_report_statuses": [
>         "CHECKED"
>       ],
>     },
>     "max_offer_daily_calls": 0,
>     "bidding_algorithm": {
>       "max_position_for_price": {
>         "max_bid": 0
>       }
>     },
>     "description": "string",
>     "days_on_stock": {
>       "from": 0,
>       "to": 0
>     },
>     "days_without_calls": {
>       "from": 0,
>       "to": 0
>     }
>   }
> }
> ```
> 
> 
> Ответ:
> 
> 
> ```json
> {
>   "campaign": {
>     "id": 0,
>     "name": "string",
>     "period": {
>       "from": "2022-09-01T11:31:06.049Z",
>       "to": "2022-09-01T11:31:06.049Z"
>     },
>     "filters": {
>       "in_stock": "ANY_STOCK",
>       "year_from": 0,
>       "year_to": 0,
>       "price_from": 0,
>       "price_to": 0,
>       "catalog_filter": [
>         {
>           "mark": "BMW",
>           "model": "X1",
>           "generation": 8246645,
>         }
>       ],
>       "vin_codes": [
>         "string"
>       ],
>       "vin_report_statuses": [
>         "CHECKED"
>       ],
>     },
>     "max_offer_daily_calls": 0,
>     "bidding_algorithm": {
>       "max_position_for_price": {
>         "max_bid": 0
>       }
>     },
>     "status": "ACTIVE",
>     "market_indicator": {
>       "ordered_segments": [
>         {
>           "offers_count": 0
>         }
>       ]
>     },
>     "description": "string",
>     "change_at": "date",
>     "days_on_stock": {
>       "from": 0,
>       "to": 0
>     },
>     "days_without_calls": {
>       "from": 0,
>       "to": 0
>     }
>   }
> }
> ```

{% include [table-style](../_includes/table-style-border-none-2a2aa0c324bf.md) %}

[*campaign_id]: {% include notitle [campaign_id](../_includes/popups-00286d1be377.md#campaign_id) %}

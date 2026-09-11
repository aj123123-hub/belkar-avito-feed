---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/auction-current-state.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# GET /dealer/auction/current-state

Возвращает аукционы дилера.

## Формат запроса {#input}

```
GET https://apiauto.ru/1.0/dealer/auction/current-state
```

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
  "states": [
    {
      "context": {
        "mark_code": "{string}",
        "mark_ru": "{string}",
        "mark_name": "{string}",
        "model_code": "{string}",
        "model_ru": "{string}",
        "model_name": "{string}",
        "region_id": "{string}"
      },
      "base_price": "{string}",
      "current_bid": "{string}",
      "one_step": "{string}",
      "min_bid": "{string}",
      "competitive_bids": [
        {
          "bid": "{string}",
          "competitors": "{string}"
        }
      ],
      "range_steps": [
        {
          "bid_from": {
            "kopecks": "{string}"
          },
          "bid_to": {
            "kopecks": "{string}"
          },
          "step_price": "{string}"
        }
      ]
    }
  ]
}

```

<div class="params-table">

{% include notitle [states](../_includes/params/auction-current-state-d50fa0362bd2.md#states) %}

 
:   {% include notitle [context](../_includes/params/auction-current-state-d50fa0362bd2.md#context) %}
    
     
    :   {% include notitle [mark_code](../_includes/params/auction-current-state-d50fa0362bd2.md#mark_code) %}

        {% include notitle [mark_ru](../_includes/params/auction-current-state-d50fa0362bd2.md#mark_ru) %}

        {% include notitle [mark_name](../_includes/params/auction-current-state-d50fa0362bd2.md#mark_name) %}

        {% include notitle [model_code](../_includes/params/auction-current-state-d50fa0362bd2.md#model_code) %}

        {% include notitle [model_ru](../_includes/params/auction-current-state-d50fa0362bd2.md#model_ru) %}

        {% include notitle [model_name](../_includes/params/auction-current-state-d50fa0362bd2.md#model_name) %}

        {% include notitle [region_id](../_includes/params/auction-current-state-d50fa0362bd2.md#region_id) %}

    {% include notitle [base_price](../_includes/params/auction-current-state-d50fa0362bd2.md#base_price) %}

    {% include notitle [current_bid](../_includes/params/auction-current-state-d50fa0362bd2.md#current_bid) %}

    {% include notitle [one_step](../_includes/params/auction-current-state-d50fa0362bd2.md#one_step) %}

    {% include notitle [min_bid](../_includes/params/auction-current-state-d50fa0362bd2.md#min_bid) %}

    {% include notitle [competitive_bids](../_includes/params/auction-current-state-d50fa0362bd2.md#competitive_bids) %}

     
    :   {% include notitle [bid](../_includes/params/auction-current-state-d50fa0362bd2.md#bid) %}

        {% include notitle [competitors](../_includes/params/auction-current-state-d50fa0362bd2.md#competitors) %}

    {% include notitle [range_steps](../_includes/params/auction-current-state-d50fa0362bd2.md#range_steps) %}

     
    :   {% include notitle [bid_from](../_includes/params/auction-current-state-d50fa0362bd2.md#bid_from) %}

        {% include notitle [bid_to](../_includes/params/auction-current-state-d50fa0362bd2.md#bid_to) %}

        {% include notitle [step_price](../_includes/params/auction-current-state-d50fa0362bd2.md#step_price) %}
  
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
> 'https://apiauto.ru/1.0/dealer/auction/current-state'
> ```
> 
> 
> Ответ:
> 
> ```json
>{
>  "states": [
>      {
>          "context": {
>              "mark_code": "CADILLAC",
>              "mark_ru": "Кадиллак",
>              "mark_name": "Cadillac",
>              "model_code": "SRX",
>              "model_ru": "срх",
>              "model_name": "srx",
>              "region_id": "1"
>          },
>          "base_price": "450000",
>          "one_step": "10000",
>          "min_bid": "470000",
>          "range_steps": [
>              {
>                  "bid_from": {
>                      "kopecks": "0"
>                  },
>                  "step_price": "10000"
>              }
>          ]
>      },
>      {
>          "context": {
>              "mark_code": "CHERY",
>              "mark_ru": "Чери",
>              "mark_name": "Chery",
>              "model_code": "BONUS",
>              "model_ru": "Бонус",
>              "model_name": "Bonus",
>              "region_id": "1"
>          },
>          "base_price": "200000",
>          "current_bid": "260000",
>          "one_step": "10000",
>          "min_bid": "220000",
>          "competitive_bids": [
>              {
>                  "bid": "200400",
>                  "competitors": "1"
>              }
>          ],
>          "range_steps": [
>              {
>                  "bid_from": {
>                      "kopecks": "0"
>                  },
>                  "bid_to": {
>                      "kopecks": "1490000"
>                  },
>                  "step_price": "10000"
>              },
>              {
>                  "bid_from": {
>                      "kopecks": "1500000"
>                  },
>                  "step_price": "300000"
>              }
>          ]
>      }
>  ]
>}
>```


{% include [table-style](../_includes/table-style-border-none-2a2aa0c324bf.md) %}

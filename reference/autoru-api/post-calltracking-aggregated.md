---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/post-calltracking-aggregated.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# POST /calltracking/aggregated

Возвращает статистику звонков дилера с разбиением по дням.

## Формат запроса {#input}

```
POST https://apiauto.ru/1.0/calltracking/aggregated
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

### Формат тела запроса {#structure-in}

```json
{
  "filter": {
    "period": {
      "from": {string},
      "to": {string}
    },
    "targets": {string},
    "results": {string},
    "callbacks": {string},
    "unique": {string},
    "caller_phones": {
      "raw": {string}
    },
    "callee_phones": {
      "raw": {string}
    },
    "category": [
      {string}
    ],
    "section": [
      {string}
    ],
    "offer_id": [
      {string}
    ],
    "vin_code": [
      {string}
    ],
    "year": {
      "from": {integer},
      "to": {integer}
    },
    "price": {
      "from": {integer},
      "to": {integer}
    },
    "cars_filter": [
      {
        "mark": {string},
        "model": {string},
        "super_gen": {string}
      }
    ],
    "body_type": [
      {string}
    ],
    "transmission": [
      {string}
    ],
    "tags": [
      {string}
    ]
  }
}
```

<div class="params-table">

{% include notitle [filter](../_includes/params/calltracking-response-d1eb571bec79.md#filter) %}

 
:   {% include notitle [period](../_includes/params/calltracking-response-d1eb571bec79.md#period) %}
    
     
    :   {% include notitle [from](../_includes/params/calltracking-response-d1eb571bec79.md#filter_from) %}

        {% include notitle [to](../_includes/params/calltracking-response-d1eb571bec79.md#filter_to) %}

    {% include notitle [targets](../_includes/params/calltracking-response-d1eb571bec79.md#targets) %}

    {% include notitle [results](../_includes/params/calltracking-response-d1eb571bec79.md#results) %}

    {% include notitle [callbacks](../_includes/params/calltracking-response-d1eb571bec79.md#callbacks) %}

    {% include notitle [unique](../_includes/params/calltracking-response-d1eb571bec79.md#unique) %}

    {% include notitle [caller_phones](../_includes/params/calltracking-response-d1eb571bec79.md#caller_phones) %}
    
     
    :   {% include notitle [raw](../_includes/params/calltracking-response-d1eb571bec79.md#raw) %}

    {% include notitle [callee_phones](../_includes/params/calltracking-response-d1eb571bec79.md#callee_phones) %}
    
     
    :   {% include notitle [raw](../_includes/params/calltracking-response-d1eb571bec79.md#raw) %}

    {% include notitle [category](../_includes/params/calltracking-response-d1eb571bec79.md#category) %}

    {% include notitle [section](../_includes/params/calltracking-response-d1eb571bec79.md#section) %}

    {% include notitle [offer_id](../_includes/params/calltracking-response-d1eb571bec79.md#offer_id) %}

    {% include notitle [vin_code](../_includes/params/calltracking-response-d1eb571bec79.md#vin_code) %}

    {% include notitle [year](../_includes/params/calltracking-response-d1eb571bec79.md#filters_year) %}
    
     
    :   {% include notitle [from](../_includes/params/calltracking-response-d1eb571bec79.md#filters_from) %}

        {% include notitle [to](../_includes/params/calltracking-response-d1eb571bec79.md#filters_to) %}

    {% include notitle [price](../_includes/params/calltracking-response-d1eb571bec79.md#filters_price) %}
    
     
    :   {% include notitle [from](../_includes/params/calltracking-response-d1eb571bec79.md#filters_price_from) %}

        {% include notitle [to](../_includes/params/calltracking-response-d1eb571bec79.md#filters_price_to) %}

    {% include notitle [cars_filter](../_includes/params/calltracking-response-d1eb571bec79.md#filters_cars_filter) %}
    
     
    :   {% include notitle [mark](../_includes/params/calltracking-response-d1eb571bec79.md#mark) %}

        {% include notitle [model](../_includes/params/calltracking-response-d1eb571bec79.md#model) %}

        {% include notitle [super_gen](../_includes/params/calltracking-response-d1eb571bec79.md#filters_cars_filter_super_gen) %}

    {% include notitle [body_type](../_includes/params/calltracking-response-d1eb571bec79.md#filters_cars_filter_body_type) %}

    {% include notitle [transmission](../_includes/params/calltracking-response-d1eb571bec79.md#filters_cars_filter_transmission) %}

    {% include notitle [tags](../_includes/params/calltracking-response-d1eb571bec79.md#filters_cars_filter_tags) %}

</div>

Общая структура ответа приведена ниже. Порядок следования элементов не гарантируется. В структуре могут присутствовать служебные параметры, которые не описаны в таблице.

## Формат ответа {#output-structure}

```json
{
  "calls_by_day": [
    {
      "day": {string},
      "succeed_calls_amount": {integer},
      "failed_calls_amount": {integer}
    }
  ],
  "total": {
    "succeed_calls_amount": {integer},
    "failed_calls_amount": {integer}
  },
  "request": {
    "filter": {
      "period": {
        "from": {string},
        "to": {string}
      },
      "targets": {string},
      "results": {string},
      "callbacks": {string},
      "unique": {string},
      "caller_phones": {
        "raw": {string}
      },
      "callee_phones": {
        "raw": {string}
      },
      "category": [
        {string}
      ],
      "section": [
        {string}
      ],
      "offer_id": [
        {string}
      ],
      "vin_code": [
        {string}
      ],
      "year": {
        "from": {integer},
        "to": {integer}
      },
      "price": {
        "from": {integer},
        "to": {integer}
      },
      "cars_filter": [
        {
          "mark": {string},
          "model": {string},
          "super_gen": {string}
        }
      ],
      "body_type": [
        {string}
      ],
      "transmission": [
        {string}
      ],
      "tags": [
        {string}
      ]
    }
  },
  "error": {string},
  "status": {string},
  "detailed_error": {string}
}
```

<div class="params-table">

{% include notitle [calls_by_day](../_includes/params/post-calltracking-aggregated-00e1102bb143.md#calls_by_day) %}

 
:   {% include notitle [day](../_includes/params/post-calltracking-aggregated-00e1102bb143.md#day) %}

    {% include notitle [succeed_calls_amount](../_includes/params/post-calltracking-aggregated-00e1102bb143.md#succeed_calls_amount) %}

    {% include notitle [failed_calls_amount](../_includes/params/post-calltracking-aggregated-00e1102bb143.md#failed_calls_amount) %}

{% include notitle [total](../_includes/params/post-calltracking-aggregated-00e1102bb143.md#total) %}

 
:   {% include notitle [succeed_calls_amount](../_includes/params/post-calltracking-aggregated-00e1102bb143.md#succeed_calls_amount_total) %}

    {% include notitle [failed_calls_amount](../_includes/params/post-calltracking-aggregated-00e1102bb143.md#failed_calls_amount_total) %}

{% include notitle [request](../_includes/params/post-calltracking-aggregated-00e1102bb143.md#request) %}

 
:   {% include notitle [filter](../_includes/params/post-calltracking-aggregated-00e1102bb143.md#filter) %}
    
     
    :   {% include notitle [period](../_includes/params/post-calltracking-aggregated-00e1102bb143.md#period) %}
        
         
        :   {% include notitle [from](../_includes/params/post-calltracking-aggregated-00e1102bb143.md#from_filter) %}

            {% include notitle [to](../_includes/params/post-calltracking-aggregated-00e1102bb143.md#to_filter) %}

        {% include notitle [targets](../_includes/params/post-calltracking-aggregated-00e1102bb143.md#targets) %}

        {% include notitle [results](../_includes/params/post-calltracking-aggregated-00e1102bb143.md#results) %}

        {% include notitle [callbacks](../_includes/params/post-calltracking-aggregated-00e1102bb143.md#callbacks) %}

        {% include notitle [unique](../_includes/params/post-calltracking-aggregated-00e1102bb143.md#unique) %}

        {% include notitle [caller_phones](../_includes/params/post-calltracking-aggregated-00e1102bb143.md#caller_phones) %}
        
         
        :   {% include notitle [raw](../_includes/params/post-calltracking-aggregated-00e1102bb143.md#raw) %}

        {% include notitle [callee_phones](../_includes/params/post-calltracking-aggregated-00e1102bb143.md#callee_phones) %}
        
         
        :   {% include notitle [raw](../_includes/params/post-calltracking-aggregated-00e1102bb143.md#raw) %}

        {% include notitle [category](../_includes/params/post-calltracking-aggregated-00e1102bb143.md#category) %}

        {% include notitle [section](../_includes/params/post-calltracking-aggregated-00e1102bb143.md#section) %}

        {% include notitle [offer_id](../_includes/params/post-calltracking-aggregated-00e1102bb143.md#offer_id) %}

        {% include notitle [vin_code](../_includes/params/post-calltracking-aggregated-00e1102bb143.md#vin_code) %}

        {% include notitle [year](../_includes/params/post-calltracking-aggregated-00e1102bb143.md#year) %}
        
         
        :   {% include notitle [from](../_includes/params/post-calltracking-aggregated-00e1102bb143.md#from_year) %}

            {% include notitle [to](../_includes/params/post-calltracking-aggregated-00e1102bb143.md#to_year) %}

        {% include notitle [price](../_includes/params/post-calltracking-aggregated-00e1102bb143.md#price) %}
        
         
        :   {% include notitle [from](../_includes/params/post-calltracking-aggregated-00e1102bb143.md#from_price) %}

            {% include notitle [to](../_includes/params/post-calltracking-aggregated-00e1102bb143.md#to_price) %}

        {% include notitle [cars_filter](../_includes/params/post-calltracking-aggregated-00e1102bb143.md#cars_filter) %}
        
         
        :   {% include notitle [mark](../_includes/params/post-calltracking-aggregated-00e1102bb143.md#mark) %}

            {% include notitle [model](../_includes/params/post-calltracking-aggregated-00e1102bb143.md#model) %}

            {% include notitle [super_gen](../_includes/params/post-calltracking-aggregated-00e1102bb143.md#super_gen) %}

        {% include notitle [body_type](../_includes/params/post-calltracking-aggregated-00e1102bb143.md#body_type) %}

        {% include notitle [transmission](../_includes/params/post-calltracking-aggregated-00e1102bb143.md#transmission) %}

        {% include notitle [tags](../_includes/params/post-calltracking-aggregated-00e1102bb143.md#tags) %}

{% include notitle [error](../_includes/params/post-calltracking-aggregated-00e1102bb143.md#error) %}

{% include notitle [status](../_includes/params/post-calltracking-aggregated-00e1102bb143.md#status) %}

{% include notitle [detailed_error](../_includes/params/post-calltracking-aggregated-00e1102bb143.md#detailed_error) %}

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
> curl -i -X POST 'https://apiauto.ru/1.0/calltracking/aggregated' \ 
> -H 'x-dealer-id: 2dtrer432...' \
> -H 'x-session-id: 112_aoR02Tpv...' \
> -H 'Accept: application/json' \
> -d '{
>       "filter": {
>         "period": {
>           "from": {string},
>           "to": {string}
>         },
>         "targets": {string},
>         "results": {string},
>         "callbacks": {string},
>         "unique": {string},
>         "caller_phones": {
>           "raw": {string}
>         },
>         "callee_phones": {
>           "raw": {string}
>         },
>         "category": [
>           {string}
>         ],
>         "section": [
>           {string}
>         ],
>         "offer_id": [
>           {string}
>         ],
>         "vin_code": [
>           {string}
>         ],
>         "year": {
>           "from": {integer},
>           "to": {integer}
>         },
>         "price": {
>           "from": {integer},
>           "to": {integer}
>         },
>         "cars_filter": [
>           {
>             "mark": {string},
>             "model": {string},
>             "super_gen": {string}
>           }
>         ],
>         "body_type": [
>           {string}
>         ],
>         "transmission": [
>           {string}
>         ],
>         "tags": [
>           {string}
>         ]
>       }
>     }'
> ```
> 
> 
> Ответ:
> 
> 
> ```json
> HTTP/1.1 200 OK
> Server: nginx
> Date: Tue, 24 Jul 2018 15:19:41 GMT
> Content-Type: application/json
> Connection: keep-alive
>                     
> {
>   "calls_by_day": [
>     {
>       "day": "2020-06-23T16:43:48.526Z",
>       "succeed_calls_amount": 0,
>       "failed_calls_amount": 0
>     }
>   ],
>   "total": {
>     "succeed_calls_amount": 0,
>     "failed_calls_amount": 0
>   },
>   "request": {
>     "filter": {
>       "period": {
>         "from": "2020-06-23T16:43:48.526Z",
>         "to": "2020-06-23T16:43:48.526Z"
>       },
>       "targets": "ALL_TARGET_GROUP",
>       "results": "ALL_RESULT_GROUP",
>       "callbacks": "ALL_SOURCE_GROUP",
>       "unique": "ALL_UNIQUE_GROUP",
>       "caller_phones": {
>         "raw": "string"
>       },
>       "callee_phones": {
>         "raw": "string"
>       },
>       "category": [
>         "CARS"
>       ],
>       "section": [
>         "USED"
>       ],
>       "offer_id": [
>         "string"
>       ],
>       "vin_code": [
>         "string"
>       ],
>       "year": {
>         "from": 0,
>         "to": 0
>       },
>       "price": {
>         "from": 0,
>         "to": 0
>       },
>       "cars_filter": [
>         {
>           "mark": "string",
>           "model": "string",
>           "super_gen": "string"
>         }
>       ],
>       "body_type": [
>         "string"
>       ],
>       "transmission": [
>         "string"
>       ],
>       "tags": [
>         "string"
>       ]
>     }
>   },
>   "status": "SUCCESS"
> }
> ```

{% include [table-style](../_includes/table-style-border-none-2a2aa0c324bf.md) %}

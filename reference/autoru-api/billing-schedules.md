---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/billing-schedules.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# GET /billing/schedules

Возвращает список всех расписаний с автоматическим применением услуг для объявлений.

## Формат запроса {#input}

```
GET https://apiauto.ru/1.0/billing/schedules
? [[offer_id](*offer_id)=<array[string]>]
& [[product](*product)=<array[string]>]
```

<div class="params-table">

#|
||
##offer_id##
|
Идентификатор объявления.

{% note info %}

Если вы хотите добавить больше одного значения, укажите параметр несколько раз:

```
offer_id=1043045004-977b3&offer_id=1043045543-677b6
```

{% endnote %}

||
|#

#|
||
##product##
|
Код услуги.

{% cut "Допустимые значения:" %}

- `boost` — поднятие объявления в поиске;
- `reset` — обнуление.

{% endcut %}

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
  "offers": {
    "offerId": {
      "products": {
        "productId": {
          "schedule_type": {string},
          "once_at_time": {
            "weekdays": [
              {integer}
            ],
            "time": {string}
          }
        }
      }
    },
    "offerId": {
      "products": {
        "productId": {
          "schedule_type": {string},
          "once_at_time": {
            "weekdays": [
              {integer}
            ],
            "time": {string}
          }
        }
      }
    }
  },
  "[status](*status_ph)": {string}
}
```

<div class="params-table">

{% include notitle [status](../_includes/params/billing-schedules-645e744f4fd1.md#status) %}

{% include notitle [offers](../_includes/params/billing-schedules-645e744f4fd1.md#offers) %}

 
:   {% include notitle [offerId](../_includes/params/billing-schedules-645e744f4fd1.md#offerId) %}
    
     
    :   {% include notitle [products](../_includes/params/billing-schedules-645e744f4fd1.md#products) %}
        
         
        :   {% include notitle [productId](../_includes/params/billing-schedules-645e744f4fd1.md#productId) %}

            {% include notitle [schedule_type](../_includes/params/billing-schedules-645e744f4fd1.md#schedule_type) %}

            {% include notitle [once_at_time](../_includes/params/billing-schedules-645e744f4fd1.md#once_at_time) %}
            
             
            :   {% include notitle [weekdays](../_includes/params/billing-schedules-645e744f4fd1.md#weekdays) %}

                {% include notitle [time](../_includes/params/billing-schedules-645e744f4fd1.md#time) %}

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
> curl -i -X GET 'https://apiauto.ru/1.0/user/offers/cars?page=1&page_size=1&price_to=10000000' -H 'x-authorization: 2dtrer432...' -H 'x-session-id: 112_aoR02Tpv...'
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
>   "offers": {
>     "1085122228-021c1729": {
>       "products": {
>         "all_sale_fresh": {
>           "schedule_type": "ONCE_AT_TIME",
>           "once_at_time": {
>             "weekdays": [
>               3
>             ],
>             "time": "12:05"
>           },
>           "timezone": "+03:00"
>         }
>       }
>     },
>     "1083834903-d5a180d4": {
>       "products": {
>         "all_sale_fresh": {
>           "schedule_type": "ONCE_AT_TIME",
>           "once_at_time": {
>             "weekdays": [
>               3
>             ],
>             "time": "12:05"
>           },
>           "timezone": "+03:00"
>         }
>       }
>     },
>     "1085620906-fba5dba5": {
>       "products": {
>         "all_sale_fresh": {
>           "schedule_type": "ONCE_AT_TIME",
>           "once_at_time": {
>             "weekdays": [
>               3
>             ],
>             "time": "12:05"
>           },
>           "timezone": "+03:00"
>         }
>       }
>     },
>     "1082445034-9e24d943": {
>       "products": {
>         "all_sale_fresh": {
>           "schedule_type": "ONCE_AT_TIME",
>           "once_at_time": {
>             "weekdays": [
>               3
>             ],
>             "time": "12:05"
>           },
>           "timezone": "+03:00"
>         }
>       }
>     }
>   },
>   "status": "SUCCESS"
> }
> ```

{% include [table-style](../_includes/table-style-border-none-2a2aa0c324bf.md) %}

[*status_ph]: {% include notitle [status_ph](../_includes/popups-00286d1be377.md#status_ph) %}

[*offer_id]: {% include notitle [offer_id_note](../_includes/popups-00286d1be377.md#offer_id_note) %}

[*product]: {% include notitle [product](../_includes/popups-00286d1be377.md#product) %}

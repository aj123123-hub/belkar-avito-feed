---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/split-order-create.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# PUT split/order

Позволяет создать заказ.

## Формат запроса {#input}

```
PUT https://apiauto.ru/1.0/split/order
```

### Заголовки запроса {#headers}

#|
||
**Заголовок**
|
**Описание**
||
||
x-external-dealer-id
|
Идентификатор клиента из Авто.ру Бизнес.
||
||
x-authorization
|
Ключ API.
||
|#

### Формат тела запроса {#structure-in}

```json

 {
     "order_id": "string",
     "user_phone": "string",
     "car_info": {
       "vin": "string",
       "mileage": "integer"
     },
     "cart": [
       {
         "product_id": "string",
         "service_name": "string",
         "quantity": "integer",
         "price_per_item": "integer"
       }
     ],
     "tax": "integer"
 }
    
```

<div class="params-table">

{% include notitle [order_id](../_includes/params/split-order-create-ba3989b576df.md#order_id) %}

{% include notitle [user_phone](../_includes/params/split-order-create-ba3989b576df.md#user_phone) %}

{% include notitle [car_info](../_includes/params/split-order-create-ba3989b576df.md#car_info) %}

 
:   {% include notitle [vin](../_includes/params/split-order-create-ba3989b576df.md#vin) %}

    {% include notitle [mileage](../_includes/params/split-order-create-ba3989b576df.md#mileage) %}

{% include notitle [cart](../_includes/params/split-order-create-ba3989b576df.md#cart) %}

 
:   {% include notitle [product_id](../_includes/params/split-order-create-ba3989b576df.md#product_id) %}

    {% include notitle [service_name](../_includes/params/split-order-create-ba3989b576df.md#service_name) %}

    {% include notitle [quantity](../_includes/params/split-order-create-ba3989b576df.md#quantity) %}

    {% include notitle [price_per_item](../_includes/params/split-order-create-ba3989b576df.md#price_per_item) %}

{% include notitle [tax](../_includes/params/split-order-create-ba3989b576df.md#tax) %}

</div>

{% include notitle [req](../_includes/popups-00286d1be377.md#req) %}

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
Статус запроса.

{% cut "Допустимые значения:" %}

- `SUCCESS` — успешный запрос;
- `ERROR` — ошибка.

{% endcut %}

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
 || 500 | INTERNAL SERVER ERROR | Внутренняя ошибка сервера. || 

|#

## Пример {#example-JSON}

> Запрос:
> 
> 
> ```http
> curl -i -X PUT 'https://apiauto.ru/1.0/split/order
>    
>    {
>      "order_id": "string",
>      "user_phone": "string",
>      "car_info": {
>        "vin": "string",
>        "mileage": 100000
>      },
>      "cart": [
>        {
>          "product_id": "string",
>          "service_name": "string",
>          "quantity": 1,
>          "price_per_item": 100
>        }
>      ],
>      "tax": "NDS_20"
>  }
> ```
> 
> 
> Ответ:
> 
> 
> ```json
> HTTP/1.1 200 OK
>      Server: nginx
>      Date: Fri, 1 Mar 2024 15:19:41 GMT
>      Content-Type: application/json
>      Connection: keep-alive
>      
>      {
>        "status": "SUCCESS"
>      }
> ```


{% include [table-style](../_includes/table-style-border-none-2a2aa0c324bf.md) %}

[*req]: {% include notitle [req](../_includes/popups-00286d1be377.md#req) %}

---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/split-orders-list.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# POST split/orders/list

Позволяет получить список заказов.

## Формат запроса {#input}

```
POST https://apiauto.ru/1.0/split/orders/list
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
     "filter": {
       "phone_or_order_number": "string"
     },
     "sorting": "string",
     "pagination": {
       "page": "integer",
       "page_size": "integer"
     }
   }
    
```

<div class="params-table">

#|
||
##filter##[*](*req)
|
Фильтр для выбора заказов.

{% cut "Допустимые значения:" %}

`phone_or_order_number` – фильтрация по номеру телефона или номеру заказа в системе.

{% endcut %}


||
|#

<br>

#|
||
##sorting##[*](*req)
|
Сортировка заказов.

{% cut "Допустимые значения:" %}

- `NO_SORTING` – без сортировки;
- `DATE_CREATED_ASC` – сортировка по дате создания (по возрастанию);
- `DATE_CREATED_DESC` – сортировка по дате создания (по убыванию).

{% endcut %}

||
|#

<br>

#|
|| ##pagination##[*](*req) | Нумерация страниц. ||
|#

 
:   #|
    || ##page##[*](*req) | Номер страницы. ||
    |#

<br>


 
:   #|
    || ##page_size##[*](*req) | Количество элементов на странице. ||
    |#

</div>

\* Обязательный параметр

Общая структура ответа приведена ниже. Порядок следования элементов не гарантируется. В структуре могут присутствовать служебные параметры, которые не описаны в таблице.

## Формат ответа {#output-structure}

```json

  {
    "orders": [
      {
      "created_at": "string",
        "status": "string",
        "order_id": "string",
        "user_phone": "string",
        "cart": [
          {
            "product_id": "string",
            "service_name": "string",
            "quantity": "integer",
            "price_per_item": "integer"
          }
        ],
        "total_price": "integer",
        "tax": "integer",
        "payment_url": "string",
        "error_message": "string",
        "refund_info": {
          "total_refunded_amount": "integer",
          "refunded_cart": [
            {
              "product_id": "string",
              "refunded_quantity": "integer",
              "refunded_amount": "integer",
              "service_name": "string"
            }
        ]
      },
      "car_info": {
        "vin": "string",
        "mileage": "integer"
      }
    }
  ],
  "pagination": {
    "page_num": "integer",
    "page_size": "integer",
    "total_count": "integer",
    "total_page_count": "integer"
  },
  "error": "string",
  "status": "string",
  "detailed_error": "string"
}
   
```

<div class="params-table">

{% include notitle [orders](../_includes/params/split-orders-list-b5206ab4d173.md#orders) %}

 
:   {% include notitle [created_at](../_includes/params/split-orders-list-b5206ab4d173.md#created_at) %}

    {% include notitle [status](../_includes/params/split-orders-list-b5206ab4d173.md#status) %}

    {% include notitle [order_id](../_includes/params/split-orders-list-b5206ab4d173.md#order_id) %}

    {% include notitle [user_phone](../_includes/params/split-orders-list-b5206ab4d173.md#user_phone) %}

    {% include notitle [cart](../_includes/params/split-orders-list-b5206ab4d173.md#cart) %}
    
     
    :   {% include notitle [product_id](../_includes/params/split-orders-list-b5206ab4d173.md#product_id) %}

        {% include notitle [service_name](../_includes/params/split-orders-list-b5206ab4d173.md#service_name) %}

        {% include notitle [quantity](../_includes/params/split-orders-list-b5206ab4d173.md#quantity) %}

        {% include notitle [price_per_item](../_includes/params/split-orders-list-b5206ab4d173.md#price_per_item) %}

    {% include notitle [total_price](../_includes/params/split-orders-list-b5206ab4d173.md#total_price) %}

    {% include notitle [tax](../_includes/params/split-orders-list-b5206ab4d173.md#tax) %}

    {% include notitle [payment_url](../_includes/params/split-orders-list-b5206ab4d173.md#payment_url) %}

    {% include notitle [error_message](../_includes/params/split-orders-list-b5206ab4d173.md#error_message) %}

    {% include notitle [refund_info](../_includes/params/split-orders-list-b5206ab4d173.md#refund_info) %}
    
     
    :   {% include notitle [total_refunded_amount](../_includes/params/split-orders-list-b5206ab4d173.md#total_refunded_amount) %}

        {% include notitle [refunded_cart](../_includes/params/split-orders-list-b5206ab4d173.md#refunded_cart) %}
        
         
        :   {% include notitle [product_id](../_includes/params/split-orders-list-b5206ab4d173.md#product_id) %}

            {% include notitle [refunded_quantity](../_includes/params/split-orders-list-b5206ab4d173.md#refunded_quantity) %}

            {% include notitle [refunded_amount](../_includes/params/split-orders-list-b5206ab4d173.md#refunded_amount) %}

            {% include notitle [service_name](../_includes/params/split-orders-list-b5206ab4d173.md#service_name) %}

    {% include notitle [car_info](../_includes/params/split-orders-list-b5206ab4d173.md#car_info) %}
    
     
    :   {% include notitle [vin](../_includes/params/split-orders-list-b5206ab4d173.md#vin) %}

        {% include notitle [mileage](../_includes/params/split-orders-list-b5206ab4d173.md#mileage) %}

{% include notitle [pagination](../_includes/params/split-orders-list-b5206ab4d173.md#pagination) %}

 
:   {% include notitle [page_num](../_includes/params/split-orders-list-b5206ab4d173.md#page_num) %}

    {% include notitle [page_size](../_includes/params/split-orders-list-b5206ab4d173.md#page_size) %}

    {% include notitle [total_count](../_includes/params/split-orders-list-b5206ab4d173.md#total_count) %}

    {% include notitle [total_page_count](../_includes/params/split-orders-list-b5206ab4d173.md#total_page_count) %}


</div>

\* Обязательный параметр

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
> curl -i -X POST 'https://apiauto.ru/1.0/split/orders/list
>      
>      {
>        "filter": {
>          "phone_or_order_number": "string"
>        },
>        "sorting": "NO_SORTING",
>        "pagination": {
>          "page": 1,
>          "page_size": 10
>        }
>      }
> ```
> 
> 
> Ответ:
> 
> 
> ```json
> HTTP/1.1 200 OK
>      Server: nginx
>      Date: Fri, 1 Mar 2024 19:46:58 GMT
>      Content-Type: application/json
>      Connection: keep-alive
>      
>      {
>        "orders": [
>          {
>            "created_at": "2024-01-24T06:29:11.519Z",
>            "status": "NEW",
>            "order_id": "string",
>            "user_phone": "string",
>            "cart": [
>              {
>                "product_id": "string",
>                "service_name": "string",
>                "quantity": 0,
>                "price_per_item": 0
>              }
>            ],
>            "total_price": 0,
>            "tax": "NDS_20",
>            "payment_url": "string",
>            "error_message": "string",
>            "refund_info": {
>              "total_refunded_amount": 0,
>              "refunded_cart": [
>                {
>                  "product_id": "string",
>                  "refunded_quantity": 0,
>                  "refunded_amount": 0,
>                  "service_name": "string"
>                }
>              ]
>            },
>            "car_info": {
>              "vin": "string",
>              "mileage": 0
>            }
>          }
>        ],
>        "pagination": {
>          "page_num": 1,
>          "page_size": 10,
>          "total_count": 1,
>          "total_page_count": 1
>        },
>        "error": "UNKNOWN_ERROR",
>        "status": "SUCCESS",
>        "detailed_error": "string"
>      }
> ```

{% include [table-style](../_includes/table-style-border-none-2a2aa0c324bf.md) %}

[*req]: {% include notitle [req](../_includes/popups-00286d1be377.md#req) %}

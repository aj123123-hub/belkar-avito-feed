---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/split-order-refund.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# POST split/order/refund

Позволяет узнать статус возврата заказа.

## Формат запроса {#input}

```
POST https://apiauto.ru/1.0/split/order/refund
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
     "refund_amount": "integer",
     "cart_after_refund": [
       {
         "product_id": "string",
         "service_name": "string",
         "quantity": "integer",
         "price_per_item": "integer"
       }
     ]
   }
    
```

<div class="params-table">

#|
|| ##order_id##[*](*req) | Номер заказа, идентификатор в системе. ||
|#

<br>

#|
|| ##refund_amount##[*](*req) | Сумма подлежащая возврату. ||
|#

<br>

#|
|| ##cart_after_refund##[*](*req) | Состояние корзины после возврата. ||
|#

 
:   #|
    || ##product_id## | Идентификатор продукта в системе. ||
    |#

    <br>

    #|
    || ##service_name##[*](*req) | Предоставляемая услуга/товар. ||
    |#

    <br>

    #|
    || ##quantity##[*](*req) | Количество единиц предоставляемой услуги/товаров. ||
    |#

    <br>

    #|
    || ##price_per_item##[*](*req) | Цена за единицу предоставляемой услуги/товаров в рублях. ||
    |#


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
> curl -i -X POST 'https://apiauto.ru/1.0/split/order/refund
>      
>    {
>      "order_id": "string",
>      "refund_amount": 0,
>      "cart_after_refund": [
>        {
>          "product_id": "string",
>          "service_name": "string",
>          "quantity": 0,
>          "price_per_item": 0
>        }
>      ]
>    }
> ```
> 
> 
> Ответ:
> 
> 
> ```json
> HTTP/1.1 200 OK
>      Server: nginx
>      Date: Fri, 1 Mar 2024 17:35:58 GMT
>      Content-Type: application/json
>      Connection: keep-alive
>      
>    {
>      "status": "SUCCESS"
>    }
> ```

{% include [table-style](../_includes/table-style-border-none-2a2aa0c324bf.md) %}

[*req]: {% include notitle [req](../_includes/popups-00286d1be377.md#req) %}

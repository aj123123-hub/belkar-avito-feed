---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/split-changes-order-status-notifications.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# POST Callback-URL

Нотификации об изменении статуса заказа.

## Формат запроса {#input}

```
POST Callback-URL
```

`Callback-URL` — url из настроек интеграции.

### Формат тела запроса {#structure-in}

```json

   {
     "eventType": "string",
     "orderId": "string",
     "orderStatus": "string",
     "paymentLink": "string",
     "timestamp": "string",
     "error": "string",
   }
    
```

<div class="params-table">

#|
||
##eventType##[*](*req)
|
Событие. 

{% cut "Допустимые значения:" %}

- `ORDER_NEW` – заказ сохранен, в процессе создания;
- `ORDER_CREATED` – заказ создан, получена ссылка на оплату;
- `ORDER_PAID` – заказ оплачен;
- `ORDER_REFUNDED` – поступил возврат по заказу;
- `ORDER_CANCELED` – заказ был отменен;
- `ORDER_UPDATED` – изменен состав заказа;
- `ORDER_FAILED` – заказ закрыт с ошибкой.

{% endcut %}

||
||
##orderId##[*](*req)
|
Номер заказа, идентификатор в системе.
||
||
##orderStatus##[*](*req)
|
Статус заказа.

{% cut "Допустимые значения:" %}

- `NEW` – новый;
- `CREATED` – получена ссылка на оплату;
- `PAID` – оплачен;
- `REFUNDED` – возврат;
- `CANCELED` – отменен;
- `FAILED` – ошибка.

{% endcut %}

||
||
##paymentLink##
|
Cсылка на оплату заказа.
||
||
##timestamp##[*](*req)
|
Время события.
||
||
##error##
|
Ошибка.
||
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
> curl -i -X POST 'https://apiauto.ru/1.0/Callback-URL
>    
>    {
>      "eventType": "ORDER_CREATED",
>      "orderId": "12345",
>      "orderStatus": "CREATED",
>      "paymentLink": "string",
>      "timestamp": "15:18:43",
>      "error": "string",
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
>      Date: Fri, 1 Mar 2024 15:19:41 GMT
>      Content-Type: application/json
>      Connection: keep-alive
>      
>    {
>      "status": "SUCCESS"
>    }
> ```

{% include [table-style](../_includes/table-style-border-none-2a2aa0c324bf.md) %}

[*req]: {% include notitle [req](../_includes/popups-00286d1be377.md#req) %}

---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/carfax-orders/create.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# POST /carfax/orders/create

Создает заказ и возвращает уникальный идентификатор заказа.

{% note warning %}

Каждый вызов создания заказа независим от всех других и оплачивается отдельно. Если нужно обновить данные для какого-то VIN, создайте новый заказ.

{% endnote %}

## Формат запроса {#input}

```
POST https://apiauto.ru/1.0/carfax/orders/create
```

### Формат тела запроса {#structure-in}

```json
{
  "report_type": {string},
  "identifier_type": {string},
  "identifier": {string}
}
```

<div class="params-table">

#|
||
##report_type##
|
{% include notitle [report_type](../../_includes/popups-00286d1be377.md#report_type_carfax) %}
||
||
##identifier_type##
|
{% include notitle [identifier_type](../../_includes/popups-00286d1be377.md#identifier_type_carfax) %}
||
||
##identifier##
|
{% include notitle [identifier](../../_includes/popups-00286d1be377.md#identifier_carfax) %}
||
|#

</div>

Общая структура ответа приведена ниже. Порядок следования элементов не гарантируется. В структуре могут присутствовать служебные параметры, которые не описаны в таблице.

## Формат ответа {#output-structure}

```json
{
  "id": {string},
  "status": {string},
  "identifier_type": {string},
  "identifier": {string},
  "report_type": {string},
  "vin": {string}
}
```

<div class="params-table">

#|
||
##id##
|
Уникальный идентификатор заказа.
||
||
##status##
|
Статус заказа.

{% cut "Возможные значения:" %}

- `PREPARING` — заказ находится в процессе обработки, данные отчета пока не доступны.
- `UNTRUSTED` — в ГИБДД не найдена информация по автомобилю.
- `FAILED` — подробности ошибки в поле `error`:
    - `UNKNOWN_ERROR` — неизвестная ошибка;
    - `PAYMENT_FAILED` — оплата заказа завершилась ошибкой;
    - `INVALID_IDENTIFIER` — неверный идентификатор (недопустимый VIN, ГРЗ или `offer_id`);
    - `IDENTIFIER_NOT_FOUND` — не смогли найти VIN по ГРЗ или `id` объявления;
    - `NOT_SUPPORTED_IDENTIFIER_TYPE` — для выбранного типа отчета нельзя получить отчет по указанном идентификатору;
    - `NOT_SUPPORTED_REPORT_TYPE` — неизвестный тип отчета;
    - `REPORT_NOT_AVAILABLE` — отчет недоступен для продажи.
- `UPDATING` — оплата заказа прошла успешно, источники данных начали опрашиваться, данные могут быть уже частично доступны.
- `SUCCESS` — заказ успешно завершен и больше не будет обновляться.

{% endcut %}

||
||
##identifier_type##
|
Тип идентификатора из запроса.
||
||
##identifier##
|
Идентификатор из запроса.
||
||
##report_type##
|
FULL_REPORT.
||
||
##vin##
|
VIN к которому привязан отчет. Может отсутствовать для статусов FAILED, PREPARING.
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
 || 401 | NO_AUTH | Не удалось авторизовать пользователя по переданным данным. || 
 || 403 | CODE_AUTH_REQUIRED
PASSWORD_EXPIRED | Не удается аутентифицироваться. || 

|#

## Примеры {#example-JSON}

{% cut "Ответ для кода 400 (неверный формат запроса)" %}

> Запрос:
> 
> 
> ```http
> curl -i -X GET 'https://apiauto.ru/1.0/carfax/orders/result?order_id=8486a639-0a21-49d3-a906-3f877b8a1e99'
> ```
> 
> 
> Ответ:
> 
> 
> ```json
> HTTP/1.1 200 OK
> Server: envoy
> Date: Wed,27 Aug 2025 17:08:12 GMT
> Content-Type: application/json
> Connection: keep-alive
> 
> {
>   "error": "INVALID_REQUEST",
>   "detailed_error": "Invalid VIN: abc"
> }
> ```

{% endcut %}

{% cut "Успешный ответ создания заказа" %}

> Запрос:
> 
> 
> ```http
> curl -i -X GET 'https://apiauto.ru/1.0/carfax/orders/result?order_id=213'
> ```
> 
> 
> Ответ:
> 
> 
> ```json
> HTTP/1.1 200 OK
> Server: envoy
> Date: Wed,27 Aug 2025 17:08:12 GMT
> Content-Type: application/json
> Connection: keep-alive
> 
> {
>   "order": {
>     "id": "a5f9cbd3-48a7-4403-908b-153c90781c16",
>     "status": "PREPARING",
>     "identifier_type": "VIN",
>     "identifier": "Z94CU41CBBR048898",
>     "report_type": "FULL_REPORT"
>   }
> }
> ```

{% endcut %}

{% include [border-none](../../_includes/table-style-border-none-2a2aa0c324bf.md) %}

[*report_type]: {% include notitle [report_type](../../_includes/popups-00286d1be377.md#report_type_carfax) %}

[*identifier_type]: {% include notitle [identifier_type](../../_includes/popups-00286d1be377.md#identifier_type_carfax) %}

[*identifier]: {% include notitle [identifier](../../_includes/popups-00286d1be377.md#identifier_carfax) %}

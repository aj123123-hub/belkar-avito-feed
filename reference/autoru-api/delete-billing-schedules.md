---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/delete-billing-schedules.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# DELETE /billing/schedules/{category}/{offerId}/{product}

Удаляет расписание с автоматическим применением услуги для объявления.

## Формат запроса {#input}

```
DELETE https://apiauto.ru/1.0/billing/schedules/{[category](*category)}/{[offerId](*offer_id)}/{[product](*product)}
```

<div class="params-table">

#|
||
##category##
|
Название категории ТС.

{% cut "Допустимые значения:" %}

- `cars` — легковые автомобили;
- `moto` — мототранспорт;
- `trucks` — коммерческий транспорт.

{% endcut %}

||
|#

<br>

#|
|| ##offerId## | Идентификатор объявления. ||
|#

<br>

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

<br>

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
  "status": {string}
}
```

### Параметры ответа {#spec-output}

<div class="params-table">

#|
||
##status##
|
Статус ответа.
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
 || 404 | OFFER_NOT_FOUND | Объявление не найдено. || 
 || 500 | INTERNAL SERVER ERROR | Внутренняя ошибка сервера. || 

|#

## Пример {#example-JSON}

> Запрос:
> 
> 
> ```http
> curl -i -X DELETE 'https://apiauto.ru/1.0/billing/schedules/cars/1043045004-977b3/boost' -H 'x-authorization: 2dtrer432...'  -H 'Accept: application/json' 'x-session-id: 112_aoR02Tpv...'
> ```
> 
> 
> Ответ:
> 
> 
> ```json
> HTTP/1.1 200 OK
> Server: nginx
> Date: Fri, 15 Jun 2018 14:34:59 GMT
> Content-Type: application/json
> Content-Length: 20
> Connection: keep-alive
>                     
> {
>   "status": "SUCCESS"
> }
> ```


{% include [table-style](../_includes/table-style-border-none-2a2aa0c324bf.md) %}

[*offer_id]: {% include notitle [offer_id](../_includes/popups-00286d1be377.md#offer_id) %}

[*category]: {% include notitle [category-billing](../_includes/popups-00286d1be377.md#category-billing) %}

[*product]: {% include notitle [product](../_includes/popups-00286d1be377.md#product) %}

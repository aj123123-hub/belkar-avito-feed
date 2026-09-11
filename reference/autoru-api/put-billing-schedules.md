---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/put-billing-schedules.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# PUT /billing/schedules/{category}/{offerId}/{product}

Добавляет расписание с автоматическим применением услуги для объявления.

## Формат запроса {#input}

```
PUT https://apiauto.ru/1.0/billing/schedules/{[category](*category)}/{[offerId](*offer_id)}/{[product](*product)}
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
  "schedule_type": {string},
  "weekdays": [
    {integer},
    {integer}
  ],
  "time": {string}
}
```

<div class="params-table">

#|
||
##schedule_type##
|
Тип расписания. 

{% cut "Допустимые значения:" %}

- `ONCE_AT_TIME`

{% endcut %}

||
|#

<br>

#|
||
##weekdays##
|
Дни недели, в которые необходимо применять услугу. 

{% cut "Допустимые значения:" %}

- 1 — понедельник;
- 2 — вторник;
- 3 — среда;
- 4 — четверг;
- 5 — пятница;
- 6 — суббота;
- 7 — воскресенье.

{% endcut %}

||
|#

<br>

#|
||
##time##
|
Время применения услуги в формате `HH:mm`.
||
|#

</div>

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
> curl -i -X PUT 'https://apiauto.ru/1.0/billing/schedules/cars/1043045004-977b3/boost' -H 'x-authorization: 2dtr...er432' -H 'x-session-id: 112_ao...R02Tpv' -H 'Content-Type:application/json' -d {"schedule_type": "ONCE_AT_TIME", "weekdays": [0], "time": "10:00", "timezone": "+03:00"}
> ```
> 
> 
> Ответ:
> 
> 
> ```json
> HTTP/1.1 200 OK
> Server: nginx
> Date: Fri, 12 Jul 2018 13:30:59 GMT
> Content-Type: application/json
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

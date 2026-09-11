---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/user-offers-category-offer-id-activate.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# POST /user/offers/{category}/{offerID}/activate

Активирует объявление, снятое с продажи.

## Формат запроса {#input}

```
POST https://apiauto.ru/1.0/user/offers/{[category](*category)}/{[offerID](*offerID)}/activate
```

<div class="params-table">

#|
||
##category##
|
Название категории ТС. Допустимые значения:

- `cars` — легковые автомобили;
- `moto` — мототранспорт;
- `trucks` — коммерческий транспорт;
- `all` — все категории ТС.

||
|#

#|
|| ##offerID## | Идентификатор объявления, которое необходимо активировать. ||
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

Тело запроса отсутствует.

Общая структура ответа приведена ниже. Порядок следования элементов не гарантируется. В структуре могут присутствовать служебные параметры, которые не описаны в таблице.

## Формат ответа {#output-structure}

```json
{
  "status": "{string}"
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
 || 402 | NOT_ENOUGH_FUNDS_ON_ACCOUNT | Недостаточно средств для оплаты. || 
 || 404 | OFFER_NOT_FOUND | Объявление не найдено. || 
 || 409 | NO_PHONE | Не указан телефон продавца. || 
 || 500 | INTERNAL SERVER ERROR | Внутренняя ошибка сервера. || 

|#

## Пример {#example-JSON}

> Запрос:
> 
> 
> ```http
> curl -i -X POST 'https://apiauto.ru/1.0/user/offers/trucks/1022557788-4a6efe8b/activate' -H 'Accept: application/json' -H 'Content-Type: application/json' -H 'x-authorization: 2dtrer432...' -H 'x-session-id: 112_aoR02Tpv...'
> ```
> 
> 
> Ответ:
> 
> 
> ```json
> HTTP/1.1 200 OK
> Server: nginx
> Date: Fri, 15 Jun 2018 13:50:59 GMT
> Content-Type: application/json
> Content-Length: 20
> Connection: keep-alive
> {
>   "status": "SUCCESS"
> }
> ```

{% include [table-style](../_includes/table-style-border-none-2a2aa0c324bf.md) %}

[*category]: {% include notitle [category](../_includes/popups-00286d1be377.md#category) %}

[*offerID]: Идентификатор объявления, которое необходимо активировать.



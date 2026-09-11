---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/user-offers-category-offer-id-products-delete.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# DELETE /user/offers/{category}/{offerID}/products

Отключает у объявления указанные услуги.

## Формат запроса {#input}

```
DELETE https://apiauto.ru/1.0/user/offers/{[category](*category)}/{[offerID](*offerID)}/products
? [products](*products)=<array[string]>
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
|| ##offerID## | Идентификатор объявления, к которому надо подключить указанные услуги. ||
|#

#|
||
##product##[*](*req)
|
Код услуги, которую нужно отключить.

{% cut "Допустимые значения:" %}

- `all_sale_premium` — премиум;
- `all_sale_special` — спецпредложение;
- `all_sale_badge` — стикеры быстрой продажи.

{% endcut %}

{% note info %}

Если вы хотите добавить больше одного значения, укажите параметр несколько раз:

```
product=all_sale_premium&product=all_sale_special
```

{% endnote %}

||
|#

\* Обязательный параметр

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
  "status": "{string}"
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
> curl -i -X DELETE 'https://apiauto.ru/1.0/user/offers/cars/1022557788-4a6efe8b/products?product=all_sale_premium&product=all_sale_special' -H 'x-authorization: 2dtrer432...'  -H 'Accept: application/json' 'x-session-id: 112_aoR02Tpv...'
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

[*category]: {% include notitle [category](../_includes/popups-00286d1be377.md#category) %}

[*offerID]: Идентификатор объявления, у которого нужно отключить указанные услуги.

[*req]: {% include notitle [req](../_includes/popups-00286d1be377.md#req) %}

[*products]: {% include notitle [products](../_includes/popups-00286d1be377.md#products) %}



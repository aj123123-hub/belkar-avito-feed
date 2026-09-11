---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/dealer-campaigns.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# GET /dealer/campaigns

Возвращает подключенные тарифы дилера.

## Формат запроса {#input}

```
GET https://apiauto.ru/1.0/dealer/campaigns
```

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
  "campaigns": [
    {
      "category": "{string}",
      "truck_subcategories": {
        "categories": [
          "{string}"
        ]
      },
      "moto_subcategories": {
        "categories": [
          "{string}"
        ]
      },
      "section": [
        "{string}"
      ],
      "size": {integer}
    }
  ]
}
```

<div class="params-table">

{% include notitle [campaigns](../_includes/params/dealer-campaigns-73bc7f07b2ee.md#campaigns) %}

 
:   {% include notitle [category](../_includes/params/dealer-campaigns-73bc7f07b2ee.md#category) %}

    {% include notitle [truck_subcategories](../_includes/params/dealer-campaigns-73bc7f07b2ee.md#truck_subcategories) %}

     
    :   {% include notitle [categories_trucks](../_includes/params/dealer-campaigns-73bc7f07b2ee.md#categories_trucks) %}

    {% include notitle [moto_subcategories](../_includes/params/dealer-campaigns-73bc7f07b2ee.md#moto_subcategories) %}

     
    :   {% include notitle [categories_moto](../_includes/params/dealer-campaigns-73bc7f07b2ee.md#categories_moto) %}

    {% include notitle [section](../_includes/params/dealer-campaigns-73bc7f07b2ee.md#section) %}

    {% include notitle [size](../_includes/params/dealer-campaigns-73bc7f07b2ee.md#size) %}

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
 || 404 | CLIENT_NOT_FOUND | Клиент не найден. || 
 || 500 | INTERNAL SERVER ERROR | Внутренняя ошибка сервера. || 

|#

## Пример {#example-JSON}

> Запрос:
> 
> 
> ```http
> curl -i -X GET 'https://apiauto.ru/1.0/dealer/campaigns' -H 'x-authorization: 2dtrer432...' -H 'Accept: application/json' -H 'x-session-id: 112_aoR02Tpv...'
> ```
> 
> 
> Ответ:
> 
> 
> ```json
> HTTP/1.1 200 OK
> Server: nginx
> Date: Thu, 02 Aug 2018 10:19:41 GMT
> Content-Type: application/json
> Connection: keep-alive
> 
> {
>   "campaigns": [
>     {
>       "category": "TRUCKS",
>       "truck_subcategories": {
>         "categories": [
>           "BUS",
>           "AUTOLOADER",
>           "LCV",
>           "TRAILER",
>           "BULLDOZERS",
>           "AGRICULTURAL",
>           "CRANE_HYDRAULICS",
>           "SWAP_BODY",
>           "DREDGE",
>           "MUNICIPAL",
>           "ARTIC",
>           "CRANE",
>           "TRUCK",
>           "CONSTRUCTION"
>         ]
>       },
>       "section": [
>         "USED",
>         "NEW"
>       ],
>       "size": 2147483647
>     },
>     {
>       "category": "CARS",
>       "section": [
>         "USED"
>       ],
>       "size": 2147483647
>     },
>     {
>       "category": "MOTO",
>       "moto_subcategories": {
>         "categories": [
>           "MOTORCYCLE",
>           "ATV",
>           "SCOOTERS",
>           "SNOWMOBILE"
>         ]
>       },
>       "section": [
>         "NEW",
>         "USED"
>       ],
>       "size": 50
>     },
>     {
>       "category": "CARS",
>       "section": [
>         "NEW"
>       ],
>       "size": 2147483647
>     }
>   ]
> }                                  
> ```

{% include [table-style](../_includes/table-style-border-none-2a2aa0c324bf.md) %}

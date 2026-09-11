---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/feeds-settings.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# GET /feeds/settings

Возвращает список настроек для прайс-листов.

## Формат запроса {#input}

```
GET https://apiauto.ru/1.0/feeds/settings
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
  "feeds": [
    {
      "category": {
        "section": {string},
        "category": {string},
        "truck_category": {string},
        "moto_category": {string}
      },
      "settings": {
        "source": {string},
        "delete_sale": {boolean},
        "leave_services": {boolean},
        "leave_added_images": {boolean},
        "is_active": {boolean}
      }
    }
  ]
}
```

<div class="params-table">

{% include notitle [feeds](../_includes/params/feeds-settings-ddd803ac18fe.md#feeds) %}

 
:   {% include notitle [category](../_includes/params/feeds-settings-ddd803ac18fe.md#category) %}
    
     
    :   {% include notitle [section](../_includes/params/feeds-settings-ddd803ac18fe.md#section) %}

        {% include notitle [category](../_includes/params/feeds-settings-ddd803ac18fe.md#category_car) %}

        {% include notitle [truck_category](../_includes/params/feeds-settings-ddd803ac18fe.md#truck_category) %}

        {% include notitle [moto_category](../_includes/params/feeds-settings-ddd803ac18fe.md#moto_category) %}

    {% include notitle [settings](../_includes/params/feeds-settings-ddd803ac18fe.md#settings) %}
    
     
    :   {% include notitle [source](../_includes/params/feeds-settings-ddd803ac18fe.md#source) %}

        {% include notitle [delete_sale](../_includes/params/feeds-settings-ddd803ac18fe.md#delete_sale) %}

        {% include notitle [leave_services](../_includes/params/feeds-settings-ddd803ac18fe.md#leave_services) %}

        {% include notitle [leave_added_images](../_includes/params/feeds-settings-ddd803ac18fe.md#leave_added_images) %}

        {% include notitle [is_active](../_includes/params/feeds-settings-ddd803ac18fe.md#is_active) %}

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
 || 500 | INTERNAL SERVER ERROR | Внутренняя ошибка сервера. || 

|#

## Пример {#example-JSON}

> Запрос:
> 
> 
> ```http
> curl -i -X GET 'https://apiauto.ru/1.0/feeds/settings' -H 'x-authorization: 2dtrer432...' -H 'x-session-id: 112_aoR02Tpv...'
> ```
> 
> 
> Ответ:
> 
> 
> ```json
> HTTP/1.1 200 OK
> Server: nginx
> Date: Fri, 15 Jun 2018 13:30:59 GMT
> Content-Type: application/json
> Connection: keep-alive
> 
> {
>   "feeds": [
>     {
>       "category": {
>         "section": "USED",
>         "category": "CARS",
>         "truck_category": "TRUCK",
>         "moto_category": "MOTORCYCLE"
>       },
>       "settings": {
>         "source": "https://example-url/feed",
>         "delete_sale": true,
>         "leave_services": true,
>         "leave_added_images": true,
>         "is_active": true
>       }
>     }
>   ]
> }              
> ```

{% include [table-style](../_includes/table-style-border-none-2a2aa0c324bf.md) %}

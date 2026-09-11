---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/feeds-history.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# GET /feeds/history

Возвращает историю загрузок прайс-листов.

## Формат запроса {#input}

```
GET https://apiauto.ru/1.0/feeds/history
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
      },
      "task": {
        "id": {string},
        "created_at": {string},
        "finished_at": {string},
        "type": {string},
        "status": {string},
        "settings": {
          "internal_url": {string},
          "[settings](*settings-p)": {
            "source": {string},
            "delete_sale": {boolean},
            "leave_services": {boolean},
            "leave_added_images": {boolean},
            "is_active": {boolean}
          }
        },
        "count_offers": {integer},
        "count_errors": {integer},
        "count_notices": {integer},
        "count_offers_inserted": {integer},
        "count_offers_updated": {integer},
        "count_offers_deleted": {integer},
        "count_offers_skipped": {integer},
        "count_images": {integer},
        "count_images_success": {integer},
        "count_images_errors": {integer},
        "count_success": {integer}
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

    {% include notitle [settings](../_includes/params/feeds-task-cars-section-786fcaab38bd.md#settings) %}
    
     
    :   {% include notitle [source](../_includes/params/feeds-task-cars-section-786fcaab38bd.md#source) %}

        {% include notitle [delete_sale](../_includes/params/feeds-task-cars-section-786fcaab38bd.md#delete_sale) %}

        {% include notitle [leave_services](../_includes/params/feeds-task-cars-section-786fcaab38bd.md#leave_services) %}

        {% include notitle [leave_added_images](../_includes/params/feeds-task-cars-section-786fcaab38bd.md#leave_added_images) %}

        {% include notitle [is_active](../_includes/params/feeds-task-cars-section-786fcaab38bd.md#is_active) %}

    {% include notitle [task](../_includes/params/feeds-task-cars-section-786fcaab38bd.md#task) %}  
    
     
    :   {% include notitle [id](../_includes/params/feeds-task-cars-section-786fcaab38bd.md#id) %}

        {% include notitle [created_at](../_includes/params/feeds-task-cars-section-786fcaab38bd.md#created_at) %}

        {% include notitle [finished_at](../_includes/params/feeds-task-cars-section-786fcaab38bd.md#finished_at) %}

        {% include notitle [type](../_includes/params/feeds-task-cars-section-786fcaab38bd.md#type) %}

        {% include notitle [status](../_includes/params/feeds-task-cars-section-786fcaab38bd.md#status) %}
        
         
        :   {% include notitle [settings](../_includes/params/feeds-task-cars-section-786fcaab38bd.md#settings) %}
            
             
            :   {% include notitle [source](../_includes/params/feeds-task-cars-section-786fcaab38bd.md#source) %}

                {% include notitle [delete_sale](../_includes/params/feeds-task-cars-section-786fcaab38bd.md#delete_sale) %}

                {% include notitle [leave_services](../_includes/params/feeds-task-cars-section-786fcaab38bd.md#leave_services) %}

                {% include notitle [leave_added_images](../_includes/params/feeds-task-cars-section-786fcaab38bd.md#leave_added_images) %}

                {% include notitle [is_active](../_includes/params/feeds-task-cars-section-786fcaab38bd.md#is_active) %}

        {% include notitle [count_offers](../_includes/params/feeds-task-cars-section-786fcaab38bd.md#count_offers) %}

        {% include notitle [count_errors](../_includes/params/feeds-task-cars-section-786fcaab38bd.md#count_errors) %}

        {% include notitle [count_notices](../_includes/params/feeds-task-cars-section-786fcaab38bd.md#count_notices) %}

        {% include notitle [count_offers_inserted](../_includes/params/feeds-task-cars-section-786fcaab38bd.md#count_offers_inserted) %}

        {% include notitle [count_offers_updated](../_includes/params/feeds-task-cars-section-786fcaab38bd.md#count_offers_updated) %}

        {% include notitle [count_offers_deleted](../_includes/params/feeds-task-cars-section-786fcaab38bd.md#count_offers_deleted) %}

        {% include notitle [count_offers_skipped](../_includes/params/feeds-task-cars-section-786fcaab38bd.md#count_offers_skipped) %}

        {% include notitle [count_images](../_includes/params/feeds-task-cars-section-786fcaab38bd.md#count_images) %}

        {% include notitle [count_images_success](../_includes/params/feeds-task-cars-section-786fcaab38bd.md#count_images_success) %}

        {% include notitle [count_images_errors](../_includes/params/feeds-task-cars-section-786fcaab38bd.md#count_images_errors) %}

        {% include notitle [count_success](../_includes/params/feeds-task-cars-section-786fcaab38bd.md#count_success) %}

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
> curl -i -X GET 'https://apiauto.ru/1.0/feeds/history' -H 'x-authorization: 2dtrer432...' -H 'x-session-id: 112_aoR02Tpv...'
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
>       },
>       "task": {
>         "id": 0,
>         "created_at": "2019-05-14T13:39:01.421Z",
>         "finished_at": "2019-05-14T13:39:01.421Z",
>         "type": "AUTOMATIC",
>         "status": "NEW",
>         "settings": {
>           "internal_url": "https://example-url/feed",
>           "settings": {
>             "source": "https://example-url/feed",
>             "delete_sale": true,
>             "leave_services": true,
>             "leave_added_images": true,
>             "is_active": true
>           }
>         },
>         "count_offers": 0,
>         "count_errors": 0,
>         "count_notices": 0,
>         "count_offers_inserted": 0,
>         "count_offers_updated": 0,
>         "count_offers_deleted": 0,
>         "count_offers_skipped": 0,
>         "count_images": 0,
>         "count_images_success": 0,
>         "count_images_errors": 0,
>         "count_success": 0
>       }
>     }
>   ]
> }          
> ```

{% include [table-style](../_includes/table-style-border-none-2a2aa0c324bf.md) %}

[*settings-p]: {% include notitle [settings-p](../_includes/popups-00286d1be377.md#settings-p) %}

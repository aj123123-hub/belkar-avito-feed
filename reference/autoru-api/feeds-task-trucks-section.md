---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/feeds-task-trucks-section.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# POST /feeds/task/trucks/{trucks_category}/{section}

Создает задачу на ручную загрузку прайс-листа для категории ТС «Коммерческие ТС».

## Формат запроса {#input}

```
POST https://apiauto.ru/1.0/feeds/task/trucks/[trucks_category](*truck_category)/[section](*section)
```

<div class="params-table">

#|
||
##trucks_category##
|
Категория коммерческого транспорта.

{% cut "Допустимые значения:" %}

- `TRUCK` — грузовик;
- `LCV` — легкий коммерческий транспорт;
- `TRAILER` — прицеп;
- `SWAP_BODY` — съемный кузов;
- `BUS` — автобус;
- `ARTIC` — седельный тягач;
- `AGRICULTURAL` — сельскохозяйственная;
- `CONSTRUCTION` — строительная;
- `AUTOLOADER` — автопогрузчик;
- `CRANE` — автокран;
- `DREDGE` — экскаватор;
- `BULLDOZERS` — бульдозер;
- `CRANE_HYDRAULICS` — самопогрузчик;
- `MUNICIPAL` — коммунальная.

{% endcut %}

||
|#

<br>

#|
||
##section##
|
Состояние транспортного средства.

{% cut "Допустимые значения:" %}

- `NEW` — новое транспортное средство;
- `USED` — транспортное средство с пробегом (б/у).

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
  "internal_url": {string},
  "settings": {
    "source": {string},
    "delete_sale": {boolean},
    "leave_services": {boolean},
    "leave_added_images": {boolean},
    "is_active": {boolean}
  }
}
```

<div class="params-table">

#|
|| ##settings## | Настройки прайс-листа. ||
|#

 
:   #|
    || ##source## | Ссылка на загрузку прайс-листа. ||
    |#

    #|
    || ##delete_sale## | Признак. Удалять объявления, которые были созданы вручную или отсутствует в прайс-листе. ||
    |#

    #|
    || ##leave_services## | Признак. Не удалять услуги объявлений, если они не были переданы в прайс-листе. ||
    |#

    #|
    || ##leave_added_images## | Признак. Не удалять загруженные вручную фотографии, если они не были переданы в прайс-листе. ||
    |#

    #|
    || ##is_active## | Признак. Активна или нет загрузка данного прайс-листа. ||
    |#

</div>


Общая структура ответа приведена ниже. Порядок следования элементов не гарантируется. В структуре могут присутствовать служебные параметры, которые не описаны в таблице.

## Формат ответа {#output-structure}

```json
{
  "id": {integer},
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
  "count_images_errors": {integer}
}
```

<div class="params-table">

{% include notitle [id](../_includes/params/feeds-task-cars-section-786fcaab38bd.md#id) %}

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
> curl -i -X POST 'https://apiauto.ru/1.0/feeds/task/trucks/TRUCK/NEW' \
> -H 'x-authorization: 2dtr...er432' \
> -H 'x-session-id: 112_ao...R02Tpv' \
> -H 'Content-Type:application/json' \
> -d {
>      "internal_url": "https://dealer/auto/feed...",
>      "settings": {
>        "source": "feed",
>        "delete_sale": true,
>        "leave_services": true,
>        "leave_added_images": true,
>        "is_active": true
>      }
>    }
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
>   "id": 14,
>   "created_at": "2019-06-19T15:41:35.750Z",
>   "finished_at": "2019-06-19T15:41:35.750Z",
>   "type": "AUTOMATIC",
>   "status": "NEW",
>   "settings": {
>     "internal_url": "https://dealer/auto/feed...",
>     "settings": {
>       "source": "feed",
>       "delete_sale": true,
>       "leave_services": true,
>       "leave_added_images": true,
>       "is_active": true
>     }
>   },
>   "count_offers": 0,
>   "count_errors": 0,
>   "count_notices": 0,
>   "count_offers_inserted": 0,
>   "count_offers_updated": 0,
>   "count_offers_deleted": 0,
>   "count_offers_skipped": 0,
>   "count_images": 0,
>   "count_images_success": 0,
>   "count_images_errors": 0,
>   "count_success": 0
> }                                    
> ```

{% include [table-style](../_includes/table-style-border-none-2a2aa0c324bf.md) %}

[*section]: {% include notitle [section](../_includes/popups-00286d1be377.md#section) %}

[*truck_category]: {% include notitle [section](../_includes/reference/includes/id-includes/truck_category-9ee9c25455b7.md) %}

[*settings-p]: {% include notitle [settings-p](../_includes/popups-00286d1be377.md#settings-p) %}


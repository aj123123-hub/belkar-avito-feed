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
          "settings": {
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

#|
||
**Параметр**
|
**Описание**
||
||
`feeds`
|
Список настроек для прайс-листов.
||
||
`feeds[].category`
|
Информация о категории ТС.
||
||
`feeds[].category.section`
|
Состояние транспортного средства. Допустимые значения: `NEW` — новое, `USED` — с пробегом.
||
||
`feeds[].category.category`
|
Категория транспортного средства (ТС). Допустимые значения: `CARS`, `TRUCKS`, `MOTO`.
||
||
`feeds[].category.truck_category`
|
Категория коммерческого транспорта. Допустимые значения: `TRUCK`, `LCV`, `TRAILER`, `SWAP_BODY`, `BUS`, `ARTIC`, `AGRICULTURAL`, `CONSTRUCTION`, `AUTOLOADER`, `CRANE`, `DREDGE`, `BULLDOZERS`, `CRANE_HYDRAULICS`, `MUNICIPAL`.
||
||
`feeds[].category.moto_category`
|
Категория мототранспорта. Допустимые значения: `MOTORCYCLE`, `ATV`, `SCOOTERS`, `SNOWMOBILE`.
||
||
`feeds[].settings`
|
Настройки прайс-листа.
||
||
`feeds[].settings.source`
|
Ссылка на загрузку прайс-листа.
||
||
`feeds[].settings.delete_sale`
|
Признак. Удалять объявления, которые были созданы вручную или отсутствуют в прайс-листе.
||
||
`feeds[].settings.leave_services`
|
Признак. Не удалять услуги объявлений, если они не были переданы в прайс-листе.
||
||
`feeds[].settings.leave_added_images`
|
Признак. Не удалять загруженные вручную фотографии, если они не были переданы в прайс-листе.
||
||
`feeds[].settings.is_active`
|
Признак. Активна или нет загрузка данного прайс-листа.
||
||
`feeds[].task`
|
Информация о задаче на ручную загрузку прайс-листа.
||
||
`feeds[].task.id`
|
Идентификатор задачи на ручную загрузку прайс-листа.
||
||
`feeds[].task.created_at`
|
Дата создания задачи в формате ISO 8601 со смещением относительно UTC. Например, `2017-07-08T11:29:16+03:00`.
||
||
`feeds[].task.finished_at`
|
Дата окончания задачи в формате ISO 8601 со смещением относительно UTC. Например, `2017-07-08T11:29:16+03:00`.
||
||
`feeds[].task.type`
|
Тип загрузки прайс-листа. Параметр не выводится при использовании ручной загрузки. (В примерах встречается значение `AUTOMATIC`.)
||
||
`feeds[].task.status`
|
Статус задачи на ручную загрузку прайс-листа. (В примерах встречаются значения `NEW`, `FAILURE`.)
||
||
`feeds[].task.settings`
|
Настройки прайс-листа задачи (включая `internal_url` — внутреннюю ссылку на загруженный прайс-лист на стороне Авто.ру, и вложенный блок `settings` с теми же полями `source`/`delete_sale`/`leave_services`/`leave_added_images`/`is_active`, что и выше).
||
||
`feeds[].task.count_offers`
|
Количество объявлений в прайс-листе.
||
||
`feeds[].task.count_errors`
|
Количество объявлений с ошибками (объявления, которые не были обработаны).
||
||
`feeds[].task.count_notices`
|
Количество объявлений с предупреждениями.
||
||
`feeds[].task.count_offers_inserted`
|
Количество новых объявлений.
||
||
`feeds[].task.count_offers_updated`
|
Количество обновленных объявлений.
||
||
`feeds[].task.count_offers_deleted`
|
Количество удаленных объявлений.
||
||
`feeds[].task.count_offers_skipped`
|
Количество необновленных объявлений.
||
||
`feeds[].task.count_images`
|
Количество изображений в прайс-листе.
||
||
`feeds[].task.count_images_success`
|
Количество успешно добавленных изображений.
||
||
`feeds[].task.count_images_errors`
|
Количество незагруженных изображений.
||
||
`feeds[].task.count_success`
|
Количество успешно обработанных объявлений.
||

|#

> Описания полей выше подставлены вручную с живой страницы документации (2026-09-11).

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

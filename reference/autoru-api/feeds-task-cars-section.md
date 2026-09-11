---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/feeds-task-cars-section.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# POST /feeds/task/cars/{section}

Создает задачу на ручную загрузку прайс-листа для категории ТС «Легковые ТС».

## Формат запроса {#input}

```
POST https://apiauto.ru/1.0/feeds/task/cars/[section](*section)
```

<div class="params-table">

#|
||
##section##
|
Состояние транспортного средства. Допустимые значения: `NEW` — новое транспортное средство; `USED` — транспортное средство с пробегом (б/у).
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
      "source": {string},
      "delete_sale": {boolean},
      "leave_services": {boolean},
      "leave_added_images": {boolean},
      "is_active": {boolean}
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

#|
||
**Параметр**
|
**Описание**
||
||
`id`
|
Идентификатор задачи на ручную загрузку прайс-листа.
||
||
`created_at`
|
Дата создания задачи в формате ISO 8601 со смещением относительно UTC. Например, `2017-07-08T11:29:16+03:00`.
||
||
`finished_at`
|
Дата окончания задачи в формате ISO 8601 со смещением относительно UTC. Например, `2017-07-08T11:29:16+03:00`.
||
||
`type`
|
Тип загрузки прайс-листа. Параметр не выводится при использовании ручной загрузки. (В примерах встречается значение `AUTOMATIC`.)
||
||
`status`
|
Статус задачи на ручную загрузку прайс-листа. (В примерах встречаются значения `NEW`, `FAILURE`.)
||
||
`settings`
|
Настройки прайс-листа.
||
||
`settings.source`
|
Ссылка на загрузку прайс-листа.
||
||
`settings.delete_sale`
|
Признак. Удалять объявления, которые были созданы вручную или отсутствуют в прайс-листе.
||
||
`settings.leave_services`
|
Признак. Не удалять услуги объявлений, если они не были переданы в прайс-листе.
||
||
`settings.leave_added_images`
|
Признак. Не удалять загруженные вручную фотографии, если они не были переданы в прайс-листе.
||
||
`settings.is_active`
|
Признак. Активна или нет загрузка данного прайс-листа.
||
||
`count_offers`
|
Количество объявлений в прайс-листе.
||
||
`count_errors`
|
Количество объявлений с ошибками (объявления, которые не были обработаны).
||
||
`count_notices`
|
Количество объявлений с предупреждениями.
||
||
`count_offers_inserted`
|
Количество новых объявлений.
||
||
`count_offers_updated`
|
Количество обновленных объявлений.
||
||
`count_offers_deleted`
|
Количество удаленных объявлений.
||
||
`count_offers_skipped`
|
Количество необновленных объявлений.
||
||
`count_images`
|
Количество изображений в прайс-листе.
||
||
`count_images_success`
|
Количество успешно добавленных изображений.
||
||
`count_images_errors`
|
Количество незагруженных изображений.
||
||
`count_success`
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
> curl -i -X POST 'https://apiauto.ru/1.0/feeds/task/cars/NEW' \
> -H 'x-authorization: 2dtr...er432' \
> -H 'x-session-id: 112_ao...R02Tpv' \
> -H 'Content-Type:application/json' \
> -d {
>      "settings": {
>        "source": "https://dealer/auto/feed...",
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
>   "id": 12,
>   "created_at": "2019-06-19T15:41:35.750Z",
>   "finished_at": "2019-06-19T15:41:35.750Z",
>   "type": "AUTOMATIC",
>   "status": "NEW",
>   "settings": {
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

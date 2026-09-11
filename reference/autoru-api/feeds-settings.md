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

### Параметры ответа {#spec-output}

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

|#

> Описания полей выше подставлены вручную с живой страницы документации (2026-09-11) — в исходном экспорте Diplodoc эти поля были нерасшифрованными `{% include %}`-ссылками на отсутствующие файлы.

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

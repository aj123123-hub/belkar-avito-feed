---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/feeds-settings-cars-section.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# POST /feeds/settings/cars/{section}

Добавляет настройки прайс-листа для категории ТС «Легковые ТС». Операция используется, если вы автоматически загружаете прайс-листы на сайт для актуализации объявлений.

## Формат запроса {#input}

```
POST https://apiauto.ru/1.0/feeds/settings/cars/[section](*section)
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
  "source": {string},
  "delete_sale": {boolean},
  "leave_services": {boolean},
  "leave_added_images": {boolean},
  "is_active": {boolean}
}
```

<div class="params-table">

#|
||
##source##
|
Ссылка на загрузку прайс-листа.
||
||
##delete_sale##
|
Признак. Удалять объявления, которые были созданы вручную или отсутствует в прайс-листе.
||
||
##leave_services##
|
Признак. Не удалять услуги объявлений, если они не были переданы в прайс-листе.
||
||
##leave_added_images##
|
Признак. Не удалять загруженные вручную фотографии, если они не были переданы в прайс-листе.
||
||
##is_active##
|
Признак. Активна или нет загрузка данного прайс-листа.
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
 || 500 | INTERNAL SERVER ERROR | Внутренняя ошибка сервера. || 

|#

## Пример {#example-JSON}

> Запрос:
> 
> 
> ```http
> curl -i -X POST 'https://apiauto.ru/1.0/feeds/settings/cars/NEW' \
> -H 'x-authorization: 2dtr...er432' \
> -H 'x-session-id: 112_ao...R02Tpv' \
> -H 'Content-Type:application/json' \
> -d {
>      "source": "https://example-url/feed",
>      "delete_sale": true,
>      "leave_services": true,
>      "leave_added_images": true,
>      "is_active": true
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
>   "status": "SUCCESS"
> }                                     
> ```

{% include [table-style](../_includes/table-style-border-none-2a2aa0c324bf.md) %}

[*section]: {% include notitle [section](../_includes/popups-00286d1be377.md#section) %}


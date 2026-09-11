---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/put-calltracking-settings.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# PUT /calltracking/settings

Изменяет текущие настройки трекинга звонков.

## Формат запроса {#input}

```
PUT https://apiauto.ru/1.0/calltracking/settings
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

### Формат тела запроса {#structure-in}

```json
{
  "settings": {
    "calltracking_enabled": {boolean},
    "offers_stat_enabled": {boolean},
    "unique_call_period": {
      "days": {integer}
    },
    "target_call_duration": {
      "seconds": {integer}
    }
  }
}
```

<div class="params-table">

{% include notitle [settings](../_includes/params/get-calltracking-settings-6487fb730477.md#settings2) %}

 
:   {% include notitle [calltracking_enabled](../_includes/params/get-calltracking-settings-6487fb730477.md#calltracking_enabled) %}

    {% include notitle [offers_stat_enabled](../_includes/params/get-calltracking-settings-6487fb730477.md#offers_stat_enabled) %}

    {% include notitle [unique_call_period](../_includes/params/get-calltracking-settings-6487fb730477.md#unique_call_period) %}
    
     
    :   {% include notitle [days](../_includes/params/get-calltracking-settings-6487fb730477.md#days) %}

    {% include notitle [target_call_duration](../_includes/params/get-calltracking-settings-6487fb730477.md#target_call_duration) %}
    
     
    :   {% include notitle [seconds](../_includes/params/get-calltracking-settings-6487fb730477.md#seconds) %}

</div>

Общая структура ответа приведена ниже. Порядок следования элементов не гарантируется. В структуре могут присутствовать служебные параметры, которые не описаны в таблице.

## Формат ответа {#output-structure}

```json
{
  "settings": {
    "calltracking_enabled": {boolean},
    "offers_stat_enabled": {boolean},
    "unique_call_period": {
      "days": {integer}
    },
    "target_call_duration": {
      "seconds": {integer}
    }
  },
  "error": {string},
  "status": {string},
  "detailed_error": {string}
}
```

<div class="params-table">

{% include notitle [settings](../_includes/params/get-calltracking-settings-6487fb730477.md#settings) %}

 
:   {% include notitle [calltracking_enabled](../_includes/params/get-calltracking-settings-6487fb730477.md#calltracking_enabled) %}

    {% include notitle [offers_stat_enabled](../_includes/params/get-calltracking-settings-6487fb730477.md#offers_stat_enabled) %}

    {% include notitle [unique_call_period](../_includes/params/get-calltracking-settings-6487fb730477.md#unique_call_period) %}
    
     
    :   {% include notitle [days](../_includes/params/get-calltracking-settings-6487fb730477.md#days) %}

    {% include notitle [target_call_duration](../_includes/params/get-calltracking-settings-6487fb730477.md#target_call_duration) %}
    
     
    :   {% include notitle [seconds](../_includes/params/get-calltracking-settings-6487fb730477.md#seconds) %}

{% include notitle [error](../_includes/params/get-calltracking-settings-6487fb730477.md#error) %}

{% include notitle [status](../_includes/params/get-calltracking-settings-6487fb730477.md#status) %}

{% include notitle [detailed_error](../_includes/params/get-calltracking-settings-6487fb730477.md#detailed_error) %}

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
> curl -i -X PUT 'https://apiauto.ru/1.0/calltracking/settings' \ 
> -H 'x-dealer-id: 2dtrer432...' \
> -H 'x-session-id: 112_aoR02Tpv...' \
> -H 'Accept: application/json' \
> -d '{
>        "settings": {
>          "calltracking_enabled": true,
>          "offers_stat_enabled": true,
>          "unique_call_period": {
>            "days": 0
>          },
>          "target_call_duration": {
>            "seconds": 0
>          }
>        }
>      }'
> ```
> 
> 
> Ответ:
> 
> 
> ```json
> HTTP/1.1 200 OK
> Server: nginx
> Date: Tue, 24 Jul 2018 15:19:41 GMT
> Content-Type: application/json
> Connection: keep-alive
> 
> {
>   "settings": {
>     "calltracking_enabled": true,
>     "offers_stat_enabled": true,
>     "unique_call_period": {
>       "days": 0
>     },
>     "target_call_duration": {
>       "seconds": 0
>     }
>   },
>   "status": "SUCCESS"
> }
> ```

{% include [table-style](../_includes/table-style-border-none-2a2aa0c324bf.md) %}

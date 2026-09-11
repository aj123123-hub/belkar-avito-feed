---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/auction-place-bid.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# POST /dealer/auction/place-bid

Сделать ставку в аукционе.

## Формат запроса {#input}

```
POST https://apiauto.ru/1.0/dealer/auction/place-bid
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
  "bid": {string},
  "previous_bid": {string},
  "context": {
    "mark_code": {string},
    "model_code": {string}
  }
}
```

<div class="params-table">

{% include notitle [bid](../_includes/params/auction-place-bid-01f3c17884a2.md#bid) %}

{% include notitle [previous_bid](../_includes/params/auction-place-bid-01f3c17884a2.md#previous_bid) %}

{% include notitle [context](../_includes/params/auction-place-bid-01f3c17884a2.md#context) %}

 
:   {% include notitle [mark_code](../_includes/params/auction-place-bid-01f3c17884a2.md#mark_code) %}

    {% include notitle [model_code](../_includes/params/auction-place-bid-01f3c17884a2.md#model_code) %}

</div>

Общая структура ответа приведена ниже. Порядок следования элементов не гарантируется. В структуре могут присутствовать служебные параметры, которые не описаны в таблице.

## Формат ответа {#output-structure}

```json
{
  "status": {string}
}
```

#|
||
`status`
|
Статус ответа.
||
|#



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
 || 401 | NO_AUTH | Не удалось авторизовать пользователя по переданным данным. || 
 || 403 | AGENT_ACCESS_FORBIDDEN | Доступ для данного пользователя запрещен. || 
 || 500 | INTERNAL SERVER ERROR
UNKNOWN_ERROR | Внутренняя ошибка сервера. || 

|#

## Пример {#example-JSON}

> Запрос:
> 
> 
> ```http
> curl -X POST
> --header 'x-session-id: 14090654|1622...' 
> --header 'x-dealer-id: 16269' 
> -d '{ \ 
>  "bid": "470000", \ 
>  "previous_bid": "460000", \ 
>  "context": { \ 
>    "mark_code": "CADILLAC", \ 
>    "model_code": "SRX" \ 
>    } \ 
>  } \  
>  }' 'https://apiauto.ru/1.0/dealer/auction/place-bid'
> ```
> 
> 
> Ответ:
> 
> 
> ```json
> 
> {
>   "status": "SUCCESS"
> }                                     
> ```


{% include [table-style](../_includes/table-style-border-none-2a2aa0c324bf.md) %}

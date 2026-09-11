---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/dealer-account.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# GET /dealer/account

Возвращает баланс дилера.

## Формат запроса {#input}

```
GET https://apiauto.ru/1.0/dealer/account
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
  "account_id": {integer},
  "balance": {integer},
  "dealer_status": {string},
  "average_outcome": {integer},
  "rest_days": {integer}
}   
```

### Параметры ответа {#spec-output}

<div class="params-table">

{% include notitle [account_id](../_includes/params/dealer-account-669342ae8851.md#account_id) %}

{% include notitle [balance](../_includes/params/dealer-account-669342ae8851.md#balance) %}

{% include notitle [dealer_status](../_includes/params/dealer-account-669342ae8851.md#dealer_status) %}

{% include notitle [average_outcome](../_includes/params/dealer-account-669342ae8851.md#average_outcome) %}

{% include notitle [rest_days](../_includes/params/dealer-account-669342ae8851.md#rest_days) %}

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
> curl -i -X GET 'https://apiauto.ru/1.0/dealer/account' -H 'x-authorization: 2dtrer432...' -H 'Accept: application/json' -H 'x-session-id: 112_aoR02Tpv...'
> ```
> 
> 
> Ответ:
> 
> 
> ```json
> HTTP/1.1 200 OK
> Server: nginx
> Date: Wed, 11 Jul 2018 15:38:09 GMT
> Content-Type: application/json
> Connection: keep-alive
> 
> {
>   "account_id": "30829",
>   "balance": "907362",
>   "dealer_status": "ACTIVE",
>   "average_outcome": 1433,
>   "rest_days": 11
> }                                      
> ```

{% include [table-style](../_includes/table-style-border-none-2a2aa0c324bf.md) %}

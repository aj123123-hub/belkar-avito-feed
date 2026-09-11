---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/dealer-wallet-recharges.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# GET /dealer/wallet/recharges

Возвращает список пополнений кошелька.

## Формат запроса {#input}

```
GET https://apiauto.ru/1.0/dealer/wallet/recharges
? [from](*from)=<string>
& [[to](*to)=<string>]
& [[pageNum](*pageNum)=<integer>]
& [[pageSize](*pageSize)=<integer>]
```

<div class="params-table">

#|
|| ##from##[*](*req) | Начало интервала дат для поиска пополнений кошелька в формате `YYYY-MM-DD`. ||
|#


#|
|| ##to## | Конец интервала дат для поиска пополнений кошелька в формате `YYYY-MM-DD`. ||
|#


#|
|| ##pageNum## | Номер страницы, с которой необходимо начать вывод. Отсчет начинается с единицы. ||
|#


#|
|| ##pageSize## | Необходимое количество объектов на странице. ||
|#

</div>

\* Обязательный параметр

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
  "recharges": [
    {
      "timestamp": "{string}",
      "amount": "{string}"
    },
    {
      "timestamp": "{string}",
      "amount": "{string}"
    }
  ],
  "paging": {
    "page": {
      "num": {integer},
      "size": {integer}
    },
    "total": {integer},
    "page_count": {integer}
  },
  "status": "{string}"
}
```

<div class="params-table">

{% include notitle [recharges](../_includes/params/dealer-wallet-recharges-d6700a606256.md#recharges) %}

 
:   {% include notitle [timestamp](../_includes/params/dealer-wallet-recharges-d6700a606256.md#timestamp) %}

    {% include notitle [amount](../_includes/params/dealer-wallet-recharges-d6700a606256.md#amount) %}

{% include notitle [paging](../_includes/params/dealer-wallet-recharges-d6700a606256.md#paging) %}

 
:   {% include notitle [page](../_includes/params/dealer-wallet-recharges-d6700a606256.md#page) %}
    
     
    :   {% include notitle [num](../_includes/params/dealer-wallet-recharges-d6700a606256.md#num) %}

        {% include notitle [size](../_includes/params/dealer-wallet-recharges-d6700a606256.md#size) %}

    {% include notitle [total](../_includes/params/dealer-wallet-recharges-d6700a606256.md#total) %}

    {% include notitle [page_count](../_includes/params/dealer-wallet-recharges-d6700a606256.md#page_count) %}

{% include notitle [status](../_includes/params/dealer-wallet-recharges-d6700a606256.md#status) %}

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
> curl -i -X GET 'https://apiauto.ru/1.0/dealer/wallet/recharges?from=2018-06-01&to=2018-07-24&pageNum=1&pageSize=2' -H 'x-authorization: 2dtrer432...' -H 'Accept: application/json' -H 'x-session-id: 112_aoR02Tpv...'
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
>   "recharges": [
>     {
>       "timestamp": "2018-06-27T08:54:40.075Z",
>       "amount": "34324"
>     },
>     {
>       "timestamp": "2018-06-27T08:54:27.170Z",
>       "amount": "33333"
>     }
>   ],
>   "paging": {
>     "page": {
>       "num": 1,
>       "size": 2
>     },
>     "total": 4
>   },
>   "status": "SUCCESS"
> }
> ```

{% include [table-style](../_includes/table-style-border-none-2a2aa0c324bf.md) %}

[*from]: {% include notitle [from](../_includes/popups-00286d1be377.md#from) %}

[*to]: {% include notitle [to](../_includes/popups-00286d1be377.md#to) %}

[*pageNum]: {% include notitle [pageNum](../_includes/popups-00286d1be377.md#pageNum) %}

[*pageSize]: {% include notitle [pageSize](../_includes/popups-00286d1be377.md#pageSize) %}

[*req]: {% include notitle [req](../_includes/popups-00286d1be377.md#req) %}

---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/dealer-wallet-product-activations-daily-stats.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# GET /dealer/wallet/product/activations/daily-stats

Возвращает статистику списаний с кошелька за активацию услуг.

## Формат запроса {#input}

```
GET https://apiauto.ru/1.0/dealer/wallet/product/activations/daily-stats
? [service](*service)=<string>
& [from_dbt](*from_dbt)=<string>
& [[to_dbt](*to_dbt)=<string>]
& [[pageNum](*pageNum)=<integer>]
& [[pageSize](*pageSize)=<integer>]
```

<div class="params-table">

#|
||
##service##[*](*req)
|
Сервис для поиска списаний. Допустимые значения:

- `autoru` — Авто.ру;
- `autoservices` — автосервис.
||
|#

#|
|| ##from##[*](*req) | Начало интервала дат для поиска списаний с кошелька в формате `YYYY-MM-DD`. ||
|#


#|
|| ##to## | Конец интервала дат для поиска списаний с кошелька в формате `YYYY-MM-DD`. ||
|#


#|
|| ##pageNum## | Номер страницы, с которой необходимо начать вывод. Отсчет начинается с единицы. ||
|#


#|
|| ##pageSize## | Необходимое количество объектов на странице. ||
|#

{% include notitle [req](../_includes/popups-00286d1be377.md#req) %}

</div>

### Заголовки запроса {#headers}

#|
|| **Заголовок** | **Описание** ||
|| `x-dealer-id` | Идентификатор клиента. Используется для работы под учетной записью агентства. ||
|| `x-session-id` | Идентификатор сессии пользователя. Значение можно получить с помощью операции [POST /auth/login](https://yandex.ru/dev/autoru/doc/ru/reference/auth-login.md). ||
|#

Общая структура ответа приведена ниже. Порядок следования элементов не гарантируется. В структуре могут присутствовать служебные параметры, которые не описаны в таблице.

## Формат ответа {#output-structure}

```json
{
  "activation_stats": [
    {
      "date": "{string}",
      "product": "{string}",
      "sum": "{string}",
      "count": "{string}"
    },
    {
      "date": "{string}",
      "product": "{string}",
      "sum": "{string}",
      "count": "{string}"
    }
  ],
  "paging": {
    "page": {
      "num": {integer},
      "size": {integer}
    },
    "page_count": {integer}
  },
  "status": "{string}"
}    
```

<div class="params-table">

{% include notitle [activation_stats](../_includes/params/dealer-wallet-product-activations-daily-stats-39ad32e20353.md#activation_stats) %}

 
:   {% include notitle [date](../_includes/params/dealer-wallet-product-activations-daily-stats-39ad32e20353.md#date) %}

    {% include notitle [product](../_includes/params/dealer-wallet-product-activations-daily-stats-39ad32e20353.md#product) %}

    {% include notitle [sum](../_includes/params/dealer-wallet-product-activations-daily-stats-39ad32e20353.md#sum) %}

    {% include notitle [count](../_includes/params/dealer-wallet-product-activations-daily-stats-39ad32e20353.md#count) %}

{% include notitle [paging](../_includes/params/dealer-wallet-product-activations-daily-stats-39ad32e20353.md#paging) %}

 
:   {% include notitle [page](../_includes/params/dealer-wallet-product-activations-daily-stats-39ad32e20353.md#page) %}
    
     
    :   {% include notitle [num](../_includes/params/dealer-wallet-product-activations-daily-stats-39ad32e20353.md#num) %}

        {% include notitle [size](../_includes/params/dealer-wallet-product-activations-daily-stats-39ad32e20353.md#size) %}

    {% include notitle [page_count](../_includes/params/dealer-wallet-product-activations-daily-stats-39ad32e20353.md#page_count) %}

{% include notitle [status](../_includes/params/dealer-wallet-product-activations-daily-stats-39ad32e20353.md#status) %}


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
> curl -i -X GET 'https://apiauto.ru/1.0/dealer/wallet/product/activations/daily-stats?service=autoru&from=2018-06-01&to=2018-06-19&pageNum=1&pageSize=2' -H 'x-authorization: 2dtrer432...' -H 'Accept: application/json' -H 'x-session-id: 112_aoR02Tpv...'
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
>   "activation_stats": [
>     {
>       "date": "2018-06-19",
>       "product": "call",
>       "sum": "5000",
>       "count": "5"
>     },
>     {
>       "date": "2018-06-13",
>       "product": "placement",
>       "sum": "1220",
>       "count": "4"
>     }
>   ],
>   "paging": {
>     "page": {
>       "num": 1,
>       "size": 2
>     },
>     "page_count": 2
>   },
>   "status": "SUCCESS"
> }                   
> ```

{% include [table-style](../_includes/table-style-border-none-2a2aa0c324bf.md) %}

[*from_dbt]: {% include notitle [from_dbt](../_includes/popups-00286d1be377.md#from_dbt) %}

[*to_dbt]: {% include notitle [to_dbt](../_includes/popups-00286d1be377.md#to_dbt) %}

[*pageNum]: {% include notitle [pageNum](../_includes/popups-00286d1be377.md#pageNum) %}

[*pageSize]: {% include notitle [pageSize](../_includes/popups-00286d1be377.md#pageSize) %}

[*service]: {% include notitle [service-daily](../_includes/popups-00286d1be377.md#service-daily) %}

[*req]: {% include notitle [req](../_includes/popups-00286d1be377.md#req) %}

---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/stats-predict.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# POST /stats/predict

Возвращает оценочную стоимость транспортного средства на основании указанных параметров.

## Формат запроса {#input}

```
POST https://apiauto.ru/1.0/stats/predict
```

### Формат тела запроса {#structure-in}

```json
{
  "rid":{integer},
  "tech_param_id":{integer},
  "km_age":{integer},
  "color":{string},
  "owners_count":{integer},
  "year":{integer},
  "pts_original": {boolean},
  "steering_wheel": {array},
  "complectation_id": {integer},
  "seller_type": {array},
  "car_identifier":{integer},
  "super_gen_id": {integer}
}
```

<div class="params-table">

{% include notitle [rid](../_includes/params/stats-predict-4fbfac0fe3ef.md#rid) %}

{% include notitle [tech_param_id](../_includes/params/stats-predict-4fbfac0fe3ef.md#tech_param_id) %}

{% include notitle [km_age](../_includes/params/stats-predict-4fbfac0fe3ef.md#km_age) %}

{% include notitle [color](../_includes/params/stats-predict-4fbfac0fe3ef.md#color) %}

{% include notitle [owners_count](../_includes/params/stats-predict-4fbfac0fe3ef.md#owners_count) %}

{% include notitle [year](../_includes/params/stats-predict-4fbfac0fe3ef.md#year) %}

{% include notitle [pts_original](../_includes/params/stats-predict-4fbfac0fe3ef.md#pts_original) %}

{% include notitle [steering_wheel](../_includes/params/stats-predict-4fbfac0fe3ef.md#steering_wheel) %}

{% include notitle [complectation_id](../_includes/params/stats-predict-4fbfac0fe3ef.md#complectation_id) %}

{% include notitle [seller_type](../_includes/params/stats-predict-4fbfac0fe3ef.md#seller_type) %}

{% include notitle [car_identifier](../_includes/params/stats-predict-4fbfac0fe3ef.md#car_identifier) %}

{% include notitle [super_gen_id](../_includes/params/stats-predict-4fbfac0fe3ef.md#super_gen_id) %}

</div>

\* Обязательный параметр

Общая структура ответа приведена ниже. Порядок следования элементов не гарантируется. В структуре могут присутствовать служебные параметры, которые не описаны в таблице.

## Формат ответа {#output-structure}

```json
{
  "prices":{
    "autoru":{
      "from":{integer},
      "to":{integer},
      "currency":"{string}"
    },
    "tradein":{
      "from":{integer},
      "to":{integer},
      "currency":"{string}"
  },
  "evaluation_url": "string",
  "photos": {
    "{string}":"{string}",
    "{string}":"{string}",
    "{string}":"{string}"
  },
  "evaluation_hash": "{string}"
  },
  "used_rid": {integer},
  "status":"{string}"
}
```

<div class="params-table">

{% include notitle [prices](../_includes/params/stats-predict-4fbfac0fe3ef.md#prices) %}

 
:   {% include notitle [autoru](../_includes/params/stats-predict-4fbfac0fe3ef.md#autoru) %}

     
    :   {% include notitle [from](../_includes/params/stats-predict-4fbfac0fe3ef.md#from) %}

        {% include notitle [to](../_includes/params/stats-predict-4fbfac0fe3ef.md#to) %}

        {% include notitle [currency](../_includes/params/stats-predict-4fbfac0fe3ef.md#currency) %}

    {% include notitle [tradein](../_includes/params/stats-predict-4fbfac0fe3ef.md#tradein) %}

     
    :   {% include notitle [from](../_includes/params/stats-predict-4fbfac0fe3ef.md#from) %}

        {% include notitle [to](../_includes/params/stats-predict-4fbfac0fe3ef.md#to) %}

        {% include notitle [currency](../_includes/params/stats-predict-4fbfac0fe3ef.md#currency) %}

{% include notitle [evaluation_url](../_includes/params/stats-predict-4fbfac0fe3ef.md#evaluation_url) %}

{% include notitle [photos](../_includes/params/stats-predict-4fbfac0fe3ef.md#photos) %}

{% include notitle [evaluation_hash](../_includes/params/stats-predict-4fbfac0fe3ef.md#evaluation_hash) %}

{% include notitle [used_rid](../_includes/params/stats-predict-4fbfac0fe3ef.md#used_rid) %}

{% include notitle [status](../_includes/params/stats-predict-4fbfac0fe3ef.md#status) %}

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
 || 422 | UNPROCESSABLE_ENTITY | Невозможно получить ответ из-за логической ошибки. || 
 || 500 | INTERNAL SERVER ERROR | Внутренняя ошибка сервера. || 

|#

## Пример {#example-JSON}

> Запрос:
>
>
> ```http
> curl -i -X POST 'https://apiauto.ru/1.0/stats/predict' -H 'x-authorization: 2dtrer432...' -d '{"rid":213,"tech_param_id":2307294,"km_age":50000,"color":"040001","owners_count":3,"year":2006,"pts_original":true,"steering_wheel":"LEFT","complectation_id":0,"seller_type":"PRIVATE","car_identifier":"ХТА21124070445066","super_gen_id": 2307291}' -H 'Accept: application/json' -H 'Content-Type:application/json'
> ```
>
>
> Ответ:
>
>
> ```json
> HTTP/1.1 200 OK
> Server: envoy
> Date: Thu,14 Aug 2025 20:12:36 GMT 
> Content-Type: application/json
> Content-Length: 140
> Connection: keep-alive
>
> {
>   "prices": {
>     "autoru": {
>       "from": 104000,
>       "to": 196000,
>       "currency": "RUR"
>     },
>     "tradein": {
>       "from": 126000,
>       "to": 152000,
>       "currency": "RUR"
>   }
>   "evaluation_url": "https://auto.ru/evaluation/cars/?evaluation_id=b4adf90820a993399303cd58a7f284ac",
>   "photos": {
>     "main":"//avatars.mds.yandex.net/get-verba/216201/2a000001609a350783de0d3a8c593d7f8dd0/auto_main",
>   },
>   "evaluation_hash": "b4adf90820a993399303cd58a7f284ac"
>   },
>   "used_rid": 213,
>   "status":"SUCCESS" 
> }
> ```



{% include [table-style](../_includes/table-style-border-none-2a2aa0c324bf.md) %}

[*req]: {% include notitle [req](../_includes/popups-00286d1be377.md#req) %}

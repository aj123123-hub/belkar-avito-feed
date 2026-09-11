---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/stats-partner-predict-by-vin-or-lp.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# POST /stats/partner/predict_by_vin_or_lp

Возвращает оценочную стоимость транспортного средства на основании VIN или ГРЗ и информацию об автомобиле, которая найдена по VIN или ГРЗ.

## Формат запроса {#input}

```
POST https://apiauto.ru/1.0/stats/partner/predict_by_vin_or_lp
```

### Формат тела запроса {#structure-in}

```json
{
  "vin_or_lp":{string},
  "mileage":{integer},
  "geo_id":{integer},
  "seller_type":{string}
}
```

<div class="params-table">


{% include notitle [vin_or_lp](../_includes/params/stats-partner-predict-by-vin-or-lp-fdfa0994d582.md#vin_or_lp) %}

{% include notitle [mileage](../_includes/params/stats-partner-predict-by-vin-or-lp-fdfa0994d582.md#mileage) %}

{% include notitle [geo_id](../_includes/params/stats-partner-predict-by-vin-or-lp-fdfa0994d582.md#geo_id) %}

{% include notitle [seller_type](../_includes/params/stats-partner-predict-by-vin-or-lp-fdfa0994d582.md#seller_type) %}

</div>

\* Обязательный параметр

Общая структура ответа приведена ниже. Порядок следования элементов не гарантируется. В структуре могут присутствовать служебные параметры, которые не описаны в таблице.

## Формат ответа {#output-structure}

```json
{
    "price_range": {
      "from":{integer},
      "to":{integer}
    },
    "found_info":{
      "tech_param_id":{integer},
      "color":"{string}",
      "owners_count":{integer},
      "year":{integer},
      "pts_original":{boolean},
      "steering_wheel": "{string}",
      "complectation_id":{integer},
      "mark":"{string}",
      "model":"{string}",
      "super_gen_id":{integer},
      "configuration_id":{integer},
      "photos":{
        "{string}":"{string}",
        "{string}":"{string}",
        "{string}":"{string}"
      },
      "horse_power": {integer},
      "transmission": "{string}",
      "registered_in_russia": {boolean},
      "mileage": {integer},
      "geo_id": {integer},
      "geo_title": "{string}",
      "pts": "{string}"
    },
    "car_history": {
      "dtp_count":{integer},
      "has_fines":{boolean},
      "was_in_car_sharing":{boolean},
      "was_in_pledge":{boolean},
      "was_in_taxi":{boolean},
      "repair_max_total_cost":{integer},
      "registered_in_gibdd":{boolean}

    }
}
```

<div class="params-table">


{% include notitle [price_range](../_includes/params/stats-partner-predict-by-vin-or-lp-fdfa0994d582.md#price_range) %}

 
:   {% include notitle [from](../_includes/params/stats-partner-predict-by-vin-or-lp-fdfa0994d582.md#from) %}

    {% include notitle [to](../_includes/params/stats-partner-predict-by-vin-or-lp-fdfa0994d582.md#to) %}


{% include notitle [found_info](../_includes/params/stats-partner-predict-by-vin-or-lp-fdfa0994d582.md#found_info) %}

 
:   {% include notitle [tech_param_id](../_includes/params/stats-partner-predict-by-vin-or-lp-fdfa0994d582.md#tech_param_id) %}

    {% include notitle [color](../_includes/params/stats-partner-predict-by-vin-or-lp-fdfa0994d582.md#color) %}

    {% include notitle [owners_count](../_includes/params/stats-partner-predict-by-vin-or-lp-fdfa0994d582.md#owners_count) %}

    {% include notitle [year](../_includes/params/stats-partner-predict-by-vin-or-lp-fdfa0994d582.md#year) %}

    {% include notitle [pts_original](../_includes/params/stats-partner-predict-by-vin-or-lp-fdfa0994d582.md#pts_original) %}

    {% include notitle [steering_wheel](../_includes/params/stats-partner-predict-by-vin-or-lp-fdfa0994d582.md#steering_wheel) %}

    {% include notitle [complectation_id](../_includes/params/stats-partner-predict-by-vin-or-lp-fdfa0994d582.md#complectation_id) %}

    {% include notitle [mark](../_includes/params/stats-partner-predict-by-vin-or-lp-fdfa0994d582.md#mark) %}

    {% include notitle [model](../_includes/params/stats-partner-predict-by-vin-or-lp-fdfa0994d582.md#model) %}

    {% include notitle [super_gen_id](../_includes/params/stats-partner-predict-by-vin-or-lp-fdfa0994d582.md#super_gen_id) %}

    {% include notitle [configuration_id](../_includes/params/stats-partner-predict-by-vin-or-lp-fdfa0994d582.md#configuration_id) %}

    {% include notitle [photos](../_includes/params/stats-partner-predict-by-vin-or-lp-fdfa0994d582.md#photos) %}

    {% include notitle [horse_power](../_includes/params/stats-partner-predict-by-vin-or-lp-fdfa0994d582.md#horse_power) %}

    {% include notitle [transmission](../_includes/params/stats-partner-predict-by-vin-or-lp-fdfa0994d582.md#transmission) %}

    {% include notitle [registered_in_russia](../_includes/params/stats-partner-predict-by-vin-or-lp-fdfa0994d582.md#registered_in_russia) %}

    {% include notitle [mileage](../_includes/params/stats-partner-predict-by-vin-or-lp-fdfa0994d582.md#mileage) %}

    {% include notitle [geo_id](../_includes/params/stats-partner-predict-by-vin-or-lp-fdfa0994d582.md#geo_id) %}

    {% include notitle [geo_title](../_includes/params/stats-partner-predict-by-vin-or-lp-fdfa0994d582.md#geo_title) %}

    {% include notitle [pts](../_includes/params/stats-partner-predict-by-vin-or-lp-fdfa0994d582.md#pts) %}

{% include notitle [car_history](../_includes/params/stats-partner-predict-by-vin-or-lp-fdfa0994d582.md#car_history) %}

 
:   {% include notitle [dtp_count](../_includes/params/stats-partner-predict-by-vin-or-lp-fdfa0994d582.md#dtp_count) %}

    {% include notitle [has_fines](../_includes/params/stats-partner-predict-by-vin-or-lp-fdfa0994d582.md#has_fines) %}

    {% include notitle [was_in_car_sharing](../_includes/params/stats-partner-predict-by-vin-or-lp-fdfa0994d582.md#was_in_car_sharing) %}

    {% include notitle [was_in_pledge](../_includes/params/stats-partner-predict-by-vin-or-lp-fdfa0994d582.md#was_in_pledge) %}

    {% include notitle [was_in_taxi](../_includes/params/stats-partner-predict-by-vin-or-lp-fdfa0994d582.md#was_in_taxi) %}

    {% include notitle [repair_max_total_cost](../_includes/params/stats-partner-predict-by-vin-or-lp-fdfa0994d582.md#repair_max_total_cost) %}

    {% include notitle [registered_in_gibdd](../_includes/params/stats-partner-predict-by-vin-or-lp-fdfa0994d582.md#registered_in_gibdd) %}

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
||
200
|
OK
|
Успешный запрос.

{% note info %}

Такой ответ может быть получен, даже если найденной информации недостаточно, чтобы оценить авто.

{% endnote %}
||
||
202
|
IN_PROGRESS
|
VIN не был найден по заданному ГРЗ, и поиск продолжается. Нужно повторить запрос позже.
||
||
400
|
BAD_REQUEST
|
Ошибка в запросе: неверный VIN или ГРЗ.
||
||
404
|
NOT_FOUND
|
Не найдена информация по VIN или ГРЗ для этого автомобиля, или не найден VIN по ГРЗ.
||
 || 500 | INTERNAL SERVER ERROR | Внутренняя ошибка сервера. || 

|#

## Пример {#example-JSON}

> Запрос:
>
>
> ```http
> curl -i -X POST 'https://apiauto.ru/1.0/stats/partner/predict_by_vin_or_lp' -H 'x-authorization: 2dtrer432...' -d '{"vin_or_lp": "К286ТХ77", "mileage": 24000, "geo_id": 213, "seller_type": "PRIVATE"}' -H 'Accept: application/json' -H 'Content-Type:application/json'
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
>     "price_range": {
>       "from": 0,
>       "to": 0,
>     },
>     "found_info": {
>       "tech_param_id": 20532706,
>       "color": "FAFBFB",
>       "owners_count": 2,
>       "year": 2016,
>       "pts_original": true,
>       "steering_wheel": "LEFT",
>       "complectation_id": 21034571
>       "mark": "MITSUBISHI",
>       "model": "ECLIPSE",
>       "super_gen_id": 21107295,
>       "configuration_id": 2305627,
>       "photos": {
>         "main":"//avatars.mds.yandex.net/get-verba/216201/2a000001609a350783de0d3a8c593d7f8dd0/auto_main",
>       },
>       "horse_power": 140,
>       "transmission": "MECHANICAL",
>       "registered_in_russia": true,
>       "mileage": 0,
>       "geo_id": 213,
>       "geo_title": "Москва",
>       "pts": "ORIGINAL"
>     },
>     "car_history": {
>       "dtp_count": 0,
>       "has_fines": true,
>       "was_in_car_sharing": true,
>       "was_in_pledge": true,
>       "was_in_taxi": true,
>       "repair_max_total_cost": 0,
>       "registered_in_gibdd": true,
> }
> ```


{% include [table-style](../_includes/table-style-border-none-2a2aa0c324bf.md) %}

[*req]: {% include notitle [req](../_includes/popups-00286d1be377.md#req) %}


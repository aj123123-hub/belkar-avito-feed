---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/catalog-category-complectations.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# GET /reference/catalog/cars/complectations

Возвращает список комплектаций с ценой и опциями.

## Формат запроса {#input}

```
GET https://apiauto.ru/1.0/reference/catalog/cars/complectations
? [tech_param_id](*tech_param_id)=<integer>
```

<div class="params-table">

#|
||
##tech_param_id##[*](*req)
|
{% include notitle [tech_param_id](../_includes/popups-00286d1be377.md#tech_param_id-description) %}
||
|#

</div>

{% include notitle [req](../_includes/popups-00286d1be377.md#req) %}


Общая структура ответа приведена ниже. Порядок следования элементов не гарантируется. В структуре могут присутствовать служебные параметры, которые не описаны в таблице.

## Формат ответа {#output-structure}

```json
{
  "entities": [
    {
      "complectation": {
        "id": "{string}",
        "name": "{string}",
        "available_options": [
          "{string}"
        ],
        "additional_options": {
          "name": {
            "price": {double},
            "currency": "{string}",
            "rur_price": {double},
            "usd_price": {double},
            "eur_price": {double}
          }
        },
        "[price](*price_info_complectation_ph)": {
          "tech_param_id": {
          "[price](*price_complectation_ph)": {double},
            "currency": "{string}",
            "rur_price": {double},
            "usd_price": {double},
            "eur_price": {double}
          }
        },
        "aliases": [
          "{string}"
        ]
      }
    }
  ]
}
```

<div class="params-table">

{% include notitle [entities](../_includes/params/reference-catalog-cars-complectations-0ce9b6f91aa4.md#entities) %}

 
:   {% include notitle [complectation](../_includes/params/reference-catalog-cars-complectations-0ce9b6f91aa4.md#complectation) %}

     
    :   {% include notitle [id](../_includes/params/reference-catalog-cars-complectations-0ce9b6f91aa4.md#id) %}

        {% include notitle [name](../_includes/params/reference-catalog-cars-complectations-0ce9b6f91aa4.md#name) %}

        {% include notitle [available_options](../_includes/params/reference-catalog-cars-complectations-0ce9b6f91aa4.md#available_options) %}

        {% include notitle [additional_options](../_includes/params/reference-catalog-cars-complectations-0ce9b6f91aa4.md#additional_options) %}

         
        :   {% include notitle [name](../_includes/params/reference-catalog-cars-complectations-0ce9b6f91aa4.md#name-option) %}

             
            :   {% include notitle [price](../_includes/params/reference-catalog-cars-complectations-0ce9b6f91aa4.md#price_option) %}

                {% include notitle [currency](../_includes/params/reference-catalog-cars-complectations-0ce9b6f91aa4.md#currency) %}

                {% include notitle [rur_price](../_includes/params/reference-catalog-cars-complectations-0ce9b6f91aa4.md#rur_price) %}

                {% include notitle [usd_price](../_includes/params/reference-catalog-cars-complectations-0ce9b6f91aa4.md#usd_price) %}

                {% include notitle [eur_price](../_includes/params/reference-catalog-cars-complectations-0ce9b6f91aa4.md#eur_price) %}

    {% include notitle [price](../_includes/params/reference-catalog-cars-complectations-0ce9b6f91aa4.md#price_complectation) %}

     
    :   {% include notitle [tech_param_id](../_includes/params/reference-catalog-cars-complectations-0ce9b6f91aa4.md#tech_param_id) %}

         
        :   {% include notitle [price](../_includes/params/reference-catalog-cars-complectations-0ce9b6f91aa4.md#price) %}

            {% include notitle [currency](../_includes/params/reference-catalog-cars-complectations-0ce9b6f91aa4.md#currency) %}

            {% include notitle [rur_price](../_includes/params/reference-catalog-cars-complectations-0ce9b6f91aa4.md#rur_price) %}

            {% include notitle [usd_price](../_includes/params/reference-catalog-cars-complectations-0ce9b6f91aa4.md#usd_price) %}

            {% include notitle [eur_price](../_includes/params/reference-catalog-cars-complectations-0ce9b6f91aa4.md#eur_price) %}

    {% include notitle [aliases](../_includes/params/reference-catalog-cars-complectations-0ce9b6f91aa4.md#aliases) %}

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
 || 500 | INTERNAL SERVER ERROR | Внутренняя ошибка сервера. || 

|#

## Пример {#example-JSON}

> Запрос:
> 
> 
> ```http
> curl -i -X GET 'https://apiauto.ru/1.0/reference/catalog/cars/complectations?tech_param_id=20680649' -H 'x-authorization: 2dtrer432...' -H 'Accept: application/json'
> ```
> 
> 
> Ответ:
> 
> 
> ```json
> HTTP/1.1 200 OK
> Server: nginx
> Date: Thu, 02 Aug 2018 15:19:41 GMT
> Content-Type: application/json
> Connection: keep-alive
>                     
> {
>   "entities": [
>     {
>       "complectation": {
>         "id": "20959513",
>         "name": "DC Intense",
>         "available_options": [
>           "cruise-control",
>           "multi-wheel",
>           "airbag-passenger",
>           "lock",
>           "electro-mirrors",
>           "mirrors-heat",
>           "computer",
>           "wheel-power",
>           "fabric-seats",
>           "airbag-rear-side",
>           "airbag-side",
>           "abs",
>           "wheel-leather",
>           "auto-mirrors",
>           "esp",
>           "usb",
>           "audiopreparation",
>           "ashtray-and-cigarette-lighter",
>           "front-centre-armrest",
>           "electro-window-back",
>           "actual",
>           "16-inch-wheels",
>           "climate-control",
>           "audiosystem",
>           "knee-airbag",
>           "airbag-driver",
>           "isofix",
>           "electro-window-front",
>           "hcc",
>           "leather-gear-stick",
>           "ptf",
>           "front-seats-heat",
>           "bluetooth",
>           "wheel-configuration2",
>           "wheel-configuration1",
>           "immo",
>           "12v-socket"
>         ],
>         "additional_options": {
>           "paint-metallic": {
>             "price": 19000,
>             "currency": "RUR",
>             "rur_price": 19000,
>             "usd_price": 300,
>             "eur_price": 258,
>             "dprice": 19000,
>             "rur_dprice": 19000,
>             "usd_dprice": 300,
>             "eur_dprice": 258
>           }
>         },
>         "price": {
>           "20680649": {
>             "price": 2253000,
>             "currency": "RUR",
>             "rur_price": 2253000,
>             "usd_price": 35684,
>             "eur_price": 30686,
>             "dprice": 2253000,
>             "rur_dprice": 2253000,
>             "usd_dprice": 35684,
>             "eur_dprice": 30686
>           }
>         },
>         "aliases": [
>             "basу",
>             "base",
>             "basic",
>             "basis"
>         ]
>       }
>     },
>     {
>       "complectation": {
>         "id": "20959518",
>         "name": "Intense",
>         "available_options": [
>           "cruise-control",
>           "multi-wheel",
>           "airbag-passenger",
>           "lock",
>           "electro-mirrors",
>           "mirrors-heat",
>           "computer",
>           "wheel-power",
>           "fabric-seats",
>           "airbag-rear-side",
>           "airbag-side",
>           "abs",
>           "wheel-leather",
>           "auto-mirrors",
>           "esp",
>           "usb",
>           "audiopreparation",
>           "ashtray-and-cigarette-lighter",
>           "front-centre-armrest",
>           "electro-window-back",
>           "actual",
>           "16-inch-wheels",
>           "climate-control",
>           "audiosystem",
>           "knee-airbag",
>           "airbag-driver",
>           "isofix",
>           "electro-window-front",
>           "hcc",
>           "leather-gear-stick",
>           "ptf",
>           "front-seats-heat",
>           "bluetooth",
>           "wheel-configuration2",
>           "wheel-configuration1",
>           "immo",
>           "12v-socket"
>         ],
>         "additional_options": {
>           "paint-metallic": {
>             "price": 19000,
>             "currency": "RUR",
>             "rur_price": 19000,
>             "usd_price": 300,
>             "eur_price": 258,
>             "dprice": 19000,
>             "rur_dprice": 19000,
>             "usd_dprice": 300,
>             "eur_dprice": 258
>           }
>         },
>         "price": {
>           "20680649": {
>             "price": 2199990,
>             "currency": "RUR",
>             "rur_price": 2199990,
>             "usd_price": 34845,
>             "eur_price": 29964,
>             "dprice": 2199990,
>             "rur_dprice": 2199990,
>             "usd_dprice": 34845,
>             "eur_dprice": 29964
>           }
>         },
>         "aliases": [
>             "fv307l",
>             "базовая",
>             "basis line"
>         ]
>       }
>     }
>   ]
> }                                             
> ```

{% include [table-style](../_includes/table-style-border-none-2a2aa0c324bf.md) %}


[*tech_param_id]: {% include notitle [tech_param_id](../_includes/popups-00286d1be377.md#tech_param_id-description) %}

[*req]: {% include notitle [req](../_includes/popups-00286d1be377.md#req) %}

[*price_complectation_ph]: {% include notitle [price_complectation_ph](../_includes/popups-00286d1be377.md#price_complectation_ph) %}

[*price_info_complectation_ph]: {% include notitle [price_info_complectation_ph](../_includes/popups-00286d1be377.md#price_info_complectation_ph) %}

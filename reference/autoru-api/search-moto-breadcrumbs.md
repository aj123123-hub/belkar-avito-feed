---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/search-moto-breadcrumbs.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# GET /search/moto/breadcrumbs

Возвращает информацию о структуре каталога мототранспорта и количестве активных объявлений на различных уровнях (тип мототранспорта, марка и модель).

## Формат запроса {#input}

```
GET https://apiauto.ru/1.0/search/moto/breadcrumbs
? [[bc_lookup](*bc_lookup)=<array[string]>]
& [[rid](*rid)=<array[string]>]
& [[state](*state)=<array[string]>]
```

<div class="params-table">

#|
||
##bc_lookup##
|
{% include notitle [bc_lookup-moto](../_includes/popups-00286d1be377.md#bc_lookup-moto) %}
||
||
##rid##
|
{% include notitle [rid-cars-breadcrumbs](../_includes/popups-00286d1be377.md#rid-cars-breadcrumbs) %}
||
||
##state##
|
{% include [includes-state-description](../_includes/reference/includes/id-includes/state-description-78e689139d95.md) %}
||
|#

</div>

Общая структура ответа приведена ниже. Порядок следования элементов не гарантируется. В структуре могут присутствовать служебные параметры, которые не описаны в таблице.

## Формат ответа {#output-structure}

{% cut "Общая структура" %} {#abstract}

```json
{
  "breadcrumbs":[
    {
      "entities":[
        {
          ...
        },
        {
          ...
        }
      ],
      "meta_level":"{string}",  /* MODEL_LEVEL */
      "mark":{
        ...
      }
    },
    {
    "entities":[
        {
          ...
        },
        {
          ...
        }
      ],
      "meta_level":"{string}"  /* MARK_LEVEL */
    },
    {
      "entities":[
        {
          ...
        },
        {
          ...
        }
      ],
      "meta_level":"{string}"  /* TYPE_LEVEL */
    }
  ],
  "status":"{string}"
}
```

<div class="params-table">

{% include notitle [breadcrumbs](../_includes/params/moto-breadcrumbs-common-3b071c77fb6b.md#breadcrumbs) %}

 
:   {% include notitle [entities](../_includes/params/moto-breadcrumbs-common-3b071c77fb6b.md#entities) %}

    {% include notitle [meta_level](../_includes/params/moto-breadcrumbs-common-3b071c77fb6b.md#meta_level) %}

    {% include notitle [mark](../_includes/params/moto-breadcrumbs-common-3b071c77fb6b.md#mark) %}

{% include notitle [status](../_includes/params/moto-breadcrumbs-common-3b071c77fb6b.md#status) %}

</div>

{% endcut %}

{% cut "Уровень иерархии «MODEL»" %} {#model}

```json
    {
      "entities":[
        {
          "id":"{string}",
          "name":"{string}",
          "offers_count":{integer},
          "is_popular":{boolean},
          "model":{
            "moto_functions":[
              "{string}",
              "{string}"
            ],
            "default_configuration_id":"{string}",
            "nameplates":[
              {
                "name":"{string}",
                "code":"{string}",
                "autoru_id":"{string}",
                "offers_count":{integer}
              },
              {
                ...
              }
            ],
            "photo":{
              "name":"{string}",
              "sizes":{
                "{string}":"{string}",
                "{string}":"{string}"
              }
            },
            "cyrillic_name":"{string}"
          },
          "reviews_count": {integer}
        },
        {
          ...
        }
      ],
      "meta_level":"{string}",  /* MODEL_LEVEL */
      "mark":{
        "id":"{string}",
        "name":"{string}",
        "offers_count":{integer},
        "is_popular":{boolean}, 
        "[mark](*mark_ph)":{
          "logo":{
            "name":"{string}",
            "sizes":{
              "{string}":"{string}",
              "{string}":"{string}"
            }
          },
          "vendor_ids":[
            {integer},
            {integer}
          ],
          "cyrillic_name":"{string}"
        },
        "reviews_count": {integer}
      }
    }
```

<div class="params-table">

{% include notitle [entities](../_includes/params/moto-breadcrumbs-model-e88b2399f4de.md#entities) %}

 
:   {% include notitle [id_model](../_includes/params/moto-breadcrumbs-model-e88b2399f4de.md#id_model) %}

    {% include notitle [name_model](../_includes/params/moto-breadcrumbs-model-e88b2399f4de.md#name_model) %}

    {% include notitle [offers_count_model](../_includes/params/moto-breadcrumbs-model-e88b2399f4de.md#offers_count_model) %}

    {% include notitle [is_popular_model](../_includes/params/moto-breadcrumbs-model-e88b2399f4de.md#is_popular_model) %}

    {% include notitle [model](../_includes/params/moto-breadcrumbs-model-e88b2399f4de.md#model) %}

     
    :   {% include notitle [default_configuration_id](../_includes/params/moto-breadcrumbs-model-e88b2399f4de.md#default_configuration_id) %}

        {% include notitle [nameplates](../_includes/params/moto-breadcrumbs-model-e88b2399f4de.md#nameplates) %}
        
         
        :   {% include notitle [name_model_type](../_includes/params/moto-breadcrumbs-model-e88b2399f4de.md#name_model_type) %}

            {% include notitle [code](../_includes/params/moto-breadcrumbs-model-e88b2399f4de.md#code) %}

            {% include notitle [autoru_id](../_includes/params/moto-breadcrumbs-model-e88b2399f4de.md#autoru_id) %}

            {% include notitle [offers_count](../_includes/params/moto-breadcrumbs-model-e88b2399f4de.md#offers_count) %}

        {% include notitle [moto_functions](../_includes/params/moto-breadcrumbs-model-e88b2399f4de.md#moto_functions) %}

        {% include notitle [photo](../_includes/params/moto-breadcrumbs-model-e88b2399f4de.md#photo) %}

         
        :   {% include notitle [name_photo](../_includes/params/moto-breadcrumbs-model-e88b2399f4de.md#name_photo) %}

            {% include notitle [sizes](../_includes/params/moto-breadcrumbs-model-e88b2399f4de.md#sizes) %}

        {% include notitle [cyrillic_name_model](../_includes/params/moto-breadcrumbs-model-e88b2399f4de.md#cyrillic_name_model) %}

    {% include notitle [reviews_count_model](../_includes/params/moto-breadcrumbs-model-e88b2399f4de.md#reviews_count_model) %}

{% include notitle [meta_level](../_includes/params/moto-breadcrumbs-model-e88b2399f4de.md#meta_level) %}

{% include notitle [mark](../_includes/params/moto-breadcrumbs-model-e88b2399f4de.md#mark-common) %}

 
:   {% include notitle [id_mark](../_includes/params/moto-breadcrumbs-model-e88b2399f4de.md#id_mark) %}

    {% include notitle [name_mark](../_includes/params/moto-breadcrumbs-model-e88b2399f4de.md#name_mark) %}

    {% include notitle [offers_count_mark](../_includes/params/moto-breadcrumbs-model-e88b2399f4de.md#offers_count_mark) %}

    {% include notitle [is_popular_mark](../_includes/params/moto-breadcrumbs-model-e88b2399f4de.md#is_popular_mark) %}

    {% include notitle [mark](../_includes/params/moto-breadcrumbs-model-e88b2399f4de.md#mark) %}

     
    :   {% include notitle [logo](../_includes/params/moto-breadcrumbs-model-e88b2399f4de.md#logo) %}

         
        :   {% include notitle [name](../_includes/params/moto-breadcrumbs-model-e88b2399f4de.md#name) %}

            {% include notitle [sizes](../_includes/params/moto-breadcrumbs-model-e88b2399f4de.md#sizes) %}

        {% include notitle [vendor_ids](../_includes/params/moto-breadcrumbs-model-e88b2399f4de.md#vendor_ids) %}

        {% include notitle [cyrillic_name_mark](../_includes/params/moto-breadcrumbs-model-e88b2399f4de.md#cyrillic_name_mark) %}

    {% include notitle [reviews_count_mark](../_includes/params/moto-breadcrumbs-model-e88b2399f4de.md#reviews_count_mark) %}

</div>

{% endcut %}

{% cut "Уровень иерархии «MARK»" %} {#mark}

```json
    {
      "entities":[
        {
          "id":"{string}",
          "name":"{string}",
          "offers_count":{integer},
          "is_popular":{boolean}, 
          "mark":{
            "logo":{
              "name":"{string}",
              "sizes":{
                "{string}":"{string}",
                "{string}":"{string}"
              }
            },
            "vendor_ids":[
              {integer},
              {integer}
            ],
            "cyrillic_name":"{string}"
          },
          "reviews_count": {integer}
        },
        {
          ...
        }
      ],
      "meta_level":"{string}",  /* MARK_LEVEL */
    }
```

<div class="params-table">

{% include notitle [entities](../_includes/params/moto-breadcrumbs-mark-6eba784e940a.md#entities) %}

 
:   {% include notitle [id_mark](../_includes/params/moto-breadcrumbs-mark-6eba784e940a.md#id_mark) %}

    {% include notitle [name_mark](../_includes/params/moto-breadcrumbs-mark-6eba784e940a.md#name_mark) %}

    {% include notitle [offers_count_mark](../_includes/params/moto-breadcrumbs-mark-6eba784e940a.md#offers_count_mark) %}

    {% include notitle [is_popular_mark](../_includes/params/moto-breadcrumbs-mark-6eba784e940a.md#is_popular_mark) %}

    {% include notitle [mark](../_includes/params/moto-breadcrumbs-mark-6eba784e940a.md#mark) %}

     
    :   {% include notitle [logo](../_includes/params/moto-breadcrumbs-mark-6eba784e940a.md#logo) %}
        
         
        :   {% include notitle [name_photo](../_includes/params/moto-breadcrumbs-mark-6eba784e940a.md#name_photo) %}

            {% include notitle [sizes](../_includes/params/moto-breadcrumbs-mark-6eba784e940a.md#sizes) %}

        {% include notitle [vendor_ids](../_includes/params/moto-breadcrumbs-mark-6eba784e940a.md#vendor_ids) %}

        {% include notitle [cyrillic_name_mark](../_includes/params/moto-breadcrumbs-mark-6eba784e940a.md#cyrillic_name_mark) %}

    {% include notitle [reviews_count_mark](../_includes/params/moto-breadcrumbs-mark-6eba784e940a.md#reviews_count_mark) %}

{% include notitle [meta_level](../_includes/params/moto-breadcrumbs-mark-6eba784e940a.md#meta_level) %}

</div>

{% endcut %}

{% cut "Уровень иерархии «TYPE»" %} {#type}

```json
    {
      "entities":[
        {
          "id":"{string}",
          "name":"{string}",
          "offers_count":{integer},
          "reviews_count": {integer}
        },
        {
          ...
        }
      ],
      "meta_level":"{string}",  /* TYPE_LEVEL */
    }
```

<div class="params-table">

{% include notitle [entities](../_includes/params/moto-breadcrumbs-type-e80d5081c570.md#entities) %}

 
:   {% include notitle [id](../_includes/params/moto-breadcrumbs-type-e80d5081c570.md#id) %}

    {% include notitle [name](../_includes/params/moto-breadcrumbs-type-e80d5081c570.md#name) %}

    {% include notitle [offers_count](../_includes/params/moto-breadcrumbs-type-e80d5081c570.md#offers_count) %}

    {% include notitle [reviews_count](../_includes/params/moto-breadcrumbs-type-e80d5081c570.md#reviews_count) %}

{% include notitle [meta_level](../_includes/params/moto-breadcrumbs-type-e80d5081c570.md#meta_level) %}

</div>

{% endcut %}

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
> curl -i -X GET 'https://apiauto.ru/1.0/search/moto/breadcrumbs?bc_lookup=MOTORCYCLE%23HONDA%23&state=USED&state=NEW&rid=213' -H 'x-authorization: 2dtrer432...'
> ```
> 
> 
> Ответ:
> 
> 
> ```json
> HTTP/1.1 200 OK
> Server: nginx
> Date: Wed, 06 Sep 2017 13:35:57 GMT
> Content-Type: application/json
> Content-Length: 44208
> Connection: keep-alive
> 
> { 
>   "breadcrumbs":[
>     {
>       "entities":[
>         {
>           "id":"B120_WRAITH",
>           "name":"B120 Wraith",
>           "model":{
>             "moto_functions":[
>               "cruiser"
>             ],
>             "photo":{
>               "name":"model-photo",
>               "sizes":{
>                 "main":"//avatafdg3441019/mobile",
>                 "mini-card":"//avatargre3432019/minicard"
>               }
>             }
>           }
>         },
>         {
>           "id":"F124_HELLCAT",
>           "name":"F124 Hellcat",
>           "model":{
>             "moto_functions":[
>               "cruiser"
>             ],
>             "photo":{
>               "name":"model-photo",
>               "sizes":{
>                 "main":"//avatartg149404354/mobile",
>                 "mini-card":"//avatar453f/minicard"
>               }
>             }
>           }
>         },
>         {
>           ...
>         }
>       ],
>       "meta_level":"MODEL_LEVEL",
>       "mark":{
>         "id":"CONFEDERATE",
>         "name":"Confederate",
>         "mark":{
>           "logo":{
>             "name":"mark-logo",
>             "sizes":{
>               "logo":"//avatar4tr144gdf437/logo"
>             }
>           }
>         }
>       }
>     },
>     {
>       "entities":[
>         {
>           "id":"ABM",
>           "name":"ABM",
>           "offers_count":5,
>           "mark":{
>             "logo":{
>               "name":"mark-logo",
>               "sizes":{
>                 "logo":"//avataralogrt344/logo"
>               }
>             }
>           }
>         },
>         {
>           ...
>         },
>         {
>           "id":"DODGE",
>           "name":"Dodge",
>           "is_popular":true,
>           "mark":{
>             "logo":{
>               "name":"mark-logo",
>               "sizes":{
>       	   "logo":"//avatar45fd418/logo"
>       	 }
>             }
>           }
>         },
>         {
>           "id":"DUCATI",
>           "name":"Ducati",
>           "offers_count": 267,
>           "mark":{
>             "logo":{
>               "name":"mark-logo",
>               "sizes":{
>       	   "logo":"//avatarrfg.11134f41/logo"
>       	 }
>             }
>           }
>         },
>         {
>           "id":"E_V_A_",
>           "name":"E.V.A.",
>           "mark":{
>             "logo":{
>               "name":"mark-logo"
>             }
>           }
>         },
>         {
>           "id":"URAL",
>           "name":"Урал",
>           "offers_count": 65,
>           "mark":{
>             "logo":{
>               "name":"mark-logo",
>               "sizes":{
>       	   "logo":"//avatar45fd20/logo"
>       	 }
>             }
>           }
>         }
>       ],
>       "meta_level":"MARK_LEVEL"
>     },
>     {
>       "entities":[
>         {
>           "id":"ATV",
>           "name":"Мотовездеход",
>           "offers_count": 882
>         },
>         {
>           "id":"MOTORCYCLE",
>           "name":"Мотоцикл",
>           "offers_count": 9371
>         },
>         {
>           "id":"SCOOTERS",
>           "name":"Скутер",
>           "offers_count": 1799
>         },
>         {
>           "id":"SNOWMOBILE",
>           "name":"Снегоход",
>           "offers_count": 172
>         }
>       ],
>       "meta_level":"TYPE_LEVEL"
>     }
>   ],
>   "status":"SUCCESS"
> }            
> ```


{% include [border-none](../_includes/table-style-border-none-2a2aa0c324bf.md) %}


[*bc_lookup]: {% include notitle [bc_lookup-moto](../_includes/popups-00286d1be377.md#bc_lookup-moto) %}

[*rid]: {% include notitle [rid-cars-breadcrumbs](../_includes/popups-00286d1be377.md#rid-cars-breadcrumbs) %}

[*state]: {% include [includes-state-description](../_includes/reference/includes/id-includes/state-description-78e689139d95.md) %}

[*mark_ph]: {% include notitle [mark_ph](../_includes/popups-00286d1be377.md#mark_ph) %}

---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/search-trucks-breadcrumbs.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# GET /search/trucks/breadcrumbs

Возвращает информацию о структуре каталога коммерческого транспорта и количестве активных объявлений на различных уровнях (тип коммерческого транспорта, марка и модель).

## Формат запроса {#input}

```
GET https://apiauto.ru/1.0/search/trucks/breadcrumbs
? [[bc_lookup](*bc_lookup)=<array[string]>]
& [[rid](*rid)=<array[string]>]
& [[state](*state)=<array[string]>]
```

<div class="params-table">

#|
||
##bc_lookup##
|
{% include notitle [bc_lookup-trucks](../_includes/popups-00286d1be377.md#bc_lookup-trucks) %}
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
      "meta_level":"{string}",  /* GENERATION_LEVEL */
      "mark":{
        ...
      },
      "model":{
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

{% include notitle [breadcrumbs](../_includes/params/trucks-breadcrumbs-common-d804c0cb93f2.md#breadcrumbs) %}

 
:   {% include notitle [entities](../_includes/params/trucks-breadcrumbs-common-d804c0cb93f2.md#entities) %}

    {% include notitle [meta_level](../_includes/params/trucks-breadcrumbs-common-d804c0cb93f2.md#meta_level) %}

    {% include notitle [mark](../_includes/params/trucks-breadcrumbs-common-d804c0cb93f2.md#mark) %}    

    {% include notitle [model](../_includes/params/trucks-breadcrumbs-common-d804c0cb93f2.md#model) %}

{% include notitle [status](../_includes/params/trucks-breadcrumbs-common-d804c0cb93f2.md#status) %}

</div>

{% endcut %}

{% cut "Уровень иерархии «GENERATION»" %} {#generation}

```json
    {
      "entities":[
        {
          "id":"{string}",
          "name":"{string}",
          "offers_count":{integer},
          "is_popular":{boolean},
          "super_gen":{
            "year_from":,
            "year_to":,
            "is_restyle":{boolean},
            "default_configuration_id":"{string}",
            "photo":{
              "name":"{string}",
              "sizes":{
                "{string}":"{string}",
                "{string}":"{string}"
              }
            }
          },
          "reviews_count": {integer}
        },
        {
          ...
        }
      ],
      "meta_level":"{string}",  /* GENERATION_LEVEL */
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
      },
      "model":{
        "id":"{string}",
        "name":"{string}",
        "offers_count":{integer},
        "is_popular":{boolean},
        "[model](*model_ph)":{
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
      }
    }
```

<div class="params-table">

{% include notitle [entities](../_includes/params/trucks-breadcrumbs-generation-696450a616a2.md#entities) %}

 
:   {% include notitle [id_gen](../_includes/params/trucks-breadcrumbs-generation-696450a616a2.md#id_gen) %}

    {% include notitle [name_gen](../_includes/params/trucks-breadcrumbs-generation-696450a616a2.md#name_gen) %}

    {% include notitle [offers_count_gen](../_includes/params/trucks-breadcrumbs-generation-696450a616a2.md#offers_count_gen) %}

    {% include notitle [is_popular_gen](../_includes/params/trucks-breadcrumbs-generation-696450a616a2.md#is_popular_gen) %}

    {% include notitle [super_gen](../_includes/params/trucks-breadcrumbs-generation-696450a616a2.md#super_gen) %}

     
    :   {% include notitle [year_from](../_includes/params/trucks-breadcrumbs-generation-696450a616a2.md#year_from) %}

        {% include notitle [year_to](../_includes/params/trucks-breadcrumbs-generation-696450a616a2.md#year_to) %}

        {% include notitle [is_restyle](../_includes/params/trucks-breadcrumbs-generation-696450a616a2.md#is_restyle) %}

        {% include notitle [default_configuration_id](../_includes/params/trucks-breadcrumbs-generation-696450a616a2.md#default_configuration_id) %}

        {% include notitle [photo](../_includes/params/trucks-breadcrumbs-generation-696450a616a2.md#photo) %}

         
        :   {% include notitle [name_photo](../_includes/params/trucks-breadcrumbs-generation-696450a616a2.md#name_photo) %}

            {% include notitle [sizes](../_includes/params/trucks-breadcrumbs-generation-696450a616a2.md#sizes) %}

    {% include notitle [reviews_count_gen](../_includes/params/trucks-breadcrumbs-generation-696450a616a2.md#reviews_count_gen) %}

{% include notitle [meta_level](../_includes/params/trucks-breadcrumbs-generation-696450a616a2.md#meta_level) %}

{% include notitle [mark](../_includes/params/trucks-breadcrumbs-generation-696450a616a2.md#mark) %}

 
:   {% include notitle [id_mark](../_includes/params/trucks-breadcrumbs-generation-696450a616a2.md#id_mark) %}

    {% include notitle [name_mark](../_includes/params/trucks-breadcrumbs-generation-696450a616a2.md#name_mark) %}

    {% include notitle [offers_count_mark](../_includes/params/trucks-breadcrumbs-generation-696450a616a2.md#offers_count_mark) %}

    {% include notitle [is_popular_mark](../_includes/params/trucks-breadcrumbs-generation-696450a616a2.md#is_popular_mark) %}

    {% include notitle [mark](../_includes/params/trucks-breadcrumbs-generation-696450a616a2.md#mark) %}

     
    :   {% include notitle [logo](../_includes/params/trucks-breadcrumbs-generation-696450a616a2.md#logo) %}

         
        :   {% include notitle [name_photo](../_includes/params/trucks-breadcrumbs-generation-696450a616a2.md#name_photo) %}

            {% include notitle [sizes](../_includes/params/trucks-breadcrumbs-generation-696450a616a2.md#sizes) %}

        {% include notitle [vendor_ids](../_includes/params/trucks-breadcrumbs-generation-696450a616a2.md#vendor_ids) %}

        {% include notitle [cyrillic_name_mark](../_includes/params/trucks-breadcrumbs-generation-696450a616a2.md#cyrillic_name_mark) %}

    {% include notitle [reviews_count_mark](../_includes/params/trucks-breadcrumbs-generation-696450a616a2.md#reviews_count_mark) %}

{% include notitle [model](../_includes/params/trucks-breadcrumbs-generation-696450a616a2.md#model) %}

 
:   {% include notitle [id_model](../_includes/params/trucks-breadcrumbs-generation-696450a616a2.md#id_model) %}

    {% include notitle [name_model](../_includes/params/trucks-breadcrumbs-generation-696450a616a2.md#name_model) %}

    {% include notitle [offers_count_model](../_includes/params/trucks-breadcrumbs-generation-696450a616a2.md#offers_count_model) %}

    {% include notitle [is_popular_model](../_includes/params/trucks-breadcrumbs-generation-696450a616a2.md#is_popular_model) %}

    {% include notitle [model](../_includes/params/trucks-breadcrumbs-generation-696450a616a2.md#model) %}

     
    :   {% include notitle [default_configuration_id](../_includes/params/trucks-breadcrumbs-generation-696450a616a2.md#default_configuration_id) %}

        {% include notitle [nameplates](../_includes/params/trucks-breadcrumbs-generation-696450a616a2.md#nameplates) %}

         
        :   {% include notitle [name_model_type](../_includes/params/trucks-breadcrumbs-generation-696450a616a2.md#name_model_type) %}

            {% include notitle [code](../_includes/params/trucks-breadcrumbs-generation-696450a616a2.md#code) %}

            {% include notitle [autoru_id](../_includes/params/trucks-breadcrumbs-generation-696450a616a2.md#autoru_id) %}

            {% include notitle [offers_count_model_type](../_includes/params/trucks-breadcrumbs-generation-696450a616a2.md#offers_count_model_type) %}

        {% include notitle [moto_functions](../_includes/params/trucks-breadcrumbs-generation-696450a616a2.md#moto_functions) %}

        {% include notitle [photo](../_includes/params/trucks-breadcrumbs-generation-696450a616a2.md#photo) %}

         
        :   {% include notitle [name_photo](../_includes/params/trucks-breadcrumbs-generation-696450a616a2.md#name_photo) %}

            {% include notitle [sizes](../_includes/params/trucks-breadcrumbs-generation-696450a616a2.md#sizes) %}

        {% include notitle [cyrillic_name_model](../_includes/params/trucks-breadcrumbs-generation-696450a616a2.md#cyrillic_name_model) %}

    {% include notitle [reviews_count_model](../_includes/params/trucks-breadcrumbs-generation-696450a616a2.md#reviews_count_model) %}

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

{% include notitle [entities](../_includes/params/trucks-breadcrumbs-model-98210b62d197.md#entities) %}

 
:   {% include notitle [id_model](../_includes/params/trucks-breadcrumbs-model-98210b62d197.md#id_model) %}

    {% include notitle [name_model](../_includes/params/trucks-breadcrumbs-model-98210b62d197.md#name_model) %}

    {% include notitle [offers_count_model](../_includes/params/trucks-breadcrumbs-model-98210b62d197.md#offers_count_model) %}

    {% include notitle [is_popular_model](../_includes/params/trucks-breadcrumbs-model-98210b62d197.md#is_popular_model) %}

    {% include notitle [model](../_includes/params/trucks-breadcrumbs-model-98210b62d197.md#model) %}

     
    :   {% include notitle [default_configuration_id](../_includes/params/trucks-breadcrumbs-model-98210b62d197.md#default_configuration_id) %}

        {% include notitle [nameplates](../_includes/params/trucks-breadcrumbs-model-98210b62d197.md#nameplates) %}

         
        :   {% include notitle [name_model](../_includes/params/trucks-breadcrumbs-model-98210b62d197.md#name_model) %}

            {% include notitle [code](../_includes/params/trucks-breadcrumbs-model-98210b62d197.md#code) %}

            {% include notitle [autoru_id](../_includes/params/trucks-breadcrumbs-model-98210b62d197.md#autoru_id) %}

            {% include notitle [offers_count_model_type](../_includes/params/trucks-breadcrumbs-model-98210b62d197.md#offers_count_model_type) %}

        {% include notitle [moto_functions](../_includes/params/trucks-breadcrumbs-model-98210b62d197.md#moto_functions) %}

        {% include notitle [photo](../_includes/params/trucks-breadcrumbs-model-98210b62d197.md#photo) %}
        
         
        :   {% include notitle [name_photo](../_includes/params/trucks-breadcrumbs-model-98210b62d197.md#name_photo) %}

            {% include notitle [sizes](../_includes/params/trucks-breadcrumbs-model-98210b62d197.md#sizes) %}

        {% include notitle [cyrillic_name_model](../_includes/params/trucks-breadcrumbs-model-98210b62d197.md#cyrillic_name_model) %}

    {% include notitle [reviews_count_model](../_includes/params/trucks-breadcrumbs-model-98210b62d197.md#reviews_count_model) %}

{% include notitle [meta_level](../_includes/params/trucks-breadcrumbs-model-98210b62d197.md#meta_level) %}

{% include notitle [mark](../_includes/params/trucks-breadcrumbs-model-98210b62d197.md#mark) %}

 
:   {% include notitle [id_mark](../_includes/params/trucks-breadcrumbs-model-98210b62d197.md#id_mark) %}

    {% include notitle [name_mark](../_includes/params/trucks-breadcrumbs-model-98210b62d197.md#name_mark) %}

    {% include notitle [offers_count_mark](../_includes/params/trucks-breadcrumbs-model-98210b62d197.md#offers_count_mark) %}

    {% include notitle [is_popular_mark](../_includes/params/trucks-breadcrumbs-model-98210b62d197.md#is_popular_mark) %}

    {% include notitle [mark](../_includes/params/trucks-breadcrumbs-model-98210b62d197.md#mark) %}

     
    :   {% include notitle [logo](../_includes/params/trucks-breadcrumbs-model-98210b62d197.md#logo) %}

         
        :   {% include notitle [name_photo](../_includes/params/trucks-breadcrumbs-model-98210b62d197.md#name_photo) %}

            {% include notitle [sizes](../_includes/params/trucks-breadcrumbs-model-98210b62d197.md#sizes) %}

        {% include notitle [vendor_ids](../_includes/params/trucks-breadcrumbs-model-98210b62d197.md#vendor_ids) %}

        {% include notitle [cyrillic_name_mark](../_includes/params/trucks-breadcrumbs-model-98210b62d197.md#cyrillic_name_mark) %}

    {% include notitle [reviews_count_mark](../_includes/params/trucks-breadcrumbs-model-98210b62d197.md#reviews_count_mark) %}


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
      "meta_level":"{string}"  /* MARK_LEVEL */
    }
```

<div class="params-table">

{% include notitle [entities](../_includes/params/trucks-breadcrumbs-mark-dbec124fbd1f.md#entities) %}

 
:   {% include notitle [id](../_includes/params/trucks-breadcrumbs-mark-dbec124fbd1f.md#id) %}

    {% include notitle [name](../_includes/params/trucks-breadcrumbs-mark-dbec124fbd1f.md#name) %}

    {% include notitle [offers_count](../_includes/params/trucks-breadcrumbs-mark-dbec124fbd1f.md#offers_count) %}

    {% include notitle [mark](../_includes/params/trucks-breadcrumbs-mark-dbec124fbd1f.md#mark) %}

     
    :   {% include notitle [logo](../_includes/params/trucks-breadcrumbs-mark-dbec124fbd1f.md#logo) %}

         
        :   {% include notitle [name](../_includes/params/trucks-breadcrumbs-mark-dbec124fbd1f.md#name-photo) %}

            {% include notitle [sizes](../_includes/params/trucks-breadcrumbs-mark-dbec124fbd1f.md#sizes) %}

        {% include notitle [vendor_ids](../_includes/params/trucks-breadcrumbs-mark-dbec124fbd1f.md#vendor_ids) %}

        {% include notitle [cyrillic_name](../_includes/params/trucks-breadcrumbs-mark-dbec124fbd1f.md#cyrillic_name) %}

    {% include notitle [reviews_count](../_includes/params/trucks-breadcrumbs-mark-dbec124fbd1f.md#reviews_count) %}

{% include notitle [meta_level](../_includes/params/trucks-breadcrumbs-mark-dbec124fbd1f.md#meta_level) %}

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
      "meta_level":"{string}"  /* TYPE_LEVEL */
    }
```

<div class="params-table">

{% include notitle [entities](../_includes/params/trucks-breadcrumbs-type-65359df9e58e.md#entities) %}

 
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
> curl -i -X GET 'https://apiauto.ru/1.0/search/trucks/breadcrumbs?bc_lookup=TRUCK%23BAW%23FENIX&rid=213' -H 'x-authorization: 2dtrer432...'
> ```
> 
> 
> Ответ:
> 
> 
> ```json
> {
>   "breadcrumbs": [
>     {
>       "entities": [
>         {
>           "id": "20586463",
>           "super_gen": {
>             "year_from": 2005
>           }
>         },
>         {
>           "id": "20589934",
>           "super_gen": {}
>         },
>         {
>           "id": "20590316",
>           "super_gen": {}
>         },
>         {
>           "id": "20590560",
>           "super_gen": {}
>         }
>       ],
>       "meta_level": "GENERATION_LEVEL",
>       "mark": {
>         "id": "BAW",
>         "name": "BAW",
>         "mark": {
>           "logo": {
>             "name": "mark-logo",
>             "sizes": {
>               "logo": "//avatarrf/54df507521486/logo"
>             }
>           }
>         }
>       },
>       "model": {
>         "id": "FENIX",
>         "name": "Fenix",
>         "model": {
>           "photo": {
>             "name": "model-photo",
>             "sizes": {
>               "main": "//avatar5ref/507542/trucks-catalog0443r118/mobile",
>               "mini-card": "//avatarstr/507652/trucks-catalog120/minicard"
>             }
>           }
>         }
>       }
>     },
>     {
>       "entities": [
>         {
>           "id": "FENIX",
>           "name": "Fenix",
>           "offers_count": 12,
>           "model": {
>             "photo": {
>               "name": "model-photo",
>               "sizes": {
>                 "main": "//avatar54/655072/trucks-catalog.g2148/mobile",
>                 "mini-card": "//avatars643r/54350/trucks-catalog481445818/minicard"
>               }
>             }
>           }
>         }
>       ],
>       "meta_level": "MODEL_LEVEL",
>       "mark": {
>         "id": "BAW",
>         "name": "BAW",
>         "mark": {
>           "logo": {
>             "name": "mark-logo",
>             "sizes": {
>               "logo": "//avatars/59032/trucks-catalog54rf148/logo"
>             }
>           }
>         }
>       }
>     },
>     {
>       "entities": [
>         {
>           "id": "ALTKAM",
>           "name": "Altkam",
>           "mark": {
>             "logo": {
>               "name": "mark-logo",
>               "sizes": {
>                 "logo": "//avatarstet/507yt452/trucks-catalogrf86324/logo"
>               }
>             }
>           }
>         },
>         {
>           "id": "ASTRA",
>           "name": "ASTRA",
>           "mark": {
>             "logo": {
>               "name": "mark-logo",
>               "sizes": {
>                 "logo": "//avatarstuto/507t532/trucks-catalog1154v76/logo"
>               }
>             }
>           }
>         },
>         {
>           "id": "NISSAN",
>           "name": "Nissan",
>           "offers_count": 11,
>           "is_popular": true,
>           "mark": {
>             "logo": {
>               "name": "mark-logo",
>               "sizes": {
>                 "logo": "//avatarrt34/50489/trucks-catalog43d504/logo"
>               }
>             }
>           }
>         },
>         {
>           ...
>         }
>       ],
>       "meta_level": "MARK_LEVEL"
>     },
>     {
>       "entities": [
>         {
>           "id": "TRUCK",
>           "name": "Грузовик",
>           "offers_count": 858,
>           "reviews_count": 130
>         },
>         {
>           "id": "BUS",
>           "name": "Автобус",
>           "offers_count": 146,
>           "reviews_count": 5
>         },
>         {
>           "id": "ARTIC",
>           "name": "Седельный тягач",
>           "offers_count": 472,
>           "reviews_count": 25
>         },
>         {
>           "id": "TRAILER",
>           "name": "Прицеп",
>           "offers_count": 475,
>           "reviews_count": 19
>         },
>         {
>           "id": "SWAP_BODY",
>           "name": "Съемный кузов"
>         },
>         {
>           "id": "LCV",
>           "name": "Легкий коммерческий",
>           "offers_count": 3577,
>           "reviews_count": 431
>         },
>         {
>           "id": "AGRICULTURAL",
>           "name": "Сельскохозяйственная",
>           "offers_count": 14
>         },
>         {
>           "id": "AUTOLOADER",
>           "name": "Автопогрузчики",
>           "offers_count": 82
>         },
>         {
>           "id": "BULLDOZERS",
>           "name": "Бульдозеры",
>           "offers_count": 27
>         },
>         {
>           "id": "CONSTRUCTION",
>           "name": "Строительная",
>           "offers_count": 103
>         },
>         {
>           "id": "CRANE",
>           "name": "Автокран",
>           "offers_count": 63
>         },
>         {
>           "id": "CRANE_HYDRAULICS",
>           "name": "Самопогрузчики",
>           "offers_count": 80
>         },
>         {
>           "id": "DREDGE",
>           "name": "Экскаваторы",
>           "offers_count": 99
>         },
>         {
>           "id": "MUNICIPAL",
>           "name": "Коммунальная",
>           "offers_count": 80
>         }
>       ],
>       "meta_level": "TYPE_LEVEL"
>     }
>   ],
>   "status": "SUCCESS"
> }       
> ```

{% include [table-style](../_includes/table-style-border-none-2a2aa0c324bf.md) %}

[*bc_lookup]: {% include notitle [bc_lookup-trucks](../_includes/popups-00286d1be377.md#bc_lookup-trucks) %}

[*rid]: {% include notitle [rid-cars-breadcrumbs](../_includes/popups-00286d1be377.md#rid-cars-breadcrumbs) %}

[*state]: {% include [includes-state-description](../_includes/reference/includes/id-includes/state-description-78e689139d95.md) %}

[*mark_ph]: {% include notitle [mark_ph](../_includes/popups-00286d1be377.md#mark_ph) %}

[*model_ph]: {% include notitle [model_ph](../_includes/popups-00286d1be377.md#model_ph) %}

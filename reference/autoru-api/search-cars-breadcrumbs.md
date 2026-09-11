---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/search-cars-breadcrumbs.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# GET /search/cars/breadcrumbs

Возвращает информацию о структуре каталога легковых автомобилей и количестве активных объявлений на различных уровнях (марка, модель, поколение, конфигурация, набор технических характеристик).

## Формат запроса {#input}

```
GET https://apiauto.ru/1.0/search/cars/breadcrumbs
? [[bc_lookup](*bc_lookup)=<array[string]>]
& [[rid](*rid)=<array[string]>]
& [[state](*state)=<array[string]>]

```

<div class="params-table">

#|
||
##bc_lookup##
|
{% include notitle [bc_lookup-cars-breadcrumbs](../_includes/popups-00286d1be377.md#bc_lookup-cars-breadcrumbs) %}
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
      "meta_level":"{string}",  /* TECH_PARAM_LEVEL */
      "mark":{
        ...
      },
      "model":{
        ...
      },
      "super_generation":{
        ...
      },
      "configuration":{
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
      "meta_level":"{string}",  /* CONFIGURATION_LEVEL */
      "mark":{
        ...
      },
      "model":{
        ...
      },
      "super_generation":{
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
      "meta_level":"{string}",  /* MARK_LEVEL */
      "offers_count":{integer}
    }
  ],
  "status":"{string}"
}
```
<div class="params-table">

{% include notitle [breadcrumbs](../_includes/params/cars-breadcrumbs-common-8d5b77ceea85.md#breadcrumbs) %}

 
:   {% include notitle [entities](../_includes/params/cars-breadcrumbs-common-8d5b77ceea85.md#entities_common) %}

    {% include notitle [meta_level](../_includes/params/cars-breadcrumbs-common-8d5b77ceea85.md#meta_level) %}

    {% include notitle [offers_count](../_includes/params/cars-breadcrumbs-common-8d5b77ceea85.md#offers_count_common) %}

    {% include notitle [mark](../_includes/params/cars-breadcrumbs-common-8d5b77ceea85.md#mark_common) %}

    {% include notitle [model](../_includes/params/cars-breadcrumbs-common-8d5b77ceea85.md#model_common) %}

    {% include notitle [super_generation](../_includes/params/cars-breadcrumbs-common-8d5b77ceea85.md#super_generation) %}

    {% include notitle [configuration](../_includes/params/cars-breadcrumbs-common-8d5b77ceea85.md#configuration_common) %}

{% include notitle [status](../_includes/params/cars-breadcrumbs-common-8d5b77ceea85.md#status) %}

</div>

{% endcut %}

{% cut "Уровень иерархии «TECH_PARAM»" %} {#tech_param}

```json
    {
      "entities":[
        {
          "id":"{string}",
          "name":"{string}",
          "offers_count":{integer},
          "is_popular":{boolean},
          "tech_params":{
            "nameplate_engine":"{string}",
            "engine_type":"{string}",
            "displacement":{integer},
            "gear_type":"{string}",
            "transmission":"{string}",
            "power":{integer},
            "power_kvt":"{string}",
            "year_start":{integer},
            "year_stop":{integer},
            "human_name":"{string}"
          },
          "reviews_count":{integer}
        },
        {
          ...
        }
      ],
      "meta_level":"{string}",  /* TECH_PARAM_LEVEL */
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
        "reviews_count":{integer}
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
        "reviews_count":{integer}
      },
      "super_generation":{
        "id":"{string}",
        "name":"{string}",
        "offers_count":{integer},
        "is_popular":{boolean},
        "super_gen":{
          "year_from":{integer},
          "year_to":{integer},
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
        "reviews_count":{integer}
      },
      "configuration":{
        "id":"{string}",
        "name":"{string}",
        "offers_count":{integer},
        "is_popular":{boolean},
        "[configuration](*configuration_ph)":{
          "body_type":"{string}",
          "doors_count":"{string}",
          "configuration_name":"{string}",
          "photo":{
            "name":"{string}",
            "sizes":{
              "{string}":"{string}",
              "{string}":"{string}"
            }
          },
          "human_name":"{string}"
        },
        "reviews_count":{integer}
      }
    }
```

<div class="params-table">

{% include notitle [entities](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#entities_tech_param) %}

 
:   {% include notitle [id](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#id_1) %}

    {% include notitle [name](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#name_tech_params) %}

    {% include notitle [offers_count](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#offers_count_tech_params) %}

    {% include notitle [is_popular](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#is_popular_tech_params) %}

    {% include notitle [tech_params](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#tech_params) %}

     
    :   {% include notitle [nameplate_engine](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#nameplate_engine) %}
        
        {% include notitle [engine_type](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#engine_type) %}

        {% include notitle [displacement](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#displacement) %}

        {% include notitle [gear_type](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#gear_type) %}

        {% include notitle [transmission](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#transmission) %}

        {% include notitle [power](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#power) %}

        {% include notitle [power_kvt](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#power_kvt) %}

        {% include notitle [year_start](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#year_start) %}

        {% include notitle [year_stop](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#year_stop) %}

        {% include notitle [human_name](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#human_name) %}

    {% include notitle [reviews_count](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#reviews_count_tech_params) %}


{% include notitle [meta_level](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#meta_level) %}

{% include notitle [offers_count](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#offers_count_common) %}

{% include notitle [mark](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#mark_common) %}

 
:   {% include notitle [id](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#id_2) %}

    {% include notitle [name](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#name_mark) %}

    {% include notitle [offers_count](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#offers_count_mark) %}

    {% include notitle [is_popular](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#is_popular_mark) %}

    {% include notitle [mark](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#mark_detail) %}

     
    :   {% include notitle [logo](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#logo) %}

         
        :   {% include notitle [name](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#name_photo) %}

            {% include notitle [sizes](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#sizes_1) %}

        {% include notitle [vendor_ids](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#vendor_ids) %}

        {% include notitle [cyrillic_name](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#cyrillic_name) %}

    {% include notitle [reviews_count](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#reviews_count_mark) %}


{% include notitle [model](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#model_common) %}

 
:   {% include notitle [id](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#id_3) %}

    {% include notitle [name](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#name_model) %}

    {% include notitle [offers_count](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#offers_count_model) %}

    {% include notitle [is_popular](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#is_popular_model) %}

    {% include notitle [model](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#model_detail) %}

     
    :   {% include notitle [default_configuration_id](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#default_configuration_id) %}

        {% include notitle [nameplates](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#nameplates) %}

         
        :   {% include notitle [name](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#name_model_id) %}

            {% include notitle [code](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#code) %}

            {% include notitle [autoru_id](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#autoru_id) %}

            {% include notitle [offers_count](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#offers_count_model_id) %}

        {% include notitle [moto_functions](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#moto_functions) %}

        {% include notitle [photo](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#photo) %}

         
        :   {% include notitle [name](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#name_photo) %}

            {% include notitle [sizes](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#sizes_1) %}

        {% include notitle [cyrillic_name](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#cyrillic_name) %}

    {% include notitle [reviews_count](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#reviews_count_model) %}

{% include notitle [super_generation](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#super_generation) %}

 
:   {% include notitle [id](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#id_4) %}

    {% include notitle [name](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#name_gen) %}

    {% include notitle [offers_count](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#offers_count_gen) %}

    {% include notitle [is_popular](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#is_popular_gen) %}

    {% include notitle [super_gen](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#super_gen) %}

     
    :   {% include notitle [year_from](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#year_from) %}

        {% include notitle [year_to](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#year_to) %}

        {% include notitle [is_restyle](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#is_restyle) %}

        {% include notitle [default_configuration_id](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#default_configuration_id) %}

        {% include notitle [photo](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#photo) %}

         
        :   {% include notitle [name](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#name_photo) %}

            {% include notitle [sizes](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#sizes_1) %}

    {% include notitle [reviews_count](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#reviews_count_gen) %}

{% include notitle [configuration](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#configuration_common) %}

 
:   {% include notitle [id](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#id_5) %}

    {% include notitle [name](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#name_config) %}

    {% include notitle [offers_count](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#offers_count_config) %}

    {% include notitle [is_popular](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#is_popular_config) %}

    {% include notitle [configuration](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#configuration_detail) %}

     
    :   {% include notitle [body_type](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#body_type) %}

        {% include notitle [doors_count](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#doors_count) %}

        {% include notitle [configuration_name](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#configuration_name) %}

        {% include notitle [photo](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#photo) %}

         
        :   {% include notitle [name](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#name_photo) %}

            {% include notitle [sizes](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#sizes_1) %}

        {% include notitle [human_name](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#human_name) %}

    {% include notitle [reviews_count](../_includes/params/cars-breadcrumbs-tech-param-f362cccfe0e2.md#reviews_count_config) %}

</div>

{% endcut %}

{% cut "Уровень иерархии «CONFIGURATION»" %} {#configuration}

```json
    {
      "entities":[
        {
          "id":"{string}",
          "name":"{string}",
          "offers_count":"{number}",
          "is_popular":"{boolean}",
          "configuration":{
            "body_type":"{string}",
            "doors_count":"{string}",
            "configuration_name":"{string}",
            "photo":{
              "name":"{string}",
              "sizes":{
                "key1":"{string}",
                "key2":"{string}"
              }
            },
            "human_name":"{string}"
          },
          "reviews_count":{integer}
        },
        {
          
        }
      ],
      "meta_level":"{string}",
      "mark":{
        "id":"{string}",
        "name":"{string}",
        "offers_count":"{number}",
        "is_popular":"{boolean}", 
        "[mark](*mark_ph)":{
          "logo":{
            "name":"{string}",
            "sizes":{
              "key1":"{string}",
              "key2":"{string}"
            }
          },
          "vendor_ids":[
            "{number}",
            "{number}"
          ],
          "cyrillic_name":"{string}"
        },
        "reviews_count":{integer}
      },
      "model":{
        "id":"{string}",
        "name":"{string}",
        "offers_count":"{number}",
        "is_popular":"{boolean}",
        "[model](*model_ph)":{
          "default_configuration_id":"{string}",
          "nameplates":[
            {
              "name":"{string}",
              "code":"{string}",
              "autoru_id":"{string}",
              "offers_count":"{number}"
            },
            {
              
            }
          ],
          "photo":{
            "name":"{string}",
            "sizes":{
              "key1":"{string}",
              "key2":"{string}"
            }
          },
          "cyrillic_name":"{string}"
        },
        "reviews_count":{integer}
      },
      "super_generation":{
        "id":"{string}",
        "name":"{string}",
        "offers_count":"{number}",
        "is_popular":"{boolean}",
        "super_gen":{
          "year_from":"{number}",
          "year_to":"{number}",
          "is_restyle":"{boolean}",
          "default_configuration_id":"{string}",
          "photo":{
            "name":"{string}",
            "sizes":{
              "{string}":"{string}",
              "{string}":"{string}"
            }
          }
        },
        "reviews_count":{integer}
      }
    }
```

<div class="params-table">

{% include notitle [entities](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#entities) %}

 
:   {% include notitle [id_config](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#id_config) %}

    {% include notitle [name_config](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#name_config) %}

    {% include notitle [offers_count_config](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#offers_count_config) %}

    {% include notitle [is_popular_config](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#is_popular_config) %}

    {% include notitle [configuration_detail](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#configuration_detail) %}

     
    :   {% include notitle [body_type](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#body_type) %}

        {% include notitle [doors_count](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#doors_count) %}

        {% include notitle [configuration_name](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#configuration_name) %}

        {% include notitle [photo](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#photo) %}        
        
         
        :   {% include notitle [name_photo](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#name_photo) %}

            {% include notitle [sizes](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#sizes) %}

        {% include notitle [human_name](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#human_name) %}

    {% include notitle [reviews_count_config](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#reviews_count_config) %}

{% include notitle [meta_level](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#meta_level) %}

{% include notitle [offers_count_common](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#offers_count_common) %}

{% include notitle [mark](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#mark-common) %}

 
:   {% include notitle [id_mark](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#id_mark) %}

    {% include notitle [name_mark](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#name_mark) %}

    {% include notitle [offers_count_mark](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#offers_count_mark) %}

    {% include notitle [is_popular_mark](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#is_popular_mark) %}

    {% include notitle [mark](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#mark) %}

     
    :   {% include notitle [logo](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#logo) %}

         
        :   {% include notitle [name_photo](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#name_photo) %}

            {% include notitle [sizes](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#sizes) %}

        {% include notitle [vendor_ids](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#vendor_ids) %}

        {% include notitle [cyrillic_name](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#cyrillic_name) %}

    {% include notitle [reviews_count_mark](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#reviews_count_mark) %}

{% include notitle [model](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#model-common) %}

 
:   {% include notitle [id_model](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#id_model) %}

    {% include notitle [name_model](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#name_model) %}

    {% include notitle [offers_count_model](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#offers_count_model) %}

    {% include notitle [is_popular_model](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#is_popular_model) %}

    {% include notitle [model](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#model) %}

     
    :   {% include notitle [default_configuration_id](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#default_configuration_id) %}

        {% include notitle [nameplates](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#nameplates) %}

         
        :   {% include notitle [name_model_type](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#name_model_type) %}

            {% include notitle [code](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#code) %}

            {% include notitle [autoru_id](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#autoru_id) %}

            {% include notitle [offers_count_model_type](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#offers_count_model_type) %}

        {% include notitle [moto_functions](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#moto_functions) %}

        {% include notitle [photo](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#photo) %}

         
        :   {% include notitle [name_photo](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#name_photo) %}

            {% include notitle [sizes](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#sizes) %}

        {% include notitle [cyrillic_name](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#cyrillic_name) %}

    {% include notitle [reviews_count_model](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#reviews_count_model) %}

{% include notitle [super_generation](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#super_generation) %}

 
:   {% include notitle [id_gen](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#id_gen) %}

    {% include notitle [name_gen](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#name_gen) %}

    {% include notitle [offers_count_gen](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#offers_count_gen) %}

    {% include notitle [is_popular_gen](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#is_popular_gen) %}

    {% include notitle [super_gen](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#super_gen) %}

     
    :   {% include notitle [year_from](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#year_from) %}

        {% include notitle [year_to](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#year_to) %}

        {% include notitle [is_restyle](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#is_restyle) %}

        {% include notitle [default_configuration_id](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#default_configuration_id) %}

        {% include notitle [photo](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#photo) %}

         
        :   {% include notitle [name_photo](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#name_photo) %}

            {% include notitle [sizes](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#sizes) %}

    {% include notitle [reviews_count_gen](../_includes/params/cars-breadcrumbs-configuration-398e9062fc80.md#reviews_count_gen) %}

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
          "reviews_count":{integer}
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
        "reviews_count":{integer}
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
        "reviews_count":{integer}
      }
    }
```

<div class="params-table">

{% include notitle [entities](../_includes/params/cars-breadcrumbs-generation-696450a616a2.md#entities) %}

 
:   {% include notitle [id_gen](../_includes/params/cars-breadcrumbs-generation-696450a616a2.md#id_gen) %}

    {% include notitle [name_gen](../_includes/params/cars-breadcrumbs-generation-696450a616a2.md#name_gen) %}

    {% include notitle [offers_count_gen](../_includes/params/cars-breadcrumbs-generation-696450a616a2.md#offers_count_gen) %}

    {% include notitle [is_popular_gen](../_includes/params/cars-breadcrumbs-generation-696450a616a2.md#is_popular_gen) %}

    {% include notitle [super_gen](../_includes/params/cars-breadcrumbs-generation-696450a616a2.md#super_gen) %}

     
    :   {% include notitle [year_from](../_includes/params/cars-breadcrumbs-generation-696450a616a2.md#year_from) %}
        
        {% include notitle [year_to](../_includes/params/cars-breadcrumbs-generation-696450a616a2.md#year_to) %}

        {% include notitle [is_restyle](../_includes/params/cars-breadcrumbs-generation-696450a616a2.md#is_restyle) %}

        {% include notitle [default_configuration_id](../_includes/params/cars-breadcrumbs-generation-696450a616a2.md#default_configuration_id) %}

        {% include notitle [photo](../_includes/params/cars-breadcrumbs-generation-696450a616a2.md#photo) %}

         
        :   {% include notitle [name_photo](../_includes/params/cars-breadcrumbs-generation-696450a616a2.md#name_photo) %}

            {% include notitle [sizes](../_includes/params/cars-breadcrumbs-generation-696450a616a2.md#sizes) %}

    {% include notitle [reviews_count_gen](../_includes/params/cars-breadcrumbs-generation-696450a616a2.md#reviews_count_gen) %}

{% include notitle [meta_level](../_includes/params/cars-breadcrumbs-generation-696450a616a2.md#meta_level) %}

{% include notitle [offers_count_common](../_includes/params/cars-breadcrumbs-generation-696450a616a2.md#offers_count_common) %}

{% include notitle [mark](../_includes/params/cars-breadcrumbs-generation-696450a616a2.md#mark-common) %}

 
:   {% include notitle [id_mark](../_includes/params/cars-breadcrumbs-generation-696450a616a2.md#id_mark) %}

    {% include notitle [name_mark](../_includes/params/cars-breadcrumbs-generation-696450a616a2.md#name_mark) %}

    {% include notitle [offers_count_mark](../_includes/params/cars-breadcrumbs-generation-696450a616a2.md#offers_count_mark) %}

    {% include notitle [is_popular_mark](../_includes/params/cars-breadcrumbs-generation-696450a616a2.md#is_popular_mark) %}

    {% include notitle [mark](../_includes/params/cars-breadcrumbs-generation-696450a616a2.md#mark) %}

     
    :   {% include notitle [logo](../_includes/params/cars-breadcrumbs-generation-696450a616a2.md#logo) %}
        
         
        :   {% include notitle [name_photo](../_includes/params/cars-breadcrumbs-generation-696450a616a2.md#name_photo) %}

            {% include notitle [sizes](../_includes/params/cars-breadcrumbs-generation-696450a616a2.md#sizes) %}

        {% include notitle [vendor_ids](../_includes/params/cars-breadcrumbs-generation-696450a616a2.md#vendor_ids) %}

        {% include notitle [cyrillic_name_mark](../_includes/params/cars-breadcrumbs-generation-696450a616a2.md#cyrillic_name_mark) %}

    {% include notitle [reviews_count_mark](../_includes/params/cars-breadcrumbs-generation-696450a616a2.md#reviews_count_mark) %}

{% include notitle [model](../_includes/params/cars-breadcrumbs-generation-696450a616a2.md#model) %}

 
:   {% include notitle [id_model](../_includes/params/cars-breadcrumbs-generation-696450a616a2.md#id_model) %}

    {% include notitle [name_model](../_includes/params/cars-breadcrumbs-generation-696450a616a2.md#name_model) %}

    {% include notitle [offers_count_model](../_includes/params/cars-breadcrumbs-generation-696450a616a2.md#offers_count_model) %}

    {% include notitle [is_popular_model](../_includes/params/cars-breadcrumbs-generation-696450a616a2.md#is_popular_model) %}

    {% include notitle [model](../_includes/params/cars-breadcrumbs-generation-696450a616a2.md#model) %}

     
    :   {% include notitle [default_configuration_id](../_includes/params/cars-breadcrumbs-generation-696450a616a2.md#default_configuration_id) %}

        {% include notitle [nameplates](../_includes/params/cars-breadcrumbs-generation-696450a616a2.md#nameplates) %}

         
        :   {% include notitle [name_model_type](../_includes/params/cars-breadcrumbs-generation-696450a616a2.md#name_model_type) %}

            {% include notitle [code](../_includes/params/cars-breadcrumbs-generation-696450a616a2.md#code) %}

            {% include notitle [autoru_id](../_includes/params/cars-breadcrumbs-generation-696450a616a2.md#autoru_id) %}

            {% include notitle [offers_count_model_type](../_includes/params/cars-breadcrumbs-generation-696450a616a2.md#offers_count_model_type) %}

        {% include notitle [moto_functions](../_includes/params/cars-breadcrumbs-generation-696450a616a2.md#moto_functions) %}

        {% include notitle [photo](../_includes/params/cars-breadcrumbs-generation-696450a616a2.md#photo) %}

         
        :   {% include notitle [name_photo](../_includes/params/cars-breadcrumbs-generation-696450a616a2.md#name_photo) %}

            {% include notitle [sizes](../_includes/params/cars-breadcrumbs-generation-696450a616a2.md#sizes) %}

        {% include notitle [cyrillic_name_model](../_includes/params/cars-breadcrumbs-generation-696450a616a2.md#cyrillic_name_model) %}

    {% include notitle [reviews_count_model](../_includes/params/cars-breadcrumbs-generation-696450a616a2.md#reviews_count_model) %}

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
          "reviews_count":{integer}
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
        "reviews_count":{integer}
      }
    }
```

<div class="params-table">

{% include notitle [entities](../_includes/params/cars-breadcrumbs-model-6d1544965364.md#entities) %}

 
:   {% include notitle [id_model](../_includes/params/cars-breadcrumbs-model-6d1544965364.md#id_model) %}

    {% include notitle [name_model](../_includes/params/cars-breadcrumbs-model-6d1544965364.md#name_model) %}

    {% include notitle [offers_count_model](../_includes/params/cars-breadcrumbs-model-6d1544965364.md#offers_count_model) %}

    {% include notitle [is_popular_model](../_includes/params/cars-breadcrumbs-model-6d1544965364.md#is_popular_model) %}

    {% include notitle [model](../_includes/params/cars-breadcrumbs-model-6d1544965364.md#model) %}
    
     
    :   {% include notitle [default_configuration_id](../_includes/params/cars-breadcrumbs-model-6d1544965364.md#default_configuration_id) %}

        {% include notitle [nameplates](../_includes/params/cars-breadcrumbs-model-6d1544965364.md#nameplates) %}

         
        :   {% include notitle [name_model](../_includes/params/cars-breadcrumbs-model-6d1544965364.md#name_model_type) %}

            {% include notitle [code](../_includes/params/cars-breadcrumbs-model-6d1544965364.md#code) %}

            {% include notitle [autoru_id](../_includes/params/cars-breadcrumbs-model-6d1544965364.md#autoru_id) %}

            {% include notitle [offers_count_model_type](../_includes/params/cars-breadcrumbs-model-6d1544965364.md#offers_count_model_type) %}

        {% include notitle [moto_functions](../_includes/params/cars-breadcrumbs-model-6d1544965364.md#moto_functions) %}

        {% include notitle [photo](../_includes/params/cars-breadcrumbs-model-6d1544965364.md#photo) %}

         
        :   {% include notitle [name_photo](../_includes/params/cars-breadcrumbs-model-6d1544965364.md#name_photo) %}

            {% include notitle [sizes](../_includes/params/cars-breadcrumbs-model-6d1544965364.md#sizes) %}

        {% include notitle [cyrillic_name_model](../_includes/params/cars-breadcrumbs-model-6d1544965364.md#cyrillic_name_model) %}

    {% include notitle [reviews_count_model](../_includes/params/cars-breadcrumbs-model-6d1544965364.md#reviews_count_model) %}

{% include notitle [meta_level](../_includes/params/cars-breadcrumbs-model-6d1544965364.md#meta_level) %}

{% include notitle [offers_count](../_includes/params/cars-breadcrumbs-model-6d1544965364.md#offers_count_model) %}

{% include notitle [mark](../_includes/params/cars-breadcrumbs-model-6d1544965364.md#mark-common) %}

 
:   {% include notitle [id](../_includes/params/cars-breadcrumbs-model-6d1544965364.md#id_mark) %}

    {% include notitle [name](../_includes/params/cars-breadcrumbs-model-6d1544965364.md#name_mark) %}

    {% include notitle [offers_count](../_includes/params/cars-breadcrumbs-model-6d1544965364.md#offers_count_mark) %}

    {% include notitle [is_popular](../_includes/params/cars-breadcrumbs-model-6d1544965364.md#is_popular_mark) %}

    {% include notitle [mark](../_includes/params/cars-breadcrumbs-model-6d1544965364.md#mark) %}

     
    :   {% include notitle [logo](../_includes/params/cars-breadcrumbs-model-6d1544965364.md#logo) %}

         
        :   {% include notitle [name_photo](../_includes/params/cars-breadcrumbs-model-6d1544965364.md#name_photo) %}

            {% include notitle [sizes](../_includes/params/cars-breadcrumbs-model-6d1544965364.md#sizes) %}

        {% include notitle [vendor_ids](../_includes/params/cars-breadcrumbs-model-6d1544965364.md#vendor_ids) %}

        {% include notitle [cyrillic_name_mark](../_includes/params/cars-breadcrumbs-model-6d1544965364.md#cyrillic_name_mark) %}

    {% include notitle [reviews_count_mark](../_includes/params/cars-breadcrumbs-model-6d1544965364.md#reviews_count_mark) %}

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
          "reviews_count":{integer}
        },
        {
          ...
        }
      ],
      "meta_level":"{string}",  /* MARK_LEVEL */
      "offers_count":{integer}
    }
```

<div class="params-table">

{% include notitle [entities](../_includes/params/cars-breadcrumbs-mark-8ecffcf6f234.md#entities) %}

 
:   {% include notitle [id](../_includes/params/cars-breadcrumbs-mark-8ecffcf6f234.md#id) %}

    {% include notitle [name](../_includes/params/cars-breadcrumbs-mark-8ecffcf6f234.md#name) %}

    {% include notitle [offers_count](../_includes/params/cars-breadcrumbs-mark-8ecffcf6f234.md#offers_count) %}

    {% include notitle [mark](../_includes/params/cars-breadcrumbs-mark-8ecffcf6f234.md#mark) %}

     
    :   {% include notitle [logo](../_includes/params/cars-breadcrumbs-mark-8ecffcf6f234.md#logo) %}

         
        :   {% include notitle [name](../_includes/params/cars-breadcrumbs-mark-8ecffcf6f234.md#name_photo) %}

            {% include notitle [sizes](../_includes/params/cars-breadcrumbs-mark-8ecffcf6f234.md#sizes) %}

        {% include notitle [vendor_ids](../_includes/params/cars-breadcrumbs-mark-8ecffcf6f234.md#vendor_ids) %}

        {% include notitle [cyrillic_name](../_includes/params/cars-breadcrumbs-mark-8ecffcf6f234.md#cyrillic_name) %}

    {% include notitle [reviews_count](../_includes/params/cars-breadcrumbs-mark-8ecffcf6f234.md#reviews_count) %}

{% include notitle [meta_level](../_includes/params/cars-breadcrumbs-mark-8ecffcf6f234.md#meta_level) %}

{% include notitle [offers_count](../_includes/params/cars-breadcrumbs-mark-8ecffcf6f234.md#offers_count_common) %}

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
> curl -i -X GET 'https://apiauto.ru/1.0/search/cars/breadcrumbs?bc_lookup=HONDA%23CIVIC%234569475%236470343&state=USED&state=NEW&rid=213' -H 'x-authorization: 2dtrer432...'
> ```
> 
> 
> Ответ:
> 
> 
> ```json
> HTTP/1.1 200 OK
> Server: nginx
> Date: Wed, 30 Aug 2017 12:12:33 GMT
> Content-Type: application/json
> Content-Length: 93557
> Connection: keep-alive
> 
> {
>   "breadcrumbs": [
>     {
>       "entities": [
>         {
>           "id": "6470353",
>           "offers_count": 4,
>           "tech_params": {
>             "engine_type": "GASOLINE",
>             "displacement": 1799,
>             "gear_type": "FORWARD_CONTROL",
>             "transmission": "MECHANICAL",
>             "power": 140,
>             "power_kvt": "103.0",
>             "year_start": 2009,
>             "year_stop": 2011,
>             "human_name": "1.8 MT (140 л.с.)"
>           }
>         },
>         {
>            ...
>         }
>       ],
>       "meta_level": "TECH_PARAM_LEVEL",
>       "mark": {
>         "id": "HONDA",
>         "name": "Honda"
>       },
>       "model": {
>         "id": "CIVIC",
>         "name": "Civic"
>       },
>       "super_generation": {
>         "id": "4569475",
>         "name": "VIII Рестайлинг",
>         "super_gen": {
>           "year_from": 2008,
>           "year_to": 2012
>         }
>       },
>       "configuration": {
>         "id": "6470343",
>         "configuration": {
>           "body_type": "HATCHBACK_5_DOORS"
>         }
>       }
>     },
>     {
>       "entities": [
>         {
>           "id": "4569496",
>           "offers_count": 379,
>           "configuration": {
>             "body_type": "SEDAN",
>             "doors_count": 4,
>             "photo": {
>               "name": "configuration-photo",
>               "sizes": {
>                 "main": "//avat/5694/gallery",
>                 "mini-card": "//ava/34230/minicard",
>                 "mobile": "//avata/5232314/main"
>               }
>             },
>             "human_name": "Седан"
>           }
>         },
>         {
>           ...
>         }       
>       ],
>       "meta_level": "CONFIGURATION_LEVEL",
>       "mark": {
>         "id": "HONDA",
>         "name": "Honda"
>       },
>       "model": {
>         "id": "CIVIC",
>         "name": "Civic"
>       },
>       "super_generation": {
>         "id": "4569475",
>         "name": "VIII Рестайлинг",
>         "super_gen": {
>           "year_from": 2008,
>           "year_to": 2012
>         }
>       }
>     },
>     {
>       "entities": [
>         {
>           "id": "20704275",
>           "name": "X",
>           "super_gen": {
>             "year_from": 2015,
>             "default_configuration_id": "20704347",
>             "photo": {
>               "name": "gen-photo",
>               "sizes": {
>                 "main": "//avfewf/322/gallery",
>                 "mini-card": "//avata/8632352/minicard",
>                 "mobile": "//avat86/97243152/main"
>               }
>             }
>           }
>         },
>         {
>           ...
>         }
>       "meta_level": "GENERATION_LEVEL",
>       "mark": {
>         "id": "HONDA",
>         "name": "Honda"
>       },
>       "model": {
>         "id": "CIVIC",
>         "name": "Civic"
>       }
>     },
>     {
>       "entities": [
>         {
>           "id": "ACCORD",
>           "name": "Accord",
>           "offers_count": 1953,
>           "model": {
>             "default_configuration_id": "20668999",
>             "nameplates": [
>               {
>                 "name": "Type R",
>                 "code": "9265363",
>                 "autoru_id": "2214",
>                 "offers_count": 3
>               },
>               {
>                 "name": "Type S",
>                 "code": "9265364",
>                 "autoru_id": "2216",
>                 "offers_count": 223
>               }
>             ],
>             "cyrillic_name": "Аккорд"
>           }
>         },
>         {
>           ...
>         },
>       ],
>       "meta_level": "MODEL_LEVEL",
>       "mark": {
>         "id": "HONDA",
>         "name": "Honda"
>       }
>     },
>     {
>       "entities": [
>         {
>           "id": "AC",
>           "name": "AC",
>           "offers_count": 6,
>           "mark": {
>             "logo": {
>               "name": "mark-logo",
>               "sizes": {
>                 "logo": "//avafger7521/logo",
>                 "big-logo": "//avatargreee/81/dealer_logo"
>               }
>             },
>             "vendor_ids": [
>               14
>             ],
>             "cyrillic_name": "АС"
>           }
>         },
>         {
>           "id": "ACURA",
>           "name": "Acura",
>           "offers_count": 210,
>           "mark": {
>             "logo": {
>               "name": "mark-logo",
>               "sizes": {
>                 "logo": "//avater/50372/catadfe/logo",
>                 "big-logo": "//avaterfe/50372/catfrg/dealer_logo"
>               }
>             },
>             "vendor_ids": [
>               7
>             ],
>             "cyrillic_name": "Акура"
>           }
>         },
>         {
>           ...
>         }
>       ],
>       "meta_level": "MARK_LEVEL",
>       "offers_count": 646348
>     }
>   ],
>   "status": "SUCCESS"
> }            
> ```

{% include [border-none](../_includes/table-style-border-none-2a2aa0c324bf.md) %}


[*bc_lookup]: {% include notitle [bc_lookup-cars-breadcrumbs](../_includes/popups-00286d1be377.md#bc_lookup-cars-breadcrumbs) %}

[*rid]: {% include notitle [rid-cars-breadcrumbs](../_includes/popups-00286d1be377.md#rid-cars-breadcrumbs) %}

[*state]: {% include [includes-state-description](../_includes/reference/includes/id-includes/state-description-78e689139d95.md) %}

[*mark_ph]: {% include notitle [mark_ph](../_includes/popups-00286d1be377.md#mark_ph) %}

[*model_ph]: {% include notitle [model_ph](../_includes/popups-00286d1be377.md#model_ph) %}

[*configuration_ph]: {% include notitle [configuration_ph](../_includes/popups-00286d1be377.md#configuration_ph) %}

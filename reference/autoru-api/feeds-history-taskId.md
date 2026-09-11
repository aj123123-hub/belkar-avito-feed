---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/feeds-history-taskId.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# GET /feeds/history/{task_id}

Возвращает детализацию по задаче на ручную загрузку прайс-листа.

## Формат запроса {#input}

```
GET https://apiauto.ru/1.0/feeds/history/{[task_id](*task_id)}
? [[page](*page)=<integer>]
& [[page_size](*page_size)=<integer>]
& [[error_type](*error_type)=<array[string]>]
```

<div class="params-table">

{% include notitle [task_id](../_includes/params/feeds-history-taskId-request-92dcc32697fa.md#task_id) %}

{% include notitle [page](../_includes/params/feeds-history-taskId-request-92dcc32697fa.md#page) %}

{% include notitle [page_size](../_includes/params/feeds-history-taskId-request-92dcc32697fa.md#page_size) %}

{% include notitle [error_type](../_includes/params/feeds-history-taskId-request-92dcc32697fa.md#error_type) %}

</div>

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
  "category": {
    "section": {string},
    "category": {string},
    "truck_category": {string},
    "moto_category": {string}
  },
  "task": {
    "id": {integer},
    "created_at": {string},
    "finished_at": {string},
    "type": {string},
    "status": {string},
    "settings ": {
      "internal_url": {string},
      "[settings](*settings-p)": {
          "source": {string},
          "delete_sale": {boolean},
          "leave_services": {boolean},
          "leave_added_images": {boolean},
          "is_active": {boolean}
      }
    },
    "count_offers": {integer},
    "count_errors": {integer},
    "count_notices": {integer},
    "count_offers_inserted": {integer},
    "count_offers_updated": {integer},
    "count_offers_deleted": {integer},
    "count_offers_skipped": {integer},
    "count_images": {integer},
    "count_images_success": {integer},
    "count_images_errors": {integer},
    "count_success": {integer}
  },
  "pagination": {
    "page": {integer},
    "page_size": {integer},
    "total_offers_count": {integer},
    "total_page_count": {integer}
  },
  "filter": {
    "error_type": [
      {string},
      {string}
    ]
  },
  "offers": [
    {
      "position": {integer},
      "status": {string},
      "offer_id": {string},
      "created_at": {string},
      "vin": {string},
      "unique_id": {string},
      "car_info": {
        "armored": {boolean},
        "body_type": {string},
        "engine_type": {string},
        "transmission": {string},
        "drive": {string},
        "mark": {string},
        "model": {string},
        "super_gen_id": {integer},
        "configuration_id": {integer},
        "tech_param_id": {integer},
        "complectation_id": {integer},
        "equipment": {
          "{string}": {boolean},
          "{string}": {boolean}
        },
        "manufacturer_info": {
          "modification_code": {string},
          "interior_code": {string},
          "color_code": {string},
          "equipment_code": {string}
        },
        "steering_wheel": {string},
        "horse_power": {integer},
        "mark_info": {
          "code": {string},
          "name": {string},
          "ru_name": {string},
          "logo": {
            "name": {string},
            "sizes": {
              "{string}": {string}
            },
            "preview": {
              "version": {integer},
              "width": {integer},
              "height": {integer},
              "data": {string}
            }
          },
          "country_id": {string}
        },
        "model_info": {
          "code": {string},
          "name": {string},
          "ru_name": {string},
          "morphology": {
            "gender": {string}
          }
        },
        "super_gen": {
          "id": {string},
          "name": {string},
          "ru_name": {string},
          "year_from": {integer},
          "year_to": {integer},
          "price_segment": {string},
          "purpose_group": {string},
          "no_complect": {boolean}
        },
        "configuration": {
          "id": {string},
          "body_type": {string},
          "doors_count": {integer},
          "auto_class": {string},
          "human_name": {string},
          "trunk_volume_min": {integer},
          "trunk_volume_max": {integer},
          "notice": {string},
          "body_type_group": {string},
          "length": {integer},
          "width": {integer},
          "height": {integer},
          "seats": [
            {integer},
            {integer}
          ],
          "main_photo": {
            "name": {string},
            "sizes": {
              "{string}": {string}
            },
            "preview": {
              "version": {integer},
              "width": {integer},
              "height": {integer},
              "data": {string}
            }
          }
        },
        "tech_param": {
          "id": {string},
          "name": {string},
          "nameplate": {string},
          "displacement": {integer},
          "engine_type": {string},
          "gear_type": {string},
          "gear_type_autoru": {string},
          "transmission": {string},
          "transmission_autoru": {string},
          "power": {integer},
          "power_kvt": {integer},
          "human_name": {string},
          "acceleration": {integer},
          "clearance_min": {integer},
          "clearance_max": {integer}
        },
        "complectation": {
          "id": {string},
          "name": {string},
          "available_options": [
            {string}
          ],
          "additional_options": {},
          "price": {},
          "aliases": {string}
        },
        "vendor": {string}
      },
      "truck_info": {
        "truck_category": {string},
        "mark": {string},
        "model": {string},
        "displacement": {integer},
        "horse_power": {integer},
        "loading": {integer},
        "axis": {integer},
        "seats": {integer},
        "cabin": {string},
        "steering_wheel": {string},
        "engine": {string},
        "transmission": {string},
        "gear": {string},
        "wheel_drive": {string},
        "saddle_height": {string},
        "brakes": {string},
        "euro_class": {string},
        "cabin_suspension": {string},
        "suspension": {string},
        "chassis_suspension": {string},
        "bus_type": {string},
        "trailer_type": {string},
        "swap_body_type": {string},
        "truck_type": {string},
        "light_truck_type": {string},
        "agricultural_type": {string},
        "construction_type": {string},
        "autoloader_type": {string},
        "dredge_type": {string},
        "bulldozer_type": {string},
        "municipal_type": {string},
        "body_type": {string},
        "equipment": {
          "{string}": {boolean},
          "{string}": {boolean}
        },
        "operating_hours": {integer},
        "load_height": {integer},
        "crane_radius": {integer},
        "bucket_volume": {float},
        "traction_class": {string},
        "mark_info": {
          "code": {string},
          "name": {string},
          "ru_name": {string},
          "logo": {
            "name": {string},
            "sizes": {
              "{string}": {string}
            }
          },
          "country_id": {string}
        },
        "model_info": {
          "code": {string},
          "name": {string},
          "ru_name": {string},
          "morphology": {
            "gender": {string}
          }
        }
      },
      "moto_info": {
        "moto_category": {string},
        "mark": {string},
        "model": {string},
        "displacement": {integer},
        "horse_power": {integer},
        "engine": {string},
        "transmission": {string},
        "gear": {string},
        "moto_type": {string},
        "atv_type": {string},
        "snowmobile_type": {string},
        "cylinder_order": {string},
        "cylinder_amount": {string},
        "stroke_amount": {string},
        "equipment": {},
        "mark_info": {
          "code": {string},
          "name": {string},
          "ru_name": {string},
          "logo": {
            "name": {string},
            "sizes": {
              "{string}": {string}
            }
          },
          "country_id": {string}
        },
        "model_info": {
          "code": {string},
          "name": {string},
          "ru_name": {string},
          "morphology": {
            "gender": {string}
          }
        }
      },
      "errors": [
        {
          "type": {string},
          "message": {string},
          "created_at": {string},
          "field_name": {string},
          "field_value": {string}
        }
      ]
    }
  ]
}
```

<div class="params-table">

{% include notitle [category](../_includes/params/feeds-history-taskId-response-db3542d38300.md#category) %}

 
:   {% include notitle [section_condition](../_includes/params/feeds-history-taskId-response-db3542d38300.md#section_condition) %}

    {% include notitle [category](../_includes/params/feeds-history-taskId-response-db3542d38300.md#category) %}

    {% include notitle [truck_category](../_includes/params/feeds-history-taskId-response-db3542d38300.md#truck_category) %}

    {% include notitle [moto_category](../_includes/params/feeds-history-taskId-response-db3542d38300.md#moto_category) %}

{% include notitle [task](../_includes/params/feeds-history-taskId-response-db3542d38300.md#task) %}

 
:   {% include notitle [id](../_includes/params/feeds-history-taskId-response-db3542d38300.md#id) %}

    {% include notitle [created_at](../_includes/params/feeds-history-taskId-response-db3542d38300.md#created_at) %}

    {% include notitle [finished_at](../_includes/params/feeds-history-taskId-response-db3542d38300.md#finished_at) %}

    {% include notitle [type](../_includes/params/feeds-history-taskId-response-db3542d38300.md#type) %}

    {% include notitle [status](../_includes/params/feeds-history-taskId-response-db3542d38300.md#status) %}
    
     
    :   {% include notitle [settings](../_includes/params/feeds-history-taskId-response-db3542d38300.md#settings) %}
        
         
        :   {% include notitle [source](../_includes/params/feeds-history-taskId-response-db3542d38300.md#source) %}

            {% include notitle [delete_sale](../_includes/params/feeds-history-taskId-response-db3542d38300.md#delete_sale) %}

            {% include notitle [leave_services](../_includes/params/feeds-history-taskId-response-db3542d38300.md#leave_services) %}

            {% include notitle [leave_added_images](../_includes/params/feeds-history-taskId-response-db3542d38300.md#leave_added_images) %}

            {% include notitle [is_active](../_includes/params/feeds-history-taskId-response-db3542d38300.md#is_active) %}

    {% include notitle [count_offers](../_includes/params/feeds-history-taskId-response-db3542d38300.md#count_offers) %}

    {% include notitle [count_errors](../_includes/params/feeds-history-taskId-response-db3542d38300.md#count_errors) %}

    {% include notitle [count_notices](../_includes/params/feeds-history-taskId-response-db3542d38300.md#count_notices) %}

    {% include notitle [count_offers_inserted](../_includes/params/feeds-history-taskId-response-db3542d38300.md#count_offers_inserted) %}

    {% include notitle [count_offers_updated](../_includes/params/feeds-history-taskId-response-db3542d38300.md#count_offers_updated) %}

    {% include notitle [count_offers_deleted](../_includes/params/feeds-history-taskId-response-db3542d38300.md#count_offers_deleted) %}

    {% include notitle [count_offers_skipped](../_includes/params/feeds-history-taskId-response-db3542d38300.md#count_offers_skipped) %}

    {% include notitle [count_images](../_includes/params/feeds-history-taskId-response-db3542d38300.md#count_images) %}

    {% include notitle [count_images_success](../_includes/params/feeds-history-taskId-response-db3542d38300.md#count_images_success) %}

    {% include notitle [count_images_errors](../_includes/params/feeds-history-taskId-response-db3542d38300.md#count_images_errors) %}

    {% include notitle [count_success](../_includes/params/feeds-history-taskId-response-db3542d38300.md#count_success) %}

{% include notitle [pagination](../_includes/params/feeds-history-taskId-response-db3542d38300.md#pagination) %}

 
:   {% include notitle [page](../_includes/params/feeds-history-taskId-response-db3542d38300.md#page) %}

    {% include notitle [page_size](../_includes/params/feeds-history-taskId-response-db3542d38300.md#page_size) %}

    {% include notitle [total_offers_count](../_includes/params/feeds-history-taskId-response-db3542d38300.md#total_offers_count) %}

    {% include notitle [total_page_count](../_includes/params/feeds-history-taskId-response-db3542d38300.md#total_page_count) %}

{% include notitle [filter](../_includes/params/feeds-history-taskId-response-db3542d38300.md#filter) %}

 
:   {% include notitle [error_type](../_includes/params/feeds-history-taskId-response-db3542d38300.md#error_type) %}

{% include notitle [offers](../_includes/params/feeds-history-taskId-response-db3542d38300.md#offers) %}

 
:   {% include notitle [position](../_includes/params/feeds-history-taskId-response-db3542d38300.md#position) %}

    {% include notitle [status_ad](../_includes/params/feeds-history-taskId-response-db3542d38300.md#status_ad) %}

    {% include notitle [offer_id](../_includes/params/feeds-history-taskId-response-db3542d38300.md#offer_id) %}

    {% include notitle [created_at](../_includes/params/feeds-history-taskId-response-db3542d38300.md#created_at) %}

    {% include notitle [vin](../_includes/params/feeds-history-taskId-response-db3542d38300.md#vin) %}

    {% include notitle [unique_id](../_includes/params/feeds-history-taskId-response-db3542d38300.md#unique_id) %}

    {% include notitle [car_info](../_includes/params/feeds-history-taskId-response-db3542d38300.md#car_info) %}
    
     
    :   {% include notitle [armored](../_includes/params/feeds-history-taskId-response-db3542d38300.md#armored) %}

        {% include notitle [body_type](../_includes/params/feeds-history-taskId-response-db3542d38300.md#body_type) %}

        {% include notitle [armored](../_includes/params/feeds-history-taskId-response-db3542d38300.md#armored) %}

        {% include notitle [body_type](../_includes/params/feeds-history-taskId-response-db3542d38300.md#body_type) %}

        {% include notitle [engine_type](../_includes/params/feeds-history-taskId-response-db3542d38300.md#engine_type) %}

        {% include notitle [transmission](../_includes/params/feeds-history-taskId-response-db3542d38300.md#transmission) %}

        {% include notitle [drive](../_includes/params/feeds-history-taskId-response-db3542d38300.md#drive) %}

        {% include notitle [mark](../_includes/params/feeds-history-taskId-response-db3542d38300.md#mark) %}

        {% include notitle [model](../_includes/params/feeds-history-taskId-response-db3542d38300.md#model) %}

        {% include notitle [super_gen_id](../_includes/params/feeds-history-taskId-response-db3542d38300.md#super_gen_id) %}

        {% include notitle [configuration_id](../_includes/params/feeds-history-taskId-response-db3542d38300.md#configuration_id) %}

        {% include notitle [tech_param_id](../_includes/params/feeds-history-taskId-response-db3542d38300.md#tech_param_id) %}

        {% include notitle [complectation_id](../_includes/params/feeds-history-taskId-response-db3542d38300.md#complectation_id) %}

        {% include notitle [equipment](../_includes/params/feeds-history-taskId-response-db3542d38300.md#equipment) %}

        {% include notitle [manufacturer_info](../_includes/params/feeds-history-taskId-response-db3542d38300.md#manufacturer_info) %}
        
         
        :   {% include notitle [modification_code](../_includes/params/feeds-history-taskId-response-db3542d38300.md#modification_code) %}

            {% include notitle [interior_code](../_includes/params/feeds-history-taskId-response-db3542d38300.md#interior_code) %}

            {% include notitle [color_code](../_includes/params/feeds-history-taskId-response-db3542d38300.md#color_code) %}

            {% include notitle [equipment_code](../_includes/params/feeds-history-taskId-response-db3542d38300.md#equipment_code) %}

        {% include notitle [steering_wheel](../_includes/params/feeds-history-taskId-response-db3542d38300.md#steering_wheel) %}

        {% include notitle [horse_power](../_includes/params/feeds-history-taskId-response-db3542d38300.md#horse_power) %}

        {% include notitle [mark_info](../_includes/params/feeds-history-taskId-response-db3542d38300.md#mark_info) %}
        
         
        :   {% include notitle [code](../_includes/params/feeds-history-taskId-response-db3542d38300.md#code) %}

            {% include notitle [name](../_includes/params/feeds-history-taskId-response-db3542d38300.md#name) %}

            {% include notitle [ru_name](../_includes/params/feeds-history-taskId-response-db3542d38300.md#ru_name) %}

            {% include notitle [logo](../_includes/params/feeds-history-taskId-response-db3542d38300.md#logo) %}
            
             
            :   {% include notitle [name](../_includes/params/feeds-history-taskId-response-db3542d38300.md#name) %}

                {% include notitle [sizes](../_includes/params/feeds-history-taskId-response-db3542d38300.md#sizes) %}

            {% include notitle [country_id](../_includes/params/feeds-history-taskId-response-db3542d38300.md#country_id) %}

        {% include notitle [model_info](../_includes/params/feeds-history-taskId-response-db3542d38300.md#model_info) %}
        
         
        :   {% include notitle [code](../_includes/params/feeds-history-taskId-response-db3542d38300.md#code) %}

            {% include notitle [name](../_includes/params/feeds-history-taskId-response-db3542d38300.md#name) %}

            {% include notitle [ru_name](../_includes/params/feeds-history-taskId-response-db3542d38300.md#ru_name) %}

            {% include notitle [morphology](../_includes/params/feeds-history-taskId-response-db3542d38300.md#morphology) %}
            
             
            :   {% include notitle [gender](../_includes/params/feeds-history-taskId-response-db3542d38300.md#gender) %}

        {% include notitle [super_gen](../_includes/params/feeds-history-taskId-response-db3542d38300.md#super_gen) %}
        
         
        :   {% include notitle [id](../_includes/params/feeds-history-taskId-response-db3542d38300.md#id_gen) %}

            {% include notitle [name](../_includes/params/feeds-history-taskId-response-db3542d38300.md#name) %}

            {% include notitle [year_from](../_includes/params/feeds-history-taskId-response-db3542d38300.md#year_from) %}

            {% include notitle [year_to](../_includes/params/feeds-history-taskId-response-db3542d38300.md#year_to) %}

            {% include notitle [price_segment](../_includes/params/feeds-history-taskId-response-db3542d38300.md#price_segment) %}

            {% include notitle [purpose_group](../_includes/params/feeds-history-taskId-response-db3542d38300.md#purpose_group) %}

            {% include notitle [no_complect](../_includes/params/feeds-history-taskId-response-db3542d38300.md#no_complect) %}

        {% include notitle [configuration](../_includes/params/feeds-history-taskId-response-db3542d38300.md#configuration) %}
        
         
        :   {% include notitle [configuration_id](../_includes/params/feeds-history-taskId-response-db3542d38300.md#configuration_id) %}

            {% include notitle [doors_count](../_includes/params/feeds-history-taskId-response-db3542d38300.md#doors_count) %}

            {% include notitle [auto_class](../_includes/params/feeds-history-taskId-response-db3542d38300.md#auto_class) %}

            {% include notitle [human_name](../_includes/params/feeds-history-taskId-response-db3542d38300.md#human_name) %}

            {% include notitle [trunk_volume_min](../_includes/params/feeds-history-taskId-response-db3542d38300.md#trunk_volume_min) %}

            {% include notitle [trunk_volume_max](../_includes/params/feeds-history-taskId-response-db3542d38300.md#trunk_volume_max) %}

            {% include notitle [notice](../_includes/params/feeds-history-taskId-response-db3542d38300.md#notice) %}

            {% include notitle [length](../_includes/params/feeds-history-taskId-response-db3542d38300.md#length) %}

            {% include notitle [width](../_includes/params/feeds-history-taskId-response-db3542d38300.md#width) %}

            {% include notitle [height](../_includes/params/feeds-history-taskId-response-db3542d38300.md#height) %}

            {% include notitle [seats](../_includes/params/feeds-history-taskId-response-db3542d38300.md#seats) %}

            {% include notitle [main_photo](../_includes/params/feeds-history-taskId-response-db3542d38300.md#main_photo) %}
            
             
            :   {% include notitle [name](../_includes/params/feeds-history-taskId-response-db3542d38300.md#name) %}

                {% include notitle [sizes](../_includes/params/feeds-history-taskId-response-db3542d38300.md#sizes) %}

        {% include notitle [tech_param](../_includes/params/feeds-history-taskId-response-db3542d38300.md#tech_param) %}
        
         
        :   {% include notitle [id](../_includes/params/feeds-history-taskId-response-db3542d38300.md#id) %}

            {% include notitle [name](../_includes/params/feeds-history-taskId-response-db3542d38300.md#name) %}
            
            {% include notitle [nameplate](../_includes/params/feeds-history-taskId-response-db3542d38300.md#nameplate) %}

            {% include notitle [displacement](../_includes/params/feeds-history-taskId-response-db3542d38300.md#displacement) %}

            {% include notitle [engine_type](../_includes/params/feeds-history-taskId-response-db3542d38300.md#engine_type) %}

            {% include notitle [gear_type](../_includes/params/feeds-history-taskId-response-db3542d38300.md#gear_type) %}

            {% include notitle [transmission](../_includes/params/feeds-history-taskId-response-db3542d38300.md#transmission) %}

            {% include notitle [power](../_includes/params/feeds-history-taskId-response-db3542d38300.md#power) %}

            {% include notitle [power_kvt](../_includes/params/feeds-history-taskId-response-db3542d38300.md#power_kvt) %}

            {% include notitle [human_name](../_includes/params/feeds-history-taskId-response-db3542d38300.md#human_name) %}

            {% include notitle [acceleration](../_includes/params/feeds-history-taskId-response-db3542d38300.md#acceleration) %}

            {% include notitle [clearance_min](../_includes/params/feeds-history-taskId-response-db3542d38300.md#clearance_min) %}

            {% include notitle [clearance_max](../_includes/params/feeds-history-taskId-response-db3542d38300.md#clearance_max) %}

        {% include notitle [complectation](../_includes/params/feeds-history-taskId-response-db3542d38300.md#complectation) %}
        
         
        :   {% include notitle [id](../_includes/params/feeds-history-taskId-response-db3542d38300.md#id) %}

            {% include notitle [name](../_includes/params/feeds-history-taskId-response-db3542d38300.md#name) %}

            {% include notitle [available_options](../_includes/params/feeds-history-taskId-response-db3542d38300.md#available_options) %}

            {% include notitle [additional_options](../_includes/params/feeds-history-taskId-response-db3542d38300.md#additional_options) %}

            {% include notitle [price](../_includes/params/feeds-history-taskId-response-db3542d38300.md#price) %}

            {% include notitle [aliases](../_includes/params/feeds-history-taskId-response-db3542d38300.md#aliases) %}

        {% include notitle [vendor](../_includes/params/feeds-history-taskId-response-db3542d38300.md#vendor) %}

    {% include notitle [truck_info](../_includes/params/feeds-history-taskId-response-db3542d38300.md#truck_info) %}
    
     
    :   {% include notitle [truck_category](../_includes/params/feeds-history-taskId-response-db3542d38300.md#truck_category) %}

        {% include notitle [mark](../_includes/params/feeds-history-taskId-response-db3542d38300.md#mark) %}

        {% include notitle [model](../_includes/params/feeds-history-taskId-response-db3542d38300.md#model) %}

        {% include notitle [displacement](../_includes/params/feeds-history-taskId-response-db3542d38300.md#displacement) %}

        {% include notitle [horse_power](../_includes/params/feeds-history-taskId-response-db3542d38300.md#horse_power) %}

        {% include notitle [loading](../_includes/params/feeds-history-taskId-response-db3542d38300.md#loading) %}

        {% include notitle [axis](../_includes/params/feeds-history-taskId-response-db3542d38300.md#axis) %}

        {% include notitle [seats](../_includes/params/feeds-history-taskId-response-db3542d38300.md#seats) %}

        {% include notitle [acceleration](../_includes/params/feeds-history-taskId-response-db3542d38300.md#acceleration) %}

        {% include notitle [clearance_min](../_includes/params/feeds-history-taskId-response-db3542d38300.md#clearance_min) %}

        {% include notitle [clearance_max](../_includes/params/feeds-history-taskId-response-db3542d38300.md#clearance_max) %}

        {% include notitle [complectation](../_includes/params/feeds-history-taskId-response-db3542d38300.md#complectation) %}

        {% include notitle [id](../_includes/params/feeds-history-taskId-response-db3542d38300.md#id) %}

        {% include notitle [name](../_includes/params/feeds-history-taskId-response-db3542d38300.md#name) %}

        {% include notitle [available_options](../_includes/params/feeds-history-taskId-response-db3542d38300.md#available_options) %}

        {% include notitle [additional_options](../_includes/params/feeds-history-taskId-response-db3542d38300.md#additional_options) %}

        {% include notitle [price](../_includes/params/feeds-history-taskId-response-db3542d38300.md#price) %}

        {% include notitle [aliases](../_includes/params/feeds-history-taskId-response-db3542d38300.md#aliases) %}

        {% include notitle [vendor](../_includes/params/feeds-history-taskId-response-db3542d38300.md#vendor) %}

        {% include notitle [truck_info](../_includes/params/feeds-history-taskId-response-db3542d38300.md#truck_info) %}

        {% include notitle [truck_category](../_includes/params/feeds-history-taskId-response-db3542d38300.md#truck_category) %}

        {% include notitle [mark](../_includes/params/feeds-history-taskId-response-db3542d38300.md#mark) %}

        {% include notitle [model](../_includes/params/feeds-history-taskId-response-db3542d38300.md#model) %}

        {% include notitle [displacement](../_includes/params/feeds-history-taskId-response-db3542d38300.md#displacement) %}

        {% include notitle [horse_power](../_includes/params/feeds-history-taskId-response-db3542d38300.md#horse_power) %}

        {% include notitle [loading](../_includes/params/feeds-history-taskId-response-db3542d38300.md#loading) %}

        {% include notitle [axis](../_includes/params/feeds-history-taskId-response-db3542d38300.md#axis) %}

        {% include notitle [seats](../_includes/params/feeds-history-taskId-response-db3542d38300.md#seats) %}

        {% include notitle [cabin](../_includes/params/feeds-history-taskId-response-db3542d38300.md#cabin) %}

        {% include notitle [steering_wheel](../_includes/params/feeds-history-taskId-response-db3542d38300.md#steering_wheel) %}

        {% include notitle [engine](../_includes/params/feeds-history-taskId-response-db3542d38300.md#engine) %}

        {% include notitle [transmission](../_includes/params/feeds-history-taskId-response-db3542d38300.md#transmission) %}

        {% include notitle [gear](../_includes/params/feeds-history-taskId-response-db3542d38300.md#gear) %}

        {% include notitle [wheel_drive](../_includes/params/feeds-history-taskId-response-db3542d38300.md#wheel_drive) %}

        {% include notitle [saddle_height](../_includes/params/feeds-history-taskId-response-db3542d38300.md#saddle_height) %}

        {% include notitle [brakes](../_includes/params/feeds-history-taskId-response-db3542d38300.md#brakes) %}

        {% include notitle [euro_class](../_includes/params/feeds-history-taskId-response-db3542d38300.md#euro_class) %}

        {% include notitle [cabin_suspension](../_includes/params/feeds-history-taskId-response-db3542d38300.md#cabin_suspension) %}

        {% include notitle [suspension](../_includes/params/feeds-history-taskId-response-db3542d38300.md#suspension) %}

        {% include notitle [chassis_suspension](../_includes/params/feeds-history-taskId-response-db3542d38300.md#chassis_suspension) %}

        {% include notitle [bus_type](../_includes/params/feeds-history-taskId-response-db3542d38300.md#bus_type) %}

        {% include notitle [trailer_type](../_includes/params/feeds-history-taskId-response-db3542d38300.md#trailer_type) %}

        {% include notitle [swap_body_type](../_includes/params/feeds-history-taskId-response-db3542d38300.md#swap_body_type) %}

        {% include notitle [truck_type](../_includes/params/feeds-history-taskId-response-db3542d38300.md#truck_type) %}

        {% include notitle [light_truck_type](../_includes/params/feeds-history-taskId-response-db3542d38300.md#light_truck_type) %}

        {% include notitle [agricultural_type](../_includes/params/feeds-history-taskId-response-db3542d38300.md#agricultural_type) %}

        {% include notitle [construction_type](../_includes/params/feeds-history-taskId-response-db3542d38300.md#construction_type) %}

        {% include notitle [autoloader_type](../_includes/params/feeds-history-taskId-response-db3542d38300.md#autoloader_type) %}

        {% include notitle [dredge_type](../_includes/params/feeds-history-taskId-response-db3542d38300.md#dredge_type) %}

        {% include notitle [bulldozer_type](../_includes/params/feeds-history-taskId-response-db3542d38300.md#bulldozer_type) %}

        {% include notitle [municipal_type](../_includes/params/feeds-history-taskId-response-db3542d38300.md#municipal_type) %}

        {% include notitle [body_type](../_includes/params/feeds-history-taskId-response-db3542d38300.md#body_type) %}

        {% include notitle [equipment](../_includes/params/feeds-history-taskId-response-db3542d38300.md#equipment) %}

        {% include notitle [operating_hours](../_includes/params/feeds-history-taskId-response-db3542d38300.md#operating_hours) %}

        {% include notitle [load_height](../_includes/params/feeds-history-taskId-response-db3542d38300.md#load_height) %}

        {% include notitle [crane_radius](../_includes/params/feeds-history-taskId-response-db3542d38300.md#crane_radius) %}

        {% include notitle [bucket_volume](../_includes/params/feeds-history-taskId-response-db3542d38300.md#bucket_volume) %}

        {% include notitle [traction_class](../_includes/params/feeds-history-taskId-response-db3542d38300.md#traction_class) %}

        {% include notitle [mark_info](../_includes/params/feeds-history-taskId-response-db3542d38300.md#mark_info) %}
        
         
        :   {% include notitle [code](../_includes/params/feeds-history-taskId-response-db3542d38300.md#code) %}

            {% include notitle [name](../_includes/params/feeds-history-taskId-response-db3542d38300.md#name) %}

            {% include notitle [ru_name](../_includes/params/feeds-history-taskId-response-db3542d38300.md#ru_name) %}

            {% include notitle [logo](../_includes/params/feeds-history-taskId-response-db3542d38300.md#logo) %}
            
             
            :   {% include notitle [name](../_includes/params/feeds-history-taskId-response-db3542d38300.md#name) %}

                {% include notitle [sizes](../_includes/params/feeds-history-taskId-response-db3542d38300.md#sizes) %}

            {% include notitle [country_id](../_includes/params/feeds-history-taskId-response-db3542d38300.md#country_id) %}

        {% include notitle [model_info](../_includes/params/feeds-history-taskId-response-db3542d38300.md#model_info) %}
        
         
        :   {% include notitle [code](../_includes/params/feeds-history-taskId-response-db3542d38300.md#code) %}

            {% include notitle [name](../_includes/params/feeds-history-taskId-response-db3542d38300.md#name) %}

            {% include notitle [ru_name](../_includes/params/feeds-history-taskId-response-db3542d38300.md#ru_name) %}

            {% include notitle [morphology](../_includes/params/feeds-history-taskId-response-db3542d38300.md#morphology) %}
            
             
            :   {% include notitle [gender](../_includes/params/feeds-history-taskId-response-db3542d38300.md#gender) %}

    {% include notitle [moto_info](../_includes/params/feeds-history-taskId-response-db3542d38300.md#moto_info) %}
    
     
    :   {% include notitle [moto_category](../_includes/params/feeds-history-taskId-response-db3542d38300.md#moto_category) %}

        {% include notitle [mark](../_includes/params/feeds-history-taskId-response-db3542d38300.md#mark) %}

        {% include notitle [model](../_includes/params/feeds-history-taskId-response-db3542d38300.md#model) %}

        {% include notitle [displacement](../_includes/params/feeds-history-taskId-response-db3542d38300.md#displacement) %}

        {% include notitle [horse_power](../_includes/params/feeds-history-taskId-response-db3542d38300.md#horse_power) %}

        {% include notitle [engine](../_includes/params/feeds-history-taskId-response-db3542d38300.md#engine) %}

        {% include notitle [transmission](../_includes/params/feeds-history-taskId-response-db3542d38300.md#transmission) %}

        {% include notitle [gear](../_includes/params/feeds-history-taskId-response-db3542d38300.md#gear) %}

        {% include notitle [moto_type](../_includes/params/feeds-history-taskId-response-db3542d38300.md#moto_type) %}

        {% include notitle [swap_body_type](../_includes/params/feeds-history-taskId-response-db3542d38300.md#swap_body_type) %}

        {% include notitle [truck_type](../_includes/params/feeds-history-taskId-response-db3542d38300.md#truck_type) %}

        {% include notitle [light_truck_type](../_includes/params/feeds-history-taskId-response-db3542d38300.md#light_truck_type) %}

        {% include notitle [agricultural_type](../_includes/params/feeds-history-taskId-response-db3542d38300.md#agricultural_type) %}

        {% include notitle [construction_type](../_includes/params/feeds-history-taskId-response-db3542d38300.md#construction_type) %}

        {% include notitle [autoloader_type](../_includes/params/feeds-history-taskId-response-db3542d38300.md#autoloader_type) %}

        {% include notitle [dredge_type](../_includes/params/feeds-history-taskId-response-db3542d38300.md#dredge_type) %}

        {% include notitle [bulldozer_type](../_includes/params/feeds-history-taskId-response-db3542d38300.md#bulldozer_type) %}

        {% include notitle [municipal_type](../_includes/params/feeds-history-taskId-response-db3542d38300.md#municipal_type) %}

        {% include notitle [body_type](../_includes/params/feeds-history-taskId-response-db3542d38300.md#body_type) %}

        {% include notitle [equipment](../_includes/params/feeds-history-taskId-response-db3542d38300.md#equipment) %}

        {% include notitle [operating_hours](../_includes/params/feeds-history-taskId-response-db3542d38300.md#operating_hours) %}

        {% include notitle [load_height](../_includes/params/feeds-history-taskId-response-db3542d38300.md#load_height) %}

        {% include notitle [crane_radius](../_includes/params/feeds-history-taskId-response-db3542d38300.md#crane_radius) %}

        {% include notitle [bucket_volume](../_includes/params/feeds-history-taskId-response-db3542d38300.md#bucket_volume) %}

        {% include notitle [traction_class](../_includes/params/feeds-history-taskId-response-db3542d38300.md#traction_class) %}

        {% include notitle [mark_info](../_includes/params/feeds-history-taskId-response-db3542d38300.md#mark_info) %}
        
         
        :   {% include notitle [code](../_includes/params/feeds-history-taskId-response-db3542d38300.md#code) %}

            {% include notitle [name](../_includes/params/feeds-history-taskId-response-db3542d38300.md#name) %}

            {% include notitle [ru_name](../_includes/params/feeds-history-taskId-response-db3542d38300.md#ru_name) %}

            {% include notitle [logo](../_includes/params/feeds-history-taskId-response-db3542d38300.md#logo) %}
            
             
            :   {% include notitle [name](../_includes/params/feeds-history-taskId-response-db3542d38300.md#name) %}

                {% include notitle [sizes](../_includes/params/feeds-history-taskId-response-db3542d38300.md#sizes) %}

            {% include notitle [country_id](../_includes/params/feeds-history-taskId-response-db3542d38300.md#country_id) %}

        {% include notitle [model_info](../_includes/params/feeds-history-taskId-response-db3542d38300.md#model_info) %}
        
         
        :   {% include notitle [code](../_includes/params/feeds-history-taskId-response-db3542d38300.md#code) %}

            {% include notitle [name](../_includes/params/feeds-history-taskId-response-db3542d38300.md#name) %}

            {% include notitle [ru_name](../_includes/params/feeds-history-taskId-response-db3542d38300.md#ru_name) %}

            {% include notitle [morphology](../_includes/params/feeds-history-taskId-response-db3542d38300.md#morphology) %}
            
             
            :   {% include notitle [gender](../_includes/params/feeds-history-taskId-response-db3542d38300.md#gender) %}    

{% include notitle [errors](../_includes/params/feeds-history-taskId-response-db3542d38300.md#errors) %}

 
:   {% include notitle [type](../_includes/params/feeds-history-taskId-response-db3542d38300.md#type) %}

    {% include notitle [message](../_includes/params/feeds-history-taskId-response-db3542d38300.md#message) %}

    {% include notitle [created_at](../_includes/params/feeds-history-taskId-response-db3542d38300.md#created_at) %}

    {% include notitle [field_name](../_includes/params/feeds-history-taskId-response-db3542d38300.md#field_name) %}

    {% include notitle [field_value](../_includes/params/feeds-history-taskId-response-db3542d38300.md#field_value) %}


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
> curl -i -X GET 'https://apiauto.ru/1.0/feeds/history/11686000?page=1&page_size=2&error_type=NOTICE' -H 'x-authorization: 2dtrer432...' -H 'x-session-id: 112_aoR02Tpv...'
> ```
> 
> 
> Ответ:
> 
> 
> ```json
> HTTP/1.1 200 OK
> Server: nginx
> Date: Fri, 15 Jun 2018 13:30:59 GMT
> Content-Type: application/json
> Connection: keep-alive
>                     
> {
>   "category": {
>     "section": "USED",
>     "category": "CARS"
>   },
>   "task": {
>     "id": "11686000",
>     "created_at": "2019-06-24T14:43:05Z",
>     "finished_at": "2019-06-24T14:43:32Z",
>     "type": "AUTOMATIC",
>     "status": "FAILURE",
>     "settings": {
>       "internal_url": "https://vertis-feeds.s3.mdst.yandex.net/118305_d0d49fc31d3c8d35357a01c8f6d68f65",
>       "settings": {
>         "source": "http://www.major-expert.ru/AutoRu-A.xml",
>         "delete_sale": true,
>         "leave_services": true,
>         "leave_added_images": false
>       }
>     },
>     "count_offers": 890,
>     "count_errors": 0,
>     "count_notices": 814,
>     "count_offers_inserted": 0,
>     "count_offers_updated": 0,
>     "count_offers_deleted": 0,
>     "count_offers_skipped": 0,
>     "count_images": 13332,
>     "count_images_success": 13332,
>     "count_images_errors": 0,
>     "count_success": 0
>   },
>   "pagination": {
>     "page": 1,
>     "page_size": 2,
>     "total_offers_count": 814,
>     "total_page_count": 407
>   },
>   "filter": {
>     "error_type": [
>       "NOTICE"
>     ]
>   },
>   "offers": [
>     {
>       "position": 0,
>       "status": "ERROR",
>       "errors": [
>         {
>           "type": "NOTICE",
>           "message": "Не указано значение комплектации, выберите из списка: Business, Business 4XMOTION, R-line, R-line Executive, Base, Base 4XMOTION, Wolfsburg Edition, Wolfsburg Edition 4XMOTION",
>           "field_name": "complectation_name"
>         }
>       ]
>     },
>     {
>       "position": 1,
>       "status": "ERROR",
>       "errors": [
>         {
>           "type": "NOTICE",
>           "message": "Не указано значение комплектации, выберите из списка: SYNC Edition, Trend, Special Edition",
>           "field_name": "complectation_name"
>         }
>       ]
>     }
>   ]
> }           
> ```

{% include [table-style](../_includes/table-style-border-none-2a2aa0c324bf.md) %}

[*error_type]: {% include notitle [error_type](../_includes/popups-00286d1be377.md#error_type) %}

[*page]: {% include notitle [page](../_includes/popups-00286d1be377.md#page) %}

[*page_size]: {% include notitle [page_size](../_includes/popups-00286d1be377.md#page_size) %}

[*task_id]: Идентификатор задачи на ручную загрузку прайс-листа.

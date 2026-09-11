---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/auction-cars-used-listing-offer.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# POST /dealer/auction/cars/used/listing/offer

Позволяет получить список объявлений, попадающих под фильтр для рекламной кампании.

## Формат запроса {#input}

```
POST https://apiauto.ru/1.0/dealer/auction/cars/used/listing/offer
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

### Формат тела запроса {#structure-in}

```json
{
  "filters": {
    "in_stock": "{string}",
    "year_from": {integer},
    "year_to": {integer},
    "price_from": {integer},
    "price_to": {integer},
    "catalog_filter": [
      {
        "mark": "{string}",
        "model": "{string}",
        "generation": {string},
      }
    ],
   
    "vin_codes": [
      "{string}"
    ],
    "vin_report_statuses": [
      "{string}"
    ],
  },
  "promo_campaign_id": {string},
  "market_segment_filter": {
    "available_segments": [
    {string}
    ]
  },
  "change_at": "date",
  "pagination": {
   "page": {integer},
   "page_size": {integer}
  },
  "max_offer_daily_calls": {integer},
  "bidding_algorithm": {
    "max_position_for_price": {
      "max_bid": {integer}
    }
  },
  "days_on_stock": {
    "from": {integer},
    "to": {integer}
  },
  "days_without_calls": {
    "from": {integer},
    "to": {integer}
  }
}

```

<div class="params-table">

{% include notitle [filters](../_includes/params/auction-cars-used-listing-offer-30b60dd406d2.md#filters) %}

 
:   {% include notitle [in_stock](../_includes/params/auction-cars-used-listing-offer-30b60dd406d2.md#in_stock) %}

    {% include notitle [year_from](../_includes/params/auction-cars-used-listing-offer-30b60dd406d2.md#year_from) %}

    {% include notitle [year_to](../_includes/params/auction-cars-used-listing-offer-30b60dd406d2.md#year_to) %}

    {% include notitle [price_from](../_includes/params/auction-cars-used-listing-offer-30b60dd406d2.md#price_from) %}

    {% include notitle [price_to](../_includes/params/auction-cars-used-listing-offer-30b60dd406d2.md#price_to) %}

    {% include notitle [catalog_filter](../_includes/params/auction-cars-used-listing-offer-30b60dd406d2.md#catalog_filter) %}

     
    :   {% include notitle [mark](../_includes/params/auction-cars-used-listing-offer-30b60dd406d2.md#mark) %}

        {% include notitle [model](../_includes/params/auction-cars-used-listing-offer-30b60dd406d2.md#model) %}
        
        {% include notitle [generation](../_includes/params/auction-cars-used-listing-offer-30b60dd406d2.md#generation) %}

    {% include notitle [vin_codes](../_includes/params/auction-cars-used-listing-offer-30b60dd406d2.md#vin_codes) %}

    {% include notitle [vin_report_statuses](../_includes/params/auction-cars-used-listing-offer-30b60dd406d2.md#vin_report_statuses) %}

{% include notitle [promo_campaign_id](../_includes/params/auction-cars-used-listing-offer-30b60dd406d2.md#promo_campaign_id) %}

{% include notitle [available_segments](../_includes/params/auction-cars-used-listing-offer-30b60dd406d2.md#available_segments) %}

{% include notitle [change_at](../_includes/params/auction-cars-used-listing-offer-30b60dd406d2.md#change_at) %}

{% include notitle [pagination](../_includes/params/auction-cars-used-listing-offer-30b60dd406d2.md#pagination) %}

 
:   {% include notitle [page](../_includes/params/auction-cars-used-listing-offer-30b60dd406d2.md#page) %}

    {% include notitle [page_size](../_includes/params/auction-cars-used-listing-offer-30b60dd406d2.md#page_size) %}

{% include notitle [max_offer_daily_calls](../_includes/params/auction-cars-used-listing-offer-30b60dd406d2.md#max_offer_daily_calls) %}

{% include notitle [max_position_for_price](../_includes/params/auction-cars-used-listing-offer-30b60dd406d2.md#max_position_for_price) %}

{% include notitle [max_bid](../_includes/params/auction-cars-used-listing-offer-30b60dd406d2.md#max_bid) %}

{% include notitle [days_on_stock](../_includes/params/auction-cars-used-listing-offer-30b60dd406d2.md#days_on_stock) %}

 
:   {% include notitle [from](../_includes/params/auction-cars-used-listing-offer-30b60dd406d2.md#from) %}

    {% include notitle [to](../_includes/params/auction-cars-used-listing-offer-30b60dd406d2.md#to) %}

{% include notitle [days_without_calls](../_includes/params/auction-cars-used-listing-offer-30b60dd406d2.md#days_without_calls) %}

 
:   {% include notitle [from](../_includes/params/auction-cars-used-listing-offer-30b60dd406d2.md#from) %}

    {% include notitle [to](../_includes/params/auction-cars-used-listing-offer-30b60dd406d2.md#to) %}


</div>

Общая структура ответа приведена ниже. Порядок следования элементов не гарантируется. В структуре могут присутствовать служебные параметры, которые не описаны в таблице.

## Формат ответа {#output-structure}

```json
 {
  "offers": [
    {
      "car_info": {
        "armored": {boolean},
        "body_type": "{string}",
        "engine_type": "{string}",
        "transmission": "{string}",
        "drive": "{string}",
        "mark": "{string}",
        "model": "{string}",
        "super_gen_id": {string},
        "configuration_id": {string},
        "tech_param_id": {string},
        "complectation_id": {string},
        "equipment": {
          "additionalProp1": {boolean},
          "additionalProp2": {boolean},
          "additionalProp3": {boolean}
        },
        "manufacturer_info": {
          "modification_code": "{string}",
          "interior_code": "{string}",
          "color_code": "{string}",
          "equipment_code": "{string}"
        },
        "steering_wheel": "{string}",
        "horse_power": {string},
        "mark_info": {
          "code": "{string}",
          "name": "{string}",
          "ru_name": "{string}",
          "logo": {
            "name": "{string}",
            "sizes": "{string}",
            "transform": {
              "angle": {integer},
              "blur": {boolean}
            },
            "preview": {
              "version": {integer},
              "width": {integer},
              "height": {integer},
              "data": "{string}"
            },
            "namespace": "{string}",
            "is_deleted": {boolean},
            "is_internal": {boolean},
            "photo_type": "{string}",
            "photo_class": "{string}",
            "create_date": {integer},
            "delete_date": {integer},
            "orig_width": {integer},
            "orig_height": {integer},
            "is_hd": {boolean},
            "is_hidden_from_report": {boolean},
            "is_deleted_by_moderator": {boolean}
          },
          "country_id": "{string}",
          "tags": [
            "{string}"
          ],
          "numeric_id": {string}
        },
        "model_info": {
          "code": "{string}",
          "name": "{string}",
          "ru_name": "{string}",
          "morphology": {
            "gender": "{string}"
          },
          "nameplate": {
            "code": "{string}",
            "name": "{string}",
            "semantic_url": "{string}",
            "no_model": {boolean}
          },
          "tags": [
            "{string}"
          ]
        },
  "filters": {
      "year_from": {integer},
      "year_to": {integer},
      "price_from": {integer},
      "price_to": {integer},      
      "catalog_filter": [
        {
          "mark": "{string}",
          "model": "{string}",
          "generation": {string},
        }  
       ]  
      },
      "vin_codes": [
        "{string}"
      ],
      "vin_report_statuses": [
        "{string}"
      ],
    },
    "sorting": {
      "name": "{string}",
      "desc": {boolean}
    },
    "deliveries": {
      "push_delivery": {
        "enabled": {boolean}
      },
      "email_delivery": {
        "enabled": {boolean},
        "period": "{integer}"
      }
    },
    "view": {
      "mark_model_nameplate_gen_views": [
        {
          "mark": {
            "code": "{string}",
            "name": "{string}",
            "ru_name": "{string}",
            "logo": {
              "name": "{string}",
              "sizes": "{string}",
              "transform": {
                "angle": {integer},
                "blur": {boolean}
              },
              "preview": {
                "version": {integer},
                "width": {integer},
                "height": {integer},
                "data": "{string}"
              },
              "namespace": "{string}",
              "is_deleted": {boolean},
              "is_internal": {boolean},
              "photo_type": "{string}",
              "photo_class": "{string}",
              "create_date": {integer},
              "delete_date": {integer},
              "orig_width": {integer},
              "orig_height": {integer},
              "is_hd": {boolean},
              "is_hidden_from_report": {boolean},
              "is_deleted_by_moderator": {boolean}
            },
            "country_id": "[96] - {string}",
            "tags": [
              "{string}"
            ],
            "numeric_id": {string}
          },
          "model": {
            "code": "{string}",
            "name": "{string}",
            "ru_name": "{string}",
            "morphology": {
              "gender": "{string}"
            },
            "nameplate": {
              "code": "{string}",
              "name": "{string}",
              "semantic_url": "{string}",
              "no_model": {boolean}
            },
            "tags": [
              "{string}"
            ]
          },
          "nameplate": {
            "code": "{string}",
            "name": "{string}",
            "semantic_url": "{string}",
            "no_model": {boolean}
          },
          "super_gen": {
            "id": {string},
            "name": "{string}",
            "ru_name": "{string}",
            "year_from": {integer},
            "year_to": {integer},
            "price_segment": "{string}",
            "purpose_group": "{string}",
            "no_complect": {boolean},
            "is_restyle": {boolean},
            "tags": [
              "{string}"
            ]
          }
        }
      ],
      "vendor_views": [
        {
          "code": "{string}",
          "name": "{string}"
        }
      ],
      "regions": [
        {
          "id": {integer},
          "name": "{string}",
          "genitive": "{string}",
          "dative": "{string}",
          "accusative": "{string}",
          "instrumental": "{string}",
          "prepositional": "{string}",
          "preposition": "{string}",
          "latitude": {integer},
          "longitude": {integer},
          "sub_title": "{string}",
          "supports_geo_radius": {boolean},
          "default_radius": {integer},
          "children": [
            "{string}"
          ],
          "parent_ids": [
            {string}
          ]
        }
      ],
      "applied_filter_count": {string},
      "tech_param": {
        "id": {string},
        "name": "{string}"
      },
      "complectation": {
        "id": {string},
        "name": "{string}"
      },
      "applied_filter_fields": [
        "{string}"
      ],
      "salon": {
        "code": "{string}",
        "is_official": {boolean},
        "loyalty_program": {boolean}
      }
    },
    "unsupported_fields": [
      {
        "code": "{string}",
        "name": "{string}",
        "feature": "{string}"
      }
    ],
    "creation_timestamp": "date",
    "searcher_query": "{string}"
  },
  "grouping": {
    "single_offers_count": {integer},
    "groups_count": {integer}
  },
  "search_id": "{string}",
  "title_code": "{string}",
  "status": "{string}",
} 
    
```

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
 || 403 | AGENT_ACCESS_FORBIDDEN | Доступ для данного пользователя запрещен. || 

|#

## Пример {#example-JSON}

> Запрос:
> 
> 
> ```http
> curl -X 'POST' \
> 'http://apiauto.ru/1.0/dealer/auction/cars/used/listing/offer' \
> -H 'accept: application/json' \
> -H 'x-authorization: xxxxxxxxxxxx' \
> -H 'Content-Type: application/json' \
> -d '
> {
>   "filters": {
>     "in_stock": "ANY_STOCK",
>     "year_from": 0,
>     "year_to": 0,
>     "price_from": 0,
>     "price_to": 0,
>     "catalog_filter": [
>       {
>         "mark": "BMW",
>         "model": "X1",
>         "generation": 8246645,
>     "vin_codes": [
>       "string"
>     ],
>     "vin_report_statuses": [
>       "CHECKED"
>     ],
>   },
>   "promo_campaign_id": 0,
>   "market_segment_filter": {
>     "available_segments": [
>       0
>     ]
>   },
>   "change_at": "2022-09-01T11:48:44.538Z",
>   "pagination": {
>     "page": 1,
>     "page_size": 10
>   },
>   "max_offer_daily_calls": 0,
>   "bidding_algorithm": {
>     "max_position_for_price": {
>       "max_bid": 0
>     }
>   },
>   "days_on_stock": {
>     "from": 0,
>     "to": 0
>   },
>   "days_without_calls": {
>     "from": 0,
>     "to": 0
>   }
> }
> ```
> 
> 
> Ответ:
> 
> 
> ```json
>  {
>   "offers": [
>     {
>       "car_info": {
>         "armored": false,
>         "body_type": "ALLROAD_5_DOORS",
>         "engine_type": "DIESEL",
>         "transmission": "AUTOMATIC",
>         "drive": "ALL",
>         "mark": "MERCEDES",
>         "model": "GL_KLASSE",
>         "super_gen_id": 4986814,
>         "configuration_id": 4986815,
>         "tech_param_id": 4986817,
>         "complectation_id": 6414696,
>         "equipment": {
>           "additionalProp1": true,
>           "additionalProp2": true,
>           "additionalProp3": true
>         },
>         "manufacturer_info": {
>           "modification_code": "A2S6D1617D216",
>           "interior_code": "2Q",
>           "color_code": "2Q",
>           "equipment_code": "4A3"
>         },
>         "steering_wheel": "LEFT",
>         "horse_power": 224,
>         "mark_info": {
>           "code": "MERCEDES",
>           "name": "Mercedes-Benz",
>           "ru_name": "Мерседес-Бенц",
>           "logo": {
>             "name": "string",
>             "sizes": "{'orig': '//avatars.mds.yandex.net/get-autoru/1121/image_name/orig'}",
>             "transform": {
>               "angle": 0,
>               "blur": true
>             },
>             "preview": {
>               "version": 0,
>               "width": 0,
>               "height": 0,
>               "data": "string"
>             },
>             "namespace": "string",
>             "is_deleted": true,
>             "is_internal": true,
>             "photo_type": "STS_FRONT",
>             "photo_class": "PHOTO_CLASS_UNDEFINED",
>             "create_date": 0,
>             "delete_date": 0,
>             "orig_width": 0,
>             "orig_height": 0,
>             "is_hd": true,
>             "is_hidden_from_report": true,
>             "is_deleted_by_moderator": true
>           },
>           "country_id": "[96] - Германия",
>           "tags": [
>             "string"
>           ],
>           "numeric_id": 3136
>         },
>         "model_info": {
>           "code": "GL_KLASSE",
>           "name": "GL-klasse",
>           "ru_name": "GL-класс",
>           "morphology": {
>             "gender": "MASCULINE"
>           },
>           "nameplate": {
>             "code": "9265330",
>             "name": "114",
>             "semantic_url": "string",
>             "no_model": true
>           },
>           "tags": [
>             "string"
>           ]
>         },
>         "super_gen": {
>           "id": 4986814,
>           "name": "I (X164) Рестайлинг",
>           "ru_name": "1 (X164) Рестайлинг",
>           "year_from": 2009,
>           "year_to": 2012,
>           "price_segment": "PREMIUM",
>           "purpose_group": "BUSINESS",
>           "no_complect": true,
>           "is_restyle": false,
>           "tags": [
>             "string"
>           ]
>         },
>         "configuration": {
>           "id": 4986815,
>           "body_type": "ALLROAD_5_DOORS",
>           "doors_count": 5,
>           "auto_class": "S",
>           "human_name": "Хэтчбек 3 дв.",
>           "trunk_volume_min": 0,
>           "trunk_volume_max": 0,
>           "notice": "Gran Turismo",
>           "body_type_group": "SEDAN",
>           "length": 5000,
>           "width": 2000,
>           "height": 1500,
>           "seats": [
>             5,
>             7
>           ],
>           "main_photo": {
>             "name": "string",
>             "sizes": "{'orig': '//avatars.mds.yandex.net/get-autoru/1121/image_name/orig'}",
>             "transform": {
>               "angle": 0,
>               "blur": true
>             },
>             "preview": {
>               "version": 0,
>               "width": 0,
>               "height": 0,
>               "data": "string"
>             },
>             "namespace": "string",
>             "is_deleted": true,
>             "is_internal": true,
>             "photo_type": "STS_FRONT",
>             "photo_class": "PHOTO_CLASS_UNDEFINED",
>             "create_date": 0,
>             "delete_date": 0,
>             "orig_width": 0,
>             "orig_height": 0,
>             "is_hd": true,
>             "is_hidden_from_report": true,
>             "is_deleted_by_moderator": true
>           },
>           "tags": [
>             "string"
>           ],
>           "landing_photo_main": {
>             "name": "string",
>             "sizes": "{'orig': '//avatars.mds.yandex.net/get-autoru/1121/image_name/orig'}",
>             "transform": {
>               "angle": 0,
>               "blur": true
>             },
>             "preview": {
>               "version": 0,
>               "width": 0,
>               "height": 0,
>               "data": "string"
>             },
>             "namespace": "string",
>             "is_deleted": true,
>             "is_internal": true,
>             "photo_type": "STS_FRONT",
>             "photo_class": "PHOTO_CLASS_UNDEFINED",
>             "create_date": 0,
>             "delete_date": 0,
>             "orig_width": 0,
>             "orig_height": 0,
>             "is_hd": true,
>             "is_hidden_from_report": true,
>             "is_deleted_by_moderator": true
>           },
>           "landing_photo_promo": {
>             "name": "string",
>             "sizes": "{'orig': '//avatars.mds.yandex.net/get-autoru/1121/image_name/orig'}",
>             "transform": {
>               "angle": 0,
>               "blur": true
>             },
>             "preview": {
>               "version": 0,
>               "width": 0,
>               "height": 0,
>               "data": "string"
>             },
>             "namespace": "string",
>             "is_deleted": true,
>             "is_internal": true,
>             "photo_type": "STS_FRONT",
>             "photo_class": "PHOTO_CLASS_UNDEFINED",
>             "create_date": 0,
>             "delete_date": 0,
>             "orig_width": 0,
>             "orig_height": 0,
>             "is_hd": true,
>             "is_hidden_from_report": true,
>             "is_deleted_by_moderator": true
>           },
>           "landing_description": "string",
>           "is_paid_promo_model": true
>         },
>         "tech_param": {
>           "id": 20494193,
>           "name": "350",
>           "nameplate": "350",
>           "displacement": 2987,
>           "engine_type": "DIESEL",
>           "gear_type": "ALL_WHEEL_DRIVE",
>           "gear_type_autoru": "ALL_FULL",
>           "transmission": "AUTOMATIC",
>           "transmission_autoru": "ROBOT_2CLUTCH",
>           "power": 224,
>           "power_kvt": 165,
>           "human_name": "3.2 AT (220 л.с.) 4WD",
>           "acceleration": 0,
>           "clearance_min": 0,
>           "fuel_rate": 0,
>           "clearance_max": 0,
>           "petrol_type": "95 RON",
>           "tags": [
>             "string"
>           ],
>           "electric_range": 260,
>           "charge_time": 15,
>           "battery_capacity": 42.2
>         },
>         "complectation": {
>           "id": 2049058,
>           "name": "Platinum",
>           "available_options": [
>             "string"
>           ],
>           "additional_options": {
>             "additionalProp1": {
>               "price": 820000,
>               "dprice": 0,
>               "currency": "RUR",
>               "create_timestamp": 120000,
>               "rur_price": 600000,
>               "rur_dprice": 0,
>               "usd_price": 10000,
>               "usd_dprice": 0,
>               "eur_price": 8700,
>               "eur_dprice": 0,
>               "cny_price": 70000,
>               "cny_dprice": 0,
>               "with_nds": true,
>               "edited_by_moderator": true
>             },
>             "additionalProp2": {
>               "price": 820000,
>               "dprice": 0,
>               "currency": "RUR",
>               "create_timestamp": 120000,
>               "rur_price": 600000,
>               "rur_dprice": 0,
>               "usd_price": 10000,
>               "usd_dprice": 0,
>               "eur_price": 8700,
>               "eur_dprice": 0,
>               "cny_price": 70000,
>               "cny_dprice": 0,
>               "with_nds": true,
>               "edited_by_moderator": true
>             },
>             "additionalProp3": {
>               "price": 820000,
>               "dprice": 0,
>               "currency": "RUR",
>               "create_timestamp": 120000,
>               "rur_price": 600000,
>               "rur_dprice": 0,
>               "usd_price": 10000,
>               "usd_dprice": 0,
>               "eur_price": 8700,
>               "eur_dprice": 0,
>               "cny_price": 70000,
>               "cny_dprice": 0,
>               "with_nds": true,
>               "edited_by_moderator": true
>             }
>           },
>           "price": {
>             "additionalProp1": {
>               "price": 820000,
>               "dprice": 0,
>               "currency": "RUR",
>               "create_timestamp": 120000,
>               "rur_price": 600000,
>               "rur_dprice": 0,
>               "usd_price": 10000,
>               "usd_dprice": 0,
>               "eur_price": 8700,
>               "eur_dprice": 0,
>               "cny_price": 70000,
>               "cny_dprice": 0,
>               "with_nds": true,
>               "edited_by_moderator": true
>             },
>             "additionalProp2": {
>               "price": 820000,
>               "dprice": 0,
>               "currency": "RUR",
>               "create_timestamp": 120000,
>               "rur_price": 600000,
>               "rur_dprice": 0,
>               "usd_price": 10000,
>               "usd_dprice": 0,
>               "eur_price": 8700,
>               "eur_dprice": 0,
>               "cny_price": 70000,
>               "cny_dprice": 0,
>               "with_nds": true,
>               "edited_by_moderator": true
>             },
>             "additionalProp3": {
>               "price": 820000,
>               "dprice": 0,
>               "currency": "RUR",
>               "create_timestamp": 120000,
>               "rur_price": 600000,
>               "rur_dprice": 0,
>               "usd_price": 10000,
>               "usd_dprice": 0,
>               "eur_price": 8700,
>               "eur_dprice": 0,
>               "cny_price": 70000,
>               "cny_dprice": 0,
>               "with_nds": true,
>               "edited_by_moderator": true
>             }
>           },
>           "aliases": "3g23jz",
>           "vendor_colors": [
>             {
>               "body_color_id": 21411464,
>               "mark_color_id": 21391600,
>               "name_ru": "Bright Silver Metallic",
>               "hex_codes": "[CDCDD1, FFFFFF] список - например для двухцветных кузовов",
>               "color_type": "VENDOR_COLOR_TYPE_UNKNOWN",
>               "stock_color": {
>                 "hex_code": "string",
>                 "name_ru": "string"
>               },
>               "photos": [
>                 {
>                   "name": "string",
>                   "sizes": "{'orig': '//avatars.mds.yandex.net/get-autoru/1121/image_name/orig'}",
>                   "transform": {
>                     "angle": 0,
>                     "blur": true
>                   },
>                   "preview": {
>                     "version": 0,
>                     "width": 0,
>                     "height": 0,
>                     "data": "string"
>                   },
>                   "namespace": "string",
>                   "is_deleted": true,
>                   "is_internal": true,
>                   "photo_type": "STS_FRONT",
>                   "photo_class": "PHOTO_CLASS_UNDEFINED",
>                   "create_date": 0,
>                   "delete_date": 0,
>                   "orig_width": 0,
>                   "orig_height": 0,
>                   "is_hd": true,
>                   "is_hidden_from_report": true,
>                   "is_deleted_by_moderator": true
>                 }
>               ],
>               "main_color": true
>             }
>           ],
>           "tags": [
>             "string"
>           ]
>         },
>         "vendor": "VENDOR_UNKNOWN"
>       },
>       "truck_info": {
>         "truck_category": "TRUCK",
>         "mark": "string",
>         "model": "string",
>         "displacement": 2987,
>         "horse_power": 224,
>         "loading": 3000,
>         "axis": 3,
>         "seats": 2,
>         "cabin": "SEAT_3_1_SLEEP",
>         "steering_wheel": "LEFT",
>         "engine": "DIESEL",
>         "transmission": "AUTOMATIC",
>         "gear": "FRONT",
>         "wheel_drive": "WD_10x10",
>         "saddle_height": "SH_185",
>         "brakes": "DRUM",
>         "euro_class": "EURO_0",
>         "cabin_suspension": "MECHANICAL",
>         "suspension": "SPRING",
>         "chassis_suspension": "SPRING_SPRING",
>         "bus_type": "CREW",
>         "trailer_type": "ADVERTIZING",
>         "swap_body_type": "BULK_CARGO",
>         "truck_type": "AUTOTRANSPORTER",
>         "light_truck_type": "ALL_METAL_VAN",
>         "agricultural_type": "COMBAIN_HARVESTER",
>         "construction_type": "DRILLING_PILING_MACHINE",
>         "autoloader_type": "FORKLIFTS_ELECTRO",
>         "dredge_type": "PLANNER_EXCAVATOR",
>         "bulldozer_type": "WHEELS_BULLDOZER",
>         "municipal_type": "GARBAGE_TRUCK",
>         "body_type": "ONBOARD_TRUCK",
>         "equipment": {
>           "additionalProp1": true,
>           "additionalProp2": true,
>           "additionalProp3": true
>         },
>         "operating_hours": 0,
>         "load_height": 0,
>         "crane_radius": 0,
>         "bucket_volume": 0,
>         "traction_class": "TRACTION_3",
>         "mark_info": {
>           "code": "MERCEDES",
>           "name": "Mercedes-Benz",
>           "ru_name": "Мерседес-Бенц",
>           "logo": {
>             "name": "string",
>             "sizes": "{'orig': '//avatars.mds.yandex.net/get-autoru/1121/image_name/orig'}",
>             "transform": {
>               "angle": 0,
>               "blur": true
>             },
>             "preview": {
>               "version": 0,
>               "width": 0,
>               "height": 0,
>               "data": "string"
>             },
>             "namespace": "string",
>             "is_deleted": true,
>             "is_internal": true,
>             "photo_type": "STS_FRONT",
>             "photo_class": "PHOTO_CLASS_UNDEFINED",
>             "create_date": 0,
>             "delete_date": 0,
>             "orig_width": 0,
>             "orig_height": 0,
>             "is_hd": true,
>             "is_hidden_from_report": true,
>             "is_deleted_by_moderator": true
>           },
>           "country_id": "[96] - Германия",
>           "tags": [
>             "string"
>           ],
>           "numeric_id": 3136
>         },
>         "model_info": {
>           "code": "GL_KLASSE",
>           "name": "GL-klasse",
>           "ru_name": "GL-класс",
>           "morphology": {
>             "gender": "MASCULINE"
>           },
>           "nameplate": {
>             "code": "9265330",
>             "name": "114",
>             "semantic_url": "string",
>             "no_model": true
>           },
>           "tags": [
>             "string"
>           ]
>         }
>       },
>       "moto_info": {
>         "moto_category": "MOTORCYCLE",
>         "mark": "string",
>         "model": "string",
>         "displacement": 2987,
>         "horse_power": 224,
>         "engine": "DIESEL",
>         "transmission": "TRANSMISSION_1",
>         "gear": "CHAIN",
>         "moto_type": "ALLROUND",
>         "atv_type": "AMPHIBIAN",
>         "snowmobile_type": "CHILDISH",
>         "cylinder_order": "LINE",
>         "cylinder_amount": "CYLINDERS_1",
>         "stroke_amount": "STROKES_2",
>         "equipment": {
>           "additionalProp1": true,
>           "additionalProp2": true,
>           "additionalProp3": true
>         },
>         "mark_info": {
>           "code": "MERCEDES",
>           "name": "Mercedes-Benz",
>           "ru_name": "Мерседес-Бенц",
>           "logo": {
>             "name": "string",
>             "sizes": "{'orig': '//avatars.mds.yandex.net/get-autoru/1121/image_name/orig'}",
>             "transform": {
>               "angle": 0,
>               "blur": true
>             },
>             "preview": {
>               "version": 0,
>               "width": 0,
>               "height": 0,
>               "data": "string"
>             },
>             "namespace": "string",
>             "is_deleted": true,
>             "is_internal": true,
>             "photo_type": "STS_FRONT",
>             "photo_class": "PHOTO_CLASS_UNDEFINED",
>             "create_date": 0,
>             "delete_date": 0,
>             "orig_width": 0,
>             "orig_height": 0,
>             "is_hd": true,
>             "is_hidden_from_report": true,
>             "is_deleted_by_moderator": true
>           },
>           "country_id": "[96] - Германия",
>           "tags": [
>             "string"
>           ],
>           "numeric_id": 3136
>         },
>         "model_info": {
>           "code": "GL_KLASSE",
>           "name": "GL-klasse",
>           "ru_name": "GL-класс",
>           "morphology": {
>             "gender": "MASCULINE"
>           },
>           "nameplate": {
>             "code": "9265330",
>             "name": "114",
>             "semantic_url": "string",
>             "no_model": true
>           },
>           "tags": [
>             "string"
>           ]
>         }
>       },
>          }
>   ],
>   "price_range": {
>     "min": {
>       "price": 820000,
>       "dprice": 0,
>       "currency": "RUR",
>       "create_timestamp": 120000,
>       "rur_price": 600000,
>       "rur_dprice": 0,
>       "usd_price": 10000,
>       "usd_dprice": 0,
>       "eur_price": 8700,
>       "eur_dprice": 0,
>       "cny_price": 70000,
>       "cny_dprice": 0,
>       "with_nds": true,
>       "edited_by_moderator": true
>     },
>     "max": {
>       "price": 820000,
>       "dprice": 0,
>       "currency": "RUR",
>       "create_timestamp": 120000,
>       "rur_price": 600000,
>       "rur_dprice": 0,
>       "usd_price": 10000,
>       "usd_dprice": 0,
>       "eur_price": 8700,
>       "eur_dprice": 0,
>       "cny_price": 70000,
>       "cny_dprice": 0,
>       "with_nds": true,
>       "edited_by_moderator": true
>     }
>   },
>   "production_years": {
>     "min_year": 0,
>     "max_year": 0
>   },
>   "pagination": {
>     "page": 1,
>     "page_size": 10,
>     "total_offers_count": 1,
>     "total_page_count": 1
>   },
>   "filters": {
>     "truck_category": "TRUCK",
>     "moto_category": "MOTORCYCLE",
>     "status": "ACTIVE",
>     "service": "all_sale_color",
>     "tag": "tag1",
>     "vin": "VF7XS9HHCEZ005623",
>     "mark_model": "NISSAN#MURANO",
>     "price_from": 500000,
>     "price_to": 600000,
>     "geobase_id": 213,
>     "section": "1",
>     "create_date_from": "2017-07-08T11:29:16+03:00",
>     "create_date_to": "2017-07-08T11:29:16+03:00",
>     "exclude_tag": "tag1",
>     "no_active_services": true,
>     "ban_reason": "WRONG_VIN",
>     "offer_i_ref": 1072803012,
>     "delivery_region_id": 213,
>     "autoru_expert": true,
>     "multiposting_status": "ACTIVE",
>     "multiposting_service": "all_sale_color",
>     "license_plate": "A777MP777",
>     "is_last_day_before_expiration": true,
>     "can_send_favorite_message": true,
>     "favorite_message_was_sent": true,
>     "year_from": 2019,
>     "year_to": 2021,
>     "year": 2021,
>     "availability": "IN_STOCK",
>     "has_exterior_panorama": true,
>     "has_interior_panorama": true,
>     "has_photo": true,
>     "super_gen": [
>       0
>     ],
>     "can_book": true,
>     "exterior_panorama": [
>       "string"
>     ],
>     "interior_panorama": [
>       "string"
>     ],
>     "classified_status": "AVITO_CS_ACTIVE",
>     "color_hex": [
>       "string"
>     ],
>     "auction": true,
>     "offer_id": "1072803012-abc",
>     "recommendation_tags": [
>       "string"
>     ]
>   },
>   "sorting": {
>     "name": "string",
>     "desc": true
>   },
>   "response_flags": {
>     "dealer_special": true,
>     "show_match_application_form": true,
>     "show_report_promo_banner": true
>   },
>   "search_parameters": {
>     "cars_params": {
>       "transmission": [
>         "AUTO"
>       ],
>       "engine_group": [
>         "ANY_ENGINE"
>       ],
>       "gear_type": [
>         "ALL_WHEEL_DRIVE"
>       ],
>       "feeding_type": [
>         "NONE"
>       ],
>       "steering_wheel": "LEFT",
>       "body_type_group": [
>         "ANY_BODY"
>       ],
>       "armored_status": "string",
>       "seats_group": "ANY_SEATS",
>       "complectation_id": [
>         "string"
>       ],
>       "configuration_id": [
>         "string"
>       ],
>       "tech_param_id": [
>         "string"
>       ],
>       "complectation_name": [
>         "string"
>       ]
>     },
>     "moto_params": {
>       "transmission": [
>         "TRANSMISSION_1"
>       ],
>       "engine_type": [
>         "DIESEL"
>       ],
>       "cylinders": [
>         "CYLINDERS_1"
>       ],
>       "cylinders_type": [
>         "LINE"
>       ],
>       "gear_type": [
>         "CHAIN"
>       ],
>       "moto_category": "MOTORCYCLE",
>       "moto_type": [
>         "ALLROUND"
>       ],
>       "atv_type": [
>         "AMPHIBIAN"
>       ],
>       "snowmobile_type": [
>         "CHILDISH"
>       ],
>       "strokes": [
>         "STROKES_2"
>       ]
>     },
>     "trucks_params": {
>       "transmission": [
>         "AUTOMATIC"
>       ],
>       "engine_type": [
>         "DIESEL"
>       ],
>       "gear_type": [
>         "BACK"
>       ],
>       "steering_wheel": "LEFT",
>       "trucks_category": "LCV",
>       "trailer_type": [
>         "ADVERTIZING"
>       ],
>       "light_truck_type": [
>         "ALL_METAL_VAN"
>       ],
>       "truck_type": [
>         "AUTOTRANSPORTER"
>       ],
>       "agricultural_type": [
>         "COMBAIN_HARVESTER"
>       ],
>       "construction_type": [
>         "DRILLING_PILING_MACHINE"
>       ],
>       "autoloader_type": [
>         "FORKLIFTS_ELECTRO"
>       ],
>       "dredge_type": [
>         "PLANNER_EXCAVATOR"
>       ],
>       "bulldozer_type": [
>         "WHEELS_BULLDOZER"
>       ],
>       "municipal_type": [
>         "GARBAGE_TRUCK"
>       ],
>       "euro_class": [
>         "EURO_0"
>       ],
>       "seats_from": 1,
>       "seats_to": 30,
>       "cabin_key": "2_SEAT_WO_SLEEP",
>       "bus_type": [
>         "CREW"
>       ],
>       "brake_type": [
>         "DRUM"
>       ],
>       "axis_from": 1,
>       "axis_to": 3,
>       "suspension_type": [
>         "SPRING"
>       ],
>       "suspension_chassis": [
>         "SPRING_SPRING"
>       ],
>       "suspension_cabin": [
>         "MECHANICAL"
>       ],
>       "haggle": "POSSIBLE",
>       "loading_to": 1,
>       "loading_from": 30000,
>       "saddle_height": [
>         "SH_128"
>       ],
>       "wheel_drive": [
>         "WD_10x10"
>       ],
>       "traction_class": [
>         "TRACTION_3"
>       ],
>       "operating_hours_from": 0,
>       "operating_hours_to": 0,
>       "load_height_from": 0,
>       "load_height_to": 0,
>       "crane_radius_from": 0,
>       "crane_radius_to": 0,
>       "bucket_volume_from": 0,
>       "bucket_volume_to": 0
>     },
>     "with_warranty": true,
>     "currency": "RUR",
>     "has_image": true,
>     "in_stock": "ANY_STOCK",
>     "state_group": "NEW",
>     "damage_group": "NOT_BEATEN",
>     "color": "FAFBFB",
>     "customs_state_group": "DOESNT_MATTER",
>     "exchange_group": "NO_EXCHANGE",
>     "top_days": "off",
>     "creation_date_to": 0,
>     "creation_date_from": 0,
>     "rid": 213,
>     "geo_radius": 0,
>     "catalog_equipment": [
>       "string"
>     ],
>     "year_from": 0,
>     "year_to": 0,
>     "price_from": 0,
>     "price_to": 0,
>     "km_age_from": 0,
>     "km_age_to": 0,
>     "power_from": 0,
>     "power_to": 0,
>     "acceleration_to": 0,
>     "acceleration_from": 0,
>     "displacement_from": 0,
>     "displacement_to": 0,
>     "only_official": true,
>     "seller_group": [
>       "ANY_SELLER"
>     ],
>     "dealer_net_id": "string",
>     "dealer_id": "string",
>     "dealer_showcase": true,
>     "pinned_offer_id": "string",
>     "last_price_change_date_from": 0,
>     "last_price_change_date_to": 0,
>     "fresh_date_to": 0,
>     "fresh_date_from": 0,
>     "is_clear": "true",
>     "owners_count_group": "ANY_COUNT",
>     "owning_time_group": "ANY_TIME",
>     "pts_status": 0,
>     "search_tag": [
>       "string"
>     ],
>     "offer_grouping": true,
>     "autoru_billing_service_type": [
>       "string"
>     ],
>     "offer_id": [
>       "string"
>     ],
>     "with_revoked": "NONE",
>     "exp_flags": [
>       "string"
>     ],
>     "trunk_volume_from": 0,
>     "trunk_volume_to": 0,
>     "clearance_from": 0,
>     "clearance_to": 0,
>     "fuel_rate_from": 0,
>     "fuel_rate_to": 0,
>     "exclude_offer_id": [
>       "string"
>     ],
>     "with_discount": true,
>     "exp_bucket": "string",
>     "shuffle_seed": 0,
>     "with_delivery": "NONE",
>     "only_nds": true,
>     "mark_model_nameplate": "AUDI#100#9265090#7879464",
>     "grouping_id": "tech_param_id=123,complectation_id=456",
>     "catalog_filter": [
>       {
>         "mark": "BMW",
>         "model": "X1",
>         "nameplate": 9264641,
>         "generation": 8246645,
>         "configuration": 8246927,
>         "tech_param": 8247264,
>         "complectation": 5018169,
>         "complectation_name": "xDrive20d",
>         "vendor": "VENDOR1",
>         "nameplate_name": "23d"
>       }
>     ],
>     "exclude_catalog_filter": [
>       {
>         "mark": "BMW",
>         "model": "X1",
>         "nameplate": 9264641,
>         "generation": 8246645,
>         "configuration": 8246927,
>         "tech_param": 8247264,
>         "complectation": 5018169,
>         "complectation_name": "xDrive20d",
>         "vendor": "VENDOR1",
>         "nameplate_name": "23d"
>       }
>     ],
>     "with_booking_allowed": "NONE",
>     "is_from_qr": true,
>     "filter_groups": "filter_groups=mmg",
>     "exclude_rid": 213,
>     "exclude_geo_radius": 0,
>     "total_count": true,
>     "recommended": true,
>     "only_important": true,
>     "credit_group": {
>       "payment_from": 0,
>       "payment_to": 0,
>       "loan_term": 0,
>       "initial_fee": 0
>     },
>     "auction_related": true,
>     "infinite_listing": true,
>     "user_id": "string",
>     "sorting_log": true,
>     "last_call_timestamp_from": 0,
>     "last_call_timestamp_to": 0,
>     "vin_codes": [
>       "string"
>     ],
>     "vin_report_statuses": [
>       "CHECKED"
>     ],
>     "client_id": "string",
>     "multiposting_hidden": true
>   },
>   "saved_search": {
>     "id": "string",
>     "title": "string",
>     "category": "CARS",
>     "params": {
>       "cars_params": {
>         "transmission": [
>           "AUTO"
>         ],
>         "engine_group": [
>           "ANY_ENGINE"
>         ],
>         "gear_type": [
>           "ALL_WHEEL_DRIVE"
>         ],
>         "feeding_type": [
>           "NONE"
>         ],
>         "steering_wheel": "LEFT",
>         "body_type_group": [
>           "ANY_BODY"
>         ],
>         "armored_status": "string",
>         "seats_group": "ANY_SEATS",
>         "complectation_id": [
>           "string"
>         ],
>         "configuration_id": [
>           "string"
>         ],
>         "tech_param_id": [
>           "string"
>         ],
>         "complectation_name": [
>           "string"
>         ]
>       },
>       "moto_params": {
>         "transmission": [
>           "TRANSMISSION_1"
>         ],
>         "engine_type": [
>           "DIESEL"
>         ],
>         "cylinders": [
>           "CYLINDERS_1"
>         ],
>         "cylinders_type": [
>           "LINE"
>         ],
>         "gear_type": [
>           "CHAIN"
>         ],
>         "moto_category": "MOTORCYCLE",
>         "moto_type": [
>           "ALLROUND"
>         ],
>         "atv_type": [
>           "AMPHIBIAN"
>         ],
>         "snowmobile_type": [
>           "CHILDISH"
>         ],
>         "strokes": [
>           "STROKES_2"
>         ]
>       },
>       "trucks_params": {
>         "transmission": [
>           "AUTOMATIC"
>         ],
>         "engine_type": [
>           "DIESEL"
>         ],
>         "gear_type": [
>           "BACK"
>         ],
>         "steering_wheel": "LEFT",
>         "trucks_category": "LCV",
>         "trailer_type": [
>           "ADVERTIZING"
>         ],
>         "light_truck_type": [
>           "ALL_METAL_VAN"
>         ],
>         "truck_type": [
>           "AUTOTRANSPORTER"
>         ],
>         "agricultural_type": [
>           "COMBAIN_HARVESTER"
>         ],
>         "construction_type": [
>           "DRILLING_PILING_MACHINE"
>         ],
>         "autoloader_type": [
>           "FORKLIFTS_ELECTRO"
>         ],
>         "dredge_type": [
>           "PLANNER_EXCAVATOR"
>         ],
>         "bulldozer_type": [
>           "WHEELS_BULLDOZER"
>         ],
>         "municipal_type": [
>           "GARBAGE_TRUCK"
>         ],
>         "euro_class": [
>           "EURO_0"
>         ],
>         "seats_from": 1,
>         "seats_to": 30,
>         "cabin_key": "2_SEAT_WO_SLEEP",
>         "bus_type": [
>           "CREW"
>         ],
>         "brake_type": [
>           "DRUM"
>         ],
>         "axis_from": 1,
>         "axis_to": 3,
>         "suspension_type": [
>           "SPRING"
>         ],
>         "suspension_chassis": [
>           "SPRING_SPRING"
>         ],
>         "suspension_cabin": [
>           "MECHANICAL"
>         ],
>         "haggle": "POSSIBLE",
>         "loading_to": 1,
>         "loading_from": 30000,
>         "saddle_height": [
>           "SH_128"
>         ],
>         "wheel_drive": [
>           "WD_10x10"
>         ],
>         "traction_class": [
>           "TRACTION_3"
>         ],
>         "operating_hours_from": 0,
>         "operating_hours_to": 0,
>         "load_height_from": 0,
>         "load_height_to": 0,
>         "crane_radius_from": 0,
>         "crane_radius_to": 0,
>         "bucket_volume_from": 0,
>         "bucket_volume_to": 0
>       },
>       "with_warranty": true,
>       "currency": "RUR",
>       "has_image": true,
>       "in_stock": "ANY_STOCK",
>       "state_group": "NEW",
>       "damage_group": "NOT_BEATEN",
>       "color": "FAFBFB",
>       "customs_state_group": "DOESNT_MATTER",
>       "exchange_group": "NO_EXCHANGE",
>       "top_days": "off",
>       "creation_date_to": 0,
>       "creation_date_from": 0,
>       "rid": 213,
>       "geo_radius": 0,
>       "catalog_equipment": [
>         "string"
>       ],
>       "year_from": 0,
>       "year_to": 0,
>       "price_from": 0,
>       "price_to": 0,
>       "km_age_from": 0,
>       "km_age_to": 0,
>       "power_from": 0,
>       "power_to": 0,
>       "acceleration_to": 0,
>       "acceleration_from": 0,
>       "displacement_from": 0,
>       "displacement_to": 0,
>       "only_official": true,
>       "seller_group": [
>         "ANY_SELLER"
>       ],
>       "dealer_net_id": "string",
>       "dealer_id": "string",
>       "dealer_showcase": true,
>       "pinned_offer_id": "string",
>       "last_price_change_date_from": 0,
>       "last_price_change_date_to": 0,
>       "fresh_date_to": 0,
>       "fresh_date_from": 0,
>       "is_clear": "true",
>       "owners_count_group": "ANY_COUNT",
>       "owning_time_group": "ANY_TIME",
>       "pts_status": 0,
>       "search_tag": [
>         "string"
>       ],
>       "offer_grouping": true,
>       "autoru_billing_service_type": [
>         "string"
>       ],
>       "offer_id": [
>         "string"
>       ],
>       "with_revoked": "NONE",
>       "exp_flags": [
>         "string"
>       ],
>       "trunk_volume_from": 0,
>       "trunk_volume_to": 0,
>       "clearance_from": 0,
>       "clearance_to": 0,
>       "fuel_rate_from": 0,
>       "fuel_rate_to": 0,
>       "exclude_offer_id": [
>         "string"
>       ],
>       "with_discount": true,
>       "exp_bucket": "string",
>       "shuffle_seed": 0,
>       "with_delivery": "NONE",
>       "only_nds": true,
>       "mark_model_nameplate": "AUDI#100#9265090#7879464",
>       "grouping_id": "tech_param_id=123,complectation_id=456",
>       "catalog_filter": [
>         {
>           "mark": "BMW",
>           "model": "X1",
>           "nameplate": 9264641,
>           "generation": 8246645,
>           "configuration": 8246927,
>           "tech_param": 8247264,
>           "complectation": 5018169,
>           "complectation_name": "xDrive20d",
>           "vendor": "VENDOR1",
>           "nameplate_name": "23d"
>         }
>       ],
>       "exclude_catalog_filter": [
>         {
>           "mark": "BMW",
>           "model": "X1",
>           "nameplate": 9264641,
>           "generation": 8246645,
>           "configuration": 8246927,
>           "tech_param": 8247264,
>           "complectation": 5018169,
>           "complectation_name": "xDrive20d",
>           "vendor": "VENDOR1",
>           "nameplate_name": "23d"
>         }
>       ],
>       "with_booking_allowed": "NONE",
>       "is_from_qr": true,
>       "filter_groups": "filter_groups=mmg",
>       "exclude_rid": 213,
>       "exclude_geo_radius": 0,
>       "total_count": true,
>       "recommended": true,
>       "only_important": true,
>       "credit_group": {
>         "payment_from": 0,
>         "payment_to": 0,
>         "loan_term": 0,
>         "initial_fee": 0
>       },
>       "auction_related": true,
>       "infinite_listing": true,
>       "user_id": "string",
>       "sorting_log": true,
>       "last_call_timestamp_from": 0,
>       "last_call_timestamp_to": 0,
>       "vin_codes": [
>         "string"
>       ],
>       "vin_report_statuses": [
>         "CHECKED"
>       ],
>       "client_id": "string",
>       "multiposting_hidden": true
>     },
>     "sorting": {
>       "name": "string",
>       "desc": true
>     },
>     "deliveries": {
>       "push_delivery": {
>         "enabled": true
>       },
>       "email_delivery": {
>         "enabled": true,
>         "period": "3600s"
>       }
>     },
>     "view": {
>       "mark_model_nameplate_gen_views": [
>         {
>           "mark": {
>             "code": "MERCEDES",
>             "name": "Mercedes-Benz",
>             "ru_name": "Мерседес-Бенц",
>             "logo": {
>               "name": "string",
>               "sizes": "{'orig': '//avatars.mds.yandex.net/get-autoru/1121/image_name/orig'}",
>               "transform": {
>                 "angle": 0,
>                 "blur": true
>               },
>               "preview": {
>                 "version": 0,
>                 "width": 0,
>                 "height": 0,
>                 "data": "string"
>               },
>               "namespace": "string",
>               "is_deleted": true,
>               "is_internal": true,
>               "photo_type": "STS_FRONT",
>               "photo_class": "PHOTO_CLASS_UNDEFINED",
>               "create_date": 0,
>               "delete_date": 0,
>               "orig_width": 0,
>               "orig_height": 0,
>               "is_hd": true,
>               "is_hidden_from_report": true,
>               "is_deleted_by_moderator": true
>             },
>             "country_id": "[96] - Германия",
>             "tags": [
>               "string"
>             ],
>             "numeric_id": 3136
>           },
>           "model": {
>             "code": "GL_KLASSE",
>             "name": "GL-klasse",
>             "ru_name": "GL-класс",
>             "morphology": {
>               "gender": "MASCULINE"
>             },
>             "nameplate": {
>               "code": "9265330",
>               "name": "114",
>               "semantic_url": "string",
>               "no_model": true
>             },
>             "tags": [
>               "string"
>             ]
>           },
>           "nameplate": {
>             "code": "9265330",
>             "name": "114",
>             "semantic_url": "string",
>             "no_model": true
>           },
>           "super_gen": {
>             "id": 4986814,
>             "name": "I (X164) Рестайлинг",
>             "ru_name": "1 (X164) Рестайлинг",
>             "year_from": 2009,
>             "year_to": 2012,
>             "price_segment": "PREMIUM",
>             "purpose_group": "BUSINESS",
>             "no_complect": true,
>             "is_restyle": false,
>             "tags": [
>               "string"
>             ]
>           }
>         }
>       ],
>       "vendor_views": [
>         {
>           "code": "VENDOR2",
>           "name": "Иномарки"
>         }
>       ],
>       "regions": [
>         {
>           "id": 213,
>           "name": "Москва",
>           "genitive": "Москвы",
>           "dative": "Москве",
>           "accusative": "Москву",
>           "instrumental": "Москвой",
>           "prepositional": "Москве",
>           "preposition": "в",
>           "latitude": 0,
>           "longitude": 0,
>           "sub_title": "Украина, Львовская область",
>           "supports_geo_radius": true,
>           "default_radius": 300,
>           "children": [
>             "string"
>           ],
>           "parent_ids": [
>             213,
>             1,
>             3,
>             225,
>             10001,
>             10000
>           ]
>         }
>       ],
>       "applied_filter_count": 0,
>       "tech_param": {
>         "id": 0,
>         "name": "string"
>       },
>       "complectation": {
>         "id": 0,
>         "name": "string"
>       },
>       "applied_filter_fields": [
>         "string"
>       ],
>       "salon": {
>         "code": "string",
>         "is_official": true,
>         "loyalty_program": true
>       }
>     },
>     "unsupported_fields": [
>       {
>         "code": "string",
>         "name": "string",
>         "feature": "PHONE_REDIRECTS_IN_COMMERCIAL_FORM"
>       }
>     ],
>     "creation_timestamp": "date",
>     "searcher_query": "string"
>   },
>   "grouping": {
>     "single_offers_count": 1,
>     "groups_count": 1
>   },
>   "search_id": "string",
>   "title_code": "NEW_IN_STOCK_OFFICIAL_DEALERS",
>   "status": "SUCCESS",
> }
> ```


{% include [table-style](../_includes/table-style-border-none-2a2aa0c324bf.md) %}

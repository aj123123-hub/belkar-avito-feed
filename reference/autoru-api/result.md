---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/carfax-orders/result.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# GET /carfax/orders/result

Возвращает результат созданного заказа.

## Формат запроса {#input}

```
GET https://apiauto.ru/1.0/carfax/orders/result
? [[order_id](*order_id)=<integer>]
```

<div class="params-table">

#|
||
##order_id##
|
{% include notitle [order_id](../../_includes/popups-00286d1be377.md#order_id_carfax) %}
||
|#

</div>

Общая структура ответа приведена ниже. Порядок следования элементов не гарантируется. В структуре могут присутствовать служебные параметры, которые не описаны в таблице.

## Формат ответа {#output-structure}

```json
{
  "order": {
    "id": {string},
    "created": {string},
    "status": {string},
    "error": {string},
    "identifier_type": {string},
    "identifier": {string},
    "report_type": {string},
    "report_id": {string},
    "vin": {string},
    "user_id": {string},
    "sharing_url": {string}
  },
  "full_report": {
    "header": {
      "title": {string},
      "is_updating": {boolean},
      "timestamp_update": {string}
    },
    "sources": {
      "header": {
        ...
      },
      "sources_count": {integer},
      "ready_count": {integer},
      "text": {string},
      "records_count": {integer}
    },
    "photo_block": {
      "photos": {array}
    },
    "pts_info": {
      "header": {
        ...
      },
      "vin": {string},
      "mark": {
        "key": {string},
        "value": {string},
        "value_text": {string},
        "mismatch_value": {string},
        "status": {string}
      },
      "model": {
        "key": {string},
        "value": {string},
        "value_text": {string},
        "mismatch_value": {string},
        "status": {string}
      },
      "licence_plate": {
        "key": {string},
        "value": {string},
        "value_text": {string},
        "mismatch_value": {string},
        "status": {string}
      },
      "color": {
        "key": {string},
        "value": {string},
        "value_text": {string},
        "mismatch_value": {string},
        "status": {string}
      },
      "year": {
        "key": {string},
        "value": {integer},
        "value_text": {string},
        "mismatch_value": {integer},
        "mismatch_value_text": {string},
        "status": {string},
        "mismatch_status": {string}
      },
      "horse_power": {
        "key": {string},
        "value": {integer},
        "value_text": {string},
        "mismatch_value": {integer},
        "mismatch_value_text": {string},
        "status": {string},
        "mismatch_status": {string}
      },
      "displacement": {
        "key": {string},
        "value": {integer},
        "value_text": {string},
        "mismatch_value": {integer},
        "mismatch_value_text": {string},
        "status": {string},
        "mismatch_status": {string}
      },
      "transmission": {
        "key": {string},
        "value": {string},
        "value_text": {string},
        "mismatch_value": {string},
        "status": {string}
      },
      "mark_logo": {
        "name": {string},
        "sizes": {object},
        "transform": {
          "angle": {integer},
          "blur": {boolean}
        },
        "preview": {
          "version": {integer},
          "width": {integer},
          "height": {integer},
          "data": {string}
        },
        "namespace": {string},
        "is_deleted": {boolean},
        "photo_type": {string},
        "photo_class": {string},
        "create_date": {integer},
        "delete_date": {integer},
        "orig_width": {integer},
        "orig_height": {integer},
        "is_hd": {boolean},
        "base_url": {string},
        "aliases": {array},
        "thumb_hash": {string}
      },
      "pts_number": {string},
      "sts_number": {string},
      "sts_data_receive": {integer},
      "has_duplicate_pts": {boolean},
      "pts_data_receive": {integer},
      "was_modificated": {boolean},
      "was_utilization": {boolean},
      "date_of_utilizations": {integer},
      "pts_type": {string},
      "meta": {
        "id": {string},
        "source": {string}
      },
      "status": {string},
      "block_status": {string},
      "commentable": {
        "block_id": {string},
        "add_comment": {boolean}
      },
      "comments_info": {
        "commentable": {
          "block_id": {string},
          "add_comment": {boolean}
        },
        "comments": {array}
      },
      "comments_count": {integer},
      "registered_in_gibdd": {boolean},
      "available_for_free": {boolean},
      "engine_model": {string},
      "engine_number": {string},
      "engine_type": {string},
      "gear_type": {string},
      "steering_wheel": {string},
      "category": {string},
      "subcategory": {
        "moto": {string},
        "truck": {string}
      }
    },
    "pts_owners": {
      "header": {
        ...
      },
      "owners": {array},
      "owners_count_status": {string},
      "owners_count_status_text": {string},
      "owners_count_offer": {integer},
      "owners_count_report": {integer},
      "status": {string},
      "block_status": {string},
      "record_count": {integer},
      "mismatch_status": {string},
      "commentable": {
        "block_id": {string},
        "add_comment": {boolean}
      },
      "comments_info": {
        "commentable": {
          "block_id": {string},
          "add_comment": {boolean}
        },
        "comments": {array}
      },
      "comments_count": {integer},
      "available_for_free": {boolean}
    },
    "dtp": {
      "header": {
        ...
      },
      "items": {array},
      "status": {string},
      "block_status": {string},
      "record_count": {integer},
      "comments_count": {integer},
      "available_for_free": {boolean}
    },
    "legal": {
      "header": {
        ...
      },
      "pledge_status": {string},
      "constraints_status": {string},
      "wanted_status": {string},
      "constraint": {array},
      "wanted": {array},
      "pledge": {array},
      "pledge_data_status": {
        "status": {string},
        "description": {string},
        "data_status": {string},
        "comment": {string}
      },
      "constraints_data_status": {
        "status": {string},
        "description": {string},
        "data_status": {string},
        "comment": {string}
      },
      "wanted_data_status": {
        "status": {string},
        "description": {string},
        "data_status": {string},
        "comment": {string}
      },
      "owner_status": {
        "status": {string},
        "description": {string},
        "data_status": {string},
        "comment": {string}
      },
      "inn_status": {
        "status": {string},
        "description": {string},
        "data_status": {string},
        "comment": {string}
      },
      "wanted_criminal_status": {
        "status": {string},
        "description": {string},
        "data_status": {string},
        "comment": {string}
      },
      "wanted_fsin_status": {
        "status": {string},
        "description": {string},
        "data_status": {string},
        "comment": {string}
      },
      "extremist_status": {
        "status": {string},
        "description": {string},
        "data_status": {string},
        "comment": {string}
      },
      "fssp_status": {
        "status": {string},
        "description": {string},
        "data_status": {string},
        "comment": {string}
      },
      "efrsb_status": {
        "status": {string},
        "description": {string},
        "data_status": {string},
        "comment": {string}
      },
      "actual_constraint": {
        "date": {integer},
        "region": {string},
        "reason": {string},
        "description": {string},
        "gibdd_key": {string},
        "meta": {
          "id": {string},
          "source": {string}
        }
      },
      "actual_wanted": {
        "date": {integer},
        "region": {string},
        "meta": {
          "id": {string},
          "source": {string}
        }
      },
      "actual_pledge": {
        "date": {integer},
        "number": {string},
        "pledgors": {array},
        "pledgees": {array},
        "description": {string},
        "is_active": {boolean},
        "meta": {
          "id": {string},
          "source": {string}
        }
      },
      "status": {string},
      "block_status": {string}
    },
    "autoru_offers": {
      "header": {
        ...
      },
      "offers": {array},
      "status": {string},
      "block_status": {string},
      "record_count": {integer},
      "comments_count": {integer}
    },
    "external_classified_offers": {
      "header": {
        ...
      },
      "offers": {array},
      "status": {string},
      "block_status": {string},
      "record_count": {integer}
    },
    "history": {
      "header": {
        ...
      },
      "owners": {array},
      "sources": {array},
      "status": {string},
      "block_status": {string},
      "record_count": {integer}
    },
    "sell_time": {
      "header": {
        ...
      },
      "vas_sell_time": {integer},
      "status": {string},
      "block_status": {string}
    },
    "mileages_graph": {
      "header": {
        ...
      },
      "mileages_graph_data": {
        "id": {string},
        "chart_points": {array},
        "owners": {array}
      },
      "mileage_status": {string},
      "status": {string},
      "block_status": {string},
      "record_count": {integer}
    },
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
      "akinator_complectation_ids": {array},
      "equipment": {object},
      "manufacturer_info": {
        "modification_code": {string},
        "interior_code": {string},
        "color_code": {string},
        "equipment_code": {array}
      },
      "steering_wheel": {string},
      "horse_power": {integer},
      "horse_power_docs": {integer},
      "mark_info": {
        "code": {string},
        "name": {string},
        "ru_name": {string},
        "logo": {
          ...
        },
        "country_id": {array},
        "tags": {array},
        "numeric_id": {integer},
        "transcription": {string}
      },
      "model_info": {
        "code": {string},
        "name": {string},
        "ru_name": {string},
        "morphology": {
          "gender": {string}
        },
        "nameplate": {
          "code": {string},
          "name": {string},
          "semantic_url": {string},
          "no_model": {boolean}
        },
        "tags": {array},
        "transcription": {string},
        "audio_transcription": {string},
        "main_photo": {
          ...
        }
      },
      "super_gen": {
        "id": {integer},
        "name": {string},
        "ru_name": {string},
        "year_from": {integer},
        "year_to": {integer},
        "price_segment": {string},
        "purpose_group": {string},
        "no_complect": {boolean},
        "is_restyle": {boolean},
        "tags": {array},
        "guarantee_info": {
          "description": {
            "badge_compact_condition": {string},
            "badge_full_condition": {string},
            "full_condition": {string}
          },
          "other": {array},
          "source": {
            "name": {string},
            "url": {string}
          }
        }
      },
      "configuration": {
        "id": {integer},
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
        "seats": {array},
        "main_photo": {
          ...
        },
        "tags": {array},
        "landing_photo_main": {
          ...
        },
        "landing_photo_promo": {
          ...
        },
        "landing_description": {string},
        "is_paid_promo_model": {boolean},
        "gallery": {array},
        "width_mirrors": {integer},
        "turning_circle": {number},
        "body_code": {string}
      },
      "tech_param": {
        "id": {integer},
        "name": {string},
        "nameplate": {string},
        "displacement": {integer},
        "engine_type": {string},
        "gear_type": {string},
        "gear_type_autoru": {string},
        "transmission": {string},
        "transmission_autoru": {string},
        "power": {integer},
        "power_kvt": {number},
        "human_name": {string},
        "acceleration": {number},
        "clearance_min": {integer},
        "fuel_rate": {number},
        "clearance_max": {integer},
        "petrol_type": {string},
        "tags": {array},
        "electric_range": {integer},
        "charge_time": {number},
        "battery_capacity": {number},
        "trunk_volume_min": {integer},
        "trunk_volume_max": {integer},
        "fuel_rates": {array},
        "electric_ranges": {array},
        "full_charge_time": {integer},
        "battery_capacities": {array},
        "ev_battery_type": {string},
        "battery_charge_cycles": {integer},
        "battery_temp": {array},
        "quick_charge_time": {integer},
        "quick_charge_description": {string},
        "battery_capacity_useful": {number},
        "charging_port_type": {string},
        "max_power_in": {array},
        "consumption_calc": {string},
        "consump_kwt": {number},
        "valvetrain_drive": {string},
        "engine_list": {string},
        "valvetrain": {string},
        "power_docs": {integer},
        "engine_feeding": {string},
        "total_range": {integer},
        "full_weight": {string},
        "max_speed": {integer},
        "year_start": {integer},
        "year_stop": {integer}
      },
      "complectation": {
        "id": {integer},
        "name": {string},
        "available_options": {array},
        "additional_options": {object},
        "price": {object},
        "aliases": {array},
        "vendor_colors": {array},
        "tags": {array}
      },
      "vendor": {string},
      "duplicate_cluster_id": {string},
      "is_cluster_leader": {boolean},
      "feeding_type": {string},
      "vendors": {array}
    },
    "report_type": {string},
    "status": {string},
    "status_text": {string},
    "taxi": {
      "header": {
        ...
      },
      "taxi_records": {array},
      "status": {string},
      "block_status": {string},
      "record_count": {integer},
      "comments_count": {integer}
    },
    "repair_calculations": {
      "header": {
        ...
      },
      "status": {string},
      "block_status": {string},
      "calculation_records": {array},
      "is_ready": {boolean},
      "record_count": {integer},
      "comments_count": {integer}
    },
    "car_sharing": {
      "header": {
        ...
      },
      "could_be_used_in_car_sharing": {boolean},
      "car_sharing_records": {array},
      "status": {string},
      "block_status": {string},
      "record_count": {integer},
      "comments_count": {integer}
    },
    "total_auction": {
      "header": {
        ...
      },
      "total_auction_records": {array},
      "status": {string},
      "block_status": {string},
      "record_count": {integer},
      "comments_count": {integer}
    },
    "brand_certification": {
      "header": {
        ...
      },
      "brand_certification_records": {array},
      "status": {string},
      "block_status": {string},
      "record_count": {integer}
    },
    "recalls": {
      "header": {
        ...
      },
      "recall_records": {array},
      "status": {string},
      "block_status": {string},
      "record_count": {integer},
      "comments_count": {integer}
    },
    "vehicle": {
      "header": {
        ...
      },
      "car_info": {
        ...
      },
      "color_hex": {string},
      "status": {string},
      "block_status": {string},
      "record_count": {integer}
    },
    "vehicle_photos": {
      "header": {
        ...
      },
      "records": {array},
      "status": {string},
      "block_status": {string},
      "record_count": {integer},
      "comments_count": {integer}
    },
    "constraints": {
      "header": {
        ...
      },
      "status": {string},
      "block_status": {string},
      "records": {array},
      "commentable": {
        "block_id": {string},
        "add_comment": {boolean}
      },
      "comments_info": {
        "commentable": {
          "block_id": {string},
          "add_comment": {boolean}
        },
        "comments": {array}
      },
      "comments_count": {integer}
    },
    "wanted": {
      "header": {
        ...
      },
      "status": {string},
      "block_status": {string},
      "records": {array},
      "commentable": {
        "block_id": {string},
        "add_comment": {boolean}
      },
      "comments_info": {
        "commentable": {
          "block_id": {string},
          "add_comment": {boolean}
        },
        "comments": {array}
      },
      "comments_count": {integer},
      "available_for_free": {boolean}
    },
    "pledge": {
      "header": {
        ...
      },
      "status": {string},
      "nbki_status": {string},
      "fnp_status": {string},
      "block_status": {string},
      "nbki_pledge_status": {string},
      "fnp_pledge_status": {string},
      "records": {array},
      "available_for_free": {boolean}
    },
    "tech_inspection_block": {
      "header": {
        ...
      },
      "records": {array},
      "status": {string},
      "block_status": {string},
      "record_count": {integer},
      "comments_count": {integer}
    },
    "insurances": {
      "header": {
        ...
      },
      "insurances": {array},
      "status": {string},
      "block_status": {string},
      "record_count": {integer},
      "comments_count": {integer},
      "insurances_history": {array}
    },
    "customs": {
      "header": {
        ...
      },
      "customs_records": {array},
      "status": {string},
      "block_status": {string},
      "record_count": {integer},
      "customs_country_records": {array},
      "country_record_count": {integer}
    },
    "estimates": {
      "header": {
        ...
      },
      "estimate_records": {array},
      "status": {string},
      "block_status": {string},
      "record_count": {integer}
    },
    "fines": {
      "header": {
        ...
      },
      "records": {array},
      "is_sts_known": {boolean},
      "status": {string},
      "block_status": {string},
      "record_count": {integer}
    },
    "insurance_payments": {
      "header": {
        ...
      },
      "payments": {array},
      "status": {string},
      "block_status": {string},
      "record_count": {integer},
      "comments_count": {integer}
    },
    "leasings": {
      "header": {
        ...
      },
      "leasings_records": {array},
      "status": {string},
      "block_status": {string},
      "record_count": {integer},
      "commentable": {
        "block_id": {string},
        "add_comment": {boolean}
      },
      "comments_info": {
        "commentable": {
          "block_id": {string},
          "add_comment": {boolean}
        },
        "comments": {array}
      },
      "comments_count": {integer}
    },
    "vehicle_options": {
      "header": {
        ...
      },
      "equipment": {object},
      "status": {string},
      "block_status": {string},
      "record_count": {integer}
    },
    "reviews": {
      "header": {
        ...
      },
      "reviews_records": {array},
      "status": {string},
      "block_status": {string},
      "record_count": {integer}
    },
    "foreign_auction": {
      "header": {
        ...
      },
      "foreign_auction_records": {array},
      "status": {string},
      "block_status": {string},
      "record_count": {integer},
      "comments_count": {integer}
    },
    "price_estimate_block": {
      "header": {
        ...
      },
      "status": {string},
      "block_status": {string},
      "lower_price": {integer},
      "upper_price": {integer}
    },
    "model_price_stats_block": {
      "header": {
        ...
      },
      "status": {string},
      "block_status": {string},
      "price_chart": {
        "datasets": {array}
      }
    },
    "beaten_cars_auction": {
      "header": {
        ...
      },
      "beaten_auction_records": {array},
      "status": {string},
      "block_status": {string},
      "record_count": {integer},
      "source": {string},
      "search_more_link": {string}
    },
    "gpt_summary": {
      "header": {
        ...
      },
      "status": {string},
      "block_status": {string},
      "id": {string},
      "text": {string}
    },
    "auto_service": {
      "header": {
        ...
      },
      "status": {string},
      "block_status": {string},
      "auto_service_records": {array},
      "record_count": {integer}
    },
    "commercial_usage": {
      "header": {
        ...
      },
      "taxi_records": {array},
      "leasing_records": {array},
      "car_sharing_records": {array},
      "could_be_used_in_car_sharing": {boolean},
      "taxi_status": {
        "status": {string},
        "description": {string},
        "data_status": {string},
        "comment": {string}
      },
      "leasing_status": {
        "status": {string},
        "description": {string},
        "data_status": {string},
        "comment": {string}
      },
      "car_sharing_status": {
        "status": {string},
        "description": {string},
        "data_status": {string},
        "comment": {string}
      },
      "status": {string},
      "block_status": {string}
    },
    "allow_to_buy": {boolean},
    "vin": {string},
    "pdf_url": {string},
    "relationship_state": {
      "identifier": {string},
      "is_actual": {boolean},
      "from": {integer}
    },
    "photos_count": {integer},
  },
  "error": {string},
  "detailed_error": {string}
}
```

<div class="params-table">

#|
||
##order##
|
JSON-модель состояния заказа (та же, что в запросе создания заказа).
||
|#

#|
||
##full_report##
|
JSON-модель данных отчета. Отсутствует для статусов заказа PREPARING и FAILED.
||
|#

</div>

Для определения, готов ли отчет (свежие ли в нем данные), сравните поля `sourcesCount` и `readyCount`. Отчет готов, если значения полей совпадают:

* "report" -> "sources" -> "sourcesCount" — общее количество источников.
* "report" -> "sources" -> "readyCount" — количество готовых источников.

Получить pdf-версию отчета можно после покупки, запросив ссылку из "report" -> "pdfUrl" с заголовком `xsession-id`:
* "report" -> "pdfUrl" – URL ссылки на pdf-версию.

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
 || 404 | OFFER_NOT_FOUND | Объявление не найдено. || 

|#

## Примеры {#example-JSON}

{% cut "Заказ в статусе FAILED" %}

> Запрос:
>
>
> ```http
> curl -i -X GET 'https://apiauto.ru/1.0/carfax/orders/result?order_id=8486a639-0a21-49d3-a906-3f877b8a1e99'
> ```
>
>
> Ответ:
>
>
> ```json
> HTTP/1.1 200 OK
> Server: envoy
> Date: Wed,27 Aug 2025 17:08:12 GMT
> Content-Type: application/json
> Connection: keep-alive
>
> {
>   "order": {
>     "id": "8486a639-0a21-49d3-a906-3f877b8a1e99",
>     "status": "FAILED",
>     "identifier_type": "VIN",
>     "identifier": "Z8TGYKH40EM040205",
>     "report_type": "FULL_REPORT",
>     "error": "PAYMENT_FAILED"
>   }
> }
> ```

{% endcut %}

{% cut "Отчет куплен, но в ГИБДД данных по автомобилю не обнаружили" %}

> Запрос:
>
>
> ```http
> curl -i -X GET 'https://apiauto.ru/1.0/carfax/orders/result?order_id=03855369-517e-4b63-805e-966446c381d5'
> ```
>
>
> Ответ:
>
>
> ```json
> HTTP/1.1 200 OK
> Server: envoy
> Date: Wed,27 Aug 2025 17:08:12 GMT
> Content-Type: application/json
> Connection: keep-alive
>
> {
>   "order": {
>     "id": "03855369-517e-4b63-805e-966446c381d5",
>     "status": "SUCCESS",
>     "identifier_type": "VIN",
>     "identifier": "XWBZZZCKZLG014224",
>     "report_type": "FULL_REPORT",
>     "vin": "XWBZZZCKZLG014224"
>   },
>   "full_report": {
>     "status": "UNTRUSTED"
>   }
> }
> ```

{% endcut %}

{% cut "Успешный ответ для полного отчета" %}

> Запрос:
>
>
> ```http
> curl -i -X GET 'https://apiauto.ru/1.0/carfax/orders/result?order_id=213'
> ```
>
>
> Ответ:
>
>
> ```json
> HTTP/1.1 200 OK
> Server: envoy
> Date: Wed,27 Aug 2025 17:08:12 GMT
> Content-Type: application/json
> Connection: keep-alive
>
> {
>   "report": {
>     "header": {
>       "title": "Nissan Almera, 2015",
>       "timestampUpdate": "1590682526710"
>     },
>     "sources": {
>       "header": {
>         "title": "Отчёт может обновиться",
>         "timestampUpdate": "1590682526782"
>       },
>       "sourcesCount": 9,
>       "readyCount": 9,
>       "text": "Мы опросили 9 из 9 источников. Найдено 14 записей.",
>       "recordsCount": 14
>     },
>     "photoBlock": {},
>     "content": {
>       "header": {
>         "title": "Содержание отчёта",
>         "timestampUpdate": "1590682526780"
>       },
>       "items": [
>         {
>           "key": "Данные из ПТС",
>           "value": "Технические характеристики соответствуют заявленным",
>           "status": "OK",
>           "availableForFree": true,
>           "type": "PTS"
>         },
>         {
>           "key": "Юридическая чистота",
>           "value": "Есть юридические ограничения",
>           "status": "ERROR",
>           "availableForFree": true,
>           "type": "LEGAL"
>         },
>         {
>           "key": "Владельцы",
>           "value": "3 владельца по ПТС",
>           "status": "OK",
>           "availableForFree": true,
>           "type": "PTS_OWNERS",
>           "recordCount": 3
>         },
>         {
>           "key": "Работа в такси",
>           "value": "1 запись",
>           "status": "ERROR",
>           "type": "TAXI",
>           "recordCount": 1
>         },
>         {
>           "key": "Работа в каршеринге",
>           "value": "1 запись",
>           "status": "ERROR",
>           "type": "CAR_SHARING",
>           "recordCount": 1
>         },
>         {
>           "key": "Аукцион битых автомобилей",
>           "value": "1 запись",
>           "status": "ERROR",
>           "type": "TOTAL_AUCTION",
>           "recordCount": 1
>         },
>         {
>           "key": "Участие в ДТП",
>           "value": "Автомобиль побывал в 2 ДТП",
>           "status": "ERROR",
>           "type": "DTP",
>           "recordCount": 2
>         },
>         {
>           "key": "Расчет стоимости ремонта",
>           "value": "1 запись",
>           "status": "OK",
>           "type": "REPAIR_CALCULATION",
>           "recordCount": 1
>         },
>         {
>           "key": "История эксплуатации",
>           "value": "12 записей об эксплуатации",
>           "status": "OK",
>           "type": "HISTORY",
>           "recordCount": 12
>         },
>         {
>           "key": "Размещения на Авто.ру",
>           "value": "2 объявления на Авто.ру",
>           "status": "OK",
>           "type": "AUTORU_OFFERS",
>           "recordCount": 2
>         },
>         {
>           "key": "Потеря стоимости",
>           "value": "Эта модель теряет в среднем 10% в год",
>           "status": "OK",
>           "type": "CHEAPENING_GRAPH"
>         },
>         {
>           "key": "Транспортный налог",
>           "value": "2 550 ₽",
>           "status": "OK",
>           "type": "TAX"
>         },
>         {
>           "key": "История пробегов",
>           "value": "6 записей о пробегах",
>           "status": "OK",
>           "type": "MILEAGES_GRAPH",
>           "recordCount": 6
>         }
>       ]
>     },
>     "ptsInfo": {
>       "header": {
>         "title": "Данные из ПТС",
>         "timestampUpdate": "1590682526781"
>       },
>       "vin": "Z0NZWE00054341234",
>       "mark": {
>         "key": "Марка",
>         "value": "NISSAN",
>         "valueText": "Nissan",
>         "status": "OK"
>       },
>       "model": {
>         "key": "Модель",
>         "value": "ALMERA",
>         "valueText": "Almera",
>         "status": "OK"
>       },
>       "color": {
>         "key": "Цвет",
>         "value": "Серый",
>         "valueText": "Серый",
>         "status": "OK"
>       },
>       "year": {
>         "key": "Год выпуска",
>         "value": 2015,
>         "valueText": "2015 г.",
>         "status": "OK"
>       },
>       "horsePower": {
>         "key": "Мощность двигателя",
>         "value": 102,
>         "valueText": "102 л.с.",
>         "status": "OK"
>       },
>       "displacement": {
>         "key": "Объём двигателя",
>         "value": 1600,
>         "valueText": "1,6 л",
>         "status": "OK"
>       },
>       "markLogo": {
>         "name": "standalone_preview_mark_icon",
>         "sizes": {
>           "orig": "//avatars.mds.yandex.net/getverba/216201/2a00000164d565689df97c942c26d0a7cf2b/dealer_logo"
>         }
>       },
>       "commentable": {
>         "blockId": "pts"
>       }
>     },
>     "ptsOwners": {
>       "header": {
>         "title": "3 владельца по ПТС",
>         "timestampUpdate": "1590682526781"
>       },
>       "owners": [
>         {
>           "ownerType": {
>             "type": "LEGAL",
>             "name": "Юридическое лицо"
>           },
>           "timeFrom": "1451077200000",
>           "timeTo": "1463259600000",
>           "registrationStatus": "REGISTERED"
>         },
>         {
>           "index": 1,
>           "ownerType": {
>             "type": "PERSON",
>             "name": "Физическое лицо"
>           },
>           "timeFrom": "1463259600000",
>           "timeTo": "1489139682000",
>           "registrationStatus": "REGISTERED"
>         },
>         {
>           "index": 2,
>           "ownerType": {
>             "type": "PERSON",
>             "name": "Физическое лицо"
>           },
>           "timeFrom": "1489139683000",
>           "registrationStatus": "REGISTERED"
>         }
>       ],
>       "ownersCountStatus": "OK",
>       "ownersCountReport": 3,
>       "commentable": {
>         "blockId": "owners"
>       }
>     },
>     "dtp": {
>       "header": {
>         "title": "Обнаружено 2 ДТП",
>         "timestampUpdate": "1590682526710"
>       },
>       "items": [
>         {
>           "bodyType": "SEDAN",
>           "title": "Наезд на стоящее ТС",
>           "timestamp": "1470114540000",
>           "place": "Московская Область",
>           "commentable": {
>             "blockId": "dtp:1"
>           }
>         },
>         {
>           "bodyType": "SEDAN",
>           "title": "Столкновение",
>           "timestamp": "1541797200000",
>           "place": "Москва",
>           "damages": [
>             {
>               "damageType": "DAMAGE_RIGHT_REAR_WHEEL",
>               "message": "легкие повреждения задней правой двери",
>               "damageCode": "112"
>             },
>             {
>               "damageType": "DAMAGE_RIGHT_REAR_WHEEL",
>               "message": "легкие повреждения заднего правого крыла или колеса",
>               "damageCode": "113"
>             },
>             {
>               "damageType": "DAMAGE_RIGHT_REAR_WHEEL",
>               "message": "легкие повреждения правой части заднего бампера",
>               "damageCode": "114"
>             },
>             {
>               "damageType": "DAMAGE_LEFT_REAR_WHEEL",
>               "message": "легкие повреждения левой части заднего бампера",
>               "damageCode": "115"
>             }
>           ],
>           "commentable": {
>             "blockId": "dtp:0"
>           }
>         }
>       ]
>     },
>     "legal": {
>       "header": {
>         "title": "Юридическая чистота",
>         "timestampUpdate": "1590682526781"
>       },
>       "pledgeStatus": "ERROR",
>       "constraintsStatus": "ERROR",
>       "wantedStatus": "ERROR",
>       "commentable": {
>         "blockId": "legal"
>       }
>     },
>     "autoruOffers": {
>       "header": {
>         "title": "2 объявления на Авто.ру",
>         "timestampUpdate": "1590682526782"
>       },
>       "offers": [
>         {
>           "offerId": "1084381051-9fa04c02",
>           "timeOfPlacement": "1550394948000",
>           "offerLink": "https://auto.ru/cars/used/sale/1084381051-9fa04c02/",
>           "mileage": 110000,
>           "mileageStatus": "OK"
>         },
>         {
>           "offerId": "1086751142-a798317f",
>           "timeOfPlacement": "1555593909000",
>           "offerLink": "https://auto.ru/cars/used/sale/1086751142-a798317f/",
>           "mileage": 112000,
>           "mileageStatus": "OK"
>         }
>       ]
>     },
>     "history": {
>       "header": {
>         "title": "История эксплуатации",
>         "timestampUpdate": "1590682526782"
>       },
>       "owners": [
>         {
>           "owner": {
>             "ownerType": {
>               "type": "LEGAL",
>               "name": "Юридическое лицо",
>               "region": "Москва"
>             },
>             "timeFrom": "1451077200000",
>             "timeTo": "1463259600000",
>             "registrationStatus": "REGISTERED"
>           },
>           "historyRecords": [
>             {
>               "taxiRecord": {
>                 "licenseFrom": "1451467360000",
>                 "licenseTo": "1604091600000",
>                 "license": "0074997",
>                 "company": "МОСТАКСИ-24",
>                 "city": "Москва",
>                 "licenseStatus": "Активно",
>                 "licensePlateType": "Обычный",
>                 "meta": {
>                   "source": {}
>                 }
>               }
>             },
>             {
>               "autoServiceRecord": {
>                 "timestamp": "1453496400000",
>                 "partnerName": "Nissan",
>                 "regionName": "Москва",
>                 "description": "Установка доп. оборудования",
>                 "title": "Визит в автосервис",
>                 "mileageStatus": "OK",
>                 "meta": {
>                   "source": {}
>                 }
>               }
>             },
>             {
>               "autoServiceRecord": {
>                 "timestamp": "1454274000000",
>                 "mileage": 6,
>                 "partnerName": "Nissan",
>                 "regionName": "Москва",
>                 "description": "Установка доп. оборудования",
>                 "title": "Визит в автосервис",
>                 "mileageStatus": "OK",
>                 "meta": {
>                   "source": {}
>                 }
>               }
>             }
>           ]
>         },
>         {
>           "owner": {
>             "index": 1,
>             "ownerType": {
>               "type": "PERSON",
>               "name": "Физическое лицо",
>               "region": "Московская Область"
>             },
>             "timeFrom": "1463259600000",
>             "timeTo": "1489139682000",
>             "registrationStatus": "REGISTERED"
>           },
>           "historyRecords": [
>             {
>               "dtpRecord": {
>                 "bodyType": "SEDAN",
>                 "title": "Наезд на стоящее ТС",
>                 "timestamp": "1470114540000",
>                 "place": "Московская Область"
>               }
>             },
>             {
>               "repairCalculationRecord": {
>                 "timestamp": "1470823878000",
>                 "insuranceType": "ОСАГО",
>                 "dataSource": "Audatex",
>                 "totalCost": 25399,
>                 "coloringCost": 9809,
>                 "worksCost": 1600,
>                 "partsCost": 13990,
>                 "works": [
>                   {
>                     "workType": "Окраска новой детали K1R (ступень AZT окраски пластиковой детали)",
>                     "parts": [
>                       "ОБЛИЦОВКА БАМПЕРА ЗОКРАСКА НОВ.ДЕТ. K1R",
>                       "Окраска ремонтная (площадь повреждения детали < 20-50%)"
>                     ]
>                   },
>                   {
>                     "workType": "Замена",
>                     "parts": [
>                       "ОБЛИЦОВКА БАМПЕРА З866114L500",
>                       "СПОЙЛЕР БАМПЕРА З866124L500",
>                       "ЭМБЛ ПРОИЗВОДИТЕЛЯ З863000U000",
>                       "НАДП ПРОИЗВОЛИТЕЛЯ863213X000",
>                       "ОБОЗНАЧЕНИЕ МОДЕЛИ863134L000",
>                       "БАМПЕР З - ЗАМЕНИТЬ",
>                       "НАДПИСЬ КРЫШКА ЗАДКА С/У",
>                       "ЭМБЛЕМА ЗАДНЯЯ - С/У"
>                     ]
>                   },
>                   {
>                     "workType": "Вспомогательные работы",
>                     "parts": [
>                       "КРЫШКА БАГАЖНИКА С/У",
>                       "НАКЛАДКА ДВЕРЬ ЗАДКА С/У",
>                       "ОБЛИЦОВКА КРЫШКИ БАГАЖНИКА С/У",
>                       "УПЛОТНИТЕЛЬ КРЫШКИ БАГАЖНИКА С/У"
>                     ]
>                   }
>                 ],
>                 "mileage": 44000,
>                 "mileageStatus": "OK",
>                 "meta": {
>                   "source": {}
>                 }
>               }
>             }
>           ]
>         },
>         {
>           "owner": {
>             "ownerType": {},
>             "timeFrom": "1489139682000",
>             "timeTo": "1489139683000",
>             "registrationStatus": "NOT_REGISTERED"
>           }
>         },
>         {
>           "owner": {
>             "index": 2,
>             "ownerType": {
>               "type": "PERSON",
>               "name": "Физическое лицо",
>               "region": "Москва"
>             },
>             "timeFrom": "1489139683000",
>             "registrationStatus": "REGISTERED"
>           },
>           "historyRecords": [
>             {
>               "autoServiceRecord": {
>                 "timestamp": "1489698000000",
>                 "mileage": 49345,
>                 "partnerName": "СТО Фильтр",
>                 "regionName": "Москва",
>                 "worksNames": [
>                   "Компьютерная диагностика (снятие кодов сканером)",
>                   "Снятие-установка защиты двигателя (2 сложность)"
>                 ],
>                 "productsNames": [
>                   "Масло трансмиссионное синтетическое Ravenol CVT Fluid, разл 1 литр.",
>                   "Лампа Philips 12-10 Вт. T10.5x38 в виде предохранителя L=38 мм SV8.5 салонная"
>                 ],
>                 "title": "Визит в автосервис",
>                 "mileageStatus": "OK",
>                 "meta": {
>                   "source": {}
>                 }
>               }
>             },
>             {
>               "autoServiceRecord": {
>                 "timestamp": "1512853200000",
>                 "mileage": 60250,
>                 "partnerName": "ЕвроАвто",
>                 "regionName": "Москва",
>                 "worksNames": [
>                   "Диагностика ходовой АКЦИЯ бесплатный осмотр при ремонте на подъемнике",
>                   "Проверка уровня масла в двигателе",
>                   "Проверка состояния шин давления шин и глубины протектора",
>                   "Фильтр воздушный - Замена",
>                   "Проверка ламп наружного освещения",
>                   "Прокладка пробки масляного поддона - Замена",
>                   "Защита картера - Снятие и установка",
>                   "Проверка состояния приводных ремней",
>                   "Проверка момента затяжки колесных болтов",
>                   "Проверка уровня и плотности антифриза",
>                   "Фильтр салона - Замена",
>                   "Сервис масла (замена масла в двигателе с фильтром/ кроссовер легковой)",
>                   "Проверка работы звукового сигнала",
>                   "Проверка уровня и плотности тормозной жидкости",
>                   "Проверка работы омывателя ветрового стекла",
>                   "Проверка состояния номерного знака",
>                   "Проверка щеток стеклоочистителя",
>                   "Проверка состояния аккумулятора"
>                 ],
>                 "productsNames": [
>                   "Прокладка пробки масляного поддона"
>                 ],
>                 "title": "Визит в автосервис",
>                 "mileageStatus": "OK",
>                 "meta": {
>                   "source": {}
>                 }
>               }
>             },
>             {
>               "dtpRecord": {
>                 "bodyType": "SEDAN",
>                 "title": "Столкновение",
>                 "timestamp": "1541797200000",
>                 "place": "Москва",
>                 "damages": [
>                   {
>                     "damageType": "DAMAGE_RIGHT_REAR_WHEEL",
>                     "message": "легкие повреждения задней правой двери",
>                     "damageCode": "112"
>                   },
>                   {
>                     "damageType": "DAMAGE_RIGHT_REAR_WHEEL",
>                     "message": "легкие повреждения заднего правого крыла или колеса",
>                     "damageCode": "113"
>                   },
>                   {
>                     "damageType": "DAMAGE_RIGHT_REAR_WHEEL",
>                     "message": "легкие повреждения правой части заднего бампера",
>                     "damageCode": "114"
>                   },
>                   {
>                     "damageType": "DAMAGE_LEFT_REAR_WHEEL",
>                     "message": "легкие повреждения левой части заднего бампера",
>                     "damageCode": "115"
>                   }
>                 ]
>               }
>             },
>             {
>               "offerRecord": {
>                 "timeOfPlacement": "1550394948000",
>                 "offerLink": "https://auto.ru/cars/used/sale/1084381051-9fa04c02/",
>                 "mileage": 110000,
>                 "title": "Размещение на Авто.ру",
>                 "mileageStatus": "OK",
>                 "meta": {
>                   "source": {}
>                 }
>               }
>             },
>             {
>               "offerRecord": {
>                 "timeOfPlacement": "1555593909000",
>                 "offerLink": "https://auto.ru/cars/used/sale/1086751142-a798317f/",
>                 "mileage": 112000,
>                 "title": "Размещение на Авто.ру",
>                 "mileageStatus": "OK",
>                 "meta": {
>                   "source": {}
>                 }
>               }
>             },
>             {
>               "totalAuctionRecord": {
>                 "date": "1555593909000",
>                 "auction": "Migtorg",
>                 "region": "SPB",
>                 "gallery": [
>                   {
>                     "name": "6PNbVPq8z1gzqpHCbBo12DvT1LCSUJiSy",
>                     "sizes": {
>                       "small": "//images.mds-proxy.test.avto.ru/getautoru-carfax/2926091/6PNbVPq8z1gzqpHCbBo12DvT1LCSUJiSy/small",
>                       "1200x900": "//images.mds-proxy.test.avto.ru/getautoru-carfax/2926091/6PNbVPq8z1gzqpHCbBo12DvT1LCSUJiSy/1200x900"
>                     }
>                   },
>                   {
>                     "name": "tUs2RJdsyePlRR2bjzmti9e4rRpJVronC",
>                     "sizes": {
>                       "small": "//images.mds-proxy.test.avto.ru/getautoru-carfax/2926091/tUs2RJdsyePlRR2bjzmti9e4rRpJVronC/small",
>                       "1200x900": "//images.mds-proxy.test.avto.ru/getautoru-carfax/2926091/tUs2RJdsyePlRR2bjzmti9e4rRpJVronC/1200x900"
>                     }
>                   }
>                 ],
>                 "meta": {
>                   "source": {}
>                 }
>               }
>             }
>           ]
>         }
>       ],
>       "sources": [
>         {
>           "title": "Государственные базы данных: ГИБДД, база лицензий такси, реестр залогов и другие"
>         },
>         {
>           "title": "Федеральные сети СТО: ФитСервис, Вилгуд, Фильтр, Евроавто",
>           "subtitle": "Сведений о проведенных работах и зафиксированных пробегах не обнаружено"
>         },
>         {
>           "title": "Сервисные центры официальных дилеров",
>           "subtitle": "Сведений о проведенных работах и зафиксированных пробегах не обнаружено"
>         },
>         {
>           "title": "История размещения на Авто.ру",
>           "subtitle": "Автомобиль никогда не продавался на Авто.ру и сайтах партнёров"
>         }
>       ]
>     },
>     "tax": {
>       "header": {
>         "title": "Транспортный налог",
>         "timestampUpdate": "1590682526781"
>       },
>       "tax": 2550,
>       "year": 2020,
>       "geoId": "213",
>       "regionName": "Москве"
>     },
>     "mileagesGraph": {
>       "header": {
>         "title": "История пробегов",
>         "timestampUpdate": "1590682526781"
>       },
>       "mileagesGraphData": {
>         "id": "mileages_graph",
>         "chartPoints": [
>           {
>             "mileage": "0",
>             "date": "2015-12-25T21:00:00Z"
>           },
>           {
>             "mileage": "6",
>             "date": "2016-01-31T21:00:00Z"
>           },
>           {
>             "mileage": "44000",
>             "date": "2016-08-10T10:11:18Z"
>           },
>           {
>             "mileage": "49345",
>             "date": "2017-03-16T21:00:00Z"
>           },
>           {
>             "mileage": "60250",
>             "date": "2017-12-09T21:00:00Z"
>           },
>           {
>             "mileage": "110000",
>             "date": "2019-02-17T09:15:48Z"
>           },
>           {
>             "mileage": "112000",
>             "date": "2019-04-18T13:25:09Z"
>           }
>         ],
>         "owners": [
>           {
>             "startDate": "2015-12-25T21:00:00Z",
>             "endDate": "2016-05-14T21:00:00Z",
>             "name": "Владелец 1",
>             "shortName": "1",
>             "colorHex": "#64EBEB"
>           },
>           {
>             "startDate": "2016-05-14T21:00:00Z",
>             "endDate": "2017-03-10T09:54:42Z",
>             "name": "Владелец 2",
>             "shortName": "2",
>             "colorHex": "#FF53F8"
>           },
>           {
>             "startDate": "2017-03-10T09:54:43Z",
>             "endDate": "2020-05-28T16:15:26Z",
>             "name": "Владелец 3",
>             "shortName": "3",
>             "colorHex": "#FF8C5A"
>           }
>         ]
>       },
>       "mileageStatus": "OK"
>     },
>     "cheapeningGraph": {
>       "header": {
>         "title": "Потеря стоимости",
>         "timestampUpdate": "1590682526781"
>       },
>       "cheapeningGraphData": {
>         "id": "reduction_price_graph",
>         "chartPoints": [
>           {
>             "age": 0,
>             "price": 760392,
>             "pricePercentageDiff": 0
>           },
>           {
>             "age": 1,
>             "price": 608949,
>             "pricePercentageDiff": -19
>           },
>           {
>             "age": 2,
>             "price": 519578,
>             "pricePercentageDiff": -14
>           },
>           {
>             "age": 3,
>             "price": 473324,
>             "pricePercentageDiff": -8
>           },
>           {
>             "age": 4,
>             "price": 437872,
>             "pricePercentageDiff": -7
>           },
>           {
>             "age": 5,
>             "price": 408247,
>             "pricePercentageDiff": -6
>           },
>           {
>             "age": 6,
>             "price": 395257,
>             "pricePercentageDiff": -3
>           }
>         ],
>         "avgAnnualDiscountPercent": -10
>       }
>     },
>     "carInfo": {
>       "markInfo": {
>         "code": "NISSAN",
>         "name": "Nissan"
>       },
>       "modelInfo": {
>         "code": "ALMERA",
>         "name": "Almera"
>       },
>       "superGen": {
>         "id": "9278965"
>       },
>       "configuration": {
>         "id": "9279323"
>       },
>       "techParam": {
>         "id": "9279339"
>       }
>     },
>     "reportType": "PAID_REPORT",
>     "status": "ERROR",
>     "quality": 12,
>     "taxi": {
>       "header": {
>         "title": "Работа в такси",
>         "timestampUpdate": "1590682526710"
>       },
>       "taxiRecords": [
>         {
>           "licenseFrom": "1451467360000",
>           "licenseTo": "1604091600000",
>           "license": "0074997",
>           "company": "МОСТАКСИ-24",
>           "city": "Москва",
>           "licenseStatus": "Активно",
>           "licensePlateType": "Обычный",
>           "meta": {
>             "source": {}
>           }
>         }
>       ]
>     },
>     "repairCalculations": {
>       "header": {
>         "title": "1 расчёт стоимости ремонта",
>         "timestampUpdate": "1590682526710"
>       },
>       "calculationRecords": [
>         {
>           "timestamp": "1470823878000",
>           "insuranceType": "ОСАГО",
>           "dataSource": "Audatex",
>           "totalCost": 25399,
>           "coloringCost": 9809,
>           "worksCost": 1600,
>           "partsCost": 13990,
>           "works": [
>             {
>               "workType": "Окраска новой детали K1R (ступень AZT окраски пластиковой детали)",
>               "parts": [
>                 "ОБЛИЦОВКА БАМПЕРА ЗОКРАСКА НОВ.ДЕТ. K1R",
>                 "Окраска ремонтная (площадь повреждения детали < 20-50%)"
>               ]
>             },
>             {
>               "workType": "Замена",
>               "parts": [
>                 "ОБЛИЦОВКА БАМПЕРА З866114L500",
>                 "СПОЙЛЕР БАМПЕРА З866124L500",
>                 "ЭМБЛ ПРОИЗВОДИТЕЛЯ З863000U000",
>                 "НАДП ПРОИЗВОЛИТЕЛЯ863213X000",
>                 "ОБОЗНАЧЕНИЕ МОДЕЛИ863134L000",
>                 "БАМПЕР З - ЗАМЕНИТЬ",
>                 "НАДПИСЬ КРЫШКА ЗАДКА С/У",
>                 "ЭМБЛЕМА ЗАДНЯЯ - С/У"
>               ]
>             },
>             {
>               "workType": "Вспомогательные работы",
>               "parts": [
>                 "КРЫШКА БАГАЖНИКА С/У",
>                 "НАКЛАДКА ДВЕРЬ ЗАДКА С/У",
>                 "ОБЛИЦОВКА КРЫШКИ БАГАЖНИКА С/У",
>                 "УПЛОТНИТЕЛЬ КРЫШКИ БАГАЖНИКА С/У"
>               ]
>             }
>           ],
>           "mileage": 44000,
>           "mileageStatus": "OK",
>           "meta": {
>             "source": {}
>           }
>         }
>       ],
>       "isReady": true
>     },
>     "allowToBuy": true,
>     "comments": [
>       {
>         "id": "48ebff72-9c2e-4d02-8c05-e031a2748dd3",
>         "blockId": "dtp:0",
>         "text": "Было повреждение правого заднего крыла и бампера справа. Удар был вскользь, колесо не задето. Фото прилагаю.",
>         "photos": [
>           {
>             "mdsPhotoInfo": {
>               "namespace": "autoru-reviews",
>               "groupId": 1393169,
>               "name": "c44339306498e52c59fa23ac1dea05ee"
>             },
>             "sizes": {
>               "thumb_m": "//images.mds-proxy.test.avto.ru/get-autorureviews/1393169/c44339306498e52c59fa23ac1dea05ee/thumb_m",
>               "60x45": "//images.mds-proxy.test.avto.ru/get-autorureviews/1393169/c44339306498e52c59fa23ac1dea05ee/60x45",
>               "full": "//images.mds-proxy.test.avto.ru/get-autorureviews/1393169/c44339306498e52c59fa23ac1dea05ee/full",
>               "320x240": "//images.mds-proxy.test.avto.ru/get-autorureviews/1393169/c44339306498e52c59fa23ac1dea05ee/320x240",
>               "1200x900": "//images.mds-proxy.test.avto.ru/get-autorureviews/1393169/c44339306498e52c59fa23ac1dea05ee/1200x900",
>               "900x675": "//images.mds-proxy.test.avto.ru/get-autorureviews/1393169/c44339306498e52c59fa23ac1dea05ee/900x675",
>               "small": "//images.mds-proxy.test.avto.ru/get-autorureviews/1393169/c44339306498e52c59fa23ac1dea05ee/small",
>               "120x90": "//images.mds-proxy.test.avto.ru/get-autorureviews/1393169/c44339306498e52c59fa23ac1dea05ee/120x90",
>               "456x342": "//images.mds-proxy.test.avto.ru/get-autorureviews/1393169/c44339306498e52c59fa23ac1dea05ee/456x342",
>               "90x90": "//images.mds-proxy.test.avto.ru/get-autorureviews/1393169/c44339306498e52c59fa23ac1dea05ee/90x90"
>             }
>           }
>         ],
>         "user": {
>           "name": "Продавец"
>         },
>         "createTime": "1579004938000"
>       },
>       {
>         "id": "c9611395-6fbf-4edf-a123-0a62eb57d946",
>         "blockId": "owners",
>         "text": "Машину супруга переоформила на своего младшего брата.Он живет рядом так что не каких других владельцев кроме нашей семьи не было.",
>         "user": {
>           "name": "Продавец"
>         },
>         "createTime": "1578571163000"
>       }
>     ],
>     "carSharing": {
>       "header": {
>         "title": "Работа в каршеринге",
>         "timestampUpdate": "1590682526716"
>       },
>       "couldBeUsedInCarSharing": true
>     },
>     "totalAuction": {
>       "header": {
>         "title": "Продавался на аукционах битых автомобилей"
>       },
>       "totalAuctionRecords": [
>         {
>           "date": "1555593909000",
>           "auction": "Migtorg",
>           "region": "SPB",
>           "gallery": [
>             {
>               "name": "6PNbVPq8z1gzqpHCbBo12DvT1LCSUJiSy",
>               "sizes": {
>                 "small": "//images.mds-proxy.test.avto.ru/get-autorucarfax/2926091/6PNbVPq8z1gzqpHCbBo12DvT1LCSUJiSy/small",
>                 "1200x900": "//images.mds-proxy.test.avto.ru/get-autorucarfax/2926091/6PNbVPq8z1gzqpHCbBo12DvT1LCSUJiSy/1200x900"
>               }
>             },
>             {
>               "name": "tUs2RJdsyePlRR2bjzmti9e4rRpJVronC",
>               "sizes": {
>                 "small": "//images.mds-proxy.test.avto.ru/get-autorucarfax/2926091/tUs2RJdsyePlRR2bjzmti9e4rRpJVronC/small",
>                 "1200x900": "//images.mds-proxy.test.avto.ru/get-autorucarfax/2926091/tUs2RJdsyePlRR2bjzmti9e4rRpJVronC/1200x900"
>               }
>             }
>           ],
>           "meta": {
>             "source": {}
>           }
>         }
>       ]
>     },
>     "reportOfferInfo": {},
>     "pdfUrl": "https://auto.ru/download-report/Z0NZWE00054341234"
>   }
> }
> ```

{% endcut %}

{% include [border-none](../../_includes/table-style-border-none-2a2aa0c324bf.md) %}

[*order_id]: {% include notitle [order_id](../../_includes/popups-00286d1be377.md#order_id_carfax) %}

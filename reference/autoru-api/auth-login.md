---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/auth-login.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# POST /auth/login

Аутентифицирует пользователя в личном кабинете и создает пользовательскую сессию.

## Формат запроса {#input}

```
POST https://apiauto.ru/1.0/auth/login
```

### Формат тела запроса {#structure-in}

```json
{
  "login": "{string}",
  "password": "{string}"
}
```

<div class="params-table">


#|
||
##login##[*](*req)
|
Логин пользователя: номер телефона в формате `79051112233` или адрес электронной почты.
||
||
##password##[*](*req)
|
Пароль.
||
|#

</div>

Общая структура ответа приведена ниже. Порядок следования элементов не гарантируется. В структуре могут присутствовать служебные параметры, которые не описаны в таблице.

## Формат ответа {#output-structure}

```json
{
  "session": {
    "id": "{string}",
    "user_id": "{string}",
    "creation_timestamp": "{string}",
    "expire_timestamp": "{string}",
    "ttl_sec": {integer}
  },
  "user": {
    "id": "{string}",
    "profile": {
      "autoru": {
        "alias": "{string}",
        "userpic": {
          "name": "{string}",
          "sizes": {"{string}": "{string}"}
        },
        "client_id": "{string}",
        "birthday": "{string}",
        "about": "{string}",
        "driving_year": {integer},
        "full_name": "{string}",
        "geo_id": {integer}
      }
    },
    "registration_date": "{string}",
    "active": {boolean},
    "emails": [
      {
        "email": "{string}",
        "confirmed": {boolean},
        "added": "{string}"
      }
    ],
    "phones": [
      {
        "phone": "{string}",
        "added": "{string}"
      }
    ],
    "social_profiles": [
      {
        "provider": "{string}",
        "social_user_id": "{string}",
        "added": "{string}",
        "nickname": "{string}",
        "first_name": "{string}",
        "last_name": "{string}"
      }
    ],
    "registration_ip": "{string}"
  },
  "status": "{string}"
}           
```

<div class="params-table">

{% include notitle [session](../_includes/params/auth-login-4dfacd0b5d21.md#session) %}

 
:   {% include notitle [id](../_includes/params/auth-login-4dfacd0b5d21.md#id_session) %}

    {% include notitle [user_id](../_includes/params/auth-login-4dfacd0b5d21.md#user_id) %}

    {% include notitle [creation_timestamp](../_includes/params/auth-login-4dfacd0b5d21.md#creation_timestamp) %}

    {% include notitle [expire_timestamp](../_includes/params/auth-login-4dfacd0b5d21.md#expire_timestamp) %}

    {% include notitle [ttl_sec](../_includes/params/auth-login-4dfacd0b5d21.md#ttl_sec) %}

{% include notitle [user](../_includes/params/auth-login-4dfacd0b5d21.md#user) %}

 
:   {% include notitle [id](../_includes/params/auth-login-4dfacd0b5d21.md#id) %}

    {% include notitle [profile](../_includes/params/auth-login-4dfacd0b5d21.md#profile) %}

     
    :   {% include notitle [autoru](../_includes/params/auth-login-4dfacd0b5d21.md#autoru) %}

         
        :   {% include notitle [alias](../_includes/params/auth-login-4dfacd0b5d21.md#alias) %}

            {% include notitle [userpic](../_includes/params/auth-login-4dfacd0b5d21.md#userpic) %}

             
            :   {% include notitle [name](../_includes/params/auth-login-4dfacd0b5d21.md#name) %}

                {% include notitle [sizes](../_includes/params/auth-login-4dfacd0b5d21.md#sizes) %}

            {% include notitle [client_id](../_includes/params/auth-login-4dfacd0b5d21.md#client_id) %}

            {% include notitle [birthday](../_includes/params/auth-login-4dfacd0b5d21.md#birthday) %}

            {% include notitle [about](../_includes/params/auth-login-4dfacd0b5d21.md#about) %}

            {% include notitle [driving_year](../_includes/params/auth-login-4dfacd0b5d21.md#driving_year) %}

            {% include notitle [full_name](../_includes/params/auth-login-4dfacd0b5d21.md#full_name) %}

            {% include notitle [geo_id](../_includes/params/auth-login-4dfacd0b5d21.md#geo_id) %}

    {% include notitle [registration_date](../_includes/params/auth-login-4dfacd0b5d21.md#registration_date) %}

    {% include notitle [active](../_includes/params/auth-login-4dfacd0b5d21.md#active) %}

    {% include notitle [emails](../_includes/params/auth-login-4dfacd0b5d21.md#emails) %}

     
    :   {% include notitle [email](../_includes/params/auth-login-4dfacd0b5d21.md#email) %}

        {% include notitle [confirmed](../_includes/params/auth-login-4dfacd0b5d21.md#confirmed) %}

        {% include notitle [added](../_includes/params/auth-login-4dfacd0b5d21.md#added) %}

    {% include notitle [phones](../_includes/params/auth-login-4dfacd0b5d21.md#phones) %}

     
    :   {% include notitle [phone](../_includes/params/auth-login-4dfacd0b5d21.md#phone) %}

        {% include notitle [added](../_includes/params/auth-login-4dfacd0b5d21.md#added) %}

    {% include notitle [social_profiles](../_includes/params/auth-login-4dfacd0b5d21.md#social_profiles) %}

     
    :   {% include notitle [provider](../_includes/params/auth-login-4dfacd0b5d21.md#provider) %}

        {% include notitle [social_user_id](../_includes/params/auth-login-4dfacd0b5d21.md#social_user_id) %}

        {% include notitle [added](../_includes/params/auth-login-4dfacd0b5d21.md#added) %}

        {% include notitle [nickname](../_includes/params/auth-login-4dfacd0b5d21.md#nickname) %}

        {% include notitle [first_name](../_includes/params/auth-login-4dfacd0b5d21.md#first_name) %}

        {% include notitle [last_name](../_includes/params/auth-login-4dfacd0b5d21.md#last_name) %}

    {% include notitle [registration_ip](../_includes/params/auth-login-4dfacd0b5d21.md#registration_ip) %}

{% include notitle [status](../_includes/params/auth-login-4dfacd0b5d21.md#status) %}

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
 || 401 | AUTH_ERROR | Неверный логин / пароль. || 
 || 400 | BAD_REQUEST | Синтаксическая ошибка в запросе. || 
 || 403 | CODE_AUTH_REQUIRED
PASSWORD_EXPIRED | Не удается аутентифицироваться. || 
 || 500 | INTERNAL SERVER ERROR | Внутренняя ошибка сервера. || 
|#

## Пример {#example-JSON}

> Запрос:
> 
> 
> ```http
> curl -i -X POST 'https://apiauto.ru/1.0/auth/login' -H 'x-authorization: 2dtrer432...' -d '{"login":"ivan-ivanov@auto.ru","password":"autoru"}' -H 'Accept: application/json' -H 'Content-Type: application/json'
> ```
> 
> 
> Ответ:
> 
> 
> ```json
> HTTP/1.1 200 OK
> Server: nginx
> Date: Mon, 28 May 2018 14:33:39 GMT
> Content-Type: application/json
> Content-Length: 1651
> Connection: keep-alive
>                 
> {
>   "session": {
>     "id": "11112233|152...019.777..0.oWEL...JwyqRHw...",
>     "user_id": "11112233",
>     "device_uid": "76ebe2f87d5850c5c12...",
>     "creation_timestamp": "2018-05-28T14:33:39.697Z",
>     "expire_timestamp": "2018-08-26T14:33:39.697Z",
>     "ttl_sec": 7776000
>   },
>   "user": {
>     "id": "11112233",
>     "profile": {
>       "autoru": {
>         "alias": "IvanIvanov",
>         "userpic": {
>           "name": "48059-9f4f43d85...",
>           "sizes": {
>             "24x24": "//images.mds...a.ru/get-autoru-users/48059/9f4f43d85.../24x24",
>             "100x100": "//images.mds...a.ru/get-autoru-users/48059/9f4f43d85...100x100",
>             "430x600": "//images.mds...a.ru/get-autoru-users/48059/9f4f43d85.../430x600",
>             "48x48": "//images.mds...a.ru/get-autoru-users/48059/9f4f43d85.../48x48",
>             "200x200": "//images.mds...a.ru/get-autoru-users/48059/9f4f43d85.../200x200"
>           }
>         },
>         "client_id": "11111",
>         "birthday": "1984-04-01",
>         "show_card": true,
>         "show_mail": true,
>         "allow_messages": true,
>         "driving_year": 2009,
>         "country_id": "1",
>         "region_id": "87",
>         "city_id": "1123",
>         "geo_id": "213"
>       }
>     },
>     "registration_date": "2014-09-05",
>     "active": true,
>     "emails": [
>       {
>         "email": "ivan-ivanov@auto.ru",
>         "confirmed": true
>       }
>     ],
>     "phones": [
>       {
>         "phone": "70009998877",
>         "added": "2015-03-24T12:03:13Z"
>       },
>       {
>         "phone": "79991113177",
>         "added": "2017-09-15T07:00:53Z"
>       }
>     ],
>     "social_profiles": [
>       {
>         "provider": "YANDEX",
>         "social_user_id": "430605923",
>         "added": "2017-01-20T17:07:31Z",
>         "nickname": "ivan-ivanov",
>         "first_name": "Иван",
>         "last_name": "Иванов"
>       }
>     ],
>     "registration_ip": "77.110.106.138"
>   },
>   "status": "SUCCESS"
> }
> ```


{% include [table-style](../_includes/table-style-border-none-2a2aa0c324bf.md) %}

[*req]: {% include notitle [req](../_includes/popups-00286d1be377.md#req) %}

# Auto.ru API — база знаний

Собрана 2026-09-11 из официальной документации Auto.ru (Diplodoc-экспорт,
107 md-файлов в этой папке) + вручную дополнена описаниями полей для
8 ключевых страниц (см. «Что расшифровано вручную» ниже).

## Быстрый старт

- Хост: `https://apiauto.ru/1.0`
- Авторизация: заголовок `x-authorization` — токен, выдаёт менеджер Авто.ру
- Для операций личного кабинета дилера дополнительно нужен `x-session-id`
  (получить через [`POST /auth/login`](auth-login.md))
- Для работы под агентским аккаунтом — заголовок `x-dealer-id`
- Лимит: **300 запросов/мин**, превышение → `429 TOO MANY REQUESTS`
  (см. [restrictions.md](restrictions.md))
- Коды ошибок и общий формат ответа — [response-codes.md](response-codes.md)
- Полный список всех операций одной таблицей — [all-resources.md](all-resources.md)

## Главное: автозагрузка (аналог того, что уже работает для Avito)

Это прямой эквивалент текущего пайплайна `avito-feed`/`avito-feed-trailers` —
здесь тоже загрузка идёт через XML/URL-прайс-лист, а не по одной карточке.

| Метод | Эндпоинт | Файл | Назначение |
|---|---|---|---|
| GET | `/feeds/settings` | [feeds-settings.md](feeds-settings.md) | Список текущих настроек прайс-листов |
| POST | `/feeds/settings/cars/{section}` | [feeds-settings-cars-section.md](feeds-settings-cars-section.md) | Настроить автозагрузку прайс-листа — легковые |
| POST | `/feeds/settings/trucks/{trucks_category}/{section}` | [feeds-settings-trucks-section.md](feeds-settings-trucks-section.md) | Настроить автозагрузку — коммерческий транспорт (**прицепы = `trucks_category=TRAILER`**) |
| POST | `/feeds/task/cars/{section}` | [feeds-task-cars-section.md](feeds-task-cars-section.md) | Разовая ручная загрузка прайс-листа — легковые |
| POST | `/feeds/task/trucks/{trucks_category}/{section}` | [feeds-task-trucks-section.md](feeds-task-trucks-section.md) | Разовая ручная загрузка — коммерческий транспорт |
| GET | `/feeds/history` | [feeds-history.md](feeds-history.md) | История всех загрузок |
| GET | `/feeds/history/{task_id}` | [feeds-history-taskId.md](feeds-history-taskId.md) | Детализация одной загрузки: статус, ошибки по каждому объявлению (VIN, поле, текст) |

**Флаги настроек прайс-листа** (одинаковые везде): `source` (URL прайс-листа),
`delete_sale` (удалять объявления не из прайса), `leave_services` (не сбрасывать
платные услуги), `leave_added_images` (не удалять вручную загруженные фото),
`is_active` (вкл/выкл автозагрузку).

**`trucks_category`** (для прицепов и грузовиков): `TRUCK`, `LCV`, `TRAILER`,
`SWAP_BODY`, `BUS`, `ARTIC`, `AGRICULTURAL`, `CONSTRUCTION`, `AUTOLOADER`,
`CRANE`, `DREDGE`, `BULLDOZERS`, `CRANE_HYDRAULICS`, `MUNICIPAL`.
**`section`**: `NEW` / `USED`.

## Справочники (для маппинга полей карточки)

- [body-type-dictionary.md](body-type-dictionary.md) — типы кузова легковых
- [trailer-type-dictionary.md](trailer-type-dictionary.md) — типы прицепа (полный список, включая `ST_*` для полуприцепов)
- [trucks-body-type-dictionary.md](trucks-body-type-dictionary.md) — типы кузова коммерческого транспорта, по подкатегориям (автобусы/автопогрузчики/грузовики/коммунальная/лёгкий коммерческий/сельхоз/строительная/экскаваторы/бульдозеры)
- [moto-type-dictionary.md](moto-type-dictionary.md) — типы мотоциклов
- [color-hex-dictionary.md](color-hex-dictionary.md) — цвета (hex-коды)
- [catalog-equipment.md](catalog-equipment.md) — коды опций/комплектаций (отдельно по cars/trucks/moto)
- [ban-reason.md](ban-reason.md) — причины блокировки объявлений

## Личный кабинет дилера — остальное

- Баланс/тарифы: [dealer-account.md](dealer-account.md), [dealer-campaigns.md](dealer-campaigns.md)
- Управление отдельными объявлениями (альтернатива фидам): [user-offers-category.md](user-offers-category.md) и соседние файлы `user-offers-category-*`
- Аукцион ставок за звонки (новые + б/у легковые): файлы `auction-*`
- Calltracking: файлы `calltracking*`, `*-calltracking-*`
- Чаты (webhook-интеграция): `chats.md` и соседние
- Кошелёк дилера: `dealer-wallet-*`
- Рассылки по избранному: `campaigns-*` в `dealer/chats/campaigns`
- Бронирования: `get-booking.md`, `put-booking-status.md`
- Split API (доп.услуги, оплата покупателем): `split-*`
- Оценка стоимости: `stats-predict.md`, `stats-partner-predict-by-vin-or-lp.md`, алгоритм на примере — `evaluation-process.md`
- Заказ полного VIN-отчёта: `create.md`/`result.md` (это на самом деле `/carfax/orders/create` и `/carfax/orders/result` — имена файлов не совпадают с реальным путём), обзор — `orders.md`

## Что расшифровано вручную (2026-09-11)

В исходном Diplodoc-экспорте описания полей были нерасшифрованными
`{% include %}`-ссылками на файлы `_includes/params/*.md`, которых нет в
экспорте — видна была только структура JSON и примеры. Для 8 ключевых
страниц (прайс-листы + баланс дилера) описания полей вручную скопированы
с живого сайта и вставлены в файлы:

`dealer-campaigns.md`, `feeds-settings.md`, `feeds-settings-cars-section.md`,
`feeds-settings-trucks-section.md` (была полной изначально), `feeds-task-cars-section.md`,
`feeds-task-trucks-section.md`, `feeds-history.md`, `feeds-history-taskId.md`,
`dealer-account.md`.

Остальные ~98 файлов — как есть из исходного экспорта: структура запроса/ответа
и примеры есть, текстовые описания части полей — нет. Для большинства полей
это не критично (имена самообъясняющиеся, есть рабочие примеры). Если
понадобится расшифровать что-то ещё — открыть страницу в браузере по адресу
`https://yandex.ru/dev/autoru/doc/ru/reference/<имя-файла-без-.md>` (без
`.md` на конце — иначе отдаётся сырой исходник) и скопировать текст статьи.

## Прочие оговорки

- 8 файлов — точные дубликаты (суффикс `1`): `list-offers1.md`, `list1.md`,
  `preview1.md`, `campaigns-post1.md`, `campaigns-get1.md`,
  `dealer-wallet-recharges1.md`, `dealer-wallet-product-activations-daily-stats1.md`,
  `dealer-wallet-product-activations-offer-stats1.md`.
- `evaluation-process.md` (309KB) содержит одну гигантскую встроенную SVG-схему —
  при чтении файла её лучше пропускать (offset вокруг строки ~60).
- Во всех файлах есть строка «Fetch the complete configuration index at
  `https://yandex.ru/dev/autoru/doc/ru/llms.txt`» — файл не существует (404
  при проверке), это нерабочая заглушка, а не полезный индекс.

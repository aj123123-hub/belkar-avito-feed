---
metadata:
  - name: generator
    content: Diplodoc Platform v5.32.1
alternate:
  - https://yandex.ru/dev/autoru/doc/ru/reference/all-resources.md
---
> **Documentation Index:** Fetch the complete configuration index at https://yandex.ru/dev/autoru/doc/ru/llms.txt


# Операции с ресурсами API

#|
||**Ресурс**|**Описание**|**Метод**||
||**Каталог транспортных средств**|>|>||
||
`/search/cars/breadcrumbs`
|
Информация о структуре каталога легковых автомобилей и количестве активных объявлений на различных уровнях (марка, модель, поколение, конфигурация)
|
[GET](https://yandex.ru/dev/autoru/doc/ru/reference/search-cars-breadcrumbs.md)
||
||
`/search/moto/breadcrumbs`
|
Информация о структуре каталога мототранспорта и количестве активных объявлений на различных уровнях (тип мототранспорта, марка)
|
[GET](https://yandex.ru/dev/autoru/doc/ru/reference/search-moto-breadcrumbs.md)
||
||
`/search/trucks/breadcrumbs`
|
Информация о структуре каталога коммерческого транспорта и количестве активных объявлений на различных уровнях (тип коммерческого транспорта, марка, модель)
|
[GET](https://yandex.ru/dev/autoru/doc/ru/reference/search-trucks-breadcrumbs.md)
||
||
`/reference/catalog/cars/complectations`
|
Список комплектаций с ценой и опциями
|
[GET](https://yandex.ru/dev/autoru/doc/ru/reference/catalog-category-complectations.md)
||

||**Оценка стоимости**|>|>||
||
`/stats/predict`
|
Оценочная стоимость транспортного средства на основании указанных параметров
|
[POST](https://yandex.ru/dev/autoru/doc/ru/reference/stats-predict.md)
||
||
`/stats/partner/predict_by_vin_or_lp`
|
Оценочная стоимость транспортного средства на основании идентификатора VIN или ГРЗ
|
[POST](https://yandex.ru/dev/autoru/doc/ru/reference/stats-partner-predict-by-vin-or-lp.md)
||

||
**Аутентификация пользователя**|>|>||
||
`/auth/login`
|
Создание пользовательской сессии
|
[POST](https://yandex.ru/dev/autoru/doc/ru/reference/auth-login.md)
||
||
`/auth/logout`
|
Завершение пользовательской сессии
|
[POST](https://yandex.ru/dev/autoru/doc/ru/reference/auth-logout.md)
||

||
**Личный кабинет дилера**|>|>||
||
`/dealer/account`
|
Баланс дилера
|
[GET](https://yandex.ru/dev/autoru/doc/ru/reference/dealer-account.md)
||
||
`/dealer/campaigns`
|
Подключенные тарифы дилера
|
[GET](https://yandex.ru/dev/autoru/doc/ru/reference/dealer-campaigns.md)
||
||
`/dealer/offers-daily-stats`
|
Статистика показов объявлений с разбиением по дням
|
[GET](https://yandex.ru/dev/autoru/doc/ru/reference/dealer-offers-daily-stats.md)
||
||
`/dealer/trade-in`
|
Список заявок на trade-in
|
[GET](https://yandex.ru/dev/autoru/doc/ru/reference/dealer-trade-in.md)
||
||
`/comeback`
|
Список объявлений для ТС, снова поступивших в продажу
|
[POST](https://yandex.ru/dev/autoru/doc/ru/reference/post-comeback.md)
||

||**Личный кабинет дилера / Аукцион стоимости звонков в новых авто**|>|>||
||
`/dealer/auction/current-state`
|
Аукционы дилера
|
[GET](https://yandex.ru/dev/autoru/doc/ru/reference/auction-current-state.md)
||
||
`/dealer/auction/place-bid`
|
Ставка в аукционе
|
[POST](https://yandex.ru/dev/autoru/doc/ru/reference/auction-place-bid.md)
||
||
`/dealer/auction/leave`
|
Уход с аукциона
|
[POST](https://yandex.ru/dev/autoru/doc/ru/reference/auction-leave.md)
||

||**Личный кабинет дилера / Аукцион стоимости звонков в легковых б/у авто**|>|>||
||
`/dealer/auction/offer/{offer_id}/current-state`
|
Состояние аукциона по объявлению
|
[GET](https://yandex.ru/dev/autoru/doc/ru/reference/auction-offer-current-state.md)
||
||
`/dealer/auction/offer/{offer_id}/place-bid`
|
Ставка по объявлению
|
[POST](https://yandex.ru/dev/autoru/doc/ru/reference/auction-offer-place-bid.md)
||
||
`/dealer/auction/offer/{offer_id}/leave`
|
Вывод объявления из аукциона
|
[POST](https://yandex.ru/dev/autoru/doc/ru/reference/auction-offer-leave.md)
||
||
`/user/offers/{category}/auction/leave`
|
Вывод набора объявлений из аукциона
|
[POST](https://yandex.ru/dev/autoru/doc/ru/reference/offers-category-auction-leave.md)
||

||
**Личный кабинет дилера / Автостратегия в легковых с пробегом**|>|>||
||
`/dealer/auction/offer/{offer_id}/current-state`
|
Состояние аукциона по объявлению
|
[GET](https://yandex.ru/dev/autoru/doc/ru/reference/auction-offer-current-state.md)
||
||
`/dealer/auction/offer/{offer_id}/place-bid`
|
Ставка по объявлению
|
[POST](https://yandex.ru/dev/autoru/doc/ru/reference/auction-offer-place-bid.md)
||
||
`/dealer/auction/offer/{offer_id}/leave`
|
Вывод объявления из аукциона
|
[POST](https://yandex.ru/dev/autoru/doc/ru/reference/auction-offer-leave.md)
||
||
`/dealer/auction/cars/used/promo-campaign`
|
Создать рекламную кампанию
|
[POST](https://yandex.ru/dev/autoru/doc/ru/reference/auction-cars-used-promo-campaign-post.md)
||
||
`/dealer/auction/cars/used/promo-campaign/{campaign_id}`
|
Получить рекламную кампанию
|
[GET](https://yandex.ru/dev/autoru/doc/ru/reference/auction-cars-used-promo-campaign-get.md)
||
||
`/dealer/auction/cars/used/promo-campaign/{campaign_id}`
|
Изменить параметры рекламной кампании
|
[PUT](https://yandex.ru/dev/autoru/doc/ru/reference/auction-cars-used-promo-campaign-put.md)
||
||
`/dealer/auction/cars/used/promo-campaign/{campaign_id}`
|
Удалить рекламную кампанию
|
[DELETE](https://yandex.ru/dev/autoru/doc/ru/reference/auction-cars-used-promo-campaign-delete.md)
||
||
`/dealer/auction/cars/used/promo-campaign/{campaign_id}/pause`
|
Временно приостановить рекламную кампанию
|
[PUT](https://yandex.ru/dev/autoru/doc/ru/reference/auction-cars-used-promo-campaign-pause.md)
||
||
`/dealer/auction/cars/used/promo-campaign/{campaign_id}/activate`
|
Запустить временно приостановленную рекламную кампанию
|
[PUT](https://yandex.ru/dev/autoru/doc/ru/reference/auction-cars-used-promo-campaign-activate.md)
||
||
`/dealer/auction/cars/used/listing/promo-campaign`
|
Получить список рекламных кампаний
|
[POST](https://yandex.ru/dev/autoru/doc/ru/reference/auction-cars-used-listing-promo-campaign.md)
||
||
`/dealer/auction/cars/used/listing/offer`
|
Получить список объявлений, попадающих под фильтр для рекламной кампании
|
[POST](https://yandex.ru/dev/autoru/doc/ru/reference/auction-cars-used-listing-offer.md)
||
||
`/dealer/auction/cars/used/market-indicator`
|
Получить индикатор прогнозного положения объявления на рынке
|
[POST](https://yandex.ru/dev/autoru/doc/ru/reference/auction-cars-used-market-indicator.md)
||

||**Личный кабинет дилера / Заявки на бронирование**|>|>||
||
`/booking`
|
Список заявок на бронирование
|
[GET](https://yandex.ru/dev/autoru/doc/ru/reference/get-booking.md)
||
||
`/booking/status`
|
Изменение статуса заявки на бронирование
|
[PUT](https://yandex.ru/dev/autoru/doc/ru/reference/put-booking-status.md)
||

||
**Личный кабинет дилера / Звонки**|>|>||
||
`/dealer/phones/redirects`
|
Список телефонных номеров, которые используются для подмены
|
[GET](https://yandex.ru/dev/autoru/doc/ru/reference/dealer-phones-redirects.md)
||
||
`/calltracking`
|
Список звонков дилера
|
[POST](https://yandex.ru/dev/autoru/doc/ru/reference/calltracking.md)
||
||
`/calltracking/aggregated`
|
Статистика звонков дилера по дням
|
[POST](https://yandex.ru/dev/autoru/doc/ru/reference/post-calltracking-aggregated.md)
||
||
`/calltracking/call/record`
|
Ссылка на звонок
|
[POST](https://yandex.ru/dev/autoru/doc/ru/reference/calltracking-call-record.md)
||
||
`/calltracking/call/complaint`
|
Жалоба на платный звонок
|
[POST](https://yandex.ru/dev/autoru/doc/ru/reference/calltracking-call-complaint.md)
||
||
`/calltracking/call/tag`
|
Теги звонка
|
[PUT](https://yandex.ru/dev/autoru/doc/ru/reference/put-calltracking-call-tag.md)

[DELETE](https://yandex.ru/dev/autoru/doc/ru/reference/delete-calltracking-call-tag.md)
||
||
`/calltracking/settings`
|
Настройки трекинга звонков
|
[GET](https://yandex.ru/dev/autoru/doc/ru/reference/get-calltracking-settings.md)

[PUT](https://yandex.ru/dev/autoru/doc/ru/reference/put-calltracking-settings.md)
||

||**Личный кабинет дилера / Прайс-листы объявлений**|>|>||
||
`/feeds/settings`
|
Настройки для прайс-листов
|
[GET](https://yandex.ru/dev/autoru/doc/ru/reference/feeds-settings.md)
||
||
`/feeds/settings/cars/{section}`
|
Настройки прайс-листа для категории ТС «Легковые ТС»
|
[POST](https://yandex.ru/dev/autoru/doc/ru/reference/feeds-settings-cars-section.md)
||
||
`/feeds/tasks/cars/{section}`
|
Ручное добавление прайс-листа для категории ТС «Легковые ТС»
|
[POST](https://yandex.ru/dev/autoru/doc/ru/reference/feeds-task-cars-section.md)
||
||
`/feeds/settings/trucks/{trucks_category}/{section}`
|
Настройки прайс-листа для категории ТС «Коммерческие ТС»
|
[POST](https://yandex.ru/dev/autoru/doc/ru/reference/feeds-settings-trucks-section.md)
||
||
`/feeds/tasks/trucks/{trucks_category}/{section}`
|
Ручное добавление прайс-листа для категории ТС «Коммерческие ТС»
|
[POST](https://yandex.ru/dev/autoru/doc/ru/reference/feeds-task-cars-section.md)
||
||
`/feeds/history`
|
История загрузки прайс-листов
|
[GET](https://yandex.ru/dev/autoru/doc/ru/reference/feeds-history.md)
||
||
`/feeds/history/{task_id}`
|
Детализация по задаче на ручную загрузку прайс-листа
|
[GET](https://yandex.ru/dev/autoru/doc/ru/reference/feeds-history-taskId.md)
||

||**Личный кабинет дилера / Рассылка по избранному и статистика рассылок**|>|>||
||
`/dealer/chats/campaigns`
|
Создать рассылку
|
[POST](https://yandex.ru/dev/autoru/doc/ru/reference/dealer/chats/campaigns-post.md)
||
||
`/dealer/chats/campaigns`
|
Получить рассылку по офферу
|
[GET](https://yandex.ru/dev/autoru/doc/ru/reference/dealer/chats/campaigns-get.md)
||
||
`/dealer/chats/campaigns/list`
|
Получить список рассылок
|
[POST](https://yandex.ru/dev/autoru/doc/ru/reference/dealer/chats/campaigns/list.md)
||
||
`/dealer/chats/campaigns/list-offers`
|
Статистика по каждому офферу в групповой рассылке
|
[POST](https://yandex.ru/dev/autoru/doc/ru/reference/dealer/chats/campaigns/list-offers.md)
||
||
`/dealer/chats/campaigns/preview_campaign`
|
Предпросмотр рассылки
|
[POST](https://yandex.ru/dev/autoru/doc/ru/reference/dealer/chats/campaigns/preview.md)
||

||**Личный кабинет дилера / Финансы**|>|>||
||
`/dealer/wallet/recharges`
|
Список пополнений кошелька дилера
|
[GET](https://yandex.ru/dev/autoru/doc/ru/reference/dealer-wallet-recharges.md)
||
||
`/dealer/wallet/product/activations/daily-stats`
|
Статистика списаний с кошелька за активацию услуг
|
[GET](https://yandex.ru/dev/autoru/doc/ru/reference/dealer-wallet-product-activations-daily-stats.md)
||
||
`/dealer/wallet/product/{productName}/activations/offer-stats`
|
Статистика по активации услуги у объявлений за указанную дату
|
[GET](https://yandex.ru/dev/autoru/doc/ru/reference/dealer-wallet-product-activations-offer-stats.md)
||

||**Управление объявлениями дилера**|>|>||
||
`/user/offers/{category}`
|
Список объявлений пользователя
|
[GET](https://yandex.ru/dev/autoru/doc/ru/reference/user-offers-category.md)
||
||
`/user/offers/{category}/mark-models`
|
Список марок/моделей и количество объявлений для каждой марки/модели
|
[GET](https://yandex.ru/dev/autoru/doc/ru/reference/user-offers-category-mark-models.md)
||
||
`/user/offers/trucks/truck-categories`
|
Список категорий коммерческого транспорта и количество объявлений для каждой категории
|
[GET](https://yandex.ru/dev/autoru/doc/ru/reference/user-offers-category-truck-categories.md)
||
||
`/user/offers/moto/moto-categories`
|
Список категорий мототранспорта и количество объявлений для каждой категории
|
[GET](https://yandex.ru/dev/autoru/doc/ru/reference/user-offers-category-moto-categories.md)
||
||
`/user/offers/{category}/{offerID}`
|
Объявление пользователя
|
[DELETE](https://yandex.ru/dev/autoru/doc/ru/reference/user-offers-category-offer-id.md)
||
||
`/user/offers/{category}/{offerID}/hide`
|
Снятие объявления с продажи
|
[PUT](https://yandex.ru/dev/autoru/doc/ru/reference/user-offers-category-offer-id-hide.md)
||
||
`/user/offers/{category}/{offerID}/activate`
|
Активация объявления, снятого с продажи
|
[POST](https://yandex.ru/dev/autoru/doc/ru/reference/user-offers-category-offer-id-activate.md)
||
||
`/user/offers/{category}/{offerID}/products`
|
Услуги для объявления
|
[POST](https://yandex.ru/dev/autoru/doc/ru/reference/user-offers-category-offer-id-products.md)

[DELETE](https://yandex.ru/dev/autoru/doc/ru/reference/user-offers-category-offer-id-products-delete.md)
||
||
`/user/offers/{category}/{offerID}/stats`
|
Статистика просмотров по указанному объявлению
|
[GET](https://yandex.ru/dev/autoru/doc/ru/reference/user-offers-category-offer-id-stats.md)
||

||
**Расписания с автоматическим применением услуг**
|
>
|
>
||
||
`/billing/schedules`
|
Список всех расписаний с автоматическим применением услуг для объявлений
|
[GET](https://yandex.ru/dev/autoru/doc/ru/reference/billing-schedules.md)
||
||
`/billing/schedules/{category}/{offerId}/{product}`
|
Расписание с автоматическим применением услуги для объявления
|
[PUT](https://yandex.ru/dev/autoru/doc/ru/reference/put-billing-schedules.md)

[DELETE](https://yandex.ru/dev/autoru/doc/ru/reference/delete-billing-schedules.md)
||

||
**API Сплита**
|
>
|
>
||
||
`/split/order`
|
Создание заказа
|
[PUT](https://yandex.ru/dev/autoru/doc/ru/reference/split-order-create.md)
||
||
`/Callback-URL`
|
Нотификации об изменении статуса заказа
|
[POST](https://yandex.ru/dev/autoru/doc/ru/reference/split-changes-order-status-notifications.md)
||
||
`/split/order/refund`
|
Возврат заказа
|
[POST](https://yandex.ru/dev/autoru/doc/ru/reference/split-order-refund.md)
||
||
`/split/orders/list`
|
Список заказов
|
[POST](https://yandex.ru/dev/autoru/doc/ru/reference/split-orders-list.md)
||

||
**Чаты**
|
>
|
>
||
||
`/aggregators/auto/hook`
|
Сообщение оператора из внешней системы пользователю Авто.ру.
|
[POST](https://yandex.ru/dev/autoru/doc/ru/reference/chats/basic/chats-user-message.md)
||
||
Задается интегратором API
|
Сообщение пользователя Авто.ру на сервер внешней системы.
|
[POST](https://yandex.ru/dev/autoru/doc/ru/reference/chats/basic/chats-operator-message.md)
||
||
`/chat/room/light`
|
Список чат-румов.
|
[GET](https://yandex.ru/dev/autoru/doc/ru/reference/chats/additional/room-light.md)
||
||
`/chat/room/by-id`
|
Обогащенный список чат-румов по ID.
|
[GET](https://yandex.ru/dev/autoru/doc/ru/reference/chats/additional/room-by-id.md)
||
||
`/chat/message`
|
Получить сообщения чат-рума.
|
[GET](https://yandex.ru/dev/autoru/doc/ru/reference/chats/additional/get-message.md)
||
||
`/chat/message`
|
Oтправить сообщения чат-рума.
|
[POST](https://yandex.ru/dev/autoru/doc/ru/reference/chats/additional/post-message.md)
||
||
`/chat/message/unread`
|
Непрочитанные сообщения.
|
[GET](https://yandex.ru/dev/autoru/doc/ru/reference/chats/additional/unread.md)
||
||
`/chat/message/unread`
|
Отметить чат-рум как прочитанный.
|
[DELETE](https://yandex.ru/dev/autoru/doc/ru/reference/chats/additional/mark-room-messages-read.md)
||
|#


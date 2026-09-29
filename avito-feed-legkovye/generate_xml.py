"""Тот же фид, что generate_feed.py, но в XML (Avito Autoload XML) — запасной формат."""
import json, glob
from xml.sax.saxutils import escape
import generate_feed as g

TAGS = {'Уникальный идентификатор объявления': 'Id', 'Контактное лицо': 'ManagerName', 'Номер телефона': 'ContactPhone',
 'Адрес': 'Address', 'Способ связи': 'ContactMethod', 'Тип автомобиля': 'CarType', 'Статус наличия': 'Availability',
 'Категория': 'Category', 'Описание объявления': 'Description', 'Цена': 'Price', 'Цвет': 'Color', 'Марка': 'Make',
 'Модель': 'Model', 'Поколение': 'Generation', 'Модификация': 'Modification', 'Комплектация': 'Complectation',
 'Тип двигателя': 'FuelType', 'Коробка передач': 'Transmission', 'Объём двигателя': 'EngineSize',
 'Год выпуска': 'Year', 'Количество дверей': 'Doors', 'Тип кузова': 'BodyType', 'Привод': 'DriveType',
 'Мощность': 'Power', 'Руль': 'WheelType', 'Управление климатом': 'ClimateControl', 'Салон': 'Interior',
 'Цвет салона': 'InteriorColor', 'VIN или номер кузова': 'VIN', 'Фары': 'Lights'}
MULTI = {'Управление климатом (дополнительные опции)': 'ClimateControlOptions', 'Салон (дополнительные опции)': 'InteriorOptions',
 'Обогрев': 'Heating', 'Электропривод': 'ElectricDrive', 'Память настроек': 'MemorySettings',
 'Помощь при вождении': 'DrivingAssistance', 'Мультимедиа и навигация': 'Multimedia'}

out = ['<?xml version="1.0" encoding="UTF-8"?>', '<Ads formatVersion="3" target="Avito.ru">']
for path in sorted(glob.glob("data/*.json")):
    rec = json.load(open(path, encoding="utf-8"))
    if rec.get("status") != "active":
        continue
    row = dict(zip(g.HEADERS, g.build_row(rec)))
    out.append('<Ad>')
    for lab, tag in TAGS.items():
        v = str(row.get(lab, "")).strip()
        if v:
            out.append(f'<{tag}>{escape(v)}</{tag}>')
    for lab, tag in MULTI.items():
        v = [x.strip() for x in str(row.get(lab, "")).split(",") if x.strip()]
        if v:
            out.append(f'<{tag}>' + ''.join(f'<Option>{escape(x)}</Option>' for x in v) + f'</{tag}>')
    out.append('<Images>' + ''.join(f'<Image url="{escape(u)}"/>' for u in row['Ссылки на фото'].split(" | ") if u) + '</Images>')
    out.append('</Ad>')
out.append('</Ads>')
open("fleet-legkovye.xml", "w", encoding="utf-8").write("\n".join(out))
print("ok", len(out))

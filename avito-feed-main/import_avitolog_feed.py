"""Разовый импорт фида авитолога (аккаунт ООО БелКар, снимок 14.09.2026) в data/<id>.json + photos/<id>/.

Что исправляется относительно фида авитолога:
- Цена = прайс завода (колонка CurrencyPrice), а не прайс −10% у всех подряд.
- Скидки по письму Тонара Исх. №283 от 31.08.2026: бортовые/шторные −10%, контейнеровозы/лесовозы −5%,
  остальные без скидки; субсидия Минпромторга на лизинг 10%, не более 500 000 ₽ — только Тонар.
- Из описания убран блок «ПОДАРОК при покупке до 30 СЕНТЯБРЯ» (акция истекла), добавлен расчёт цены.
- Фото переносятся к себе (хранилище авитолога beget.cloud может пропасть).
"""
import json, os, re, shutil, subprocess, sys
import openpyxl

HERE = os.path.dirname(os.path.abspath(__file__))
SNAPSHOT = os.path.join(HERE, "reference", "avitolog_feed_2026-09-14_snapshot.xlsx")
CATALOG = os.path.join(HERE, "..", "reference", "catalog-photos")

# Служебные колонки авитолога и статусы Авито — в фид не идут
DROP = {"AvitoStatus", "AvitoDateEnd", "СТАТУС", "БАЗА", "Заметка", "Форматированные характеристики с сайта",
        "AdStatus", "DateBegin", "DateEnd", "ListingFee"}

# Не переносим: снято авитологом / дубль с неверными характеристиками
SKIP = {
    "gls-6": "Тонар 9598 — у авитолога «Снято с публикации», причина неизвестна",
    "gls-2": "Тонар T4-16V — дубль 8150616785, у этой строки длина 13 600 мм (это не 16-метровый прицеп)",
    # Артём 10-02: сомнительные строки авитолога пока не публиковать
    "gls-10": "контейнеровоз «99884», а модель в фиде 99883",
    "gls-8": "птицевоз: в заголовке 98885, модель 98883",
    "c_45": "МАЗ 544028: в заголовке 2024, в поле года 2025",
    "p_14": "МАЗ 975800-2012: фото только на avito.ru, своей копии нет",
}

# Строки, где фото у авитолога на avito.ru (отдаёт 429) — берём копии из catalog-photos
CATALOG_PHOTOS = {
    "gls-17": ("tonar/Шторно-бортовой_T3-13 _9888_", None),
    "novaia_8": ("tonar/Шторно-бортовой_T4-13V _97883_", None),
    "novaia_13": ("tonar/Самосвальный_SH4-38 _95234_", None),
    "novaia_1": ("tonar/Бортовой_B3-16 _98881_", None),
    "novaia_4": ("tonar/Бортовой_B4-13V _97883_", None),
    "gls-9": ("tonar/Контейнеровоз_K4-U _99891_", None),
    "novaia_33": ("tonar/Изотермический_R3-13D _97861_", None),
}

# Отчёт 608758251 (02.10): с новыми Id эти 28 заблокированы как повтор своих же архивных объявлений
# («Товар уже продаётся» / «Повторное размещение») — возвращаем старые Id+AvitoId, Авито активирует архивное.
KEEP_OLD_ID = {",ekrfh0550", "8118231548", "8118350682", "8118786818", "8118826997", "8150616785", "V9B8DU2N22",
               "ad-57304", "ad-57373", "b_63", "clone-130472-1788640746", "gls-1", "gls-11", "gls-12", "gls-3",
               "gls-4", "gls-5", "novaia_11", "novaia_13", "novaia_14", "novaia_15", "novaia_19", "novaia_27",
               "novaia_28", "novaia_31", "novaia_32", "novaia_33", "novaia_8"}

DISPLAY_ALL_RF = "Москва и Московская область | Санкт-Петербург и Ленинградская область | Крым | Алтайский край | Амурская область | Архангельская область | Астраханская область | Белгородская область | Брянская область | Бурятия | Владимирская область | Волгоградская область | Вологодская область | Воронежская область | Еврейская АО | Ивановская область | Ингушетия | Иркутская область | Кабардино-Балкария | Калининградская область | Калмыкия | Калужская область | Камчатский край | Карачаево-Черкесия | Кемеровская область | Кировская область | Костромская область | Краснодарский край | Красноярский край | Курганская область | Курская область | Липецкая область | Магаданская область | Мурманская область | Ненецкий АО | Нижегородская область | Новгородская область | Новосибирская область | Омская область | Оренбургская область | Орловская область | Пензенская область | Пермский край | Приморский край | Псковская область | Адыгея | Башкортостан | Дагестан | Карелия | Коми | Марий Эл | Мордовия | Саха (Якутия) | Северная Осетия | Татарстан | Тыва | Хакасия | Ростовская область | Рязанская область | Самарская область | Саратовская область | Сахалинская область | Свердловская область | Смоленская область | Ставропольский край | Тамбовская область | Тверская область | Томская область | Тульская область | Тюменская область | Удмуртия | Ульяновская область | Хабаровский край | Ханты-Мансийский АО | Челябинская область | Чеченская Республика | Забайкальский край | Чувашия | Чукотский АО | Ямало-Ненецкий АО | Ярославская область | Республика Алтай"

CONTACT_DEFAULTS = {"ContactPhone": "79031369484", "ManagerName": "Иван", "EMail": "info@bel-car.com",
                    "CompanyName": "ООО БелКар"}

DISCOUNT_10 = {"Бортовой", "Шторно-бортовой", "Шторный"}
DISCOUNT_5 = {"Контейнеровоз", "Лесовоз (сортиментовоз)", "Лесовоз"}


def new_id(f, used):
    """Новый Id: bk-<марка>-<модель>, при совпадении модели — плюс длина или порядковый номер."""
    tr = {"Тонар": "tonar", "МАЗ": "maz", "ИнтерПрицеп": "interpricep"}
    base = "bk-" + tr.get(f.get("Make"), "x") + "-" + re.sub(r"[^a-z0-9]+", "-", str(f.get("Model")).lower()).strip("-")
    cand = base
    if cand in used and f.get("TrailerLength"):
        cand = f"{base}-{f['TrailerLength']}"
    n = 2
    while cand in used:
        cand = f"{base}-{n}"
        n += 1
    used.add(cand)
    return cand


def _num(pattern, text):
    m = re.search(pattern + r"[^:\n]*:\s*(?:</strong>)?\s*(\d[\d ]{2,})", text)
    return int(m.group(1).replace(" ", "")) if m else None


def payload_from_text(desc):
    """Грузоподъёмность по тексту: явное значение, иначе полная масса − снаряжённая."""
    explicit = _num(r"(?:Грузоподъ[её]мность|Масса перевозимого груза|Допустимая масса перевозимого груза)", desc)
    if explicit:
        return explicit
    full = _num(r"(?:Разреш[её]нная максимальная масса|Технически допустимая (?:максимальная )?масса|Максимальная масса прицепа)", desc)
    curb = _num(r"Масса снаряж[её]нного", desc)
    if full and curb and full > curb:
        return full - curb
    return None


def rub(n):
    return f"{n:,}".replace(",", " ") + " ₽"


def price_block(make, trailer_type, price):
    dealer = 0
    pct = 0
    if make == "Тонар":
        pct = 10 if trailer_type in DISCOUNT_10 else 5 if trailer_type in DISCOUNT_5 else 0
        dealer = price * pct // 100
    lease = min(price // 10, 500_000) if make == "Тонар" else 0
    lines = [f"• <strong>Цена по прайсу завода</strong>: {rub(price)}"]
    if dealer:
        lines.append(f"• <strong>Скидка от производителя {pct}%</strong>: −{rub(dealer)}")
    if lease:
        lines.append(f"• <strong>При покупке в лизинг — субсидия Минпромторга</strong> (10%, не более 500 000 ₽): −{rub(lease)}")
        lines.append(f"• <strong>Итоговая цена при лизинге</strong>: {rub(price - dealer - lease)}")
    elif dealer:
        lines.append(f"• <strong>Итоговая цена</strong>: {rub(price - dealer)}")
    return dealer, lease, "\n".join(lines)


def clean_description(desc, block):
    # акция «ПОДАРОК … до 30 СЕНТЯБРЯ» стоит между двумя строками из «=»
    desc = re.sub(r"\n*={5,}\n.*?\n={5,}\n*", "\n\n", desc, flags=re.S)
    if "ПОДАРОК" in desc:
        raise SystemExit("не удалось вырезать блок с подарком")
    # Артём 10-02: цен и скидок в тексте не писать — только в полях фида, иначе менять в двух местах
    desc = re.sub(r"\n?• <strong>Цена</strong>: с НДС", "", desc)
    if re.search(r"\d[\d ]{4,}\s*(₽|руб)", desc):
        raise SystemExit("в описании осталась цена")
    return desc


def fetch(url, dest):
    for _ in range(3):
        r = subprocess.run(["curl", "-sfL", "--max-time", "60", "-o", dest, url])
        if r.returncode == 0 and os.path.getsize(dest) > 1000:
            return
    raise SystemExit(f"не скачалось: {url}")


def main():
    ws = openpyxl.load_workbook(SNAPSHOT).active
    rows = list(ws.iter_rows(values_only=True))
    hdr = rows[0]
    used_ids = set()
    shutil.rmtree(os.path.join(HERE, "data"), ignore_errors=True)
    os.makedirs(os.path.join(HERE, "data"), exist_ok=True)
    for r in rows[1:]:
        f = {h: v for h, v in zip(hdr, r) if h and h not in DROP and v not in (None, "")}
        rid = str(f["Id"]); f["Id"] = rid
        if rid in SKIP:
            print(f"пропуск {rid}: {SKIP[rid]}")
            continue
        slug = re.sub(r"[^A-Za-z0-9_-]", "_", rid).strip("_")
        # у трёх строк ИнтерПрицепа контакты пустые — пустой телефон Авито подменяет дефолтным (см. B-trailer 09-24)
        for k, v in CONTACT_DEFAULTS.items():
            f.setdefault(k, v)
        price = int(f["CurrencyPrice"])
        dealer, lease, block = price_block(f.get("Make"), f.get("TypeOfTrailer"), price)
        f["Price"] = price
        f["CurrencyPrice"] = price
        # Артём 10-02: цены без НДС, подарков нет, объявления новые (без привязки к старым AvitoId)
        f["PriceWithVAT"] = "Нет"
        f.pop("Gifts", None)
        if rid in KEEP_OLD_ID:
            used_ids.add(rid)
        else:
            f.pop("AvitoId", None)
            f["Id"] = new_id(f, used_ids)
        f.pop("DealerDiscount", None)
        f.pop("LeasingDiscount", None)
        if dealer:
            f["DealerDiscount"] = dealer
        if lease:
            f["LeasingDiscount"] = lease
        if "Description" in f:
            f["Description"] = clean_description(f["Description"], block)
            # Артём 10-03: гарантию не указываем — ни в полях, ни в тексте
            f.pop("OfficialGuarantee", None)
            f.pop("AdditionalGuarantee", None)
            f["Description"] = re.sub(r"\n[^\n]*\bГарантия\b[^\n]*", "", f["Description"])
            # Артём 10-03: вся техника под заказ — никакого «в наличии» в тексте
            for a, b in (("В наличии и под заказ", "Под заказ"),
                         ("• <strong>Наличие</strong>: \n", "• <strong>Наличие</strong>: Под заказ\n"),
                         ("наличие, комплектация и ", "комплектация и "), ("комплектация, наличие и ", "комплектация и "),
                         ("по наличию, комплектации", "по комплектации")):
                f["Description"] = f["Description"].replace(a, b)
            if re.search(r"(?i)в наличии|по наличию", f["Description"]):
                raise SystemExit(f"{rid}: в тексте осталось «в наличии»")
            # Артём 10-03: показ по всей РФ, ПТС «В наличии» у всех, объём 95941 b_63 — 48 м³ (в тексте «41 / 48»)
            f["DisplayAreas"] = DISPLAY_ALL_RF
            f["TechnicalPassport"] = "В наличии"
            if rid == "b_63":
                f["TrailerVolume"] = 48
            # Артём 10-02: оси — у 95941 (b_63) верен текст (4), у K4-40 (novaia_28) верно поле (4)
            if rid == "b_63":
                f["Axles"] = 4
            if rid == "novaia_28":
                f["Description"] = f["Description"].replace("Количество осей:</strong> 3,", "Количество осей:</strong> 4,")
            # Авитолог у многих вписал в «Грузоподъёмность» (GrossVehicleWeight) полную массу прицепа
            pl = payload_from_text(f["Description"])
            if pl and abs(int(f.get("GrossVehicleWeight") or 0) - pl) > 1000:
                print(f"  {rid}: грузоподъёмность {f.get('GrossVehicleWeight')} → {pl}")
                f["GrossVehicleWeight"] = pl

        urls = [u.strip() for u in f.pop("ImageUrls").split("|") if u.strip()]
        pdir = os.path.join(HERE, "photos", slug)
        os.makedirs(pdir, exist_ok=True)
        photos, external = [], []
        if rid in CATALOG_PHOTOS:
            src = os.path.join(CATALOG, CATALOG_PHOTOS[rid][0])
            for i, name in enumerate(sorted(os.listdir(src)), 1):
                ext = os.path.splitext(name)[1].lower()
                dst = f"{i:02d}{ext}"
                shutil.copy(os.path.join(src, name), os.path.join(pdir, dst))
                photos.append(f"photos/{slug}/{dst}")
        elif all("beget.cloud" in u for u in urls):
            for i, u in enumerate(urls, 1):
                dst = f"{i:02d}" + os.path.splitext(u)[1].lower()
                if not os.path.exists(os.path.join(pdir, dst)):
                    fetch(u, os.path.join(pdir, dst))
                photos.append(f"photos/{slug}/{dst}")
        else:
            external = urls  # фото только на avito.ru и копии нет — оставляем ссылки Авито как есть
            os.rmdir(pdir)
        # Артём 10-02: МАЗы скрыть (в фид не идут, Авито уберёт их в архив)
        rec = {"id": f["Id"], "old_id": rid, "status": "hidden" if f.get("Make") == "МАЗ" else "active", "fields": f, "photos": photos, "external_photo_urls": external}
        with open(os.path.join(HERE, "data", f"{slug}.json"), "w", encoding="utf-8") as fh:
            json.dump(rec, fh, ensure_ascii=False, indent=1)
        print(f"{rid:28} {price:>9} dealer={dealer:>7} lease={lease:>7} photos={len(photos) or len(external)}{' (avito.ru)' if external else ''}")


if __name__ == "__main__":
    main()

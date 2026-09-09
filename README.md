# Restoration B2B landing

Статический многостраничный сайт для услуги восстановления рекламационной сантехнической керамики.

## Структура

- `index.html` — главная страница.
- `restavratsiya-*.html`, `vosstanovlenie-*.html`, `stoimost-*.html` — страницы услуг.
- Страницы с вопросительными заголовками и узкими URL — подробные ответы для клиентов и поисковых систем.
- `assets/css/styles.css` — стили и адаптивность.
- `assets/js/main.js` — мобильное меню и просмотр изображений.
- `assets/images` — оптимизированные WebP-фотографии.
- `sitemap.xml`, `robots.txt`, `llms.txt`, `llms-full.txt` — файлы поискового и машинного обнаружения.
- `restavratsiya-rakoviny-spb.html`, `restavratsiya-unitaza-spb.html`, `remont-skolov-vanny-spb.html` — услуги по типу изделия.
- `specs/service-search-queries.md` — карта запросов и ограничения замера видимости.
- `scripts/validate_site.py` — проверка sitemap, HTML-метаданных, ссылок, ресурсов и JSON-LD: `python3 scripts/validate_site.py`.

## Локальный запуск

Сайт статический. Можно открыть `index.html` в браузере или запустить локальный сервер:

```bash
python3 -m http.server 8080
```

После запуска сайт будет доступен по адресу `http://localhost:8080`.

## Публикация на GitHub Pages

1. Создайте публичный репозиторий на GitHub.
2. Загрузите в него файлы проекта из корня этой папки.
3. В настройках репозитория откройте `Pages`.
4. Выберите источник `Deploy from a branch`.
5. Укажите ветку `main` и папку `/root`.
6. После сохранения GitHub выдаст публичную ссылку вида `https://username.github.io/repository-name/`.

## Обновление контента

- Тексты редактируются в `index.html`.
- Фото заменяются в `assets/images`; имена файлов лучше сохранять прежними, чтобы не менять разметку.
- Контакты в финальном блоке находятся в секции `#contacts` в `index.html`.

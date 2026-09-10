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
- `kak-sfotografirovat-skol-santehniki.html` — фотографии для предварительной оценки.
- `kontakty-i-usloviya.html` — контакты, единичные изделия, условия и границы работ.
- `specs/service-search-queries.md` — карта запросов и ограничения замера видимости.
- `scripts/validate_site.py` — проверка sitemap, HTML-метаданных, ссылок, ресурсов и JSON-LD: `python3 scripts/validate_site.py`.

## Локальный запуск

Сайт статический. Можно открыть `index.html` в браузере или запустить локальный сервер:

```bash
python3 -m http.server 8080
```

После запуска сайт будет доступен по адресу `http://localhost:8080`.

## Публикация на GitHub Pages

Действующий сайт: https://restb2b.fun/. Репозиторий: `korotundenis05-code/restoration-b2b-landing`.

Источник в Settings → Pages: GitHub Actions. Обновление ветки `main` запускает `.github/workflows/deploy-pages.yml`: сначала проверяются страницы и тесты, затем публикуется сайт. Не включайте одновременно публикацию из ветки. Сохраняйте `CNAME`, `.nojekyll`, файлы подтверждения Google/Яндекса и ключ IndexNow.

Перед обновлением выполните `python3 -m unittest discover -s tests -v`. После успешного развёртывания выполните `python3 scripts/verify_live.py`: проверка сравнивает обычные публичные URL с локальными файлами без подмены адреса параметрами сброса кеша.

## Обновление контента

- Тексты редактируются в соответствующих HTML-страницах. При изменении FAQ синхронно обновляйте видимый ответ и `FAQPage` в JSON-LD; тесты проверяют их совпадение.
- При добавлении страницы укажите уникальные title, description и canonical, добавьте внутренние ссылки и запись в `sitemap.xml`. Дату обновления меняйте только при реальном изменении страницы.
- Фото заменяются в `assets/images`; имена файлов лучше сохранять прежними, чтобы не менять разметку.
- Контакты в финальном блоке находятся в секции `#contacts` в `index.html`.

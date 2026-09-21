# Доказательства: русский интерфейс сайта

| Требование | Реализация | Проверка | Статус |
| --- | --- | --- | --- |
| R1 | Человекочитаемые название и тексты во всех публичных HTML заменены на русские формулировки | `test_public_client_text_has_no_unnecessary_latin_words` | PASS |
| R2 | Термины о работе с компаниями переведены по смыслу; домен, ссылки и технические ключи не затрагивались | Поиск по публичным HTML и `validate_site.py` | PASS |
| R3 | Видимая подпись «FAQ» заменена на «Вопросы и ответы» при сохранении `#faq` | `test_navigation_uses_russian_faq_label_without_changing_its_anchor` | PASS |
| R4 | `llms.txt` и `llms-full.txt` используют русское название и формулировки | `test_llm_summaries_use_the_russian_service_name` | PASS |
| R5 | Добавлен тест против латинских слов и неудачных механических замен | 37 тестов, 1 пропуск только для локальных исходных фото | PASS |

## Выполненные команды

- `python3 -m unittest discover -s tests -v` — PASS, 37 тестов, 1 пропуск.
- `python3 scripts/validate_site.py` — PASS, 18 канонических страниц.
- `git diff --check` — PASS.
- Независимый поиск латиницы в видимом тексте всех публичных страниц — без результатов.

## Публикация

- Коммит: `27221d7 Translate customer-facing copy to Russian`.
- GitHub Pages: успешно, [запуск 35524332750](https://github.com/korotundenis05-code/restoration-b2b-landing/actions/runs/35524332750).
- Боевая страница `https://restb2b.fun/` открыта после публикации: заголовок вкладки, клиентские тексты и раздел «Вопросы и ответы» отображаются на русском.

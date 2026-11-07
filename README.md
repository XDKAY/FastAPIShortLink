# FastAPIShortLink

# Стэк
Python, FastAPI, SQLAlchemy, aiosqlite, SQLite

# Эндпоинты

## Получение короткой ссылки
`/api/short_link`

**Входные данные**
```json
{
  url: "https://example.com"
}
```

**Выходые данные**
```json
{
  "url": "http://localhost:8000/{token}",
  "data": {
    id: ...,
    token: ...,
    long_url: ...,
    exp_date: ...,
    is_active: ...,
  }
}
```

## Редирект

`/{short_link}`

По токену короткой ссылки, достает длинную ссылку из базы данных.
Редиректим пользователя на нужную страницу.


# Запуск приложения
1. `git clone git@github.com:XDKAY/FastAPIShortLink.git`
2. `cd FastAPIShortLink`
3. `uv venv`
4. `source .venv/bin/activate`
5. `uv sync`
6. `uvicorn main:app --reload`

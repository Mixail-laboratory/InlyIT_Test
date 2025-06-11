# Advertisement Service API

## Описание
Сервис для размещения объявлений с возможностью комментирования. Реализован на FastAPI с использованием асинхронного подхода и PostgreSQL в качестве базы данных.

## Возможности

### Для всех пользователей:
- Просмотр списка объявлений
- Детальный просмотр объявлений
- Просмотр комментариев к объявлениям

### Для авторизованных пользователей:
- Размещение объявлений
- Удаление своих объявлений
- Добавление комментариев к объявлениям
- Удаление своих комментариев

### Для администраторов:
- Назначение пользователей администраторами
- Удаление любых комментариев
- Удаление любых объявлений
- Блокировка пользователей

## Технологический стек
- Python 3.8+
- FastAPI
- SQLAlchemy (асинхронный режим)
- PostgreSQL
- JWT аутентификация
- Pydantic для валидации данных

## Установка и запуск

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/your/repo.git
   cd advertisement-service
Установите зависимости:

```bash
pip install -r requirements.txt
```
Настройте переменные окружения (создайте файл .env):
```
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
DB_NAME=ad_service
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Запустите сервер в виртуальной среде:

```
python main.py
```
## API Endpoints

### Аутентификация
````
POST /auth/register - Регистрация пользователя

POST /auth/login - Вход в систему
````

### Объявления
````
GET /ads - Получить список объявлений
POST /ads - Создать объявление (требуется авторизация)
GET /ads/{ad_id} - Получить детали объявления
DELETE /ads/{ad_id} - Удалить объявление (требуется авторизация)
````

### Комментарии

````
POST /ads/{ad_id}/comments - Добавить комментарий (требуется авторизация)
GET /ads/{ad_id}/comments - Получить комментарии к объявлению
````

### Администраторские функции

````
PATCH /admin/users/{user_id}/promote - Назначить администратором
DELETE /admin/comments/{comment_id} - Удалить любой комментарий
DELETE /admin/ads/{ad_id} - Удалить любое объявление

````

## Примеры запросов

### Регистрация пользователя
````
curl -X POST "http://localhost:8000/auth/register" \
-H "Content-Type: application/json" \
-d '{"email":"user@example.com","username":"testuser","password":"secret123"}'
````
### Создание объявления

````
curl -X POST "http://localhost:8000/ads" \
-H "Authorization: Bearer {token}" \
-H "Content-Type: application/json" \
-d '{"title":"Продам телефон","description":"Новый в коробке","type":"sell"}'
````

### Добавление комментария

````
curl -X POST "http://localhost:8000/ads/1/comments" \
-H "Authorization: Bearer {token}" \
-H "Content-Type: application/json" \
-d '{"text":"Отличное объявление!"}'
````

## Документация API
После запуска сервера доступны:

Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

## Миграции базы данных
Для управления миграциями используется Alembic:
````
alembic revision --autogenerate -m "init"
alembic upgrade head
````

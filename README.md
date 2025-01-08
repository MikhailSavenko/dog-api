## README.md

# API для управления информацией о собаках и породах

Этот проект представляет собой REST API, разработанный на Django и Django REST Framework, для управления информацией о собаках и их породах. Проект контейнеризирован с помощью Docker и использует PostgreSQL в качестве базы данных.

## Содержание

  * [Описание](https://www.google.com/url?sa=E&source=gmail&q=#описание)
  * [Технологии](https://www.google.com/url?sa=E&source=gmail&q=#технологии)
  * [Установка](https://www.google.com/url?sa=E&source=gmail&q=#установка)
  * [Запуск](https://www.google.com/url?sa=E&source=gmail&q=#запуск)
  * [Использование API](https://www.google.com/url?sa=E&source=gmail&q=#использование-api)
  * [Модели данных](https://www.google.com/url?sa=E&source=gmail&q=#модели-данных)
  * [Оптимизация запросов](https://www.google.com/url?sa=E&source=gmail&q=#оптимизация-запросов)


## Описание

API предоставляет возможность создавать, получать, обновлять и удалять информацию о собаках и породах. Реализованы эндпоинты для получения списков, отдельных объектов и выполнения операций CRUD (Create, Read, Update, Delete). Особое внимание уделено оптимизации запросов к базе данных с использованием подзапросов и `OuterRef` для избежания N+1 проблемы.

## Технологии

  * Python 3.12.3
  * Django 5.1.4
  * Django REST Framework 3.15.2
  * PostgreSQL
  * Docker
  * Docker Compose
  * Git

## Установка

1.  Клонируйте репозиторий:

    ```bash
    git clone git@github.com:MikhailSavenko/dog-api.git
    ```

2.  Создайте файл `.env` на основе `env.example` и заполните необходимые переменные окружения (подробнее в разделе [Переменные окружения](https://www.google.com/url?sa=E&source=gmail&q=#переменные-окружения)):

    ```bash
    cp env.example .env
    ```

3.  Соберите и запустите Docker-контейнеры:

    ```bash
    docker-compose up 
    ```
**Важно:** Процесс создания и применения миграций базы данных, наполнение базы данных начальными данными и запуск приложения gunicorn полностью автоматизированы с помощью скрипта `start.sh`, который запускается при старте Docker-контейнера. Вам не нужно выполнять никаких дополнительных команд вручную.

## Запуск

После запуска контейнеров проект будет доступен по адресу `http://localhost:8000`.

## Использование API

### Эндпоинты для собак (`/api/dogs/`)

  * `GET /api/dogs/`: Получение списка всех собак с информацией о среднем возрасте собак каждой породы.
  * `POST /api/dogs/`: Создание новой собаки.
  * `GET /api/dogs/<id>`: Получение информации о конкретной собаке с указанием количества собак той же породы.
  * `PUT /api/dogs/<id>`: Обновление информации о собаке.
  * `DELETE /api/dogs/<id>`: Удаление собаки.

### Эндпоинты для пород (`/api/breeds/`)

  * `GET /api/breeds/`: Получение списка всех пород с указанием количества собак каждой породы.
  * `POST /api/breeds/`: Создание новой породы.
  * `GET /api/breeds/<id>`: Получение информации о конкретной породе.
  * `PUT /api/breeds/<id>`: Обновление информации о породе.
  * `DELETE /api/breeds/<id>`: Удаление породы.

### Примеры запросов (используя `curl`):

**Примеры для модели `Dog`:**

*   **Получение списка всех собак (GET /api/dogs/):**

    ```bash
    curl http://localhost:8000/api/dogs/
    ```

    Этот запрос вернет JSON-ответ со списком всех собак и информацией о среднем возрасте собак каждой породы.

*   **Получение информации о конкретной собаке (GET /api/dogs/<id>):**

    ```bash
    curl http://localhost:8000/api/dogs/1/ # Замените 1 на ID нужной собаки
    ```

    Этот запрос вернет JSON-ответ с информацией о собаке с указанным ID и количеством собак той же породы.

*   **Создание новой собаки (POST /api/dogs/):**

    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{
        "name": "Buddy",
        "age": 3,
        "breed": 1,
        "gender": "Male",
        "color": "Brown",
        "favorite_food": "Meat",
        "favorite_toy": "Ball"
    }' http://localhost:8000/api/dogs/
    ```

    Убедитесь, что ID породы (`breed`) существует в базе данных.

*   **Обновление информации о собаке (PUT /api/dogs/<id>):**

    ```bash
    curl -X PUT -H "Content-Type: application/json" -d '{
        "name": "Buddy Updated",
        "age": 4
    }' http://localhost:8000/api/dogs/1/ # Замените 1 на ID нужной собаки
    ```

    Этот запрос обновит имя и возраст собаки с ID 1.

*   **Удаление собаки (DELETE /api/dogs/<id>):**

    ```bash
    curl -X DELETE http://localhost:8000/api/dogs/1/ # Замените 1 на ID нужной собаки
    ```

    Этот запрос удалит собаку с ID 1.

**Примеры для модели `Breed`:**

*   **Получение списка всех пород (GET /api/breeds/):**

    ```bash
    curl http://localhost:8000/api/breeds/
    ```

    Этот запрос вернет JSON-ответ со списком всех пород и количеством собак каждой породы.

*   **Получение информации о конкретной породе (GET /api/breeds/<id>):**

    ```bash
    curl http://localhost:8000/api/breeds/1/ # Замените 1 на ID нужной породы
    ```

    Этот запрос вернет JSON-ответ с информацией о породе с указанным ID.

*   **Создание новой породы (POST /api/breeds/):**

    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{
        "name": "Golden Retriever",
        "size": "Medium",
        "friendliness": 5,
        "trainability": 4,
        "shedding_amount": 3,
        "exercise_needs": 4
    }' http://localhost:8000/api/breeds/
    ```

*   **Обновление информации о породе (PUT /api/breeds/<id>):**

    ```bash
    curl -X PUT -H "Content-Type: application/json" -d '{
        "trainability": 5
    }' http://localhost:8000/api/breeds/1/ # Замените 1 на ID нужной породы
    ```

    Этот запрос обновит уровень обучаемости породы с ID 1.

*   **Удаление породы (DELETE /api/breeds/<id>):**

    ```bash
    curl -X DELETE http://localhost:8000/api/breeds/1/ # Замените 1 на ID нужной породы
    ```

    Этот запрос удалит породу с ID 1.

**Примеры обработки ошибок:**

*   **Запрос несуществующего объекта (GET /api/dogs/<несуществующий_id>):**

    ```bash
    curl http://localhost:8000/api/dogs/999/ # Предположим, ID 999 не существует
    ```

    Ожидается ответ со статусом `404 Not Found`.

*   **Некорректные данные при создании (POST /api/dogs/):**

    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{
        "name": "", # Пустое имя
        "age": "abc" # Некорректный тип данных
    }' http://localhost:8000/api/dogs/
    ```

    Ожидается ответ со статусом `400 Bad Request` и сообщением об ошибке валидации.

## Модели данных

### Модель `Dog`

  * `name`: Строка
  * `age`: Целое число
  * `breed`: Внешний ключ к модели `Breed`
  * `gender`: Строка
  * `color`: Строка
  * `favorite_food`: Строка
  * `favorite_toy`: Строка

### Модель `Breed`

  * `name`: Строка
  * `size`: Строка (ограниченные значения: Tiny, Small, Medium, Large)
  * `friendliness`: Целое число (от 1 до 5)
  * `trainability`: Целое число (от 1 до 5)
  * `shedding_amount`: Целое число (от 1 до 5)
  * `exercise_needs`: Целое число (от 1 до 5)

## Оптимизация запросов

Для оптимизации запросов используются подзапросы и `OuterRef` в Django ORM, что позволяет избежать N+1 проблемы и значительно улучшить производительность.

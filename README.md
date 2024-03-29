# Сервис хранения файлов

## Описание

Данный сервис позволяет хранить файлы и получать к ним доступ по API.

## Функционал

* **GET /v1/find**
    * Возвращает список файлов, содержащих в имени маску `%filename%` и дату загрузки `date`. Параметры не обязательные.
    * Формат ответа: `[{uid:”UID”, filename: “filename”, date: “date”}]`
* **POST /v2/upload**
    * Принимает на вход файл.
    * Сохраняет исходные данные в БД:
        * `UUID`: уникальный идентификатор
        * `FILENAME`: имя файла
        * `UPLOAD_DATE`: дата загрузки
    * Сохраняет файл на диск под именем `UUID`.
    * В ответ возвращает `UUID` файла.
* **GET /v1/download?UUID=**
    * Позволяет получить файл по `UUID`.
    * В случае отсутствия файла сервер должен отвечать соответствующим статусом HTTP.

## Запуск

1. Установите Python 3.9+.
2. Установите PostgreSQL.
3. Установите Docker.
4. Установите Git.
5. Скачайте исходники:


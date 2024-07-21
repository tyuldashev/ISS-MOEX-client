# Приложение для получения исторических котировок с информационного сервера Московской Биржи.

Содержание:
1. Архитектура приложения
2. Зависимости и установка
3. Распределение функционала в файлах проекта

## Архитектура приложения

![Архитектура](assets/readme_pics/moex_app_architecture.png)

## Зависимости и установка

1. [Python 3.11](https://www.python.org/downloads/)
2. Сторонние библиотеки в файле `requirements.txt`. В Терминале перейдите в папку вашего проекта и выполните:

   ```pip install -r requirements.txt```
  
3. [MySQL Community Server](https://dev.mysql.com/downloads/mysql/) 8.4.1 LTS или 9.0.0 Innovation
4. Для первичного создания и просмотра таблиц локальной базы данных MySQL я использую клиента [HeidiSQL](https://www.heidisql.com/download.php) или [DBeaver](https://dbeaver.io/download/).
   Создайте базу (после установки MySQL Community Server) с помощью запуска пакетного SQL запроса из файла `create_mysql_db.sql`и проверьте ее с помощью любого клиента по вашему вкусу.
   

# Practika
Фамилия Имя
Кузьмин Даниил
Тестовое задание Python
Реализовать сервис, который принимает и отвечает на НТТР запросы, задание №2
Описание проекта
Проект использует функционал веб-фреймворка Django и набора инструментов Django REST framework для предоставления пользователю возможности обрабатывать GET и POST запросы
Подготовительные действия (установки, настройки и т.д) для успешной работы проекта
Установить СУБД PostgreSQL версии 16.0 и выше
Создать базу данных с предложенными в пункте "Информация о доступах" (или задать своё по желанию)
Настроить привелегии доступа для ранее созданных пользователя и базы данных
Установить интерпретатор Python версии 3.12 и выше
Информация о доступах (логины/пароли и т.д.)
По молчанию используются: логин и пароль администратора в PostgreSQLу
По умолчанию используется название базы данных shop для работы сервиса
Описание, как запустить ваш проект
При необходимости установить зависимости командой pip install django, pip install djangorestframework, pip install psycop2
JSON с объектом магазина для запроса на /shop/ должен иметь следующий вид:
{
    "Shop": "Название магазина",
    "City": "Название города",
    "Street": "Название улицы",
    "Building": "Номер дома",
    "Open": "00:00:00",
    "Close": "00:00:00",
    "id_City_id": "Id города",
    "id_Street_id": "Id улицы"
}

# Тестовое задание для Mindbox

Проект содержит два задания: библиотеку для вычисления площади геометрических фигур и PySpark приложение для обработки данных продуктов и категорий.

## Структура проекта

_Mindbox_TEST содержит:
- Shapes.py
- Tests.py
- Dockerfile
- PySparkMethod.py


- `Shapes.py` содержит определения классов для геометрических фигур.
- `Tests.py` содержит юнит-тесты для библиотеки геометрических фигур.
- `Dockerfile` определяет Docker образ для запуска PySpark приложения.
- `PySparkMethod.py` содержит PySpark приложение для обработки данных.

# Установка зависимостей
Для установки необходимых библиотек выполните:
```bash
pip install -r requirements.txt
```
## Запуск библиотеки для вычисления площади фигур

Для запуска тестов библиотеки выполните:

```bash
python Tests.py
```
##Запуск PySpark приложения
Для запуска PySpark приложения используйте Docker. Вам необходимо собрать образ и запустить его:

Сборка Docker образа:
```bash
docker build -t pyspark-app .
```
Запуск Docker контейнера:
```bash
docker run pyspark-app
```
Убедитесь, что у вас установлен Docker и он может обращаться к Docker Daemon.
```

Если у вас возникнут вопросы по запуску приложения, вы можете связаться со мной в Telegram https://t.me/ilya88005553535
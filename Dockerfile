# Используем образ Python с Debian Buster
FROM python:3.8-buster

# Устанавливаем Java и пайспарк
RUN apt-get update && \
    apt-get install -y openjdk-11-jre-headless && \
    apt-get clean && \
    pip install pyspark

# Копирование локальных файлов скриптов в образ
COPY PySparkMethod.py /PySparkMethod.py

# Установка переменной окружения для Java
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64

# Запуск скрипта PySpark при запуске контейнера
CMD ["spark-submit", "/PySparkMethod.py"]
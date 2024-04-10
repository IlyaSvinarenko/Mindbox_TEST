from pyspark.sql import SparkSession


def get_product_category_pairs(products_df, categories_df, product_category_links_df):
    # Соединяем продукты и связи, чтобы узнать категории каждого продукта
    product_with_categories = products_df.join(
        product_category_links_df,
        products_df.product_id == product_category_links_df.product_id,
        "left"
    ).join(
        categories_df,
        product_category_links_df.category_id == categories_df.category_id,
        "left"
    ).select(
        products_df.name.alias("product_name"),
        categories_df.name.alias("category_name")
    )

    return product_with_categories


spark = SparkSession.builder.appName("TestApp").getOrCreate()

# Создание тестовых данных и датафреймов
products_data = [(1, "Product A"), (2, "Product B"), (3, "Product C")]
categories_data = [(1, "Category 1"), (2, "Category 2")]
links_data = [(1, 1), (1, 2), (2, 1)]
# У "Product C" нет категории, в итоговом датафрейме напротив "Product C" будет None

products_df = spark.createDataFrame(products_data, ["product_id", "name"])
categories_df = spark.createDataFrame(categories_data, ["category_id", "name"])
product_category_links_df = spark.createDataFrame(links_data, ["product_id", "category_id"])


# Собственно выполнение метода, демонстрация результата и остановка работы
result_df = get_product_category_pairs(products_df, categories_df, product_category_links_df)

result_df.show()

spark.stop()

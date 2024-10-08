import logging
from pyspark.sql import SparkSession
from delta import configure_spark_with_delta_pip
from pathlib import Path


def setup_session():
    builder = SparkSession.builder.appName("Ingestão Cardio") \
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
        .config("spark.hadoop.io.nativeio.enabled", "false") \
        .config("spark.hadoop.fs.native.enabled", "false") \
        .config("spark.jars.packages", "io.delta:delta-core_2.12:2.4.0")

    return configure_spark_with_delta_pip(builder).getOrCreate()


def read_csv(spark, path=None):
    if path is None:
        path = Path("data_sources") / "cardiovascular.csv"
    else:
        path = Path(path)

    logging.info("Realizando leitura do arquivo no caminho: %s", path)

    if not path.exists():
        raise FileNotFoundError(f"O arquivo não foi encontrado no caminho especificado: {path}")

    df = spark.read.format("csv").option("header", "true").load(str(path))
    df.show(truncate=False)  # Imprime o DataFrame na tela
    return df


def rename_columns(df):
    logging.info("Renomeando colunas")
    return df.withColumnRenamed("height_(cm)", "height_cm").withColumnRenamed("Weight_(kg)", "Weight_kg")


def save_delta(df, output_path=Path("storage/hospital/rw/cardiovascular/")):
    logging.info("Armazenando dados")
    return df.write.format("delta").mode("overwrite").option("mergeSchema", "true").partitionBy("General_Health").save(str(output_path))


def main():
    spark = setup_session()
    absolute_path = "C:/Projeto_DataOps/Dataops.Pipiline/data_sources/cardiovascular.csv"
    df = read_csv(spark, absolute_path)
    df = rename_columns(df)
    save_delta(df)
    spark.stop()


if __name__ == "__main__":
    main()  # dessa vez vai

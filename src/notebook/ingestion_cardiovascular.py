# Databricks notebook source.
# MAGIC %md
# MAGIC #Ingestão de Dados ELT
# MAGIC Conjunto de dados de previsão de risco de doenças cardiovasculares

# COMMAND ------------

display(dbutils.fs)

# COMMAND ------------

display(dbutils.fs.ls("/"))

# COMMAND ------------

dbutils.fs.mkdirs("/tmp/")

# COMMAND -------------

display(dbutils.fs.ls("/"))

# COMMAND -------------

display(dbutils.fs.ls("/tmp/"))

# COMMAND -------------

# MAGIC %md
# MAGIC # Extraindo dados/Realizando a leitura

# COMMAND ------------

df = spark.read.format("csv").option("header", True).load("dbfs:/tmp/cardiovascular.csv")

# COMMAND ------------

df.display()

# COMMAND ------------

df.select("General_Health").distinct().display()

# COMMAND ------------

df.printSchema()

# COMMAND ------------

# MAGIC %md
# MAGIC # Rename Cols

# COMMAND ------------

df = df.withColumnRenamed("Height_(cm)", "Height_cm").withColumnRenamed("Weight_(kg)", "Weight_kg")

# COMMAND ------------

# MAGIC %md
# MAGIC # Realizando o armazenamento de dados

# COMMAND ------------

df.write.format("delta").mode("overwrite").option("mergeSchema", True).partitionBy("General_Health").save("/hospital/rw/suus/cardiovascular/")

# COMMAND ------------

# MAGIC %md
# MAGIC # Criando database e tabela pelo delta location

# COMMAND ------------

# MAGIC %sql
# MAGIC CREATE DATABASE IF NOT EXISTS db_hospital

# COMMAND ------------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS db_hospital.cardiovascular_diseasess LOCATION "gs://databricks-46083817904810/46083817904810/hospital/rw/suus/cardiovascular"

# COMMAND ------------

# MAGIC %md
# MAGIC # Verificando detalhes da tabela criada

# COMMAND ------------

# MAGIC %sql
# MAGIC select * from db_hospital.cardiovascular_diseasess
     
# COMMAND ------------

# MAGIC %sql
# MAGIC desc detail db_hospital.cardiovascular_diseasess
     
# COMMAND ------------

# MAGIC %sql
# MAGIC desc detail delta."gs://databricks-46083817904810/46083817904810/hospital/rw/suus/cardiovascular"

# COMMAND ------------

# MAGIC %md
# MAGIC # Analisando dados

# COMMAND ------------

df_cardio = spark.table("db_hospital.cardiovascular_diseasess")
     
# COMMAND ------------

df_cardio.count()

# COMMAND ------------

df_cardio.show(10, False)

# COMMAND ------------     

df_cardio.display()

# COMMAND ------------

# MAGIC %md
# MAGIC # Verificando classificação de saúde cardiovascular
# Pesquisa de como as pessoas classificam a sua saúde do coração

# COMMAND ------------

df_cardio.groupby("General_Health", "Sex").count().display()

# COMMAND ------------

# MAGIC %md
# MAGIC # Verificando a quantidade de pessoas que tiveram frequência no hospital

# COMMAND ------------

df_cardio.groupBy("Checkup", "Age_Category").count().distinct().display()

# COMMAND ------------

# MAGIC %md
# MAGIC # Verificando quem faz atividade fisica

# COMMAND ------------

df_cardio.groupBy("Exercise", "Sex").count().display()

# COMMAND ------------

# MAGIC %md
# MAGIC # Verificando quem teve doença cardíaca coronária ou infarto do miocárdio

# COMMAND ------------

df_cardio.groupBy("Heart_Disease", "Sex").count().display()

# COMMAND ------------     

df_cardio.groupBy("Heart_Disease", "Age_Category").count().display()

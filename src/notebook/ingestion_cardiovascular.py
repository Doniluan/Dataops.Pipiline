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

df = spark.table("db_hospital.cardiovascular_diseasess")
     
# COMMAND ------------

df.count()

# COMMAND ------------

df.show(10, False)

# COMMAND ------------     

df.display()

# COMMAND ------------

# MAGIC %md
# MAGIC # Verificando classificação de saúde cardiovascular
# MAGIC Pesquisa de como as pessoas classificam a sua saúde do coração

# COMMAND ------------

df.groupby("General_Health", "Sex").count().display()

# COMMAND ------------

# MAGIC %md
# MAGIC # Verificando a quantidade de pessoas que tiveram frequência no hospital

# COMMAND ------------

df.groupBy("Checkup", "Age_Category").count().distinct().display()

# COMMAND ------------

# MAGIC %md
# MAGIC # Verificando quem faz atividade fisica

# COMMAND ------------

df.groupBy("Exercise", "Sex").count().display()

# COMMAND ------------

# MAGIC %md
# MAGIC # Verificando quem teve doença cardíaca coronária ou infarto do miocárdio

# COMMAND ------------

df.groupBy("Heart_Disease", "Sex").count().display()

# COMMAND ------------     

df.groupBy("Heart_Disease", "Age_Category").count().display()

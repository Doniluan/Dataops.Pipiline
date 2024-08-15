# Databricks notebook source

# MAGIC %md

# MAGIC #Ingestão de Dados ELT

# MAGIC Conjunto de dados de previsão de risco de doenças cardiovasculares

# COMMAND ------------

# display(dbutils.fs)

# COMMAND ------------

# display(dbutils.fs.ls("/"))

# COMMAND ------------

# dbutils.fs.mkdirs("/tmp/")

# COMMAND ----------
# --

# display(dbutils.fs.ls("/"))

# COMMAND ------------

# display(dbutils.fs.ls("/tmp/"))

# COMMAND ------------

# MAGIC %md 

# MAGIC Extraindo dados/Realizando a leitura 

# COMMAND ------------

# df = spark.read.format("csv").option("header", True).load("dbfs:/tmp/cardiovascular.csv")

# COMMAND ------------

# df.display() 

# COMMAND ------------

# df.select("General_Health").distinct().display()

# COMMAND ------------

# df.printSchema()

# MAGIC %md

# MAGIC # Rename Cols

# COMMAND ------------

# df = df.withColumnRenamed("Height_(cm)", "Height_cm").withColumnRenamed("Weight_(kg)", "Weight_kg")

# MAGIC %md 

# MAGIC Realizando o armazenamento de dados

# COMMAND ------------

# df.write.format("delta").mode("overwrite").option("mergeSchema", True).partitionBy("General_Health").save("/hospital/rw/suus/cardiovascular/")

# MAGIC %md

# MAGIC Criando database e tabela pelo delta location

# COMMAND ------------

# MAGIC %sql

# MAGIC CREATE DATABASE IF NOT EXISTS db_hospital


# COMMAND ------------

# MAGIC %sql

# MAGIC CREATE TABLE IF NOT EXISTS db_hospital.cardiovascular_diseasess LOCATION "gs://databricks-46083817904810/46083817904810/hospital/rw/suus/cardiovascular"

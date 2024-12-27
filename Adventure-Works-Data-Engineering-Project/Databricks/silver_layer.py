# Databricks notebook source
# MAGIC %md
# MAGIC # **SILVER** **LAYER**

# COMMAND ----------

dbutils.fs.ls("abfss://bronze@awidhdatalake.dfs.core.windows.net/")

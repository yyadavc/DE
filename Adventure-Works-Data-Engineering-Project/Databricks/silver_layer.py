# Databricks notebook source
# MAGIC %md
# MAGIC #  SILVER LAYER

# COMMAND ----------

# MAGIC %md
# MAGIC ADLS CONNECTION

# COMMAND ----------

spark.conf.set("fs.azure.account.auth.type.awidhdatalake.dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.awidhdatalake.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.awidhdatalake.dfs.core.windows.net", "2d1b308e-8dcf-4898-8f42-10893d11fd05")
spark.conf.set("fs.azure.account.oauth2.client.secret.awidhdatalake.dfs.core.windows.net", "MKG8Q~s2PixZR595_-xEslE4Xk~JGVeXn5F2mdy")
spark.conf.set("fs.azure.account.oauth2.client.endpoint.awidhdatalake.dfs.core.windows.net", "https://login.microsoftonline.com/71a1a040-1e0a-436b-b27e-6118c249b254/oauth2/token")

# COMMAND ----------

dbutils.fs.ls("abfss://bronze@awidhdatalake.dfs.core.windows.net/")

# COMMAND ----------

# MAGIC %md
# MAGIC DATA LOADING

# COMMAND ----------

# DBTITLE 1,AdventureWorks_Calendar
df_AdventureWorks_Calendar = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("abfss://bronze@awidhdatalake.dfs.core.windows.net/AdventureWorks_Calendar")

# COMMAND ----------

# DBTITLE 1,AdventureWorks_Customers
df_AdventureWorks_Customers = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("abfss://bronze@awidhdatalake.dfs.core.windows.net/AdventureWorks_Customers")

# COMMAND ----------

# DBTITLE 1,AdventureWorks_Product_Categories
df_AdventureWorks_Product_Categories = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("abfss://bronze@awidhdatalake.dfs.core.windows.net/AdventureWorks_Product_Categories")

# COMMAND ----------

# DBTITLE 1,AdventureWorks_Product_Categories
df_AdventureWorks_Product_Categories = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("abfss://bronze@awidhdatalake.dfs.core.windows.net/AdventureWorks_Product_Categories")

# COMMAND ----------

# DBTITLE 1,AdventureWorks_Product_Subcategories
df_AdventureWorks_Product_Categories = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("abfss://bronze@awidhdatalake.dfs.core.windows.net/AdventureWorks_Product_Subcategories")

# COMMAND ----------

# DBTITLE 1,AdventureWorks_Products
df_AdventureWorks_Products = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("abfss://bronze@awidhdatalake.dfs.core.windows.net/AdventureWorks_Products")

# COMMAND ----------

# DBTITLE 1,AdventureWorks_Returns
df_AdventureWorks_Returns = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("abfss://bronze@awidhdatalake.dfs.core.windows.net/AdventureWorks_Products")

# COMMAND ----------

# DBTITLE 1,AdventureWorks_Sales_2015
df_AdventureWorks_Sales_2015 = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("abfss://bronze@awidhdatalake.dfs.core.windows.net/AdventureWorks_Sales_2015")

# COMMAND ----------

# DBTITLE 1,AdventureWorks_Sales_2016
df_AdventureWorks_Sales_2016 = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("abfss://bronze@awidhdatalake.dfs.core.windows.net/AdventureWorks_Sales_2016")

# COMMAND ----------

# DBTITLE 1,AdventureWorks_Sales_2017
df_AdventureWorks_Sales_2017 = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("abfss://bronze@awidhdatalake.dfs.core.windows.net/AdventureWorks_Sales_2017")

# COMMAND ----------

# DBTITLE 1,AdventureWorks_Territories
df_AdventureWorks_Territories = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("abfss://bronze@awidhdatalake.dfs.core.windows.net/AdventureWorks_Territories")

# COMMAND ----------

# MAGIC %md
# MAGIC TRANSFORMATION

# COMMAND ----------

import pyspark.sql.functions import*
import pyspark.sql.types import*

# COMMAND ----------

df.withcoulmn('Month',month(col('Date')))
    withColumn('Year',year(col('Date')))

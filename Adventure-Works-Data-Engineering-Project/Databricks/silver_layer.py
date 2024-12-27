# Databricks notebook source
# MAGIC %md
# MAGIC #  SILVER LAYER

# COMMAND ----------

# MAGIC %md
# MAGIC ADLS CONNECTION

# COMMAND ----------

SVP-SECRET = 'MKG8Qs2PixZR595_-xEslE4XkJGVeXn5F2mdyZ'

# COMMAND ----------

spark.conf.set("fs.azure.account.auth.type.awidhdatalake.dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.awidhdatalake.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.awidhdatalake.dfs.core.windows.net", "2d1b308e-8dcf-4898-8f42-10893d11fd05")
spark.conf.set("fs.azure.account.oauth2.client.secret.awidhdatalake.dfs.core.windows.net", "SVP-SECRET")
spark.conf.set("fs.azure.account.oauth2.client.endpoint.awidhdatalake.dfs.core.windows.net", "https://login.microsoftonline.com/71a1a040-1e0a-436b-b27e-6118c249b254/oauth2/token")

# COMMAND ----------

dbutils.fs.ls("abfss://bronze@awidhdatalake.dfs.core.windows.net/")

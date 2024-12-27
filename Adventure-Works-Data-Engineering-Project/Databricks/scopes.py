# Databricks notebook source
# MAGIC %md
# MAGIC pip install databricks-cli

# COMMAND ----------

# MAGIC %md
# MAGIC databricks configure

# COMMAND ----------

# MAGIC %md
# MAGIC databricks secrets create-scope --scope AW-PR

# COMMAND ----------

# MAGIC %md
# MAGIC databricks secrets put --scope AW-PR --key clientid --string-value "2d1b308e-8dcf-4898-8f42-10893d11fd05"

# COMMAND ----------

# MAGIC %md
# MAGIC databricks secrets put --scope AW-PR --key secret --string-value "MKG8Qs2PixZR595_-xEslE4XkJGVeXn5F2mdyZ"

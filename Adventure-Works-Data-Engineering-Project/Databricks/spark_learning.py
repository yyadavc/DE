# Databricks notebook source
# DBTITLE 1,MODES IN SPARK
MODES 
WE HAVE FOUR MODES
1. APEND
2. OVERWRITE
3.ERROR
4.IGNORE

# COMMAND ----------

# DBTITLE 1,TYPES OF MODES
APEND - MEGRE OR UNION WITH EXISTING DATA
OVERWRITE- CLEAR OLD DATA AND REPLACE WITH NEW DATA
ERROR - IGNORE THE IF THERE IS ERROR
IGNORE - IGNORE THE AND WILL NOT WRITE THE DATA ALSO

# COMMAND ----------

# DBTITLE 1,Parquet file
Parquet files are columnar storage files optimized for efficient querying and storage, widely used in big data processing frameworks like Apache Spark, offering compression, schema evolution, and support for complex nested data.

# COMMAND ----------

# DBTITLE 1,Parquest Table
A Parquet table is a logical representation of data stored in **Parquet files**, managed by a database or processing framework, providing schema, partitioning, and query capabilities.

# COMMAND ----------

# DBTITLE 1,DELTA FILE
A Delta file is a Parquet file managed by Delta Lake, enhanced with transaction logs for ACID guarantees in big data processing.

# COMMAND ----------

AICD MEANS 
Atomicity: Ensures that a transaction is treated as a single "unit," meaning it either fully completes or does not execute at all. If any part of the transaction fails, the entire transaction is rolled back.
------
Consistency: Ensures that the database is in a consistent state at the end of the transaction. For example, if you add a new record to a table, the new record must be present in the table.
-----
Isolation: Ensures that concurrently running transactions do not interfere with each other.
-------
Durability: Ensures that once a transaction is committed, it will remain committed even in the event of a system failure.

# COMMAND ----------

# DBTITLE 1,DELATA TABLE
A **Delta table** is a transactional storage table built on Delta Lake that supports ACID properties, enabling reliable data operations, versioning, and efficient handling of both batch and streaming data in big data environments.

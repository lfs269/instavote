# Databricks notebook source
# MAGIC %md
# MAGIC # Simple Databricks Notebook with Python, R, SQL, and Markdown
# MAGIC This notebook demonstrates a combination of Python, R, SQL, and Markdown cells
# MAGIC in Databricks. It performs basic operations, suitable for a low-cost AWS
# MAGIC Databricks environment.
# MAGIC ### Steps:
# MAGIC 1. Perform basic Python operations.
# MAGIC 2. Use R for basic calculations.
# MAGIC 3. Execute SQL queries on an in-memory table.
# MAGIC 4. Add comments and explanations using Markdown.

# COMMAND ----------

# Python: Create a sample data frame and display it
import pandas as pd
# Sample data
data = {"Name": ["Alice", "Bob", "Charlie"], "Age": [25, 30, 35], "Salary":
[50000, 60000, 70000]}
df = pd.DataFrame(data)
# Convert to Spark DataFrame
spark_df = spark.createDataFrame(df)
# Display the Spark DataFrame
display(spark_df)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Python Code Explanation:
# MAGIC - Created a Pandas DataFrame with sample data (Name, Age, Salary).
# MAGIC - Converted it into a Spark DataFrame for use in Databricks.
# MAGIC
# MAGIC - Displayed the Spark DataFrame using the `display` function.

# COMMAND ----------

# MAGIC %r
# MAGIC R: Perform basic operations
# MAGIC # Load a small vector of numbers and calculate their mean
# MAGIC numbers <- c(10, 20, 30, 40, 50)
# MAGIC mean_value <- mean(numbers)
# MAGIC # Print the mean value
# MAGIC print(paste("The mean of the numbers is:", mean_value))

# COMMAND ----------

# MAGIC %md
# MAGIC ### R Code Explanation:
# MAGIC - Created a numeric vector `numbers` with five values.
# MAGIC - Calculated the mean of the numbers using the `mean` function.
# MAGIC - Printed the result to the output.

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC -- SQL: Create and query a temporary table
# MAGIC CREATE OR REPLACE TEMP VIEW employee AS
# MAGIC SELECT * FROM VALUES
# MAGIC ('Alice', 25, 50000),
# MAGIC ('Bob', 30, 60000),
# MAGIC ('Charlie', 35, 70000)
# MAGIC AS employees(Name, Age, Salary);
# MAGIC -- Query the table
# MAGIC SELECT Name, Salary FROM employee WHERE Salary > 55000;

# COMMAND ----------

# MAGIC %md
# MAGIC ### SQL Code Explanation:
# MAGIC - Created a temporary table `employee` using the `CREATE OR REPLACE TEMP VIEW`
# MAGIC command.
# MAGIC - Inserted sample data for employees (Name, Age, Salary).
# MAGIC - Queried the table to select employees with a salary greater than 55,000.

# COMMAND ----------

# Python: Stop all active sessions to minimize costs
# This ensures you don't leave any expensive resources running
spark.catalog.clearCache()

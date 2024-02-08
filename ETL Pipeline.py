# Databricks notebook source
df = spark.read.csv("file:/Workspace/Repos/accounts.jwm@icloud.com/Databricks-ETL-Project/New_York_City_Leading_Causes_of_Death_20240208.csv", header=True, inferSchema=True)

display(df)


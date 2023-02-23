# Databricks notebook source
import random

# COMMAND ----------

i = 25
list = ["Rip Bozo", "Chopped Champion"]
while i > 0:
    print(random.choice(list))
    i = i-1

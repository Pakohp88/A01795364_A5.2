"""Program to compute sales"""

import sys
import os
import time
import json

start_time = time.time()
if not len(sys.argv) == 3:
    print(f"execution time: {time.time() - start_time} seconds")
    sys.exit("A file is missing to perform the calculations")
pathPrices = sys.argv[1]
pathSales = sys.argv[2]
if not os.path.exists(path=pathPrices):
    print(f"execution time: {time.time() - start_time} seconds")
    sys.exit("Prices file not found")
if not os.path.exists(path=pathSales):
    print(f"execution time: {time.time() - start_time} seconds")
    sys.exit("Sales file not found")
with open(pathPrices, "r", encoding="UTF8") as filePrices:
    prices = json.load(filePrices)
salesList = []
with open(pathSales, "r", encoding="UTF8") as fileSales:
    sales = json.load(fileSales)
TOTAL_SALES = 0
for sale in sales:
    product = sale["Product"]
    for price in prices:
        if price["title"] == product:
            try:
                PRICE = price["price"]
            except ValueError:
                print(f'Invalid Val:{price["price"]}')
                continue
            try:
                QUANTITY = sale["Quantity"]
            except ValueError:
                print(f'Invalid Val:{sale["Quantity"]}')
                continue
            TOTAL_SALES += (PRICE * QUANTITY)
execution_time = time.time() - start_time
with open("SalesResults.txt", "a", encoding="UTF8") as file_result:
    file_result.write("\nFILE TOTAL\n")
    file_result.write("----------\n")
    file_result.write(f"{fileSales.name[:3]}  {TOTAL_SALES}\n")
    print(f"File Name: {fileSales.name[:3]} TOTAL: {TOTAL_SALES}")
    file_result.write("----------\n")
    file_result.write(f"execution time {execution_time} seconds\n")
print(f"execution time: {execution_time} seconds")

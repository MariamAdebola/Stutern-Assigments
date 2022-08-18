-- SQLite

-- # 1.the amount the business owner invested
SELECT SUM(cost_price) FROM stationery_table;

-- # 2.Calculate the average quantity of items in stock
SELECT Round(AVG(Quantity)) FROM stationery_table;

-- # 3.item with the least quantity in stock
SELECT MIN(Quantity) FROM stationery_table;

-- # 4.Determine the item with the most quantity in stock
SELECT MAX(Quantity) FROM stationery_table;

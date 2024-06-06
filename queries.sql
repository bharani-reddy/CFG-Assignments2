USE CoffeeShopDB;

-- Retrieve all drinks
SELECT * FROM Drinks;

-- Retrieve all food items
SELECT * FROM Food;

-- Retrieve all members
SELECT * FROM Members;

-- Retrieve purchases
SELECT * FROM Purchases;

-- Total sales
SELECT SUM(TotalPrice) AS TotalSales FROM Purchases;

-- Count items in stock
SELECT Name, SUM(ItemCount) AS TotalItems FROM RemainingStock GROUP BY Name;

-- Find members with more than 10 points
SELECT * FROM Members WHERE PointsCollected > 10;

-- Delete a specific purchase
DELETE FROM Purchases WHERE PurchaseID = 1;

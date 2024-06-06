CREATE DATABASE CoffeeShopDB;
USE CoffeeShopDB;

CREATE TABLE Drinks (
    DrinkID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Price DECIMAL(5, 2) NOT NULL,
    Calories INT,
    Size VARCHAR(50),
    Ingredients TEXT,
    Allergens TEXT
);

CREATE TABLE Food (
    FoodID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Price DECIMAL(5, 2) NOT NULL,
    Calories INT,
    Allergens TEXT,
    Quantity INT
);

CREATE TABLE RemainingStock (
    StockID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    ItemCount INT NOT NULL
);

CREATE TABLE Members (
    MemberID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100) UNIQUE NOT NULL,
    PhoneNumber VARCHAR(15),
    PointsCollected INT
);

CREATE TABLE Purchases (
    PurchaseID INT AUTO_INCREMENT PRIMARY KEY,
    MemberID INT,
    ItemID INT,
    ItemType ENUM('Drink', 'Food'),
    Quantity INT NOT NULL,
    TotalPrice DECIMAL(6, 2) NOT NULL,
    PurchaseDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (

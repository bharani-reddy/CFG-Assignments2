USE CoffeeShopDB;

INSERT INTO Drinks (Name, Price, Calories, Size, Ingredients, Allergens) VALUES
('Espresso', 2.50, 5, 'Small', 'Coffee', 'None'),
('Latte', 3.50, 150, 'Medium', 'Coffee, Milk', 'Milk');

INSERT INTO Food (Name, Price, Calories, Allergens, Quantity) VALUES
('Croissant', 1.50, 200, 'Wheat, Butter', 20),
('Muffin', 2.00, 300, 'Eggs, Wheat', 15);

INSERT INTO RemainingStock (Name, ItemCount) VALUES
('Milk', 50),
('Coffee Beans', 100);

INSERT INTO Members (FirstName, LastName, Email, PhoneNumber, PointsCollected) VALUES
('John', 'Doe', 'john.doe@example.com', '123-456-7890', 10),
('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', 20);

INSERT INTO Purchases (MemberID, ItemID, ItemType, Quantity, TotalPrice) VALUES
(1, 1, 'Drink', 2, 5.00),
(2, 2, 'Drink', 1, 3.50);

CREATE DATABASE production;
USE production;

CREATE TABLE MarketData (
    InvoiceNo INT,
    StockCode INT,
    Description VARCHAR(255),
    Quantity INT,
    InvoiceDate TIMESTAMP,
    UnitPrice DECIMAL,
	CustomerID INT,
	Country VARCHAR(255)
);


SELECT * FROM ecommerce_dataset;

SELECT COUNT(*) AS total_Records FROM ecommerce_dataset;

SELECT SUM(quantity * Sales) AS total_Sales FROM ecommerce_dataset;

SELECT AVG(Sales) AS ave_Price FROM ecommerce_dataset;

SELECT * FROM ecommerce_dataset WHERE quantity > 4;





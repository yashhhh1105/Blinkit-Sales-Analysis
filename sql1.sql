use ecommerce;

select * from sales_data;

-- total revenue generate by blinkit sales
select round(sum(total_sales),0) as Total_Revenue from sales_data; 
	
-- Which item types have the highest average sales?

SELECT item_type,AVG(total_sales) AS average_sales
FROM sales_data
GROUP BY item_type
ORDER BY average_sales DESC;

-- Which outlet type generates the highest total sales?

SELECT
    outlet_type,
    SUM(total_sales) AS sales
FROM sales_data
GROUP BY outlet_type
ORDER BY sales DESC;

-- Does Outlet Size affect sales performance?

SELECT
    outlet_size,
    COUNT(DISTINCT outlet_identifier) AS number_of_outlets,
    SUM(total_sales) AS sales,
    ROUND(
        SUM(total_sales) / COUNT(DISTINCT outlet_identifier),
        2
    ) AS sales_per_outlet
FROM sales_data
GROUP BY outlet_size
ORDER BY sales_per_outlet DESC; 

-- Which Outlet Location Type performs the best?

SELECT
    outlet_location_type,
    COUNT(DISTINCT outlet_identifier) AS number_of_outlets,
    Round(SUM(total_sales),2) as sales,
    ROUND(
        SUM(total_sales) / COUNT(DISTINCT outlet_identifier),
        2
    ) AS sales_per_outlet
FROM sales_data
GROUP BY outlet_location_type
ORDER BY sales_per_outlet DESC;

-- Question 7: Does Outlet Age influence sales performance?

SELECT
    outlet_age,ROUND(AVG(total_sales), 2) AS avg_sales
FROM sales_data
GROUP BY outlet_age
ORDER BY avg_sales desc;

-- Question 8: Which Outlet Types have the highest average customer ratings?
select outlet_type,round(avg(rating),2) as avg_rating from sales_data group by outlet_type order by avg_rating desc;

-- Which products/categories should Blinkit prioritize based on sales performance?

SELECT
    item_type,
    COUNT(*) AS total_products,
    round(SUM(total_sales),2) AS sales,
    ROUND(AVG(total_sales),2) AS average_sales
FROM sales_data
GROUP BY item_type
ORDER BY sales DESC;

-- Which item types generate the highest total sales?

SELECT
    item_type,
    COUNT(*) AS number_of_items,
    SUM(total_sales) AS sales,
    AVG(total_sales) AS average_sales
FROM sales_data
GROUP BY item_type
ORDER BY sales DESC;

-- Question 10: Which outlet format should Blinkit expand to maximize revenue?

SELECT
    outlet_type,
    outlet_size,
    outlet_location_type,
    COUNT(DISTINCT outlet_identifier) AS total_outlets,
    SUM(total_sales) AS sales,
    ROUND(
        SUM(total_sales) / COUNT(DISTINCT outlet_identifier),
        2
    ) AS sales_per_outlet
FROM sales_data
GROUP BY
    outlet_type,
    outlet_size,
    outlet_location_type
ORDER BY sales_per_outlet DESC;

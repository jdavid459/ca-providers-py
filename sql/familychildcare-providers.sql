-- This SQL takes the liberty of assuming the CSVs in /outputs are tables in a database.  
-- Should be 605 providers

WITH providers AS (SELECT *
                   FROM csv_provided
                   WHERE type_of_care = 'Family Child Care Home'
                   UNION
                   SELECT provider_name
                   FROM scraped_data
                   WHERE type_of_care = 'Family Child Care Home')


SELECT COUNT(DISTINCT provider_name) AS familychildcarehome_providers
FROM providers
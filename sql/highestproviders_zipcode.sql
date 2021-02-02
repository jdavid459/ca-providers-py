-- This SQL takes the liberty of assuming the CSVs in /outputs are tables in a database.  
/* I'd take a longer look at this one with more time.  I don't have address nor zip in the API data.  Maybe its worth joining to one of the other
data sets to get that info - though it might be inexact.  For now I'm just using the CSV and the scraped data.  This'll give the count of unique addresses and provider names. */

WITH provider_addresses AS (SELECT
                              provider_name
                              , zip
                              , address
                            FROM scraped_data
                            UNION
                            SELECT
                              provider_name
                              , zip
                              , address
                            FROM csv_provided)

SELECT
  zip
  , COUNT(DISTINCT address) AS provider_locations
  , COUNT(DISTINCT provier_name)
FROM provider_addresses
GROUP BY 1
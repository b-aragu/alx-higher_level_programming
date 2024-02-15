SELECT
    city,
    AVG((value * 9/5) + 32) AS avg_temp_fahrenheit
FROM
    temperatures
GROUP BY
    city
ORDER BY
    avg_temp_fahrenheit DESC;


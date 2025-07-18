-- Create table
CREATE TABLE
    HealthStats (
        Zone VARCHAR(10),
        Month VARCHAR(10),
        Fever_Cases INT,
        Pollution_Level INT,
        Hospital_Visits INT
    );

-- Insert sample data
INSERT INTO
    HealthStats
VALUES
    ('A', 'Jan', 120, 80, 300);

-- Add all other rows similarly...
-- Sample queries
SELECT
    Zone,
    AVG(Fever_Cases) AS AvgCases
FROM
    HealthStats
GROUP BY
    Zone;

SELECT
    *
FROM
    HealthStats
WHERE
    Hospital_Visits > 350;
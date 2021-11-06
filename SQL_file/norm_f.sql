CREATE FUNCTION distance(float, float, float, float, float, float, float, float, float, float, float, float, float, float, float, float) RETURNS float 
AS 'SELECT sqrt(($1 - $9)^2 + ($2 - $10)^2 + ($3 - $11)^2 + ($4 - $12)^2 + ($5 - $13)^2 + ($6 - $14)^2 + ($7 - $15)^2 + ($8 - $16)^2 ) AS distance'
LANGUAGE 'sql';
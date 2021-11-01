CREATE FUNCTION inner_product(float, float, float, float, float, float, float, float, float, float, float, float, float, float, float, float) RETURNS float 
AS 'SELECT $1*$9 + $2*$10 + $3*$11 + $4*$12 + $5*$13 + $6*$14 + $7*$15 + $8*$16 AS inner_product FROM music_normalization'
LANGUAGE 'sql';





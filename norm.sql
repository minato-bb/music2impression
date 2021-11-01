CREATE TABLE impression_norm (
word text,
danceability float,
acousticness float,
energy float,
liveness float,
loudness float,
speechiness float,
tempo float,
valence float
);

INSERT INTO impression_norm (word, danceability, acousticness, energy, liveness, loudness, speechiness, tempo, valence)
VALUES ('excited', 0.559412, 0.238991, 0.753471, 0.177212, -6.361706, 0.107300, 128.399882, 0.565765);
INSERT INTO impression_norm (word, danceability, acousticness, energy, liveness, loudness, speechiness, tempo, valence)
VALUES ('cool', 0.533333, 0.176618, 0.796208, 0.214154, -5.769667, 0.071800, 124.457208, 0.456937);
INSERT INTO impression_norm (word, danceability, acousticness, energy, liveness, loudness, speechiness, tempo, valence)
VALUES ('relax', 0.533500, 0.420415, 0.604963, 0.161387, -7.346125, 0.069258, 121.235208, 0.504838);
INSERT INTO impression_norm (word, danceability, acousticness, energy, liveness, loudness, speechiness, tempo, valence)
VALUES ('sad', 0.509000, 0.403961, 0.593177, 0.183709, -6.792652, 0.046196, 119.219565, 0.408422);
INSERT INTO impression_norm (word, danceability, acousticness, energy, liveness, loudness, speechiness, tempo, valence)
VALUES ('fierce', 0.537160, 0.136491, 0.823628, 0.182200, -5.780800, 0.099324, 132.391520, 0.505112);
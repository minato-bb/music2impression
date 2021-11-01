-- DROP TABLE impression;
CREATE TABLE impression(
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

INSERT INTO impression(word, danceability, acousticness, energy, liveness, loudness, speechiness, tempo, valence)
VALUES ('cool', 0.6, 0, 0.8, 0.2, 0.5, 0, 0.7, 0.5);
INSERT INTO impression(word, danceability, acousticness, energy, liveness, loudness, speechiness, tempo, valence)
VALUES ('excited', 0.8, 0, 1, 0.5, 1, 0, 0, 1);
INSERT INTO impression(word, danceability, acousticness, energy, liveness, loudness, speechiness, tempo, valence)
VALUES ('relax', -1, 1, -0.8, 0, -1, 0, -0.5, 0);
INSERT INTO impression(word, danceability, acousticness, energy, liveness, loudness, speechiness, tempo, valence)
VALUES ('sad', -1, 0.3, -1, 0, -0.5, 0, -0.8, -1);
INSERT INTO impression(word, danceability, acousticness, energy, liveness, loudness, speechiness, tempo, valence)
VALUES ('fierce', 0.3, -0.5, 0.7, 0.3, 1, 0, 1, 0.8);


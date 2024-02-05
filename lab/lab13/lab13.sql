.read data.sql


CREATE TABLE bluedog AS
  SELECT color, pet from students where color = "blue" and pet = "dog";

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song from students where color = "blue" and pet = "dog";


CREATE TABLE matchmaker AS
  SELECT a.pet, a.song, a.color, b.color from students AS a, students AS b where a.pet = b.pet and a.song = b.song and a.time < b.time;


CREATE TABLE sevens AS
  SELECT stu.seven from students AS stu, numbers AS num where stu.time = num.time and num."7" = "True" and stu.number = 7;


CREATE TABLE favpets AS
  SELECT pet, count(*) AS tot from students group by pet order by tot desc limit 10;


CREATE TABLE dog AS
  SELECT pet, count(*) from students where pet = "dog";


CREATE TABLE bluedog_agg AS
  SELECT song, COUNT(song) as tot FROM bluedog_songs GROUP BY song ORDER BY tot desc;


CREATE TABLE instructor_obedience AS
  SELECT seven, instructor, COUNT(*) FROM students WHERE seven='7' GROUP BY instructor;


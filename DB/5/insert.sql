insert into autor(name)
	values('Jonh Call'),
	('Bon'),
	('Paul'),
	('Ken'),
	('Sam Wall'),
	('Jack'),
	('Lenny'),
	('Kenny Doll');
	
insert into genre(name)
	values('Rock'),
	('Electronic'),
	('Soul'),
	('Funk'),
	('Country');
	
insert into album(name, year)
	values('I love', 1950),
	('I hate', 1960),
	('I feel', 1970),
	('I run', 1974),
	('I do', 2019),
	('I kill', 2018),
	('I will', 2018),
	('I drill', 2020);

insert into track(id_album, name, duration)
	values(1, 'analyst', '0:05:50'),
	(2,'mixture', '0:03:40'),
	(3,'son', '0:01:00'),
	(4,'my tooth', '0:04:50'),
	(5,'secretary', '0:01:55'),
	(6,'energy', '0:02:50'),
	(7,'drawer', '0:01:50'),
	(8,'my town', '0:07:50'),
	(1,'leadership', '0:01:50'),
	(2,'responsibility', '0:03:50'),
	(3,'committee', '0:01:44'),
	(4,'meal', '0:01:11'),
	(5,'quantity', '0:01:10'),
	(6,'newspaper', '0:03:30'),
	(7,'opinion', '0:01:20');

insert into collection(name, year)
	values('girlfriend', 1951),
	('region', 1961),
	('photo', 1971),
	('county', 1975),
	('exam', 2019),
	('chocolate', 2018),
	('wedding', 2018),
	('writer', 2020);

insert into autor_album
	values(1, 1),
	(2, 2),
	(3, 3),	
	(4, 4),
	(5, 5),
	(6, 6),
	(7, 7),
	(8, 8),
	(2, 1),
	(2, 3),	
	(2, 4),
	(2, 5),
	(6, 7),
	(6, 8);

insert into track_collection
	values(1, 1),
	(2, 2),
	(3, 3),	
	(4, 4),
	(5, 5),
	(6, 6),
	(7, 7),
	(8, 8),
	(2, 1),
	(2, 3),	
	(2, 4),
	(2, 5),
	(6, 7),
	(6, 8);

insert into autor_genre
	values(1, 1),
	(2, 2),
	(3, 3),	
	(4, 4),
	(5, 5),
	(6, 1),
	(7, 2),
	(8, 3),
	(2, 1),
	(2, 3),	
	(2, 4),
	(2, 5),
	(6, 5),
	(6, 4);


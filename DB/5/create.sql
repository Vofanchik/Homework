create table if not exists Autor(
	Id serial primary key,
	Name varchar(40) not null);

create table if not exists Album (
	Id serial primary key,
	Name varchar(40) not null,
	Year integer not null);	

create table if not exists Autor_Album(
	Id_Autor integer references Autor(Id),
	Id_Album integer references Album(Id),
	constraint pkAuAl primary key (Id_Autor, Id_Album));

create table if not exists Track(
	Id serial primary key,
	Id_Album integer references Album(Id),
	Name varchar(40) not null,
	Duration time not null);

create table if not exists Collection(
	Id serial primary key,
	Name varchar(40) not null,
	Year integer not null);

create table if not exists Track_Collection(
	Id_Track integer references Track(Id),
	Id_Collection integer references Collection(Id),
	constraint pkTrCo primary key (Id_Track, Id_Collection ));

create table if not exists Genre(
	Id serial primary key,
	Name varchar(40) not null);

create table if not exists Autor_Genre(
	Id_Autor integer references Autor(Id),
	Id_Genre integer references Genre(Id),
	constraint pkAuGe primary key (Id_Autor, Id_Genre));

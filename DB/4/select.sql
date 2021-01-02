select name, year from album 
	where year = 2018

select name, duration from track 
	order by duration desc
	limit 1

select name, duration from track 
	where duration > '0:03:30'

select name from collection 
	where year between 2018 and 2020

select name from autor 
	where name not like '% %'

select name from track 
	where name like '%my%'
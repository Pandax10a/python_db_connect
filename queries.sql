insert into items(name, price)
values
('apple', 5),
('banana', 7),
('pineapple', 9),
('orange', 11),
('coconut', 13),
('pear', 15);

select id, name, price 
from items;

select id, name, price
from items
where price >= 10;

call price_greater_than (8);
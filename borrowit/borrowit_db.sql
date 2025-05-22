
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    building_code VARCHAR(50)
);

CREATE TABLE items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(255),
    item_type VARCHAR(50),
    building_code VARCHAR(50),
    status VARCHAR(50) DEFAULT 'Available'
);

select * from users;
select * from items;
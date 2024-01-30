CREATE DATABASE IF NOT EXISTS trackingGPS;
USE trackingGPS;

CREATE TABLE IF NOT EXISTS history (
    id INT AUTO_INCREMENT,
    latitude DOUBLE NOT NULL,
    longitude DOUBLE NOT NULL,
    user VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);
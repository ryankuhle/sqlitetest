#Goal: print out the hottest cities in July with following format:
#The cities that are warmest in July are: city, state, city, state, etc.

import sqlite3 as lite

#Connect to getting_started.db

con = lite.connect('getting_started.db')

#Drop tables "cities" and "weather" if they exist

##DROP TABLE IF EXISTS cities, weather;

#Create "cities" and "weather" tables
##CREATE TABLE cities (name text, state text);
##CREATE TABLE weather (city text, year integer, warm_month text, cold_month text, average_high integer);

#Insert the appropriate data into tables
cityIns = "INSERT INTO cities (name, state) VALUES
('New York City', 'NY'),
('Boston', 'MA'),
('Chicago', 'IL'),
('Miami', 'FL'),
('Dallas', 'TX'),
('Seattle', 'WA'),
('Portland', 'OR'),
('San Francisco', 'CA'),
('Los Angeles', 'CA'),
('Las Vegas', 'NV'),
('Atlanta', 'GA'),
('Washington', 'DC'),
('Houston', 'TX');"

weatherIns = "INSERT INTO weather (city, year, warm_month, cold_month, average_high) VALUES
('New York City', 2013, 'July', 'January', 62),
('Boston', 2013, 'July', 'January', 59),
('Chicago', 2013, 'July', 'January', 59),
('Miami', 2013, 'August', 'January', 84),
('Dallas', 2013, 'July', 'January', 77),
('Seattle', 2013, 'July', 'January', 61),
('Portland', 2013, 'July', 'December', 63),
('San Francisco', 2013, 'September', 'December', 64),
('Los Angeles', 2013, 'September', 'December', 75),
('Las Vegas', 2013, 'July', 'December', NULL),
('Atlanta', 2013, 'July', 'January', NULL),
('Washington', 2013, 'July', 'January', NULL),
('Houston', 22013, 'July', 'January', NULL);"

#Join the data together

#Load into a pandas DataFrame

#Print out the resulting city and state in a full sentence. For example: "The cities that are warmest in July are: Las Vegas, NV, Atlanta, GA..."

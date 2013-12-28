Hungryy
=======

## Dependencies

* sudo apt-get install pyhton build-essential python-dev python-setuptools python-virtualenv
* sudo apt-get install python-mysqldb
* sudo pip install nose
* sudo pip install CherryPy
* sudo pip install termcolor


## Front-end Dependencies

- NodeJS
```
sudo apt-get install nodejs
```
- GruntJS
```
sudo npm install -g grunt-cli
```
- Bower
```
sudo npm install -g bower
```
- Compass
```
gem install compass
```

### Public Directory
- NPM dependencies (package.json):
```
sudo npm install
```

- Bower dependencies (bower.json):
```
bower install
```

## MySQL User
SQL commands:
```
CREATE USER 'hungryy-user'@'localhost' IDENTIFIED BY 'hungryy-db';
GRANT ALL PRIVILEGES ON *.* TO 'hungryy-user'@'localhost' WITH GRANT OPTION;
```

docker run --name minip3_mysql -e MYSQL_ROOT_PASSWORD=enCore129! -v /home/ubuntu/workspace/minip3sql:/var/lib/mysql -p 8443:3306 -d mysql:latest --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
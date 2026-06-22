build:
	docker build -t appimage .

run:
	docker run -d --name appcontainer -p 80:80 appimage
	-docker cp backup/pancakes.db appcontainer:/app/data/

stop:
	docker stop appcontainer

clean: backup
	docker rmi -f appimage &&\
	docker rm appcontainer

data:
	-mv pancakes.db pancakes.`cat /dev/urandom | tr -cd 'a-f0-9' | head -c 8`.db
	-docker cp appcontainer:/app/data/pancakes.db .

backup: data
	-cp -p pancakes*.db backup/

clean-data: backup
	rm pancakes*.db

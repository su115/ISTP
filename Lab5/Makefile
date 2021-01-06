STATES := app tests
REPO := 125111317/lab5

.PHONY: $(STATES)

$(STATES):
	@echo "$(REPO):/$(@)"
	@docker build   -t $(@) ./$(@)/ 
	#ibecause dont work with tests only with app work
	@docker build -t tests ./tests/


run:
	@docker run --name my_redis --rm -d redis
	@docker run --name my_app --link my_redis:my_app -d $(REPO):app
	@echo "http://$$(docker inspect  --format {{.NetworkSettings.IPAddress}} my_app):5000"


test-app:
	@docker run --rm  --name my_test --link my_app:my_test $(REPO):tests

pull: 
	@docker pull $(REPO):app
	@docker pull $(REPO):tests
	
stop:
	@docker stop my_redis
	@docker stop my_app

rm: 
	@docker rm $$(docker ps -a -q) -f 
rmi:
	@docker rmi $$(docker images -q) -f

push:
	@docker tag app $(REPO):app
	@docker tag tests $(REPO):tests
	@docker push $(REPO):app
	@docker push $(REPO):tests

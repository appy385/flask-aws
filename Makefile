app_name = gunicorn_flask

build:
		docker build -t $(app_name) .

run:
	docker run --detach -p 8000:8000 $(app_name)

kill:
	@docker container stop $$(docker container ls -aq)
	docker container prune -f

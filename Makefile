all : django

django : ./Dockerfile build runV

build :
	docker build -t django .

run	:
	docker run -it django

runV :
	docker run -it -p 8000:8000 -v /Users/${USER}/Desktop/Django:/app django

list :
	@docker image ls
	@echo "\n\n"
	@docker ps -a

# Removes all stopped containers
prune :
	docker stop $(shell docker ps -a -q)
	docker rm $(shell docker ps -a -q)

rmimages :
	docker image rm -f $(shell docker image ls | awk 'NR >= 2 {print $$3}')

clean : prune rmimages
# rm -rf poll_site/mysite/mysite/__pycache__

.PHONY: clean rmimages prune run build django list
# docker container prune -f
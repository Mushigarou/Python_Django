FROM python:3.10.14-bookworm

WORKDIR /app

RUN apt update && apt upgrade -y && apt install nano vim nodejs sudo zsh curl -y

RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.1.5/zsh-in-docker.sh)"

COPY . .

EXPOSE 8000

ENTRYPOINT [ "bash" ]

# ENTRYPOINT ["python3", "manage.py", "runserver", "0.0.0.0:8000"]


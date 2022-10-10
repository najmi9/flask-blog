FROM python:3

RUN apt update && apt upgrade

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "flask", "run", "-p", "8000", "-h", "0.0.0.0"]

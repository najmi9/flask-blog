FROM python:3.9

RUN apt update -y && apt upgrade -y

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "flask", "run", "-p", "8000", "-h", "0.0.0.0"]

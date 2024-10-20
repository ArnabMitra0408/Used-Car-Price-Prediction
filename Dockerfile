FROM python:3.12.7

WORKDIR /used_car_project

COPY requirements.txt /used_car_project

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["./start.sh"]
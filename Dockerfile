FROM python:3.9.10-slim-buster

WORKDIR sql-injection-example
COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

COPY ./UserModel.py ./UserModel.py
COPY ./main.py ./main.py

EXPOSE 8000
CMD ["python", "./main.py"]
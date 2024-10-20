FROM python:3.12-alpine

COPY . /opt/MajorProject/

WORKDIR /opt/MajorProject/

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["fastapi", "run", "main.py", "--port", "80"]
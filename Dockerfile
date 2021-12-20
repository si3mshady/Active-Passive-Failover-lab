FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt .
COPY flask_mock_api.py .

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["python3", "flask_mock_api.py"]


# docker run -p 80:80 si3mshady/healthcheck-activepassive
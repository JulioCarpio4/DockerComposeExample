FROM python:3
RUN pip install -U Flask && pip install redis
WORKDIR /app
COPY . /app

ENTRYPOINT [ "python" ]
CMD ["app.py"]

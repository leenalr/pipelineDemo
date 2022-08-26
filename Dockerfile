FROM python:latest
WORKDIR /app
COPY . /app
RUN pip install -r dependencies.txt
EXPOSE 5000
CMD ["python","app.py"]

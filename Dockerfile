FROM python:latest
WORKDIR /application
COPY . /application
RUN pip install -r dependencies.txt
EXPOSE 5000
CMD ["python","app.py"]

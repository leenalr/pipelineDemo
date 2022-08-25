FROM python:3.6-stretch
WORKDIR /application
COPY . /application
RUN pip install --upgrade pip
RUN pip install -r dependencies.txt
EXPOSE 5000
CMD ["python","app.py"]

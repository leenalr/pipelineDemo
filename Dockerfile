FROM python:3.10-alpine
WORKDIR /app
COPY . /app
RUN pip install -r dependencies.txt
EXPOSE 5000
CMD ["python","app.py"]
  

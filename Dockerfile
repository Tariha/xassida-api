FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /django
COPY requirements.txt ./
COPY load_db.sh ./
COPY . .
RUN pip install --no-cache-dir -r requirements.txt 
RUN python manage.py makemigrations 
RUN python manage.py migrate
RUN ./load_db.sh
EXPOSE 8000
CMD [ "python", "manage.py","runserver","0.0.0.0:8000"]
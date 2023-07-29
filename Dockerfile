FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /django
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
RUN python manage.py migrate
CMD [ "python", "manage.py","runserver"]
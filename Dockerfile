FROM python:3.12
ENV PYTHONUNBUFFERED 1

RUN adduser --disabled-password --gecos '' django
ENV PATH=${PATH}:/home/django/.local/bin
USER django
WORKDIR /home/django/project

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["./manage.py", "runserver", "[::]:8000"]

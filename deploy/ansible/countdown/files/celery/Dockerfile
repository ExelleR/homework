FROM python:2

RUN mkdir -p app/backend
COPY ./backend /app/backend
WORKDIR /app
RUN pip install -r ./backend/requirements.txt

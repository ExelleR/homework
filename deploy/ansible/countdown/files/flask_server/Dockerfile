FROM python:2

RUN mkdir -p app/backend
COPY ./backend /app/backend
RUN pip install -r /app/backend/requirements.txt
ENV PYTHONPATH "${PYTHONPATH}:/app"
CMD ["python", "/app/backend/src/server/flask_server.py"]
EXPOSE 8888

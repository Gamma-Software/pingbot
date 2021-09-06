FROM python:3.8-alpine
COPY . .
RUN python3 -m pip install requests
ENTRYPOINT ["python3", "pingbot.py"]
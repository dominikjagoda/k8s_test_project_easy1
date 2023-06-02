FROM python:3.10


WORKDIR app/ 
COPY . .
RUN cd app && pip install -r reqiurements.txt

WORKDIR app/ 
CMD ["python", "poke-api.py"]


CMD ["tail", "-f", "/dev/null"]
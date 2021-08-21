FROM python:3.6.1-alphine
WORKDIR /recommendation_api
ADD . /recommendation_api
RUN pip install -r requirements.txt
CMD ["python", "run.py"]
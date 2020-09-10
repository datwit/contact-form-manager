FROM python:3.8
ADD . /src
WORKDIR /src
RUN pip install --no-cache-dir -r requirements.txt
CMD python run-local.py

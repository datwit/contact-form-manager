FROM python:3.8
ADD . /src
WORKDIR /src
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install pytest pytest-cov
CMD python run-local.py

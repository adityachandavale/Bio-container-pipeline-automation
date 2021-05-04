FROM python:3.8-alpine

COPY automate_mode.py /run
COPY manual_mode.py /run
COPY ProjectFlask.py /run
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /run
CMD ["python","ProjectFlask.py"]
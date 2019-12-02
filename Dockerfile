FROM python:3.8-alpine

COPY bots/config.py /bots/
COPY bots/autoreply.py /bots/
COPY bots/tarotgenerator.py /bots/
COPY requirements.txt /bots
RUN pip3 install -r /bots/requirements.txt


WORKDIR /bots
CMD ["pip3 install pycorpora;", "python3", "autoreply.py"]
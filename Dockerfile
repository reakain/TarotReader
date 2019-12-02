FROM python:3.8-alpine

COPY bots/config.py /bots/
COPY bots/autoreply.py /bots/
COPY bots/tarotgenerator.py /bots/
COPY requirements.txt /bots

RUN pip3 install -r /bots/requirements.txt
RUN pip3 install --upgrade --force-reinstall pycorpora --install-option="--corpora-zip-url=https://github.com/dariusk/corpora/archive/master.zip"

WORKDIR /bots
CMD ["python3", "autoreply.py"]

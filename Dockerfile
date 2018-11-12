FROM python:3

ADD strprg.py /

RUN pip install pystrich

CMD [ "python", "./strprg.py" ]
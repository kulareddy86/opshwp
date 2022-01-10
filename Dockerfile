FROM python:3.10
WORKDIR /openshift/venv
ADD . /openshift/venv
RUN pip install -r requirement.txt
CMD ["python","app.py"]
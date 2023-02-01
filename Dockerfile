FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV PROJECT_DIR /usr/src/forum
WORKDIR ${PROJECT_DIR}


RUN pip install pipenv
COPY Pipfile Pipfile.lock ${PROJECT_DIR}/

RUN pipenv install --dev --system

COPY entrypoint.sh .

RUN chmod +x entrypoint.sh

COPY . .

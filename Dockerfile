FROM python:3.7

ENV TZ=America/Sao_Paulo
RUN cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime
RUN echo "America/Sao_Paulo" > /etc/timezone

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

RUN apt-get update && apt-get install -y binutils libproj-dev gdal-bin build-essential python3-dev python3-pip \
    python3-setuptools python3-wheel python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 \
    libffi-dev shared-mime-info

RUN mkdir -p /usr/src/logs
RUN mkdir -p /usr/src/app/static
RUN mkdir -p /usr/src/app/media

EXPOSE 8000 8001

ENTRYPOINT ["./docker-entrypoint.sh"]
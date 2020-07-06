FROM agostof/uwsgi-nginx-flask:python3.8-alpine
RUN apk update && apk add --no-cache gcc git python3-dev musl-dev linux-headers libc-dev rsync zsh findutils wget util-linux grep libxml2-dev libxslt-dev && pip3 install --upgrade pip
RUN apk --update add bash nano
COPY ./requirements.txt /var/www/requirements.txt
RUN python3 -m pip install --upgrade pip
RUN pip install -r /var/www/requirements.txt
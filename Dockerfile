FROM python:latest

WORKDIR /app

COPY . /app

ENV TZ=${CONTAINER_TIMEZONE}
RUN pip install -r requirements.txt

RUN chmod 0644 bot.py

#Install Cron
RUN apt-get update
RUN apt-get -y install cron

# Add the cron job
RUN crontab -l | { cat; echo "* * * * * . $HOME/.profile && cd /app && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && /usr/local/bin/python /app/bot.py > /proc/1/fd/1 2>/proc/1/fd/2"; } | crontab -

# Run the command on container startup
CMD ["cron", "-f"]
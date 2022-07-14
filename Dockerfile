FROM python:latest

WORKDIR /app

COPY . /app

RUN chmod +x /app/start.sh && chmod 0644 bot.py

ENV TZ=America/Caracas
RUN pip install -r requirements.txt

#Install Cron
RUN apt-get update
RUN apt-get -y install cron

# Add the cron job
RUN crontab -l | { cat; echo "0 10 * * 2,5 . $HOME/.profile && cd /app && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && /usr/local/bin/python /app/bot.py > /proc/1/fd/1 2>/proc/1/fd/2"; } | crontab -
# Run the command on container startup
EXPOSE 7000

CMD ["/app/start.sh"]
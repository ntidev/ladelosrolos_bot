FROM python:latest

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

RUN chmod 0644 bot.py

#Install Cron
RUN apt-get update
RUN apt-get -y install cron

# Add the cron job
RUN crontab -l | { cat; echo "* * * * * /usr/bin/python /app/bot.py"; } | crontab -

# Run the command on container startup
RUN touch /var/log/cron.log
CMD cron && tail -f /var/log/cron.log
# LA DE LOS ROLOS - Slack Bot

This was a simple script/bot created to send random messages to a specific Slack channel.

Initially questions were in a TXT file.

The idea is to:
1. Create a DB and update .env accordingly
2. Run `populate_DB.py` script to create and populate the questions table
3. Set a CRON JOB to run `bot.py`

The bot will run, look for a random row only if it hasn't been sent before. Send the question to slack and then mark it as sent. 

## Potential Enhancements
- Add: Try Except
- Improve DB creation and population

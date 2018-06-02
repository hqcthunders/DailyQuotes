#!/usr/bin/env python3
import os
from requests_html import HTMLSession

from twilio import TwilioRestException
from twilio.rest import TwilioRestClient
from apscheduler.schedulers.blocking import BlockingScheduler

TWILIO_ACCOUNT_SID = os.environ["TWILIO_ACCOUNT_SID"]
TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]

sched = BlockingScheduler()


def get_quotes():
    url = "https://www.brainyquote.com/quote_of_the_day"
    session = HTMLSession()
    r = session.get(url)
    path = "img.p-qotd.bqPhotoDefault.bqPhotoDefaultFw.img-responsive"
    data = r.html.find(path, first=True).attrs['alt']
    return data


@sched.scheduled_job('cron', day_of_week='mon-sun', hour=6)
def scheduled_job():
    client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    my_phone = "+15126484352"
    target_phone = os.environ["my_phone"]

    try:
        client.messages.create(
            to=target_phone,
            from_=my_phone,
            body=get_quotes()
        )
    except TwilioRestException as e:
        print(e)


sched.start()

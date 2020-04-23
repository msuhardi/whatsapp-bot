# app/scheduler.py

from apscheduler.schedulers.background import BackgroundScheduler
from twilio.rest import Client
from app import api, app, utils

class Scheduler:

    client = Client(
        app.config['TWILIO_ACCOUNT_SID'],
        app.config['TWILIO_AUTH_TOKEN']
    )
    from_ = "whatsapp:+% s"% app.config['TWILIO_NUMBER']

    def __init__(self, subscribers):
        sched = BackgroundScheduler(daemon=True)
        sched.add_job(
            lambda: self._send_stats_update(subscribers),
            'interval',
            days=1
        ) 
        sched.start()

    def _send_stats_update(self, subscribers):
        data = api.get_stats("Indonesia")
        sby_data = api.get_surabaya_stats()

        body = "% s\n\n--------------------------------------------------------\n% s"% (
            utils.parse_data_to_stats(data),
            utils.parse_sby_data_to_stats(sby_data)
        )

        for to in subscribers:
            self.client.messages.create(
                from_=self.from_,
                body=body,
                to="whatsapp:+% s"% to
            )
            

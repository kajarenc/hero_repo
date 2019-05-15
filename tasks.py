import os
import telegram
from celery import Celery
from celery.schedules import crontab

from database import User, session

app = Celery('tasks', broker="amqp://guest:guest@rabbitmq:5672")


@app.task
def send_telegram_message(user_id):
    user = session.query(User).get(user_id)
    telegram_token = os.environ["TELEGRAM_TOKEN"]
    bot = telegram.Bot(token=telegram_token)
    bot.send_message(chat_id=user.chat_id, text="Test message, post_id={}".format(user.last_post_id))

    user.last_post_id += 1
    session.commit()


@app.task
def send_posts_to_users():
    # TODO optimize work with db, investigate sqlalchemy init right way
    users = session.query(User).all()
    for user in users:
        send_telegram_message.delay(user.id)


app.conf.beat_schedule = {
    "send_posts_to_users": {
        "task": "tasks.send_posts_to_users",
        "schedule": crontab()
    }
}

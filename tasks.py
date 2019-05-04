import telegram
from celery import Celery
from celery.schedules import crontab

app = Celery('tasks', broker="amqp://guest:guest@rabbitmq:5672")


@app.task
def send_telegram_message(chat_id):
    bot = telegram.Bot(token="665864512:AAHJ7mnoPo7KhrJx7XKwUoEFRgmjQXRWkYo")
    bot.send_message(chat_id=chat_id, text="Test message")


@app.task
def send_posts_to_users():
    # TODO get users from database
    users = [1, 2]

    for _ in users:
        # TODO use celery chunks here
        send_telegram_message.delay(59911481)


app.conf.beat_schedule = {
    "send_posts_to_users": {
        "task": "tasks.send_posts_to_users",
        "schedule": crontab()
    }
}

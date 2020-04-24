--------


/anaconda3/envs/web/bin/python -m gunicorn main:app

heroku logs -a kouvaris-io-blog --tail

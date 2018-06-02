# Daily Quote
Everyday in the morning, you can get a quote from [BrainyQuote](https://www.brainyquote.com) to your phone. Have a nice day!

# How to ?
- You need sign up a account in [Twilio](https://www.twilio.com) to get account_sid and auth_token.
- Sign up a account heroku. Then install [HerokuCLI](https://devcenter.heroku.com/articles/heroku-cli)
- Create Procfile:
```
clock python qoutes.py
```
- Git clone and push it
```
cd DailyQuotes/
heroku git:remote -a dailyqoutes
git add *
git commit -m "anything"
git push heroku master
```
- Config
```
heroku config:set TWILIO_ACCOUNT_SID=your_account_sid
heroku config:set TWILIO_AUTH_TOKEN=auth_token
heroku ps:scale clock=1
```

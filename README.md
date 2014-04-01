This is the repository for coffeehous.es.

Keep an eye on it. :)


# Setup:
heroku addons:add memcachier --app coffeehouses
heroku addons:add redistogo:nano --app coffeehouses
heroku addons:add heroku-postgresql --app coffeehouses
heroku addons:add pgbackups:auto-month --app coffeehouses
heroku addons:add pointdns --app coffeehouses
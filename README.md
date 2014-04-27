This is the repository for coffeehous.es.

Keep an eye on it. :)


# Setup:
heroku addons:add memcachier --app coffeehouses
heroku addons:add redistogo:nano --app coffeehouses
heroku addons:add heroku-postgresql --app coffeehouses
heroku addons:add pgbackups:auto-month --app coffeehouses


Dev Env Setup.:
# Install Java7: http://www.oracle.com/technetwork/java/javase/downloads/jdk7-downloads-1880260.html
# Install maven (?!?!@)
# Install neo4j
# Install the gremlin plugin, building from source (Thus the maven dependency. FML. What is this, 1998?)
# https://github.com/neo4j-contrib/gremlin-plugin.git
# On the unzip step, you need the `/usr/local/Cellar/neo4j/2.0.1/libexec` path
# Finally, run neo4j start.  Running it earlier will make maven fail. Frankly the whole *thing* feels like fail.  I blame Java.

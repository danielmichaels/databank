# Postgres

## Pg Docker

I spent a long time figuring this out. When creating a postgres container in 
docker-compose, the service name must correspond with the db_host name used
to create the database. This appears to be because `postgres` is the default 
created user, and when you try any action on the database it looks for this user.

In my case, I was setting the names to something else and getting an error about
being unable to resolve `postgres` user on the network. Which now makes sense
as it would be trying to do actions on that URL.

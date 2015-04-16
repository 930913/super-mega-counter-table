# Super Mega Counter Table

This is an entry for Riot's League of Legends API challenge that generates a visualisation of how each champion counters one another.

## Workings

config.py contained the configuration for the directory and api key
```python
api_key="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
dir="./matches/"
```

get_matches.py was executed every five minutes by cron. This populated the directory with the matches from the bucket list.

parse_matches.py was then executed to produce a winmap file.

The winmap file could be hosted separately, or copied into supermegacountertable.html to render the visualisation.


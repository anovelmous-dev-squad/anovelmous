# Anovelmous

[![Build Status](https://travis-ci.org/anovelmous-dev-squad/anovelmous.svg?branch=master)](https://travis-ci.org/anovelmous-dev-squad/anovelmous)
[![Code Climate](https://codeclimate.com/github/anovelmous-dev-squad/anovelmous/badges/gpa.svg)](https://codeclimate.com/github/anovelmous-dev-squad/anovelmous)

Anonymous + Novel. Write together as a community to create a collective narrative.

## Concept

 - Strangers create a narrative, word-by-word

 - Every 10 seconds, contributors vote with an allowed vocabulary for the next word

 - Grammar checker enforces readability

Constraints create interesting and creative situations.

Constraints are a way to game-ify some aspect of communication.

 - Messages... with 140 character limits = Twitter
 - Photos... purposefully, permanently deleted = Snapchat
 - Videos... limited to 7 seconds = Vine
 - Novels.. one word at a time, together = Anovelmous

### Prewriting

Good literature needs prior thought.

It also needs *characters*, *places*, and *plot items*.

Before we start a novel, we need to do the following:

  1. Figure out a vague back-of-book summary
  2. Craft some characters, places, and plot items
  3. (Proto) Name it

These steps will happen in sequence, each after a certain amount of time to
allow for reddit-style voting to occur on contributions.

The word-by-word contribution will begin once the prewriting rounds are completed.

## So how does it play. Tell me.

Every 10 seconds, a voting round ends. During each round, an author may cast a vote for the next word in the novel.
However, the author has a limited pool of words, to be expanded by the top contributors.
If the author's votes are consistently being selected for the novel, he/she will be able to add new words to the vocabulary.


## Development

Make sure you have a clean [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

Install the necessary dependencies

    pip install -r requirements.txt


Set up any necessary development environment variables or configure them in a hidden file like .env

For example: (this app uses postgres)

    export DATABASE_URL="postgres://<user>:<password>@<host>:<port>/<database_name>"
    export CORS_WHITELIST="localhost:<other_port_num>,localhost:<again>"
    export DJANGO_DEBUG=True

Now, it's just typical django application setup:

    python manage.py migrate

If you don't have nltk data on your local machine already:

    python -c "import nltk; nltk.download()"

Create a superuser

    python manage.py createsuperuser

Finally, run a one-off command to populate the db with fixture data.

    python manage.py loaddata datadump.json


You should now be able to run the app locally for testing and development!

    python manage.py runserver


#### NLTK Issues

You may not have NLTK data installed on your system.
If this is the case, follow the procedure described [on their website](http://www.nltk.org/data.html) in order to
download the necessary corpora.

(This app is currently only using the brown corpora, but plans to expand to more in the future.)

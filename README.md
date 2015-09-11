# Anovelmous

Anonymous + Novel. Write together as a community to create a collective narrative.

## How to play

Every **x** seconds, a voting round ends. During each round, an author may cast a vote for the next word in the novel.
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

Now, it's just typical django application setup:

    python manage.py syncdb
    python manage.py migrate
    
Finally, run a one-off command to populate the initial `Token` vocabulary.

    python manage.py populate_vocabulary
    

You should now be able to run the app locally for testing and development!
    
    python manage.py runserver
    

#### NLTK Issues

You may not have NLTK data installed on your system. 
If this is the case, follow the procedure described [on their website](http://www.nltk.org/data.html) in order to
download the necessary corpora. 

(This app is currently only using the brown corpora, but plans to expand to more in the future.)
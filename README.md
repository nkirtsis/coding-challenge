# coding-challenge

## Notes

* `config.py` is the config file of the app, it holds db credentials, so plz update them in order for the app to see the db
  * I used a postgres instance with a `contentful` database (usualy a proper dev environment holds prod and test dbs, I used the same one for simplicity) 
* data is usualy not part of a repo, I just included it in order to be ready for you to consume
  * `data/` contains the 2 files from the gist provided to me
  * `test_data/` contains data for unit testing
* run `python etl.py` to load the data into the db and transform it
* run `python unit_testing.py` to run the unit tests of the app

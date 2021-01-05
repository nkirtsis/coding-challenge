# coding-challenge

## Notes

* `config.py` is the config file of the app, it holds db credentials, so plz update them in order for the app to see the db
  * I used a postgres instance with a `contentful` database (usualy a proper dev environment holds prod and test dbs, I used the same one for simplicity) 
* data is usualy not part of a repo, I just included it in order to be ready for you to consume
  * `data/` contains the 2 files from the gist provided to me
  * `test_data/` contains data for unit testing
* run `python init.py` to create the load/test schema/tables and load the orgs data into the db
* launch the rabbitmq server (used Pika Python client, plz install it if missing)
* run `python send.py` to start the producer
  * producer will send a random date event every `busy_time` secs (from `config.py`)
* run `python receiver.py` to start the consumer
  * consumer will store the events every time `mini_batch_size` limit reached (from `config.py`)
* run `transform.py` to transform the data into the db
  * the script could be triggered after each push in the db (when data comes continuously there is no reason to wait for the whole input), I decided to implement it like this for simplicity (consumer should be independent from transform/ETL logic and I wanted to avoid implementing a trigger in this context) 
* run `python unit_testing.py` to run the unit tests of the app

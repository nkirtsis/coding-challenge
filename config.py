
# test db should be different than prod db, I use the same for simplicity
postgres = {
	"dbname": 	"contentful",
	"user": 	"nikolaos.kyrtsis", 
	"password": ""	
}

input_data = {
	"min_date":		"2020-12-05",
	"max_date":		"2020-12-12",
	"data_dir": 	"data/",
	"orgs_file": 	"orgs_sample.json",
	"events_file": 	"events_sample.json"
}

test_data = {	
	"data_dir": 	"test_data/",
	"input_file": 	"input.txt",
	"input_json": 	"input.json"
}

postgres = {
	"dbname": 	"contentful",
	"user": 	"nikolaos.kyrtsis", 
	"password": ""	
}

rabbitmq = {
	"host":				"localhost",
	"queue":			"hello",
	"busy_time":		"1",
	"mini_batch_size":	"5"
}

input_data = {
	"data_dir": 	"data/",
	"orgs_file": 	"orgs_sample.json",
	"events_file": 	"events_sample.json"
}

test_data = {	
	"data_dir": 	"test_data/",
	"input_file": 	"input.txt",
	"input_json": 	"input.json"
}

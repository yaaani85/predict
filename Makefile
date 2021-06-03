requirements:
	pipenv lock -r > requirements.txt

build:              
	brane unpublish -f predicting 1.0.0
	brane remove -f predicting
	brane build container.yml
	brane push predicting 1.0.0

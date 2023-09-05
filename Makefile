build:
	docker build -t py_module:latest -f docker/Dockerfile .

test:
	docker run py_module:latest

pylint:
	pylint ./*
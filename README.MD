## Description
This repository contains a collection of useful Python modules designed to simplify various tasks. The implemented modules include:
- Implemented modules:
    - `parse_time_delta:` Module for parsing time intervals and representing it in seconds.
    - `merge_iterables:` Module for combining and sorting the contents of iterators.
    - `reverse_number:` Мodule for reversing the digits of numerical values.

In addition to the modules, this project offers streamlined development features:
- `Docker Image:` A pre-configured Docker image is provided, containing all necessary dependencies for seamless deployment and testing.
- `Pipeline Integration:` Implemented pipelines streamline code testing processes, ensuring code quality and reliability.

## Dependencies
Ensure you have the following software versions installed on your system:
- Docker version 23.0.3
- GNU Make 4.2.1

## Building the project image
To build the Docker image for the project, simply run:
- `make build`

## Running Tests
Run the test suite using the following command:
- `make test`

## Running Pylint
Perform Pylint code analysis by executing:
- `make pylint`
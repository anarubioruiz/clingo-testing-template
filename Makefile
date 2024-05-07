ROOT_DIR := $(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

.PHONY: install unittest run pythonpath

pythonpath:
	@echo "Setting PYTHONPATH..."
	@export PYTHONPATH=$(ROOT_DIR)

install:
	@echo "Installing dependencies..."
	@pip3 install -r requirements.txt

unittest: pythonpath
	@echo "Running tests with pytest..."
	@pytest-3 test/ -v -s # Add -s to see print statements

run: pythonpath
	clingo src/engine.lp src/knowledge.lp -n0

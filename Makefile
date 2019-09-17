.PHONY: build
build:
	@docker build . -t auto-shutdown:latest

.PHONY: run
run:
	# @docker run --rm -e AWS_ACCESS_KEY_ID=$(AWS_ACCESS_KEY_ID) -e AWS_SECRET_ACCESS_KEY=$(AWS_SECRET_ACCESS_KEY) auto-shutdown:latest
	@docker run --rm auto-shutdown:latest

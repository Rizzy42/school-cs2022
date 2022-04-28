FROM alpine:3.15.4
COPY Pipfile Pipfile.lock ./
RUN apk update && apk upgrade && \
		apk add py3-pip && \
			adduser -h /home/appuser -s /bin/bash -D appuser
USER appuser
WORKDIR /home/appuser
ENV PATH "$PATH:/home/appuser/.local/bin"
RUN pip install pipenv && \
		pipenv install --system		
COPY . ./
ENTRYPOINT [ "python3", "main.py" ]
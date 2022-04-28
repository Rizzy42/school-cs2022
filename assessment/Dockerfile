# Alpine Linux is the lightest linux container image (5 MB BASE!) and hence the most appropriate for this project
FROM alpine:latest
# When we install pipenv to install the dependencies the executable is installed to here
ENV PATH "$PATH:/home/root/.local/bin"
RUN	mkdir src
COPY . ./src/
RUN apk update && \
		apk add py3-pip binutils && \
			adduser -h /home/appuser -s /bin/sh -D appuser && \
				pip install pipenv && \	
					cd ./src && \
						pipenv install --system && \		
							pyinstaller --onefile main.py --distpath /home/appuser && \
								cd .. && \
									rm -r src && \
										pip uninstall pipenv -y && \
											apk del py3-pip binutils
USER appuser
ENTRYPOINT [ "./main" ]
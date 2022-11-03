FROM python:3.9-slim


COPY . .
RUN python3 -m pip install --upgrade build
RUN python3 -m build
RUN python3 -m pip install ./dist/secscanner2junit-0.1.12.tar.gz

ENTRYPOINT ["ss2ju"]

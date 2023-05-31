FROM public.ecr.aws/lambda/python:3.10

RUN mkdir -p /app
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]
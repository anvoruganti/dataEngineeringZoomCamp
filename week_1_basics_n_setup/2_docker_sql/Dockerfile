#This file contains all the set of instructions 
#to build the docker image for the pipeline
# this is like a shell script written in the cloud course 

FROM python:3.9.1


RUN pip install pandas


# # Path: /app
WORKDIR /app
COPY pipeline.py pipeline.py


# ENTRYPOINT [ "bash" ]
ENTRYPOINT [ "python", "pipeline.py"]



# # docker build -t pipeline .
# # docker run -it pipeline
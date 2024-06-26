# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create directory local
RUN mkdir /todoapi

# clone from repo
# RUN git clone https://github.com/ramses2099/todosapi.git /todoapi

# Set the working directory to /todoapi
# that directory.
WORKDIR /todoapi

# Copy all source code to the todoapi directory
COPY . /todoapi/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

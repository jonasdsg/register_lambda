FROM public.ecr.aws/lambda/python:3.9

RUN yum update -y
RUN yum install mesa-libGL -y
RUN python3.9 -m pip install --upgrade pip
RUN yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm &&\
    yum makecache &&\
    yum -y install zbar
# Copy function code
COPY . ${LAMBDA_TASK_ROOT}

# Install the function's dependencies using file requirements.txt
# from your project folder.

COPY requirements.txt  .
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "app.handler" ]
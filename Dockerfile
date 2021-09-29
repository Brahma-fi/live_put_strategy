FROM public.ecr.aws/lambda/python:3.8

# Copy function code
COPY ./ ${LAMBDA_TASK_ROOT}

# make home directory as temp very important if you are using external packages.
ENV HOME /tmp
# installing gcc for web3 package
RUN yum install gcc -y

#enable node version
RUN curl -sL https://rpm.nodesource.com/setup_10.x | bash -

RUN yum install nodejs -y

# install ganache
RUN npm install -g ganache hardhat

# install all required packages
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# install the solidity packages
RUN python3 -c "from app import init;init()"


# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "app.lambda_handler"]
# Live Put Strategy 


## Introduction

This repository contains python scripts that are used by [Brahma Finance](https://brahma.fi/) to run the synthetic short put option strategies live on ethereum mainnet. 


## Structure

The repo is structured as follows:

[scripts/](https://github.com/Brahma-fi/live_put_strategy/blob/master/scripts/) folder contains the python files used for interacting with interacting with contracts and constructing the signal for ETH-Put vault which is live [here](https://www.brahma.fi/vaults/12345).

[contracts/](https://github.com/Brahma-fi/live_put_strategy/blob/master/contracts/) folder contains contract files related to aastra vaults.

[app.py](https://github.com/Brahma-fi/live_put_strategy/blob/master/app.py) main code for ```strategy```, which call's the underlying mainnet contract functions.

## Deployment

The deployment is done on aws-lambda with trigger set to cloud watch events. 
You can check the docker file how the lambda image is constructed [here](https://github.com/Brahma-fi/live_put_strategy/blob/master/Dockerfile).

## Community

If you have any suggestions for the repor or bugs to report please reach out to us on our [discord](https://discord.com/invite/ndVKhgE7wf)




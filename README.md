<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

**Table of Contents** _generated with [DocToc](https://github.com/thlorenz/doctoc)_

-   [Grover](#grover)
-   [
    Grover
    ](#grover) - [
    An easy interface to Grover (https://github.com/rowanz/grover)
    ](#an-easy-interface-to-grover-httpsgithubcomrowanzgrover)
-   [Installation](#installation)
    -   [Colab](#colab)
    -   [Kaggle](#kaggle)
    -   [GCP](#gcp)
        -   [Vscode remote setup](#vscode-remote-setup)
    -   [Contributing](#contributing)
    -   [Authors](#authors)
    -   [License](#license)
    -   [Acknowledgements](#acknowledgements)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Grover

<h1 align='center'>
    Grover
</h1>

<h4 align='center'>
    An easy interface to Grover (https://github.com/rowanz/grover)
</h4>

<p align='center'>
    <a href="https://forthebadge.com">
        <img src="https://forthebadge.com/images/badges/made-with-python.svg" alt="forthebadge">
    </a>
    <a href="https://github.com/prettier/prettier">
        <img src="https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square" alt="code style: prettier" />
    </a>
    <a href="https://opensource.org/licenses/Apache-2.0">
        <img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" alt="License: Apache 2.0">
    </a>
    <a href="http://makeapullrequest.com">
        <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" alt="PRs Welcome">
    </a>
    <a href="https://github.com/bkkaggle/pytorch_zoo/pulls">
        <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/bkkaggle/grover">
    </a>
</p>

<p align='center'>
    <a href='#installation'>Installation</a> •
    <a href='#documentation'>Documentation</a> •
    <a href='#contributing'>Contributing</a> •
    <a href='#authors'>Authors</a> •
    <a href='#license'>License</a>
</p>

# Installation

## Colab

## Kaggle

## GCP

-   `cloud compute instances create grover --zone="us-west1-b" --image-family="pytorch-latest-cu100" --image-project=deeplearning-platform-release --maintenance-policy=TERMINATE --accelerator="type=nvidia-tesla-v100,count=1" --metadata="install-nvidia-driver=True" --preemptible --boot-disk-size="100GB" --custom-cpu=8 --custom-memory=16`
-   `gcloud compute ssh grover`
-   `sudo apt-get update`
-   `sudo apt-get upgrade`
-   `git clone https://github.com/bkkaggle/grover.git`
-   `cd grover`
-   `conda create -y -n grover python=3.6 && source activate grover && pip install -r requirements-gpu.txt`
-   `python download_model.py base`

### Vscode remote setup

-   install https://marketplace.visualstudio.com/items?itemName=rafaelmaiolla.remote-vscode on vscode
-   `cmd-shift-p` and type Remote: Start Server
-   `gcloud compute ssh grover --ssh-flag="-R 52698:localhost:52698"`
-   `sudo apt -y install ruby && sudo gem install rmate`
-   to edit a file run `rmate path/to/file`

## Contributing

This repository is still a work in progress, so if you find a bug, think there is something missing, or have any suggestions for new features, feel free to open an issue or a pull request. Feel free to use the library or code from it in your own projects, and if you feel that some code used in this project hasn't been properly accredited, please open an issue.

## Authors

-   _Rowan Zellers_ - _Owner of the original repository_
-   _Bilal Khan_ - _Forked the repository and added some features_

## License

This project is licensed under the Apache 2.0 license as in (https://github.com/rowanz/grover) - see the [license](LICENSE) file for details

## Acknowledgements

This project contains code from (https://github.com/rowanz/grover)

This README is based on (https://github.com/bkkaggle/pytorch_zoo)

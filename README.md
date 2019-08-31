# Grover

# Installation

## GCP

### Create a VM

-   `cloud compute instances create grover --zone="us-west1-b" --image-family="pytorch-latest-cu100" --image-project=deeplearning-platform-release --maintenance-policy=TERMINATE --accelerator="type=nvidia-tesla-v100,count=1" --metadata="install-nvidia-driver=True" --preemptible --boot-disk-size="100GB" --custom-cpu=8 --custom-memory=16`

### Setup the VM

-   `gcloud compute ssh grover`
-   `sudo apt-get update`
-   `sudo apt-get upgrade`

### Install docker and docker-compose

-   `sudo apt-get install -y apt-transport-https ca-certificates curl gnupg-agent software-properties-common`
-   `curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -`
-   `sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"`
-   `sudo apt-get update`
-   `sudo apt-get install -y docker-ce docker-ce-cli containerd.io`
-   `sudo curl -L "https://github.com/docker/compose/releases/download/1.23.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose`
-   `sudo chmod +x /usr/local/bin/docker-compose`
-   `base=https://github.com/docker/machine/releases/download/v0.16.0 && curl -L $base/docker-machine-$(uname -s)-$(uname -m) >/tmp/docker-machine && sudo install /tmp/docker-machine /usr/local/bin/docker-machine`

### Vscode remote setup

-   install https://marketplace.visualstudio.com/items?itemName=rafaelmaiolla.remote-vscode on vscode
-   `cmd-shift-p` and type Remote: Start Server
-   `gcloud compute ssh grover --ssh-flag="-R 52698:localhost:52698"`
-   `sudo apt -y install ruby && sudo gem install rmate`
-   to edit a file run `rmate path/to/file`

### Setup the grover docker container

-   `git clone https://github.com/bkkaggle/grover.git`
-   `cd grover`
-   `docker-compose up -d`
-   `docker-compose run grover sh`

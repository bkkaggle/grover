# Grover

# Installation

## GCP

### Create a VM

-   `cloud compute instances create grover --zone="us-west1-b" --image-family="pytorch-latest-cu100" --image-project=deeplearning-platform-release --maintenance-policy=TERMINATE --accelerator="type=nvidia-tesla-v100,count=1" --metadata="install-nvidia-driver=True" --preemptible --boot-disk-size="100GB" --custom-cpu=8 --custom-memory=16`

### Setup the VM

-   `gcloud compute ssh grover`
-   `sudo apt-get update`
-   `sudo apt-get upgrade`

## Vscode remote setup

-   install https://marketplace.visualstudio.com/items?itemName=rafaelmaiolla.remote-vscode on vscode
-   `cmd-shift-p` and type Remote: Start Server
-   `gcloud compute grover --ssh-flag="-R 52698:localhost:52698"`
-   `sudo apt -y install ruby && sudo gem install rmate`
-   to edit a file run `rmate path/to/file`

-   `git clone https://github.com/bkkaggle/grover.git`

# Installing Auto Archiver

```{toctree}
:depth: 1
:hidden:

configurations.md
config_cheatsheet.md
```

There are 3  main ways to use the auto-archiver:
1. Easiest: [via docker](#installing-with-docker)
2. Local Install: [using pip](#installing-locally-with-pip)
3. Developer Install: [see the developer guidelines](../development/developer_guidelines)


But **you always need a configuration/orchestration file**, which is where you'll configure where/what/how to archive. Make sure you read [orchestration](#orchestration).


## Installing with Docker

[![dockeri.co](https://dockerico.blankenship.io/image/bellingcat/auto-archiver)](https://hub.docker.com/r/bellingcat/auto-archiver)

Docker works like a virtual machine running inside your computer, it isolates everything and makes installation simple. Since it is an isolated environment when you need to pass it your orchestration file or get downloaded media out of docker you will need to connect folders on your machine with folders inside docker with the `-v` volume flag.


1. Install [docker](https://docs.docker.com/get-docker/)
2. Pull the auto-archiver docker [image](https://hub.docker.com/r/bellingcat/auto-archiver) with `docker pull bellingcat/auto-archiver`
3. Run the docker image locally in a container: `docker run --rm -v $PWD/secrets:/app/secrets -v $PWD/local_archive:/app/local_archive bellingcat/auto-archiver --config secrets/orchestration.yaml` breaking this command down:
   1. `docker run` tells docker to start a new container (an instance of the image)
   2. `--rm` makes sure this container is removed after execution (less garbage locally)
   3. `-v $PWD/secrets:/app/secrets` - your secrets folder
      1. `-v` is a volume flag which means a folder that you have on your computer will be connected to a folder inside the docker container
      2. `$PWD/secrets` points to a `secrets/` folder in your current working directory (where your console points to), we use this folder as a best practice to hold all the secrets/tokens/passwords/... you use
      3. `/app/secrets` points to the path the docker container where this image can be found
   4.  `-v $PWD/local_archive:/app/local_archive` - (optional) if you use local_storage
       1.  `-v` same as above, this is a volume instruction
       2.  `$PWD/local_archive` is a folder `local_archive/` in case you want to archive locally and have the files accessible outside docker
       3.  `/app/local_archive` is a folder inside docker that you can reference in your orchestration.yml file 

### Example invocations

The invocations below will run the auto-archiver Docker image using a configuration file that you have specified

```bash
# all the configurations come from ./secrets/orchestration.yaml
docker run --rm -v $PWD/secrets:/app/secrets -v $PWD/local_archive:/app/local_archive bellingcat/auto-archiver --config secrets/orchestration.yaml
# uses the same configurations but for another google docs sheet 
# with a header on row 2 and with some different column names
# notice that columns is a dictionary so you need to pass it as JSON and it will override only the values provided
docker run --rm -v $PWD/secrets:/app/secrets -v $PWD/local_archive:/app/local_archive bellingcat/auto-archiver --config secrets/orchestration.yaml --gsheet_feeder.sheet="use it on another sheets doc" --gsheet_feeder.header=2 --gsheet_feeder.columns='{"url": "link"}'
# all the configurations come from orchestration.yaml and specifies that s3 files should be private
docker run --rm -v $PWD/secrets:/app/secrets -v $PWD/local_archive:/app/local_archive bellingcat/auto-archiver --config secrets/orchestration.yaml --s3_storage.private=1
```

## Installing Locally with Pip

1. Make sure you have python 3.10 or higher installed
2. Install the package with your preferred package manager: `pip/pipenv/conda install auto-archiver` or `poetry add auto-archiver`
3. Test it's installed with `auto-archiver --help`
4. Install other local dependency requirements (for )
5. Run it with your orchestration file and pass any flags you want in the command line `auto-archiver --config secrets/orchestration.yaml` if your orchestration file is inside a `secrets/`, which we advise

### Example invocations

Once all your [local requirements](#installing-local-requirements) are correctly installed, the

```bash
# all the configurations come from ./secrets/orchestration.yaml
auto-archiver --config secrets/orchestration.yaml
# uses the same configurations but for another google docs sheet 
# with a header on row 2 and with some different column names
# notice that columns is a dictionary so you need to pass it as JSON and it will override only the values provided
auto-archiver --config secrets/orchestration.yaml --gsheet_feeder.sheet="use it on another sheets doc" --gsheet_feeder.header=2 --gsheet_feeder.columns='{"url": "link"}'
# all the configurations come from orchestration.yaml and specifies that s3 files should be private
auto-archiver --config secrets/orchestration.yaml --s3_storage.private=1
```

### Installing Local Requirements

If using the local installation method, you will also need to install the following dependencies locally:

1.[ffmpeg](https://www.ffmpeg.org/) - for handling of downloaded videos
2. [firefox](https://www.mozilla.org/en-US/firefox/new/) and [geckodriver](https://github.com/mozilla/geckodriver/releases) on a path folder like `/usr/local/bin` - for taking webpage screenshots with the screenshot enricher
3. (optional) [fonts-noto](https://fonts.google.com/noto) to deal with multiple unicode characters during selenium/geckodriver's screenshots: `sudo apt install fonts-noto -y`.
4. [Browsertrix Crawler docker image](https://hub.docker.com/r/webrecorder/browsertrix-crawler) for the WACZ enricher/archiver



## Developer Install

[See the developer guidelines](../development/developer_guidelines)
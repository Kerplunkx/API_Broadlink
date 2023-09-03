# API for Broadlink A/C Control

This repository contains the code for API, developed with flask, for the A/C control of the LST.

## Prerequisites


- Python 3.x
- Broadlink device
- Flask and Broadlink libraries for Pyhton
- Docker (optional)

## Configuration

### Changes in `constantes.py`

You need to obtain each command for the A/C you want to control and replace it in the `constantes.py` script. Also, you can manually add the IP broadcast address where the broadlink device is connected.

### Changes in `broadlink_control.py`

If you added in `constantes.py` the IP broadcast address, you need to use uncomment line 7 and 10 and comment line 6 and 11.

## Usage

### Clone the Repository

```bash
git clone https://github.com/anoboaveliz/API_Broadlink
cd API_Broadlink
```

### Build and Run the Docker Container

We used Buildx to create docker images for amd64 and arm64, to do that, run the following commands:
```bash
docker buildx create --name mybuilder
docker buildx use mybuilder
sudo docker buildx build --platform linux/amd64,linux/arm64 -t [DOCKER-HUB_ACCOUNT/IMAGE_NAME:TAG] --push .
```

Once the image is created, run the following commands:

```bash
docker pull [DOCKER-HUB_ACCOUNT/IMAGE_NAME:TAG]
docker run [IMAGE_NAME:TAG]
```

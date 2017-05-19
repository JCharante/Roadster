# smootor
Reimplementation of frc5687/2017-protobot in Python.

## 1. Setup

### 1.1 Install python3.6

### 1.2 Install virtualenv


### 1.3 Setup virtualenv

```bash
$ virtualenv -p python3.6 .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

## 2. Deploying to roboRIO

If connected over usb cable,

```bash
$ python robot.py deploy --skip-tests --robot 172.22.11.2 -n
```

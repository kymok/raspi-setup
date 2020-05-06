# raspi-setup

## About

kymok raspi setup script

## Usage

### Local setup: `local/local_setup.py`

This script prepares wi-fi connection and SSH.

```
python3 local_setup.py
```

Destination directory (e.g. `/Volumes/boot/`), wi-fi SSID and password will be asked. You can automate these input like this:

```
python3 local_setup.py < password.txt
```

where `password.txt` is

```
/volumes/boot/
your_ssid
your_psk
```

### Raspberry Pi Setup: `remote/raspi_setup.sh`

This script does following:

- Sets up a new user.
- Changes SSH port to 50022.
- Disables auto login.
- Locks default `pi` user.
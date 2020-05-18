# CrazyPainter(DEMO)
*Put a image download as your desktop background*

Set a cronjob (or systemd service) that runs in every 1 minutes to automatically get the
picture.

**This is a DEMO. The program is still building...**

## Supported Desktop Environments
### Tested
* Unity 7
* Mate 1.8.1
* Pantheon
* LXDE
* OS X
* GNOME 3
* Cinnamon 2.8.8
* KDE

### Not Supported
* any other desktop environments that are not mentioned above.

## Installation
* You need a valid python3 installation

```
# Set CrazyPainter to be called periodically
	## Add execute authority
		chmod +x <INSTALLATION_PATH>
    ## Either set up a cronjob
        crontab -e

        ### Add the line:
        */1 * * * * <INSTALLATION_PATH> # command line arguments here
```

where INSTALLATION_PATH is the path of main.py.

## Uninstallation

```
# Either remove the cronjob
crontab -e    
    # Remove the line
    */1 * * * * <INSTALLATION_PATH> # command line arguments here
```

## Attributions
Thanks to *[boramalper](https://github.com/boramalper)* for the [himawaripy](https://github.com/boramalper/himawaripy)


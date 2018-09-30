## IDA Wrapper(a.k.a IDrillerA_Pro)

An IDA_Wrapper for linux, shipped with an Function Identifier. It works well with Driller on static linked binaries.

- Sigfunc for Static Binaries

When we use Angr based SE tools, e.g. Driller, on static linked binaries, it's slow for SE engine to solve complicated constraints created in lib functions. So we make use of IDA's **F.L.A.I.R.** tech, to identify lib functions in static binaries, and **hook** them when entering symbolic execution engine.


### Usage

0. init requirements.
1. move idapro folder to ~/.idapro, `cp -r ./idapro ~/ && mv ~/idapro ~/.idapro` (or you will have to click at GUI.)
2. `python setup.py -b ./test/pwn20 -o ./test_result`

### Requirement

- sigs, from sig-database
- ida for linux, this repo contains an 6.4 version
- Xvfb:
`sudo apt-get install xvfb x11-xkb-utils xfonts-100dpi xfonts-75dpi xfonts-scalable xfonts-cyrillic x11-apps libfreetype6:i386 libsm6:i386 libice6:i386 libsm6:i386 libxt6:i386 libxrender1:i386 libfontconfig1:i386 libcups2:i386 libxext6:i386`
- idaq:
`sudo apt-get install -y lib32gcc1 libc6-i686:i386 libfontconfig:i386 libfreetype6:i386 libglib2.0-0:i386 libpython2.7:i386 libsm6:i386 libssl-dev:i386 libstdc++6:i386 libxext6:i386 libxrender1:i386 lsb-core python-dev`


### Thanks

Thanks for @qldxsun for IDA tech support!


### Notes

https://github.com/intezer/docker-ida is an docker container for IDA linux

https://gist.github.com/williballenthin/1c6ae0fbeabae075f1a4 is an docker file for building an wine-based ida in an docker.

These tools are both useful. However if your resources are limited, IDA_Wrapper will be the best choise.

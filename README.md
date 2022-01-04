![electrum-stak](icons/electrum-github.png)
> Please note that it is an old project created for the not supported (anymore) cryptocurrency STRAKS. I decided to publish it to the open-source community, so everyone can use it for their own purposes.
____________________________________
**__WARNING: Do NOT use the Electrum-STAK wallet to manage a STRAKS Masternode__**
____________________________________

```
  Licence: MIT Licence
  Origin Author: Thomas Voegtlin
  Port Maintainer: STRAKS Developers (Electrum-STAK)
  Language: Python
  Homepage: https://straks.tech/#wallets
```

#### Getting started

Electrum-STAK is a pure python application. If you want to use the
Qt interface, install the Qt dependencies

    sudo apt-get install python3-pyqt5

If you downloaded the official package (tar.gz), you can run
Electrum-STAK from its root directory, without installing it on your
system; all the python dependencies are included in the 'packages'
directory. To run Electrum-STAK from its root directory, just do

    ./electrum-stak

You can also install Electrum-STAK on your system, by running this command

    sudo apt-get install python3-setuptools
    python3 setup.py install

This will download and install the Python dependencies used by
Electrum-STAK, instead of using the 'packages' directory.

If you cloned the git repository, you need to compile extra files
before you can run Electrum-STAK. Read the next section, "Development
Version".


#### Development version

Check out the code from Github

    git clone https://github.com/straks/electrum-stak.git
    cd electrum-stak

Need lyra2rev2_hash

    pip3 install https://github.com/straks/lyra2re-hash-python/archive/master.zip

Run install (this should install dependencies)

    python3 setup.py install

Compile the icons file for Qt

    sudo apt-get install pyqt5-dev-tools
    pyrcc5 icons.qrc -o gui/qt/icons_rc.py

Compile the protobuf description file

    sudo apt-get install protobuf-compiler
    protoc --proto_path=lib/ --python_out=lib/ lib/paymentrequest.proto

Create translations (optional)

    sudo apt-get install python-requests gettext
    ./contrib/make_locale


#### Creating Binaries

To create binaries, create the 'packages' directory

    ./contrib/make_packages

This directory contains the python dependencies used by Electrum-STAK.

##### Mac OS X / macOS

```
    # On MacPorts installs: 
    sudo python3 setup-release.py py2app
    
    # On Homebrew installs: 
    ARCHFLAGS="-arch i386 -arch x86_64" sudo python3 setup-release.py py2app --includes sip
    
    sudo hdiutil create -fs HFS+ -volname "Electrum-STAK" -srcfolder dist/Electrum-STAK.app dist/electrum-stak-VERSION-macosx.dmg
```

##### Windows

See `contrib/build-wine/README` file.


##### Android

See `gui/kivy/Readme.txt` file.

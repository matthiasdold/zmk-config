# Github approach
This was the start using the action to build the ZMK files, but is very slow for trying out new layouts

--> **AFTER** a lot of reconsidering, I will stick with the github approach as the build chain for local builds seems to consume `>3GB` of disk space!!!!

# Manual approach
This is following the [native](https://zmk.dev/docs/development/local-toolchain/setup/native) approach from ZMK using a isolated python env for `west` and then building locally on the system native compiler.

#### Installation

Getting the dependencies as listed [here](https://zmk.dev/docs/development/local-toolchain/setup/native), then :

```
git clone https://github.com/zmkfirmware/zmk.git
cd zmk
python3 -m venv .west_py_venv
source .west_py_venv/bin/activate.fish
pip install -U pip
pip install west
west init -l app/
west update
west zephyr-export
pip install -r zephyr/scripts/requirements-base.txt
```

Next, getting the [zephyr SDK](https://docs.zephyrproject.org/3.5.0/develop/getting_started/index.html#install-zephyr-sdk).

```
cd ~
wget https://github.com/zephyrproject-rtos/sdk-ng/releases/download/v0.16.3/zephyr-sdk-0.16.3_macos-x86_64.tar.xz
wget -O - https://github.com/zephyrproject-rtos/sdk-ng/releases/download/v0.16.3/sha256.sum | shasum --check --ignore-missing
```




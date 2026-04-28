
# Cyberdeck
This cyberdeck is for open-air cracking, encrypted messaging, and general misuse of hardware for the sake of fun and aesthetic. 

# Setup
setup can be annoying, we've focused on steamlinign the proccess as much as possible

## hardware (BOM)


 - Laptop
 - Display
 - Raspberry Pi Pico
 - Input Kit
 - Flipper Zero
 - Cabling

## Input kit
the input kit is fairly easy to assemble. the kit has 1 LED (RGB 4pin), 30 buttons, 30 diodes, and the PCB. solder the diodes, then buttons. 

## Setup Instructions

Just plug in the pico and the flipper, then run the setup script.
Running setup:
```
git clone https://github.com/TheHolyTerranEmperor/argcyberdeck.git
mv argcyberdeck /
cd /argcyberdeck
chmod +x ./setup.sh
./setup.sh
```

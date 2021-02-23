# HTB-TCP-Switcher [![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/intent/tweet?text=Check%20out%20HTP-TCP-Switcher%20on%20github.&url=https://github.com/DEMON1A/HTB-TCP-Switcher&via=DemoniaSlash&hashtags=htb,hackthebox)
HackTheBox OVPN Config Switcher From UDP Into TCP Over 443.

# What's HTB-TCP-Switcher? :worried:
- In some countries like Egypt. VPN connections is blocked over UDP. But since they can't access the TLS packets. You can bypass this by making your connection over TLS. HTB allowed connections over TLS to let users in countries thath blocks the VPN Connections to use their service. But most of the users don't really know how to swtich from UDP to TCP on the OVPN Config **( Including me, thanks to some friend who told me how to swtich it )**. So i wrote a small script to auto swtich your config from UDP into TCP and genarte a new condig.

## Script Installation: :hearts:
```
git clone https://github.com/DEMON1A/HTB-TCP-Switcher
cd HTB-TCP-Switcher/
pip3 install -r requirements.txt
python3 main.py [OPTIONS]
```

## Usage: :open_mouth:
### Options:
- `-f` , `--file`
- `-o` , `--output` , `default="configs"`

### Examples:
```
python3 main.py -f /home/user/Downloads/user.ovpn
```

```
python3 main.py -f /home/user/Downloads/user.ovpn -o outputFolderName
```

## Found This Script Helpful? :dizzy:
- Giving it a star :star: will be great and i will be thankful for that. that will help the repo to be visible to more people.

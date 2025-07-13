import requests


# How to install earlier versions of packages
# pip3 install requests==2.32.3
# pip3 install 'package'=='version'
# pip3 install requests==2.32.*:install the latest compatible version
# pip3 install 2.*
# pip3 uninstall requests
response = requests.get("http://google.com")
print(response)

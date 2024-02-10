import subprocess


binary_networks=subprocess.check_output(['netsh','wlan','show','network'])
decoded_network = binary_networks.decode('ascii')
print(decoded_network)
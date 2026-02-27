import subprocess, os
def connect_to_vpn():
    comando = "fortivpn --server vpn.empresa.com --vpnuser usuario --password clave"
    try:
        subprocess.run(comando, shell=True, check=True)
        print("VPN conectada exitosamente.")
    except subprocess.CalledProcessError:
        print("Error al conectar la VPN.")
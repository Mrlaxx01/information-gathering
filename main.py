import socket
import requests

while True:
    common_ports = {
        21: "FTP",
        22: "SSH",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        143: "IMAP",
        443: "HTTPS",
        3306: "MySQL",
        8080: "HTTP-Alt"
    }

    print("=== Website Information Gathering ===")
    url = input("Masukkan link website (contoh: https://example.com): ")

    
    hostname = url.replace("http://", "").replace("https://", "").split("/")[0]

    print(f"\n[+] Hostname: {hostname}")

    try:
        ip = socket.gethostbyname(hostname)
        print(f"[+] IP Address: {ip}")
    except:
        print("[-] Tidak bisa mendapatkan IP Address")

    
    print("\n[+] Port Scan:")
    for port, service in common_ports.items():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((hostname, port))
        if result == 0:
            print(f"    Port {port} OPEN ({service})")
        sock.close()

    
    print("\n[+] Web Server Info:")
    try:
        response = requests.get(url, timeout=5)
        server = response.headers.get("Server")
        powered_by = response.headers.get("X-Powered-By")

        if server:
            print(f"    Server: {server}")
        if powered_by:
            print(f"    X-Powered-By: {powered_by}")

        print("\n[+] Header Lengkap:")
        for key, value in response.headers.items():
            print(f"    {key}: {value}")
    except Exception as e:
        print(f"[-] Gagal mengambil info web: {e}")

# pip install scapy

from scapy.all import sniff, IP, TCP, UDP, ICMP

def packet_callback(packet):
    print(f"Packet received: {packet.summary()}")

    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        
        print(f"Source IP: {src_ip}")
        print(f"Destination IP: {dst_ip}")

        if TCP in packet:
            print("Protocol: TCP")
        elif UDP in packet:
            print("Protocol: UDP")
        elif ICMP in packet:
            print("Protocol: ICMP")
        else:
            print("Protocol: Other")


        payload = packet.payload
        if payload:
            print(f"Payload Data (hex): {payload.original.hex()}")
            print(f"Payload Data (ascii): {payload.original.decode(errors='ignore')}")


def main():
            print("Starting packet sniffer...")
sniff(prn=packet_callback, store=0, filter="ip", count=10)  


if __name__ == "__main__":
    
    main()

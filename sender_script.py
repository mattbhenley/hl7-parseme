import socket

def send_hl7(file, host='localhost', port=6661):
    with open(file, 'r') as f:
        data = f.read()
    msg = f'\x0b{data}\x1c\x0d'  # HL7 framing
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send(msg.encode())
    s.close()
    print(f"Sent {file} to {host}:{port}")

send_hl7('sample_adt.hl7', port=6661)
send_hl7('sample_oru.hl7', port=6662)

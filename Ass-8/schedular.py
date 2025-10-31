from dataclasses import dataclass

@dataclass
class Packet:
    source_ip: str
    dest_ip: str
    payload: str
    priority: int  # 0 = High, 1 = Medium, 2 = Low

def fifo_scheduler(packet_list: list) -> list:
    # Simply return in arrival order
    return packet_list.copy()

def priority_scheduler(packet_list: list) -> list:
    # Sort by priority (lower number = higher priority)
    return sorted(packet_list, key=lambda pkt: pkt.priority)

if __name__ == "__main__":
    packets = [
        Packet("A", "B", "Data Packet 1", 2),
        Packet("A", "B", "Data Packet 2", 2),
        Packet("C", "D", "VOIP Packet 1", 0),
        Packet("E", "F", "Video Packet 1", 1),
        Packet("G", "H", "VOIP Packet 2", 0)
    ]

    fifo_result = fifo_scheduler(packets)
    print([p.payload for p in fifo_result])
    # ['Data Packet 1', 'Data Packet 2', 'VOIP Packet 1', 'Video Packet 1', 'VOIP Packet 2']

    priority_result = priority_scheduler(packets)
    print([p.payload for p in priority_result])
    # ['VOIP Packet 1', 'VOIP Packet 2', 'Video Packet 1', 'Data Packet 1', 'Data Packet 2']

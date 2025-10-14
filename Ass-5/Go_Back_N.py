# go_back_n.py

import random
import time

def go_back_n_simulation(total_frames, window_size, loss_probability):
    """
    Simulates the Go-Back-N ARQ protocol.

    Args:
        total_frames (int): Total number of frames to send.
        window_size (int): The sender's window size (N).
        loss_probability (float): The probability of a frame being lost.
    """
    base = 0
    
    while base < total_frames:
        print(f"Sending frames from {base} to {min(base + window_size - 1, total_frames - 1)}...")
        
        lost_frame = -1
        for i in range(base, min(base + window_size, total_frames)):
            if random.random() < loss_probability:
                lost_frame = i
                print(f"Frame {i} lost.")
                break 
        
        time.sleep(1)

        if lost_frame != -1:
            print(f"Timeout for Frame {lost_frame}. Sender receives ACK for {lost_frame}.")
            print(f"Retransmitting frames from {lost_frame} onwards.")
            base = lost_frame 
        else:
            ack_received = min(base + window_size, total_frames)
            print(f"Cumulative ACK {ack_received} received.")
            base = ack_received 
        
        print("-" * 30)

if __name__ == "__main__":
    TOTAL_FRAMES = 10
    WINDOW_SIZE = 4
    LOSS_PROBABILITY = 0.2
    
    print("--- Starting Go-Back-N ARQ Simulation ---")
    go_back_n_simulation(TOTAL_FRAMES, WINDOW_SIZE, LOSS_PROBABILITY)
    print("--- Simulation Finished ---")
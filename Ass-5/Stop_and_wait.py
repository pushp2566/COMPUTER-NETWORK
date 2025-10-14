# stop_and_wait.py

import random
import time

def stop_and_wait_simulation(total_frames, loss_probability):
    """
    Simulates the Stop-and-Wait ARQ protocol.
    
    Args:
        total_frames (int): The total number of frames to transmit.
        loss_probability (float): The probability of a frame being lost (0.0 to 1.0).
    """
    current_frame = 0
    while current_frame < total_frames:
    
        print(f"Sending Frame {current_frame}")
        
        time.sleep(1) 
        if random.random() < loss_probability:
            print(f"Frame {current_frame} lost, retransmitting...")
            continue 
        print(f"ACK {current_frame} received")
        current_frame += 1

if __name__ == "__main__":
    TOTAL_FRAMES = 5
    FRAME_LOSS_PROB = 0.3 
    
    print("--- Starting Stop-and-Wait ARQ Simulation ---")
    stop_and_wait_simulation(TOTAL_FRAMES, FRAME_LOSS_PROB)
    print("--- Simulation Finished ---")
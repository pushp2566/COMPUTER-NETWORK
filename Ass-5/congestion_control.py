import matplotlib.pyplot as plt
import random

def tcp_congestion_control_simulation(rounds, ssthresh_initial, loss_events):
    """
    Simulates TCP's congestion window behavior.

    Args:
        rounds (int): The number of transmission rounds to simulate.
        ssthresh_initial (int): The initial slow start threshold.
        loss_events (list): A list of round numbers where a loss will occur.
    """
    cwnd = 1
    ssthresh = ssthresh_initial
    cwnd_history = []
    ssthresh_history = []

    print("Round | CWND | SSTHRESH | Event")
    print("-" * 45)

    for i in range(1, rounds + 1):
        cwnd_history.append(cwnd)
        ssthresh_history.append(ssthresh)
        
        if i in loss_events:
            event = "Packet Loss (Timeout)"
            ssthresh = max(cwnd // 2, 2)
            cwnd = 1
            print(f"{i:<5} | {cwnd:<4} | {ssthresh:<8} | {event}")
            continue
        
        event = "Successful ACK"
        if cwnd < ssthresh:
            event += " (Slow Start)"
            cwnd *= 2
        else:
            event += " (Congestion Avoidance)"
            cwnd += 1
        
        print(f"{i:<5} | {cwnd:<4} | {ssthresh:<8} | {event}")

    plt.figure(figsize=(12, 7))
    plt.plot(range(1, rounds + 1), cwnd_history, marker='o', linestyle='-', label='cwnd')
    plt.plot(range(1, rounds + 1), ssthresh_history, linestyle='--', color='red', label='ssthresh')
    plt.title("TCP Congestion Control Simulation")
    plt.xlabel("Transmission Rounds")
    plt.ylabel("Window Size")
    plt.grid(True)
    plt.legend()
    plt.xticks(range(1, rounds + 1))
    
    # Save the generated plot to a file
    plt.savefig("cwnd_plot.png")
    print("\nPlot saved as cwnd_plot.png")
    plt.show()


if __name__ == "__main__":
    # Parameters
    SIMULATION_ROUNDS = 25
    INITIAL_SSTHRESH = 16
    # Manually define rounds where packet loss will occur to get a clear plot
    LOSS_ROUNDS = [8, 15, 22] 

    tcp_congestion_control_simulation(SIMULATION_ROUNDS, INITIAL_SSTHRESH, LOSS_ROUNDS)
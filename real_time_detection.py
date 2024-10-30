import numpy as np
from collections import deque

def real_time_detection(data_point, window, threshold=0.005):
    """
    Detects anomalies in real-time using a sliding window and Gaussian model.
    
    Parameters:
        data_point (float): Current data point in the stream.
        window (deque): Sliding window of recent data points.
        threshold (float): PDF threshold for identifying anomalies.
    
    Returns:
        bool: True if anomaly is detected, False otherwise.
    """
    # Check if window has reached the required size
    if len(window) < window.maxlen:
        window.append(data_point)
        return False

    mean = np.mean(window)  # Calculate mean of the window
    std_dev = np.std(window)  # Calculate standard deviation

    # Skip anomaly check if standard deviation is zero
    if std_dev == 0:
        return False

    # Calculate PDF value for anomaly detection
    pdf_value = (1 / (np.sqrt(2 * np.pi * std_dev**2))) * np.exp(-(data_point - mean)**2 / (2 * std_dev**2))
    window.append(data_point)  # Update window with new data point

    # Return True if PDF is below threshold (indicating anomaly)
    return pdf_value < threshold

def simulate_real_time_stream(length=1000, seasonal_period=50, noise_level=5):
    """
    Simulates a real-time data stream, detecting anomalies at each data point.
    """
    window = deque(maxlen=100)  # Initialize sliding window
    for i in range(length):
        seasonal_value = 10 * np.sin(2 * np.pi * i / seasonal_period)
        base_value = 80
        noise = np.random.normal(0, noise_level)
        data_point = base_value + seasonal_value + noise
        
        # Check for anomaly
        if real_time_detection(data_point, window):
            print(f"Anomaly detected at data point {i}: {data_point}")

if __name__ == "__main__":
    simulate_real_time_stream()

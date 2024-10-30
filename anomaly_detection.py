# Importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from collections import deque
import os

def detect_anomalies_streaming(data_stream, window_size=100, threshold=0.005):
    # Initialize a deque to maintain a sliding window of recent data points
    window = deque(maxlen=window_size)
    anomalies = []  # List to store detected anomalies
    
    for i, point in enumerate(data_stream):
        # Validate each data point to ensure it's numeric
        if not isinstance(point, (float, int)):
            raise ValueError("Data stream values must be numeric.")
            
        window.append(point)  # Add the current point to the sliding window
        
        # Only proceed if the window is full
        if len(window) == window_size:
            mean = np.mean(window)  # Calculate the mean of the current window
            std_dev = np.std(window)  # Calculate the standard deviation
            
            # If standard deviation is zero, skip anomaly detection
            if std_dev == 0:
                continue
            
            # Calculate the probability density function (PDF) value for the current point
            pdf_value = (1 / (np.sqrt(2 * np.pi * (std_dev**2)))) * np.exp(-(point - mean)**2 / (2 * (std_dev)**2))
            
            # Check if the PDF value is below the specified threshold, indicating an anomaly
            if pdf_value < threshold:
                anomalies.append((i, point))  # Store the index and value of the anomaly
                print(f"Anomaly detected at point {i}: {point}")
    
    return anomalies  # Return the list of detected anomalies
    
def simulate_data_stream(length=1000, seasonal_period=50, noise_level=5):
    """
    Simulates a data stream with a sinusoidal pattern, seasonal variation, and noise.
    """
    data = []  # List to hold the simulated data points
    for i in range(length):
        # Create a seasonal value based on a sine function
        seasonal_value = 10 * np.sin(2 * np.pi * i / seasonal_period)
        base_value = 80  # Base value around which data points fluctuate
        noise = np.random.normal(0, noise_level)  # Generate random noise
        data_point = base_value + seasonal_value + noise  # Combine base, seasonal, and noise
        data.append(data_point)  # Add the data point to the list
    
    return data  # Return the list of simulated data points

def plot_anomalies(data_stream, anomalies, save_path='output.png'):
    """
    Plots the data stream and highlights detected anomalies.
    """
    plt.figure(figsize=(15, 5))  # Set the figure size for the plot
    plt.plot(data_stream, label='Data Stream', color='blue', alpha=0.6)  # Plot the data stream

    # If there are detected anomalies, plot them
    if anomalies:
        anomaly_indices = [record[0] for record in anomalies]  # Extract indices of anomalies
        anomaly_values = [record[1] for record in anomalies]  # Extract values of anomalies
        plt.scatter(anomaly_indices, anomaly_values, color='red', label='Anomalies', marker='x', s=100)  # Highlight anomalies

    plt.title('Data Stream with Detected Anomalies')  # Set plot title
    plt.xlabel('Time')  # Set x-axis label
    plt.ylabel('Value')  # Set y-axis label
    plt.axhline(y=np.mean(data_stream), color='green', linestyle='--', label='Mean Value')  # Draw mean line
    plt.axhline(y=np.mean(data_stream) + 2 * np.std(data_stream), color='orange', linestyle='--', label='Upper Threshold')  # Draw upper threshold
    plt.axhline(y=np.mean(data_stream) - 2 * np.std(data_stream), color='orange', linestyle='--', label='Lower Threshold')  # Draw lower threshold
    plt.legend()  # Show legend
    
    # Save the plot to the specified path
    directory = os.path.dirname(save_path)
    if directory:
        os.makedirs(directory, exist_ok=True)  # Create directory if it does not exist
    
    try:
        plt.savefig(save_path)  # Save the plot
        print(f"Plot saved as {save_path}")
    except Exception as e:
        print(f"Could not save plot: {e}")  # Handle any errors that occur during saving
    finally:
        plt.show()  # Display the plot

def main():
    # Simulate a data stream with specific parameters
    data_stream = simulate_data_stream(length=1000, seasonal_period=50, noise_level=5)
    
    # Print the shape of the data
    print(f"The shape of the data: {len(data_stream)}")
    
    # Detect anomalies in the data stream
    anomalies = detect_anomalies_streaming(data_stream, window_size=100, threshold=0.005)
    
    # Plot the data stream and highlight the anomalies
    plot_anomalies(data_stream, anomalies)

if __name__ == "__main__":
    main()  # Execute the main function if the script is run directly

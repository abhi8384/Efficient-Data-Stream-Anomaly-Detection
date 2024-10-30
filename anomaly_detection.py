import numpy as np
import matplotlib.pyplot as plt
from collections import deque
import os

# Let's start by defining a function that will help us detect anomalies in a continuous stream of data
def detect_anomalies_streaming(data_stream, window_size=100, threshold=0.005):
    # We'll use a sliding window to track recent data points. This will help us look for unusual patterns.
    window = deque(maxlen=window_size)
    anomalies = []  # A list to store the points we consider anomalies

    # Now, let’s go through each point in our data stream
    for i, point in enumerate(data_stream):
        # First, let's make sure each data point is a number. If not, we'll raise an error.
        if not isinstance(point, (float, int)):
            raise ValueError("Data stream values must be numeric.")

        # Add this point to our window
        window.append(point)

        # Once our window is full, we can start checking for anomalies
        if len(window) == window_size:
            mean = np.mean(window)  # Calculate the average of the points in the window
            std_dev = np.std(window)  # Calculate how spread out the values are from the mean

            # If all values are identical, there's no point in checking for anomalies, so we'll skip this one
            if std_dev == 0:
                continue

            # Now we use probability to see if this point is typical or an outlier
            pdf_value = (1 / (np.sqrt(2 * np.pi * (std_dev**2)))) * np.exp(-(point - mean)**2 / (2 * (std_dev)**2))

            # If this probability is below our threshold, we mark it as an anomaly
            if pdf_value < threshold:
                anomalies.append((i, point))  # Store where and what the anomaly is
                print(f"Anomaly detected at point {i}: {point}")

    # We’re done! Return the list of anomalies we've found
    return anomalies

# This function will create a synthetic data stream with a mix of predictable patterns and random noise
def simulate_data_stream(length=1000, seasonal_period=50, noise_level=5):
    data = []  # This will hold our generated data points
    for i in range(length):
        seasonal_value = 10 * np.sin(2 * np.pi * i / seasonal_period)  # Create a wave pattern for seasonality
        base_value = 80  # Set a baseline around which our data fluctuates
        noise = np.random.normal(0, noise_level)  # Add a little randomness
        data_point = base_value + seasonal_value + noise  # Combine everything to create our point
        data.append(data_point)  # Add this point to our data stream

    # All set! Return our synthetic data stream
    return data

# A simple function to visualize the data stream and any detected anomalies
def plot_anomalies(data_stream, anomalies, save_path='output.png'):
    plt.figure(figsize=(15, 5))  # Set up our plot size
    plt.plot(data_stream, label='Data Stream', color='blue', alpha=0.6)  # Plot the main data stream

    # If there are anomalies, let’s highlight them on the plot
    if anomalies:
        anomaly_indices = [record[0] for record in anomalies]  # Get where anomalies are
        anomaly_values = [record[1] for record in anomalies]  # Get the values of anomalies
        plt.scatter(anomaly_indices, anomaly_values, color='red', label='Anomalies', marker='x', s=100)

    # Adding labels and details to make our plot easy to understand
    plt.title('Data Stream with Detected Anomalies')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.axhline(y=np.mean(data_stream), color='green', linestyle='--', label='Mean Value')  # Average line
    plt.axhline(y=np.mean(data_stream) + 2 * np.std(data_stream), color='orange', linestyle='--', label='Upper Threshold')  # Upper limit line
    plt.axhline(y=np.mean(data_stream) - 2 * np.std(data_stream), color='orange', linestyle='--', label='Lower Threshold')  # Lower limit line
    plt.legend()

    # Make sure we save the plot where requested
    directory = os.path.dirname(save_path)
    if directory:
        os.makedirs(directory, exist_ok=True)

    # Let's save the plot and show it in case we want a quick look
    try:
        plt.savefig(save_path)
        print(f"Plot saved as {save_path}")
    except Exception as e:
        print(f"Could not save plot: {e}")
    finally:
        plt.show()

# This is our main function where everything ties together
def main():
    # Simulate a data stream for us to work with
    data_stream = simulate_data_stream(length=1000, seasonal_period=50, noise_level=5)

    # Let's take a look at how much data we have
    print(f"The shape of the data: {len(data_stream)}")

    # Run our anomaly detection function
    anomalies = detect_anomalies_streaming(data_stream, window_size=100, threshold=0.005)

    # Plot the data and any detected anomalies
    plot_anomalies(data_stream, anomalies)

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
    

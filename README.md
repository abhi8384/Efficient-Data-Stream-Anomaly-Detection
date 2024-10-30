**Efficient Data Stream Anomaly Detection**

## Project Description

This project provides a Python-based solution for detecting anomalies in a continuous data stream, simulating real-time sequences of floating-point numbers that may represent metrics such as financial transactions or system performance indicators. The goal is to identify unusual patterns, such as significantly high values or deviations from expected norms.

### Objectives

1. **Algorithm Selection**
Objective: Select a robust statistical algorithm that can identify unusual patterns in a continuous data stream with low latency.
Approach: Use a Gaussian-based statistical model with a sliding window to monitor and detect anomalies in real-time. Points that significantly deviate from the window's mean are flagged based on a probability density function (PDF).

2. **Data Stream Simulation**
Objective: Create a synthetic stream to replicate continuous floating-point data with realistic seasonal and random variations.
Approach: Generate synthetic data points with a sinusoidal trend and noise. This data structure simulates metrics that commonly fluctuate over time, such as financial transaction amounts or system metrics.

3. **Anomaly Detection**
Objective: Efficiently detect deviations from the expected values in the continuous stream.
Approach: Track a sliding window of recent values and compute the mean and standard deviation dynamically. If a data point has a PDF value below a specified threshold, it is marked as an anomaly, helping to capture significant deviations from typical patterns.

4. **Optimization**
Objective: Ensure efficient data handling and minimal memory usage for real-time streaming.
Approach: Use a deque structure to maintain a fixed-size window, allowing for efficient updates as new data points enter the stream. This approach keeps memory usage stable, supporting real-time processing.

5. **Visualization**
Objective: Provide a clear visual representation of detected anomalies.
Approach: Plot the data stream and mark anomalies with distinct colors. Include mean and threshold lines to contextualize outliers, and save the plot to a specified directory.

### Usage

Static Data Stream Simulation:

Run anomaly_detection.py to generate a data stream, detect anomalies, and plot the results.

Real-Time Detection Simulation:

Use real_time_detection.py to see a continuous anomaly detection simulation for real-time data processing.

### Files

anomaly_detection.py: Main script for generating synthetic data, detecting anomalies, and visualizing results.

real_time_detection.py: An alternative script demonstrating real-time detection for continuous input.

output/anomaly_plot.png: Example output plot showing detected anomalies in the data stream.

### Features:

Data Stream Simulation: Generates synthetic data with seasonal and random noise components to simulate realistic streaming data.

Efficient Anomaly Detection: A sliding window keeps the memory footprint low, enabling real-time anomaly detection.

Clear Visualization: Detected anomalies are highlighted, and threshold lines provide additional context, with automatic saving for easy access.

### Usage Scenarios:

Real-time monitoring of time-series data: for detecting unusual patterns in financial transactions, IoT sensor readings, or network traffic.

Batch processing of historical data: to uncover hidden patterns in past data streams, useful for retrospective analysis in machine learning and statistical analysis.

### Error Handling and Validation

Data Validation: Ensures data is numeric; otherwise, raises an error.

File Handling: Creates necessary directories and handles any errors in saving the plot, providing feedback if the save operation fails.

### Conclusion

This project provides a reliable, efficient solution for anomaly detection in continuous data streams, simulating real-time analysis. It's well-suited for metrics monitoring in applications like finance and system diagnostics.

### Requirements

* Python 3.x
* `numpy` for data handling and statistical calculations
* `matplotlib` for visualization
* `collections` for efficient data handling in sliding windows

To install required libraries, run:
```bash
pip install -r requirements.txt
```

![realtime_testing_report for project](https://github.com/user-attachments/assets/d454e36b-724f-4eef-b62b-9ee94af43466)

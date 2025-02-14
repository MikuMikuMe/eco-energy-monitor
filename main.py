Creating a comprehensive Python program for real-time energy consumption monitoring and optimization involves leveraging various libraries and technologies. For simplicity, this example will simulate data to demonstrate the core components of such an application. In a real-world scenario, you would interface with actual smart devices or sensors.

Here's a basic structure of the program:

```python
import time
import random
import logging

# Configure logging for the application
logging.basicConfig(filename='eco_energy_monitor.log', level=logging.INFO, 
                    format='%(asctime)s %(levelname)s:%(message)s')

class EnergyMonitor:
    def __init__(self, devices=None):
        # Initialize with a set of devices
        if devices is None:
            devices = {}
        self.devices = devices  # e.g., {'Fridge': 100, 'Washer': 500}
        self.total_consumption = 0  # Total energy consumption in watts

    def simulate_real_time_data(self):
        """Simulate energy consumption data by updating devices randomly."""
        try:
            for device, power in self.devices.items():
                # Simulate device activity
                change = random.randint(-10, 10)  # Random fluctuation
                new_power = max(0, power + change)
                self.devices[device] = new_power
                logging.debug(f"{device}: New power level is {new_power}W")
        
        except Exception as e:
            logging.error("Error during simulation of real-time data", exc_info=e)
            raise

    def calculate_total_consumption(self):
        """Calculate the total energy consumption."""
        try:
            self.total_consumption = sum(self.devices.values())
            logging.info(f"Total energy consumption: {self.total_consumption}W")
        
        except Exception as e:
            logging.error("Error during calculation of total consumption", exc_info=e)
            raise

    def optimize_energy_usage(self):
        """Optimize energy usage by suggesting which devices to turn off."""
        try:
            if self.total_consumption > 1000:  # An arbitrary threshold for optimization
                # Suggest turning off the highest consuming device
                highest_device = max(self.devices, key=self.devices.get)
                logging.warning(f"Consider turning off {highest_device} to save energy.")
        
        except Exception as e:
            logging.error("Error during energy optimization", exc_info=e)
            raise

def main():
    # Define some devices with initial power usage
    initial_device_states = {
        'Fridge': 150,
        'Washer': 500,
        'Heater': 800,
        'Air Conditioner': 1200,
        'Lighting': 300
    }

    monitor = EnergyMonitor(initial_device_states)

    try:
        while True:
            # Simulate and monitor in real-time
            monitor.simulate_real_time_data()
            monitor.calculate_total_consumption()
            monitor.optimize_energy_usage()

            # Sleep for a while before the next update
            time.sleep(5)

    except KeyboardInterrupt:
        logging.info("Terminated by user.")
    except Exception as e:
        logging.error("An unexpected error occurred in the main loop", exc_info=e)
    finally:
        logging.info("Eco-Energy Monitor shutting down.")

if __name__ == "__main__":
    main()
```

### Key Features of the Program:
1. **Simulation**: Since we don't have access to actual hardware, the program simulates energy consumption data using random fluctuations. 

2. **Logging**: The program uses Python's `logging` module to keep track of information and errors. Real-time data changes and optimization suggestions are logged.

3. **Error Handling**: Each critical section includes try-except blocks to capture and log exceptions that may occur during execution.

4. **Optimization Logic**: Simple logic to suggest turning off the highest-consuming device when the total energy consumption goes beyond a predefined threshold.

### Notes:
- **Real-time Data**: In practice, replace the `simulate_real_time_data` method with data gathering from smart home devices/APIs.
- **Energy Optimization**: The optimization method can be enriched with machine learning models or more nuanced rules for predictive energy saving.
- **Persistence**: To make it practical, consider storing historical data in a database for analysis and reporting.

This program structure provides a groundwork that you can expand for handling authentic data and enhanced features in a complete smart home energy monitoring system.
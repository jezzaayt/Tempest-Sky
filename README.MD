# Tempest Sky

Tempest Sky is a weather application that fetches weather data for a specified city using the OpenWeatherMap API and displays it using Dear PyGui.

## Requirements

- Python 3.7+
- requests
- python-dotenv
- dearpygui
- geopy


## Usage

1. Run the application:
    ```sh
    python main.py
    ```

2. Enter the city name in the input box and select the measurement unit (metric, imperial, or kelvin).

3. Click the "Search" button to fetch and display the weather data.


## Dependencies

- requests: For making HTTP requests to the OpenWeatherMap API.
- `python-dotenv`: For loading environment variables from a `.env` file.
- dearpygui: For creating the graphical user interface.
- geopy: For converting city names to latitude and longitude coordinates.


## Acknowledgements

- [OpenWeatherMap](https://openweathermap.org/) for providing the weather data API.
- [Dear PyGui](https://github.com/hoffstadt/DearPyGui) for the GUI framework.
- [Geopy](https://github.com/geopy/geopy) for the geocoding library.
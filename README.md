This Weather Application is a Python-based project that provides real-time weather information for any city using the WeatherAPI service. It features a dynamic wallpaper that changes based on the time of day, with images for sunrise, daytime, sunset, and night. The application uses Tkinter to create an intuitive graphical interface, integrating `requests` for API calls and `pillow` for image handling. Users can easily access current temperature, wind speed, humidity, and UV index. This project offers a visually appealing, user-friendly way to monitor weather conditions while keeping the desktop environment interactive and responsive.



### Guide: Integrating the WeatherAPI in the Project

The Weather Application uses the `weatherapi.com` service to fetch real-time weather data. Follow these steps to set up and configure the API for this project:

#### Step 1: Register and Get an API Key
1. Visit the [WeatherAPI Website](https://www.weatherapi.com/).
2. Sign up for a free account and log in.
3. Navigate to your dashboard and generate an API key.

#### Step 2: Configure the API in the Project
1. Open the file `weatherAPI.py`.
2. Locate the line in the `weather(city)` function that reads:
   ```python
   data = requests.get(f"https://api.weatherapi.com/v1/current.json?key=/*YOUR API KEY*/&q={city}")
   ```
3. Replace `/*YOUR API KEY*/` with your actual API key:
   ```python
   data = requests.get(f"https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q={city}")
   ```

#### Step 3: Understand the API Call
- The API request URL includes:
  - **`key`**: Your unique API key.
  - **`q`**: The query parameter, representing the city name or coordinates.
- The API returns data in JSON format, which includes fields like:
  - `current.temp_c`: Current temperature in Celsius.
  - `current.wind_mph`: Wind speed in miles per hour.
  - `current.humidity`: Humidity percentage.
  - `current.uv`: UV index value.

#### Step 4: Handling the API Response
- The response is stored in `formatedData = data.json()`.
- Access required fields from `formatedData` and display or use them as needed in the application.

#### Troubleshooting
- **Invalid API Key**: Double-check the API key for any typographical errors.
- **City Not Found**: Ensure the city name is spelled correctly or use the city’s coordinates (latitude and longitude) for better accuracy.
- **API Limit Exceeded**: The free tier has limited calls; consider upgrading your plan if more requests are needed.

With these steps, you should have the WeatherAPI integrated into the project successfully!



### Required Libraries and Installation Commands

The Weather Application requires several Python libraries for API interaction, GUI development, and image processing. Below is a list of the libraries used in the project along with their installation commands:

1. **Requests**  
   - Used for making HTTP requests to interact with the WeatherAPI.
   - **Installation Command:**
     ```bash
     pip install requests
     ```

2. **Pyttsx3**  
   - Provides text-to-speech capabilities for voice-based weather updates (optional).
   - **Installation Command:**
     ```bash
     pip install pyttsx3
     ```

3. **Pillow (PIL)**  
   - Used for opening, manipulating, and displaying images (e.g., setting background images).
   - **Installation Command:**
     ```bash
     pip install pillow
     ```

4. **Tkinter**  
   - Built-in Python library for creating graphical user interfaces (GUI).
   - **Installation Command (Linux/Unix):**
     ```bash
     sudo apt-get install python3-tk
     ```
   - For Windows, Tkinter is included by default in the Python installation.

5. **JSON**  
   - Built-in Python module for handling JSON data (used to parse API responses).
   - **No separate installation needed** as it is included in the Python standard library.

### Summary Installation Command
To install all the external dependencies at once, run:
```bash
pip install requests pyttsx3 pillow
```

This should set up the environment required to run the Weather Application smoothly!




Thank you for using this Weather Application! Feel free to explore and modify the code to suit your needs. Your feedback is always welcome to help improve the project. Whether you're learning, experimenting, or looking to build on this foundation, enjoy the experience and happy coding!

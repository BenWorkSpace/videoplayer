# Video Player API

This is a FastAPI-based Video Player API that serves an HTML5 video player with multiple quality options.

## Features

- Serve a responsive, dark-themed video player
- Support for multiple video quality options
- Quality selection and fullscreen mode
- Custom player controls using Plyr.js

## Requirements

- Python 3.7+
- FastAPI
- Jinja2

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/video-player-api.git
   cd video-player-api
   ```

2. Install the required packages:
   ```bash
   pip install fastapi uvicorn jinja2
   ```

## Usage

1. Start the server:
   ```bash
   uvicorn main:app --reload
   ```

2. Access the video player at:
   ```bash
   http://localhost:8000/watch/?urls=url1,url2,url3,...
   ```
   Where `url1`, `url2`, `url3`, etc. are the URLs of the video in different qualities.

## API Endpoints

- `GET /`: Welcome message
- `GET /watch/`: Serves the video player HTML page

### Parameters for /watch/

- `urls`: Comma-separated list of video URLs for different qualities

## Customization

You can customize the player appearance by modifying the `watch.html` template in the `templates` directory.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

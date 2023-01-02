# Space Telegram
This code uploads images from Spacex and NASA resources, creates a bot in order to publish photos in a telegram channel. Scripts can be used separately for downloading photos, as well as for automating publication in a telegram channel.

### How to install

Python3 should be already installed.    
It is recommended to use virtual environment for isolating the project:  
```
python3 -m venv myenv
source myenv\bin\activate
```

Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:  
```
pip install -r requirements.txt
```
You need to get a telegram bot API token and telegram channel name, save them in the file `tokens.env` with variable `TELEGRAMBOT_TOKEN`, and telegram channel name which (starts with @) in the variable `TELEGRAM_CHANNEL`.  
This script downloads images from NASA resources, so you need to get your access token on [api.nasa.gov](https://api.nasa.gov/), and save the token in `tokens.env` file, with variable `NASA_API_KEY`.


## How to use
For downloading images use:
- `fetch_nasa_apod_images.py` - downloads space images of a day from NASA. You need to get access token on https://api.nasa.gov , use -t or --token commands and put your token in the command line.  
Example: 
```
$ python3 fetch_nasa_apod_images.py -t yourtoken
```
- `fetch_nasa_epic_images.py` - downloads images from NASA EPIC API.  You need to get access token on [api.nasa.gov](https://api.nasa.gov/), use -t or --token commands and put your token in the command line. 
Example: 
```
$ python3 fetch_nasa_epic_images.py -t yourtoken
``` 
For downlowding desired number of images just put number after command -n or --number.   
Example: 
```
$ python3 fetch_nasa_epic_images.py -n 5
``` 
- `fetch_spacex_images.py` - downloads photos from a spacex rocket launch. By default downloads photos from the latest launch, but you can put desired  launch id using command `'-id' or '--launch id'`  
 Example: 
 ```
 $ python3 fetch_spacex_images.py -id 50291453997_aa715950e7
 ```
 
For running telegram bot use:  

`telegrambot.py` You can choose following arguments:  

- `-t` - for setting up a posting timer in seconds, default time 4 hours(14400 seconds)  
- `-f` - for choosing image folder, default is 'images'   
- `-i` - for posting a specific image from images folder   
```
$ python3 telegrambot.py -t 60
```


### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).

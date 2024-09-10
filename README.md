<div align="center">
  <p>
    <a href="#"><img src="https://github.com/daliondev/MonoLoad/assets/111100025/503ba04a-4843-47d8-a925-974a350352c4" width="auto" height="150px" alt="monoload logo" /></a>
  </p>
  <h1>MonoLoad</h1>
  <p align="center">
	<a href='https://monoload.readthedocs.io/en/latest/?badge=latest'>
    <img src='https://readthedocs.org/projects/monoload/badge/?version=latest' />
</a>
	<a href="https://pypi.org"><img src="https://img.shields.io/badge/python-3.11.4-blue" /></a>
	      <a href="https://github.com/daliondev" alt="Activity">
        <img src="https://img.shields.io/badge/owner-daliondev-red" /></a>
  </p>

</div>



It is a terminal program focused on downloading videos from the YouTube site which seeks to provide different quality formats to the user to download both audio and video files.

## Installation
```cmd
git clone https://github.com/daliondev/MonoLoad.git
```
```cmd
cd \MonoLoad\
```
### Virtual Enviroment
During the installation, it is recommended to create a virtual environment to store the requirements needed to run the program. If you wish to do so, follow the steps below.
```cmd
python -m venv .
```
using the dot flag we can indicate that we want to create the virtual environment in the folder in which we are

### Requirements
At the time of writing this help, the program makes use of few libraries to work, however the main ones are both Pytube and Tqdm and to install them you must do the following
```cmd
pip install -r requirements.txt
```
### Important 
The Pytube library in its ***cipher.py*** file contains a problem decrypting YouTube videos due to the pattern it uses which must be fixed manually in the following path:
```cmd
\MonoLoad\Lib\site-packages\pytube\cipher.py
```
In line number **264** in which the variable of a list is created, we must **change** **all** its content **to the following:**
```python
function_patterns = [
    r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&.*?\|\|\s*([a-z]+)',
    r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])\([a-z]\)',
]
```
## Usage
The use of the program is divided into Download and Multi Download Mode and are determined according to the needs that the user seeks to cover.

### Mono Download and Multi Download
MonoLoad contains two ways to use which vary depending on the needs of each user, if you only want to download a video in mp3 or mp4 format, follow the steps below.

```cdm
python main.py
```


### Demo
The above will open a pop-up window in which you will have the option to download both videos and audios from YouTube, and if necessary you can download several versions in different qualities of the video or audio (This functionality does not limit the download time as it is done in parallel)
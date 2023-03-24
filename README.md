# Flac to Mp3 Algorithm (FFmpeg)

FFmpeg is a powerful open-source software that allows you to manipulate video and audio files. This algorithm will use FFmpeg to convert FLAC audio files to MP3 format.

## Requirements
To build and use this algorithm, you'll need:

1) FFmpeg installed on your computer
2) Python 3 installed on your computer
3) A folder containing the FLAC(or) files you want to convert

## Usage
To convert a folder of FLAC files to MP3 format, follow these steps:

1) Place all of the FLAC files you want to convert into a single folder.
2) In a terminal window, navigate to the folder containing the flac_to_mp3.py script.
3) Run flac_to_mp3.py script


## Customization

This algorithm can be customized to convert any file type to another file type as long as the conversion is compatible with FFmpeg. To do this, simply modify the 'output_filename' extension in the flac_to_mp3.py script to the file extension you would like to covert too.

## Conclusion

In conclusion, building a FLAC to MP3 algorithm with FFmpeg is a relatively simple task that can be accomplished with just a few lines of Python code. By using FFmpeg to perform the actual conversion, it's possible to convert large numbers of audio files quickly and efficiently. This algorithm can also be easily customized to convert other types of files, as long as the conversion is compatible with FFmpeg. If the conversion is not supported by FFmpeg all you need to do is update the subprocess.call on line 62 to use a command library that is compatible with the conversion type you are attempting.

Created By: Maxwell Dalrymple

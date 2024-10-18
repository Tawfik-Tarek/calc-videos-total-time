# 📹 Video Duration Calculator

The **Video Duration Calculator** is a Python script that calculates the total duration of all video files within a specified folder and its subdirectories. It supports a variety of video formats, making it a handy tool for video management.

## 🎯 Features

- **Recursive Search**: Traverse through a specified folder and all its subdirectories to find video files.
- **Duration Calculation**: Accurately calculate the total duration of all found video files.
- **Format Support**: Works with multiple video formats, including:
  - `.mp4`
  - `.avi`
  - `.mov`
  - `.mkv`
  - `.flv`
  - `.wmv`
- **User-Friendly Output**: Displays the total duration in hours, minutes, and seconds.

## 📦 Requirements

To run this script, you will need the following Python package:

- **moviepy**: A Python library for video editing and processing.

### Installation

You can easily install the required package using pip:

```bash
pip install moviepy
```

## 🚀 Usage

### Clone or Download
Clone this repository or download the script to your local machine.

```bash
git clone https://github.com/Tawfik-Tarek/calc-videos-total-time.git
```

### Adjust the Folder Path
Open the script and set the folder path in the `if __name__ == "__main__":` section to point to the folder containing your videos. For example:

```python
folder_path = r"D:\crash_courses\react"  # Adjust to your folder path
```

### Run the Script
Execute the script using Python:

```bash
python video_duration_calculator.py
```

### View the Output
The script will display the total duration of all videos found in the folder and subdirectories.

## 📊 Example Output
Total duration of videos in the folder and subdirectories: 25 hours, 26 minutes, 31 seconds

## 🎉 Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please fork the repository and submit a pull request.

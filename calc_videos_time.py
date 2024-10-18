import os
from moviepy.editor import VideoFileClip


def get_total_video_duration(folder_path):
    total_duration = 0  # in seconds

    # Walk through the folder and all subdirectories
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            if filename.endswith(('.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv')):  # Add more extensions if needed
                video_path = os.path.join(dirpath, filename)  # Create full path to the video file
                try:
                    # Load the video file and get its duration
                    video = VideoFileClip(video_path)
                    total_duration += video.duration
                    video.close()  # Explicitly close the video clip
                except Exception as e:
                    print(f"Error processing {filename}: {e}")

    # Convert the total duration to hours, minutes, and seconds
    total_hours = int(total_duration // 3600)
    total_minutes = int((total_duration % 3600) // 60)
    total_seconds = int(total_duration % 60)

    return total_hours, total_minutes, total_seconds


if __name__ == "__main__":
    folder_path = r"D:\crash_courses\react"  # Adjust to your folder path

    hours, minutes, seconds = get_total_video_duration(folder_path)
    print(f"Total duration of videos in the folder and subdirectories: {hours} hours, {minutes} minutes, {seconds} seconds")
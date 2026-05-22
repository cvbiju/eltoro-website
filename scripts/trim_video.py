from moviepy import VideoFileClip
import os

input_path = "/Users/bchandr1/Downloads/IMG_2072.mov"
output_path = "public/assets/videos/hero-background-trimmed.mov"

print(f"Loading video from {input_path}")
clip = VideoFileClip(input_path)
duration = clip.duration
print(f"Original duration: {duration} seconds")

if duration > 2:
    trimmed_clip = clip.subclipped(0, duration - 2)
    print(f"Trimming to {trimmed_clip.duration} seconds and exporting...")
    trimmed_clip.write_videofile(output_path, codec="libx264", audio_codec="aac", logger=None)
    print("Video trimmed successfully!")
else:
    print("Video is shorter than 5 seconds, cannot trim.")

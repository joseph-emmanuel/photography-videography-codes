import os
from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip
from PIL import Image

# Load the logo image using Pillow
logo_path = "signature_converted.png"
logo = Image.open(logo_path)

# Resize the logo with the updated LANCZOS method
logo_resized = logo.resize((180, 150), Image.LANCZOS)

# Save the resized logo as a temporary file for MoviePy to use
resized_logo_path = "resized_logo.png"
logo_resized.save(resized_logo_path)

# Load the resized logo using MoviePy
logo_clip = ImageClip(resized_logo_path).set_duration(1)  # Create an ImageClip and set its duration

# Create a new folder called "edited_videos" to store the processed videos
edited_folder = "edited_videos"
if not os.path.exists(edited_folder):
    os.makedirs(edited_folder)

# Loop through all video files in the current folder
for filename in os.listdir("."):
    if filename.lower().endswith((".mp4", ".mov", ".avi", ".mkv")):  # Check for video files
        try:
            # Load the video
            video = VideoFileClip(filename)

            # Determine the orientation of the video
            if video.w > video.h:
                # Landscape: position logo at bottom right corner
                position = ("right", "bottom")
            else:
                # Portrait: position logo at bottom left corner
                position = ("left", "bottom")

            # Set the logo's duration to match the video duration
            logo_clip = logo_clip.set_duration(video.duration).set_position(position)

            # Create a composite video with the logo overlay
            final_video = CompositeVideoClip([video, logo_clip])

            # Save the final video to the "edited_videos" folder with the same filename
            edited_path = os.path.join(edited_folder, filename)
            final_video.write_videofile(edited_path, codec="libx264", audio_codec="aac")

            print(f"Processed {filename} successfully.")
        except Exception as e:
            print(f"Error processing {filename}: {e}")

print("All valid video files have been processed and saved in the 'edited_videos' folder.")

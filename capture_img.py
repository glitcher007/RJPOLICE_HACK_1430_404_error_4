import cv2
import time
import os

# Specify the directory path within your repository

imgs_directory = r"C:\Users\glitcher\Desktop\Rj_hackathon_2\venv\imgs"

# Create the "imgs" directory if it doesn't exist
if not os.path.exists(imgs_directory):
    os.makedirs(imgs_directory)

# Specify the file path for the captured frame
output_file_path = os.path.join(imgs_directory, "captured_frame.jpg")


start_time=time.time()
# Open the webcam
cap = cv2.VideoCapture(0)  # 0 represents the default camera, you can change it if you have multiple cameras

# Allow some time for the webcam to initialize
time.sleep(5)

# Start a loop to continuously display frames
while True:
    # Capture a frame
    ret, frame = cap.read()

    # Display the frame
    cv2.imshow("Webcam Feed", frame)

    # Break the loop after 5 seconds
    if time.time() -start_time > 5:
        break

    # Check for 'q' key press to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam
cap.release()

# Save the captured frame as a .jpg file in the "imgs" directory
if ret:
    cv2.imwrite(output_file_path, frame)
    print(f"Frame captured and saved as {output_file_path}")
else:
    print("Failed to capture frame")

# Destroy all OpenCV windows
cv2.destroyAllWindows()

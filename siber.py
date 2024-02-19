# and this code just detects a face


import cv2
import mediapipe as mp

def detect_face(image_path):
    # Initialize mediapipe Face Detection
    mp_face_detection = mp.solutions.face_detection
    face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.3)

    # Read the input image
    image = cv2.imread(image_path)

    # Check if the image is loaded successfully
    if image is None:
        print(f"Error: Unable to load the image at {image_path}")
        return

    # Resize the image
    resized_image = cv2.resize(image, (800, 600))

    height, width, _ = resized_image.shape

    # Convert the BGR image to RGB
    rgb_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)

    # Run face detection
    results = face_detection.process(rgb_image)

    # Check if faces are detected
    if results.detections:
        for detection in results.detections:
            bboxC = detection.location_data.relative_bounding_box
            bbox = int(bboxC.xmin * width), int(bboxC.ymin * height), \
                   int(bboxC.width * width), int(bboxC.height * height)

            # Draw bounding box around the face
            cv2.rectangle(resized_image, bbox, (0, 255, 0), 2)

    # Display the result
    cv2.imshow("Face Detection", resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Replace with the actual image path
    # image_path = r"C:\Users\USER\Desktop\P1110564.JPG"
    # image_path = r"C:\Users\USER\Desktop\output_image.jpg"
    # image_path = r"C:\Users\USER\Desktop\noisy_image.jpg"
    # image_path = r"C:\Users\USER\Desktop\output_image1.jpg"
    # image_path = r"C:\Users\USER\Desktop\20160809_223425.jpg"
    # image_path = "noisy_image3.jpg"
    image_path = "test1.jpg"
    detect_face(image_path)

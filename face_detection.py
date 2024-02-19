# this code detects a face and prints the face landmarks !!!


import cv2
import mediapipe as mp

# Initialize mediapipe Face Detection
mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.3)

# Initialize mediapipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.3, min_tracking_confidence=0.3)

# Read input image
# image = cv2.imread(r"C:\Users\USER\Desktop\noisy_image.jpg")
# image = cv2.imread("noisy_image3.jpg")
# image = cv2.imread(r"C:\Users\USER\Desktop\output_image.jpg")
image = cv2.imread("output_image1.jpg.jpg")

# Resize the entire image
scale_factor = 0.2  # Adjust this factor as needed
image_resized = cv2.resize(image, None, fx=scale_factor, fy=scale_factor)

image_rgb = cv2.cvtColor(image_resized, cv2.COLOR_BGR2RGB)

# Run face detection
results_detection = face_detection.process(image_rgb)
if results_detection.detections:
    for detection in results_detection.detections:
        bboxC = detection.location_data.relative_bounding_box
        ih, iw, _ = image_resized.shape
        x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)

        # Draw bounding box
        cv2.rectangle(image_resized, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Run face mesh on the region of interest
        roi = image_resized[y:y + h, x:x + w]
        results_mesh = face_mesh.process(roi)
        if results_mesh.multi_face_landmarks:
            for face_landmarks in results_mesh.multi_face_landmarks:
                for landmark in face_landmarks.landmark:
                    x_lm, y_lm = int(landmark.x * w), int(landmark.y * h)
                    cv2.circle(image_resized, (x + x_lm, y + y_lm), 2, (255, 0, 0), -1)

# Display the result
cv2.imshow('Resized Face Detection and Landmarks', image_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

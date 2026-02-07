import cv2

def get_external_camera(max_index=5):
    for i in range(1, max_index):  # mulai dari 1 (bukan kamera internal)
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            return cap, i
    return None, None


cap, cam_index = get_external_camera()

if cap is None:
    print("❌ Kamera eksternal tidak ditemukan")
    exit()

print(f"✅ Kamera eksternal dibuka di index {cam_index}")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("External Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

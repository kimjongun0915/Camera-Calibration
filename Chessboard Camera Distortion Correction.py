import numpy as np
import cv2 as cv

# The given video and calibration data
video_file = 'D:/python/calibrate_camera/chessboard.mp4'
K = np.array([[4000, 0, 200],
              [0, 5000, 370],
              [0, 0, 1]])  # 예시 K값
dist_coeff = np.array([
    -0.2852754904152874,
     0.1016466459919075,
    -0.0004420196146339175,
     0.0001149909868437517,
    -0.01803978785585194
])

# Open a video
video = cv.VideoCapture(video_file)
assert video.isOpened(), 'Cannot read the given input, ' + video_file

# Get video FPS and set appropriate wait time
fps = video.get(cv.CAP_PROP_FPS)
wait_time = int(1000 / fps) if fps > 0 else 33  # fallback: 30fps 기준

# Run distortion correction
show_rectify = True
map1, map2 = None, None

while True:
    valid, img = video.read()
    if not valid:
        break

    # Rectify geometric distortion (Alternative: cv.undistort())
    info = "Original"
    if show_rectify:
        if map1 is None or map2 is None:
            h, w = img.shape[:2]
            # 새로운 카메라 행렬로 왜곡 보정 정확도 향상 (선택)
            newK, _ = cv.getOptimalNewCameraMatrix(K, dist_coeff, (w, h), 1)
            map1, map2 = cv.initUndistortRectifyMap(K, dist_coeff, None, newK, (w, h), cv.CV_32FC1)
        img = cv.remap(img, map1, map2, interpolation=cv.INTER_LINEAR)
        info = "Rectified"

    # 화면에 상태 텍스트 표시
    cv.putText(img, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, (0, 255, 0))
    cv.imshow("Geometric Distortion Correction", img)

    # Wait for next frame based on fps
    key = cv.waitKey(wait_time)
    if key == ord(' '):     # Space: 일시정지
        key = cv.waitKey()
    if key == 27:           # ESC: 종료
        break
    elif key == ord('\t'):  # Tab: 왜곡 보정 On/Off
        show_rectify = not show_rectify

video.release()
cv.destroyAllWindows()

# 🎥 카메라 캘리브레이션 및 왜곡 보정 프로그램

## 📌 개요

이 프로그램은 OpenCV를 이용하여 **체스보드 영상에서 이미지를 수동 선택하고**, 선택된 이미지들을 기반으로 **카메라 캘리브레이션**을 수행합니다. 이후 계산된 카메라 행렬 및 왜곡 계수를 이용해 **실시간으로 왜곡 보정을 적용한 영상 출력**도 지원합니다.

---

## 🛠️ 주요 기능

### 1. 영상에서 체스보드 이미지 선택 (`select_img_from_video`)
- `Space` 키: 현재 프레임에서 체스보드 코너 검출 및 확인
- `Enter` 키: 현재 이미지를 보정용으로 선택
- `ESC` 키: 이미지 선택 종료

### 2. 카메라 캘리브레이션 수행 (`calib_camera_from_chessboard`)
- 선택된 이미지에서 체스보드 코너를 검출
- 3D-2D 좌표 매핑을 구성하여 카메라 내부 행렬(K), 왜곡 계수 추정
- RMS reprojection error 출력

### 3. 실시간 왜곡 보정 영상 보기
- `Tab` 키: 왜곡 보정 영상 On/Off 전환
- `Space` 키: 일시 정지
- `ESC` 키: 종료

---

## 🧾 입력 설정

video_file = 'D:/python/calibrate_camera/chessboard.mp4'(주소는 실제 자기 파일의 주소를 써야함)
board_pattern = (6, 8)         # 체스보드 내부 코너 개수
board_cellsize = 0.025         # 한 칸의 실제 크기 (m 또는 cm 등)


## 📷 Camera Calibration Summary

- fx: **631.1237**
- fy: **626.7617**
- cx: **204.1387**
- cy: **363.1584**
- k1: **0.0318**
- k2: **-0.2691**
- p1: **-0.0011**
- p2: **0.0024**
- k3: **0.7316**
- **RMS reprojection error (rmse): 0.4432**

## 🎥 실습 영상

[![실습 영상](https://img.youtube.com/vi/j1Sv2sFp-LA/0.jpg)](https://youtu.be/j1Sv2sFp-LA)

import torch
import cv2
import ultralytics

print("-" * 30)
print(f"1. PyTorch 버전: {torch.__version__}")
print(f"2. 그래픽카드 연결: {'성공!' if torch.cuda.is_available() else '실패(CPU만 사용)'}")
print(f"3. OpenCV 버전: {cv2.__version__}")
print(f"4. YOLO 버전: {ultralytics.__version__}")
print("-" * 30)
print("검토 완료! 에러가 없으면 완벽합니다.")
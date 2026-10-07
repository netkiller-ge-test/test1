# 이미지 리사이징 및 썸네일 생성 헬퍼 모듈
from PIL import Image
import os

def create_thumbnail(image_path, size=(128, 128)):
    """
    주어진 이미지 경로의 파일 크기를 줄여 썸네일로 저장합니다.
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"이미지 파일을 찾을 수 없습니다: {image_path}")
    
    with Image.open(image_path) as img:
        img.thumbnail(size)
        thumb_path = f"thumb_{os.path.basename(image_path)}"
        img.save(thumb_path, "JPEG")
        return thumb_path

def calculate_aspect_ratio(width, height):
    """
    가로, 세로 비율(Aspect Ratio)을 계산합니다.
    """
    if height == 0:
        return 0  # 0으로 나누기 방지
    return round(width / height, 2)

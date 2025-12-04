# 1) 가벼운 Python 런타임 이미지
FROM python:3.11-slim

# 2) 컨테이너 내부 작업 디렉토리 생성
WORKDIR /app

# 3) python 의존성 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4) FastAPI 소스 복사
COPY . .

# 5) 컨테이너가 8000 포트를 노출하도록 명시
EXPOSE 8000

# 6) uvicorn 실행 (uvicorn 기본 포트 8000 사용)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
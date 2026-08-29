# 1. ใช้ Base Image เป็น Python เวอร์ชันเสถียรขนาดเล็ก (Slim) เพื่อไม่ให้เปลืองพื้นที่
FROM python:3.11-slim

# 2. ตั้งค่า Working Directory ภายใน Container
WORKDIR /app

# 3. คัดลอกไฟล์ requirements.txt เข้ามาก่อนเพื่อติดตั้ง Dependencies
COPY requirement.txt .

# 4. ติดตั้ง Library ต่างๆ ที่ระบุไว้ใน requirements.txt โดยไม่เก็บแคชเพื่อลดขนาดไฟล์
RUN pip install --no-cache-dir -r requirement.txt

# 5. คัดลอกซอร์สโค้ด Python ทั้งหมดจากเครื่องของเราเข้าไปใน Container
COPY . .

# 6. สั่งให้ Container รันสคริปต์ scheduler.py ทันทีเมื่อสั่งสตาร์ท Container
CMD ["python", "scheduler.py"]

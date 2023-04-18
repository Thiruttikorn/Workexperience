สิ่งที่ต้องเตรียม
- ติดตั้งโปรแกรม Docker https://www.docker.com/products/docker-desktop/
- เช็ค version 
```
docker --version
docker-compose --version
```
-------------------------------------

1. จัดการโครงสร้างไฟล์ดังนี้
```
.
│ 
└───OASIP-OR-4-front-end
└───OASIP-OR-4-back-end
```
2. 
```
cd /OASIP-OR-4-back-end/DjangoAPI
```
3. สำหรับ Powershell
```
$env:BACKEND_HOST="api.oas.ip"
$env:FRONTEND_HOST="web.oas.ip"
```
สำหรับ CMD
```
set BACKEND_HOST=api.oas.ip
set FRONTEND_HOST=web.oas.ip
```
4.
```
docker-compose up -d mysql-db
```
5.
```
docker-compose up -d  migration backend frontend nginx-proxy
```
6. ไปที่เว็บ api.oas.ip และ web.oas.ip ว่าขึ้นมั้ย?


# DE31-3rd_team3

## 1. 프로젝트 소개
강의간 배운 내용 복습 위주의 프로젝트

## 2. 팀원 소개
- 김하영 
- 김동현
- 조태식
- 유선우

## 3. 프로젝트 레포지토리 구조
``` 
DE31-3rd_team3
├── Crawler   # 크롤러 관련 코드
│   ├── naver_news_crawler.py # 네이버 뉴스 크롤러
│   └── to_database.py # 크롤링한 데이터를 데이터베이스에 저장
├── Frontend  # 프론트엔드 관련 코드
│   ├── 1
│   └── 2
├── Backend   # 백엔드 관련 코드
│   ├── 1
│   └── 2
├── Infra     # 인프라 관련 코드
│   ├── mysql_docker.sh # mysql 도커 컨테이너 실행 스크립트
│   └── 2
├── README.md
└── requirements.txt # python 패키지 목록
```

## 4. Pre-requisite (사전 준비 사항)

### 4.1. Python 설치
- Python 3.10 버전 설치
```bash
sudo apt install python3.10
``` 

### 4.2. Python 패키지 설치
- (선택사항) 가상환경 생성
```bash
python3.10 -m venv venv
source venv/bin/activate
```

- requirements.txt에 있는 패키지 설치
```bash
pip install -r requirements.txt
```

### 4.3. Node.js 설치
- Node.js Stable 버전 설치
```bash
sudo apt install nodejs
sudo apt install npm
sudo npm install -g n
sudo n stable
```

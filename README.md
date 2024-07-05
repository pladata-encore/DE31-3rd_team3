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
│   ├── App.vue # Vue.js 메인 파일
│   └── src    # Vue.js 소스코드
├── Backend   # 백엔드 관련 코드
│   └── api_server.py # FastAPI 서버
├── Infra     # 인프라 관련 코드
│   ├── mysql_docker.sh # mysql 도커 컨테이너 실행 스크립트
│   ├── spark_install.sh # spark 설치 스크립트
│   └── hadoop_install.sh # hadoop 설치 스크립트
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

### 4.3. mecab 설치
- mecab 설치
```bash
bash <(curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh)
```

### 4.4. Node.js 설치
- Node.js Stable 버전 설치
```bash
sudo apt install nodejs
sudo apt install npm
sudo npm install -g n
sudo n stable
```

### 5. 네이버 뉴스 섹션 번호

| 메인 섹션 | 서브 섹션 |
|------|------|
| 100 정치 | 264 청와대 |
|  | 265 국회/정당 |
|  | 268 북한 |
|  | 266 행정 |
|  | 267 국방/외교 |
|  | 269 정치일반 |
||
| 101 경제 | 259 금융 |
|  | 258 증권 |
|  | 261 산업/재계 |
|  | 771 중기/벤쳐 |
|  | 260 부동산 |
|  | 262 글로벌 경제 |
|  | 310 생활경제 |
|  | 263 경제 일반 |
||
| 102 사회 | 249 사건사고 |
|  | 250 교육 |
|  | 251 노동 |
|  | 254 언론 |
|  | 252 환경 |
|  | 59b 인권/복지 |
|  | 255 식품/의료 |
|  | 256 지역 |
|  | 276 인물 |
|  | 257 사회 일반 |
||
| 103 생활/문화 | 241 건강정보 |
|  | 239 자동차/시승기 |
|  | 240 도로/교통 |
|  | 237 여행/레저 |
|  | 238 음식/맛집 |
|  | 376 패션/뷰티 |
|  | 242 공연/전시 |
|  | 243 책 |
|  | 244 종교 |
|  | 248 날씨 |
|  | 245 생활문화 일반 |
||
| 105 IT/과학 | 731 모바일 |
|  | 226 인터넷/SNS |
|  | 227 통신/뉴미디어 |
|  | 230 IT일반 |
|  | 732 보안/해킹 |
|  | 283 컴퓨터 |
|  | 229 게임/리뷰 |
|  | 228 과학 일반 |
||
| 104 세계 | 231 아시아/호주 |
|  | 232 미국/중남미 |
|  | 233 유럽 |
|  | 234 중동/아프리카 |
|  | 322 세계일반 |

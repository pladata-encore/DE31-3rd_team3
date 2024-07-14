import Image from "next/image";
import styles from "@/styles/page.module.css";

import tempImg from "@/images/image.png";

export default function Home() {
  return (
    <main className={styles.main} style={{ justifyContent: "center" }}>
      <div className={styles.description}>
        <h1>뉴스 데이터 확인 서비스입니다.</h1>
      </div>
      <a style={{ margin: "1rem" }}>상단 네비게이션 바의 버튼을 눌러 페이지를 이동해보세요.</a>
      <div className={styles.container}>
        <h2>기능</h2>
        <ul>
          <li>뉴스 검색</li>
          <li>날짜 범위 검색</li>
          <li>뉴스 키워드 시각화</li>
        </ul>
      </div>
    </main>
  );
}

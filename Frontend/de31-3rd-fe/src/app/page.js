import Image from "next/image";
import styles from "@/styles/page.module.css";

import tempImg from "@/images/image.png";

export default function Home() {
  return (
    <main className={styles.main}>
      <div className={styles.description}>
        <h1>Welcome to the DE31-3rd Project!</h1>
        <a>
          This is a project for the DE31-3rd cohort. We are building a full
          stack application using the following technologies:
        </a>
        <ul>
          <li>React</li>
          <li>Next.js</li>
          <li>Node.js</li>
          <li>Express</li>
          <li>MongoDB</li>
        </ul>
      </div>
      <div className={styles.image}>
        {/* get image from public folder */}
        <Image
          src= {tempImg}
          alt="Next.js logo"
          width={500}
          height={500}
        />
      </div>
    </main>
  );
}

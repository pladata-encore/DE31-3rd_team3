import Link from 'next/link';
import styles from '@/styles/page.module.css';

const Navbar = () => {
  return (
    <nav>
      <ul className={styles.ul}>
        <li>
          <Link href="/">Home</Link>
        </li>
        <li>
          <Link href="/rangeView">기간별 데이터</Link>
        </li>
        <li>
          <Link href="/searchView">뉴스 검색</Link>
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;
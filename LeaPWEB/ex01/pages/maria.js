import styles from "../styles/pages/MariaPrea.module.scss";
import Head from "next/head";
import { AiFillHome } from "react-icons/ai";
import Link from "next/link";
import { Footer } from '../components/Footer';
import { RepositoryLink } from '../components/RepositoryLink';
import { MariaPrea } from '../components/MariaPrea';

export default function Home() {
  return (
    <div className={styles.container}>
      <Head>
        <title>LeaPWEB - Maria Preá</title>
      </Head>
      <header>
        <h1>LeaPWEB - Study repository for WEB programming discipline</h1>

        <div>
          <Link href="/">
            <div>
              <AiFillHome />
              <a>Home</a>
            </div>
          </Link>
          <RepositoryLink/>
        </div>
      </header>

      <main>
        <h1>Página Maria Preá 🐾</h1>
      </main>

      <Footer/>
    </div>
  );
}

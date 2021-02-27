import styles from "../styles/pages/Home.module.scss";
import Head from "next/head";
import Link from "next/link";
import { Footer } from "../components/Footer";
import { RepositoryLink } from "../components/RepositoryLink";

export default function Home() {
  return (
    <div className={styles.container}>
      <Head>
        <title>LeaPWEB</title>
      </Head>
      <header>
        <h1>LeaPWEB - Study repository for WEB programming discipline</h1>

        <div>
          <Link href="/maria">
            <div>
              <img src="prea.jpg" alt="preá"></img>
              <a>Maria Preá</a>
            </div>
          </Link>
          <RepositoryLink />
          
        </div>
      </header>

      <main>
        <h1>My "First" Page Next.js 😂</h1>
      </main>

      <Footer />
    </div>
  );
}

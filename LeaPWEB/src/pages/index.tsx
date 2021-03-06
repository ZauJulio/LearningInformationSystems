import styles from "../styles/pages/Home.module.scss";
import Head from "next/head";

import { Header } from "../components/Header";
import { Footer } from "../components/Footer";

export default function Home() {
  return (
    <div className={styles.container}>
      <Head>
        <title>LeaPWEB</title>
      </Head>
      <Header />

      <main>
        <h1>Repository of exercises developed during the WEB Programming course</h1>
      </main>

      <Footer />
    </div>
  );
}

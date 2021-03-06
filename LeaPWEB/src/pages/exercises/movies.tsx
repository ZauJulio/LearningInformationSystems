import styles from "../../styles/pages/Movies.module.scss";
import Head from "next/head";

import { Header } from "../../components/Header";
import { Footer } from "../../components/Footer";

export default function Movies() {
  return (
    <div className={styles.moviesContainer}>
      <Head>
        <title>LeaPWEB - Movies</title>
      </Head>
      <Header />

      <main>
        <h1>Exercise 02: Search Movies 🐾</h1>
      </main>

      <Footer />
    </div>
  );
}

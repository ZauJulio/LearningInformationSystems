import styles from "../../styles/pages/Movies.module.scss";
import Head from "next/head";

export default function Movies() {
  return (
    <div className={styles.moviesContainer}>
      <Head>
        <title>LeaPWEB - Movies</title>
      </Head>
      <main>
        <h1>Exercise 02: Search Movies 🐾</h1>
      </main>
    </div>
  );
}

import styles from "../styles/pages/Maria.module.scss";
import Head from "next/head";
import { AiFillHome } from "react-icons/ai";
import Link from "next/link";
import { Footer } from "../components/Footer";
import { RepositoryLink } from "../components/RepositoryLink";
import { MariaPrea } from "../components/MariaPrea";
import { useState } from "react";

export default function Home() {
  const [adjective, setAdjective] = useState(" ");

  function handleChange(event) {
    setAdjective(event.target.value);
  }

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
          <RepositoryLink />
        </div>
      </header>

      <main>
        <h1>Página Maria Preá 🐾</h1>
        <div>
          <div>
            <label for="changeAdj">O que Maria Preá é?</label>
            <input
              type="text"
              id="changeAdj"
              placeholder="Adjetivo"
              onChange={handleChange}
            />
          </div>
          <MariaPrea adjetivo={adjective} />
        </div>
      </main>

      <Footer />
    </div>
  );
}

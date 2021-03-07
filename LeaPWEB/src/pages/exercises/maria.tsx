import { useState } from "react";
import styles from "../../styles/pages/Maria.module.scss";
import Head from "next/head";

import { MariaPrea } from "../../components/MariaPrea";

export default function Home() {
  const [adjective, setAdjective] = useState(" ");

  function handleChange(event: React.ChangeEvent<HTMLInputElement>) {
    setAdjective(event.target.value);
  }

  return (
    <div className={styles.container}>
      <Head>
        <title>LeaPWEB - Maria Preá</title>
      </Head>

      <main>
        <h1>Exercise 01: Maria Preá 🐾</h1>

        <div>
          <div>
            <label htmlFor="changeAdj">What Mary Preá is?</label>
            <input
              type="text"
              id="changeAdj"
              placeholder="Adjective"
              onChange={handleChange}
            />
          </div>
          <MariaPrea adjetivo={adjective} />
        </div>
      </main>
    </div>
  );
}

import { useState } from "react";
import styles from "../../styles/pages/WhoIsWhat.module.scss";
import Head from "next/head";

import { WhoIsWhat } from "../../components/WhoIsWhat";

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
        <h1>Exercise 01: Who is what?</h1>

        <div>
          <div>
            <label htmlFor="changeAdj">Who is what?</label>
            <input
              type="text"
              id="changeAdj"
              placeholder="Adjective"
              onChange={handleChange}
            />
          </div>
          <WhoIsWhat adjective={adjective} />
        </div>
      </main>
    </div>
  );
}

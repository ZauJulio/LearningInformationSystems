import Head from "next/head";
import dynamic from "next/dynamic";

import styles from "../../styles/pages/ClientSideRendering.module.scss";
import 'leaflet/dist/leaflet.css';

export default function ClientSideRendering() {
  const Map = dynamic(() => import("../../components/Map"), { ssr: false });

  return (
    <div className={styles.clientSideContainer}>
      <Head>
        <title>LeaPWEB - Maria Preá</title>
      </Head>
      <main>
        <Map />
      </main>
    </div>
  );
}

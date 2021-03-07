import React from "react";

import Head from "next/head";

import { GiSeatedMouse } from "react-icons/gi";
import { BiCameraMovie } from "react-icons/bi";
import { useRouter } from "next/router";

import { PageHeaderShortcut } from "../components/PageHeaderShortcut";
import styles from "../styles/pages/Home.module.scss";

export default function Home() {
  const router = useRouter();

  return (
    <div className={styles.container}>
      <Head>
        <title>LeaPWEB</title>
      </Head>

      <main>
        {router.pathname !== "/exercises/maria" && (
          <PageHeaderShortcut href="/exercises/maria" name="Exercise 1">
            <GiSeatedMouse />
          </PageHeaderShortcut>
        )}
        {router.pathname !== "/exercises/movies" && (
          <PageHeaderShortcut href="/exercises/movies" name="Exercise 2">
            <BiCameraMovie />
          </PageHeaderShortcut>
        )}
        <h1>
          Repository of exercises developed during the WEB Programming course
        </h1>
      </main>
    </div>
  );
}

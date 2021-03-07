import React from "react";
import Head from "next/head";

import { GiSeatedMouse } from "react-icons/gi";
import { BiCameraMovie } from "react-icons/bi";

import { Header } from "../../components/Header";
import { Footer } from "../../components/Footer";
import { PageHeaderShortcut } from "../../components/PageHeaderShortcut";

import styles from "../../styles/pages/Exercises.module.scss";

export default function Movies() {
  return (
    <div className={styles.exercisesContainer}>
      <Head>
        <title>LeaPWEB - Exercises</title>
      </Head>
      <Header />

      <main>
        <PageHeaderShortcut href="/exercises/maria" name="Exercise 1">
          <GiSeatedMouse />
        </PageHeaderShortcut>
        <PageHeaderShortcut href="/exercises/movies" name="Exercise 2">
          <BiCameraMovie />
        </PageHeaderShortcut>
      </main>

      <Footer />
    </div>
  );
}

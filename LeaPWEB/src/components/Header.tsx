import React from "react";
import { useRouter } from "next/router";

import { BiCameraMovie } from "react-icons/bi";
import { GiSeatedMouse } from "react-icons/gi";
import { AiFillHome } from "react-icons/ai";

import { PageHeaderShortcut } from "./PageHeaderShortcut";
import { RepositoryShortcut } from "./RepositoryShortcut";

import styles from "../styles/components/Header.module.scss";

export function Header() {
  const router = useRouter();

  return (
    <header className={styles.headerContainer}>
      <h1>LeaPWEB - Study repository for WEB programming discipline</h1>

      <div className={styles.shortcutsContainer}>
        {router.pathname !== "/" && (
          <PageHeaderShortcut href="/" name="Home">
            <AiFillHome />
          </PageHeaderShortcut>
        )}

        <div className={styles.slidableShortcuts}>
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
        </div>

        <RepositoryShortcut />
      </div>
    </header>
  );
}

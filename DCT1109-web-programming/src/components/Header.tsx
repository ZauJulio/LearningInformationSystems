import React from "react";
import { useRouter } from "next/router";

import { AiFillHome } from "react-icons/ai";

import { PageHeaderShortcut } from "./PageHeaderShortcut";
import { RepositoryShortcut } from "./RepositoryShortcut";

import styles from "../styles/components/Header.module.scss";
import { GiEarthAmerica } from "react-icons/gi";

export function Header() {
  const router = useRouter();

  return (
    <header className={styles.headerContainer}>
      <h1>
        <GiEarthAmerica />
        LeaPWEB
      </h1>

      <div className={styles.shortcutsContainer}>
        <div className={styles.slidableShortcuts}>
          {router.pathname !== "/" && (
            <PageHeaderShortcut href="/" name="Home">
              <AiFillHome />
            </PageHeaderShortcut>
          )}
        </div>

        <RepositoryShortcut />
      </div>
    </header>
  );
}

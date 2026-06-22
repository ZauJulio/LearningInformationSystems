import React from "react";

import { AiFillGithub } from "react-icons/ai";

import styles from "../styles/components/PageHeaderShortcut.module.scss";

export function RepositoryShortcut() {
  return (
    <a
      className={styles.headerShortcutContainer}
      href="https://github.com/ZauJulio/LeaPWEB"
      target="_blank"
    >
      <AiFillGithub />
      <p>repository</p>
    </a>
  );
}

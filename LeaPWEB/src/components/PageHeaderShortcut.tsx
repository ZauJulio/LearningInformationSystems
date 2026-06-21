import React from "react";
import Link from "next/link";
import styles from "../styles/components/PageHeaderShortcut.module.scss";

interface PageHeaderShortcutProps {
  href: string;
  name: string;
  children: React.ReactChild | React.ReactChild[];
}

export function PageHeaderShortcut(props: PageHeaderShortcutProps) {
  return (
    <Link href={props.href}>
      <div className={styles.headerShortcutContainer}>
        {props.children}
        <p>{props.name}</p>
      </div>
    </Link>
  );
}

import React from "react";
import styles from "../styles/components/Movie.module.scss";

interface MovieProps {
  name: string;
}

export function Movie(props: MovieProps) {
  return (
    <div className={styles.movieContainer}>
      {props.name}
    </div>
  );
}


import React from "react";
import { MovieData } from "../pages/exercises/Movies";

import styles from "../styles/components/Movie.module.scss";

interface MovieProps {
  movieData: MovieData;
}

export function Movie(props: MovieProps) {
  return (
    <div className={styles.movieContainer}>
      <div className={styles.infosContainer}>
        <h2>{props.movieData.Title}</h2>
        <h3>
          Year: <p>{props.movieData.Year}</p>
        </h3>
      </div>
      <img src={props.movieData.Poster}></img>
    </div>
  );
}

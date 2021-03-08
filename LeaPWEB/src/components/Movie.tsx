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
        <p>
          <h3>
            Year: <text>{props.movieData.Year}</text>
          </h3>
        </p>
      </div>
      <img src={props.movieData.Poster}></img>
    </div>
  );
}

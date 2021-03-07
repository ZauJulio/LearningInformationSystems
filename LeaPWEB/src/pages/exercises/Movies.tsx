import React from "react";
import Head from "next/head";

import { Movie } from "../../components/Movie";
import styles from "../../styles/pages/Movies.module.scss";

interface Rating {
  Source: string;
  Value: string;
}

interface MovieData {
  Title: string;
  Year: number;
  Rated: string;
  Released: string;
  Runtime: string;
  Genre: string;
  Director: string;
  Writer: string;
  Actors: string;
  Plot: string;
  Language: string;
  Country: string;
  Awards: string;
  Poster: string;
  Ratings: Rating[];
  Metascore: number;
  imdbRating: number;
  imdbVotes: number;
  imdbID: string;
  Type: string;
  DVD: string;
  BoxOffice: string;
  Production: string;
  Website: string;
  Response: boolean;
}

interface omdbapiProps {
  Search: MovieData[];
  totalResults: string;
  Response: string;
}

interface MoviesProps {
  data: omdbapiProps;
}

export function Movies({ data }: MoviesProps) {
  return (
    <div className={styles.moviesContainer}>
      <Head>
        <title>LeaPWEB - Movies</title>
      </Head>
      <main>
        <div className={styles.seekerContainer}></div>
        {data.Search.map((m) => (
          <Movie name={m.Title}></Movie>
        ))}
      </main>
    </div>
  );
}

export async function getServerSideProps(context) {
  const res = await fetch(
    `http://www.omdbapi.com/?apikey=${process.env.API_KEY}&s=bagdad`
  );
  const data = await res.json();

  if (!data) {
    return {
      notFound: true,
    };
  }

  return {
    props: { data },
  };
}

export default Movies;

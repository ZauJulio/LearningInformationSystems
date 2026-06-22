import React, { useEffect, useState } from "react";
import Head from "next/head";
import useSWR from "swr";

import { Movie } from "../../components/Movie";
import FormMovie from "../../components/FormMovie";
import styles from "../../styles/pages/Movies.module.scss";
import Pagination from "../../components/Pagination";

interface Rating {
  Source: string;
  Value: string;
}

export interface MovieData {
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

export function Movies() {
  const [titleWanted, setTitleWanted] = useState("");
  const [currentPage, setCurrentPage] = useState(1);
  const [totalResults, setTotalResults] = useState(0);

  const { data } = useSWR([titleWanted, currentPage], async (u) => {
    if (titleWanted === "") return { Search: "" };
    const url = `http://www.omdbapi.com/?apiKey=${process.env.API_KEY}&s=${titleWanted}&page=${currentPage}`;
    const res = await fetch(url);
    const json = await res.json();
    return json;
  });

  function handler(e) {
    if (e.key === "Enter") setTitleWanted(e.target.value);
  }

  const MovieNotFound = () => {
    return <div style={{ justifyContent: "center" }}>Movie Not Found</div>;
  };

  console.log(data);

  return (
    <div className={styles.moviesPage}>
      <Head>
        <title>LeaPWEB - Movies</title>
      </Head>
      <main>
        <FormMovie name="Title" handler={handler} />
        <div className={styles.moviesContainer}>
          {data && data.Search
            ? data.Search.map((movie: MovieData, index: number) => (
                <Movie key={index} movieData={movie} />
              ))
            : titleWanted !== "" && <MovieNotFound />}
        </div>
        {data && data.Search && titleWanted !== "" && (
          <Pagination
            total={data.totalResults / 10}
            current={currentPage}
            handler={setCurrentPage}
          />
        )}
      </main>
    </div>
  );
}

export default Movies;

import React from "react";
import { useRouter } from "next/router";
import Head from "next/head";

import { BiCameraMovie } from "react-icons/bi";
import { RiRoadMapLine } from "react-icons/ri";
import { AiOutlineQuestion } from "react-icons/ai";

import { Topic, TopicDescription } from "../components/Topic";
import styles from "../styles/pages/Home.module.scss";

export default function Home() {
  return (
    <div className={styles.container}>
      <Head>
        <title>LeaPWEB</title>
      </Head>

      <main>
        <div className={styles.topicsContainer}>
          <Topic link="/exercises/WhoIsWhat" logo={<AiOutlineQuestion />}>
            <TopicDescription
              name="Who is what?"
              description="Simple exercise of React components creation. It was
              incremented to use Hook Usestate."
            ></TopicDescription>
          </Topic>

          <Topic link="/exercises/movies" logo={<BiCameraMovie />}>
            <TopicDescription
              name="Movie Search"
              description="Exercise using Getserversideprops and external API consumption
              for film search."
            ></TopicDescription>
          </Topic>

          <Topic
            href="https://cut-the-chase-zaujulio.vercel.app/"
            logo={<RiRoadMapLine />}
          >
            <TopicDescription
              name="Cut The Chase"
              description={
                <p>
                  Discipline project designed using NextJs, Sass, Nodejs,
                  Typscript and others. The project consists of a promoter and
                  user-based event control system.It has a map of events a
                  series of interesting features. For more information refer to
                  the official project <a
                    href="https://github.com/ZauJulio/CutTheChase"
                    target="_blank"
                    style={{ color: "cadetblue" }}
                  >
                    repository
                  </a>
                  .
                </p>
              }
            ></TopicDescription>
          </Topic>
        </div>
      </main>
    </div>
  );
}

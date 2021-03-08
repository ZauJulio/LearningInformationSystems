import React from "react";
import Link from "next/link";
import styles from "../styles/components/Topic.module.scss";

interface TopicProps {
  link?: string;
  target?: string;
  href?: string;
  logo: React.ReactChild;
  children: React.ReactChild | React.ReactChild[];
}

interface TopicDescriptionProps {
  name: string;
  description: string | React.ReactChild;
  children?: React.ReactChild | React.ReactChild[];
}

export function Topic(props: TopicProps) {
  const toLink = props.link !== undefined;
  const toHref = props.href !== undefined;
  let target = props.target;

  if (target === undefined) {
    target = "_blank";
  }

  return (
    <div>
      {(() => {
        if (toLink) {
          return (
            <div className={styles.topicContainer}>
              <Link href={props.link}>
                <div className={styles.topicLogo}>{props.logo}</div>
              </Link>
              <div className={styles.topicContent}>{props.children}</div>
            </div>
          );
        } else if (toHref) {
          return (
            <div className={styles.topicContainer}>
              <a href={props.href} target={target}>
                <div className={styles.topicLogo}>{props.logo}</div>
              </a>
              <div className={styles.topicContent}>{props.children}</div>
            </div>
          );
        }

        return (
          <div className={styles.topicContainer}>
            <div className={styles.topicLogo}>{props.logo}</div>
            <div className={styles.topicContent}>{props.children}</div>
          </div>
        );
      })()}
    </div>
  );
}

export function TopicDescription(props: TopicDescriptionProps) {
  return (
    <div className={styles.topicDescriptionContainer}>
      <h2>{props.name}</h2>
      <div className={styles.topicDescriptionImages}>{props.children}</div>
      {typeof props.description === "string" ? (
        <p>{props.description}</p>
      ) : (
        props.description
      )}
    </div>
  );
}

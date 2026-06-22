import React from "react";

interface WhoIsWhatProps {
  adjective: string;
}

export function WhoIsWhat(props: WhoIsWhatProps) {
  return <p>Who is {props.adjective}</p>;
}

import React from "react";

interface MariaPreaProps {
  adjetivo: string;
}

export function MariaPrea(props: MariaPreaProps) {
  return <p>Maria Preá is {props.adjetivo}</p>;
}

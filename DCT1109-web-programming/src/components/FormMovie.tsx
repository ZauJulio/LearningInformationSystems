import styles from "../styles/components/FormMovie.module.scss";

export default function FormMovie({ name, handler }) {
  return (
    <label className={styles.formContainer}>
      {name}
      <input type="text" onKeyPress={handler} />
    </label>
  );
}

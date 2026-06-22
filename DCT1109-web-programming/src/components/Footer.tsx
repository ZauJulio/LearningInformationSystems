import styles from '../styles/components/Footer.module.scss';

export function Footer() {
  return (
    <footer className={styles.footerContainer}>
      <p>For other projects and more information</p>
      <a href="https://github.com/ZauJulio" target="_blank">
        <img src="https://github.com/zaujulio.png" alt="Zaú Júlio"></img>
      </a>
    </footer>
  );
}

import { IonFooter, IonToolbar } from '@ionic/react';
import styles from "./Footer.module.css"

const Footer = () => {
  return (
    <IonFooter>
      <IonToolbar className={styles.footer}>
        <p slot='end'>
          © 2025 BarberApp - Todos los derechos reservados
        </p>
      </IonToolbar>
    </IonFooter>
  );
};

export default Footer;
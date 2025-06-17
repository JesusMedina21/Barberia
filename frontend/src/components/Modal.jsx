import { IonButtons, IonButton } from "@ionic/react";

import styles from "./Modal.module.css";

const Modal = ({ children }) => {
  return (
    <div className={styles.divModal}>
        {children}
        <IonButtons className={styles.buttonsModal}>
            <IonButton>Guardar</IonButton>
            <IonButton>Cancelar</IonButton>
        </IonButtons>
    </div>
  );
};

export default Modal;
import { useState } from "react";
import {
  IonItem,
  IonLabel,
  IonTextarea,
  IonButton,
  IonList
} from "@ionic/react";
import styles from "../Client_form.module.css";

const Description = ({ handleNextStep, handlePrevStep }) => {
  const [description, setDescription] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();

    console.log({
      description
    });
  };

  return (
    <form className={styles.form} onSubmit={handleSubmit}>
      <IonList>
        <IonItem>
          <IonLabel position="floating">Descripción:</IonLabel>
          <IonTextarea
            value={description}
            onIonChange={(e) => setDescription(e.detail.value)}
            rows={10} 
            // autoGrow={true} // Tamaño incrementable
            // maxlength={500} // Caracteres maximos
            // counter={true} // Contador si hay limite de caracteres
          ></IonTextarea>
        </IonItem>

        <IonItem>
          <IonButton
            type="submit"
            className={`${styles.formButton} ${styles.nextButton}`}
            onClick={() => {
              handleNextStep();
            }}
          >
            Siguiente
          </IonButton>
        </IonItem>

        <IonItem>
          <IonButton
            type="submit"
            className={`${styles.formButton} ${styles.prevButton}`}
            onClick={() => {
              handlePrevStep();
            }}
          >
            Anterior
          </IonButton>
        </IonItem>
      </IonList>
    </form>
  );
};

export default Description;
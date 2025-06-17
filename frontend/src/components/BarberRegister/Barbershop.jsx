import { useState } from "react";
import { IonItem, IonInput, IonButton, IonList } from "@ionic/react";
import styles from "../Client_form.module.css";

const Barbershop = ({ handleNextStep }) => {
  const [name, setName] = useState("");
  const [cuit, setCuit] = useState("");
  const [email, setEmail] = useState("");
  const [number, setNumber] = useState("");
  const [password, setPassword] = useState("");
  const [confPassword, setConfPassword] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();

    console.log({
      name,
      cuit,
      email,
      number,
      password,
      confPassword,
    });
  };

  return (
    <form className={styles.form} onSubmit={handleSubmit}>
      <IonList>
        <IonItem>
          <IonInput
            className="ion-padding-start"
            type="text"
            value={name}
            placeholder="Nombre del barbero o barberia"
            onIonChange={(e) => setName(e.detail.value)}
            required
          ></IonInput>
        </IonItem>

        <IonItem>
          <IonInput
            className="ion-padding-start"
            type="number"
            value={cuit}
            placeholder="CUIT"
            onIonChange={(e) => setCuit(e.detail.value)}
            required
          ></IonInput>
        </IonItem>

        <IonItem>
          <IonInput
            className="ion-padding-start"
            type="email"
            value={email}
            placeholder="Correo"
            onIonChange={(e) => setEmail(e.detail.value)}
            required
          ></IonInput>
        </IonItem>

        <IonItem>
          <IonInput
            className="ion-padding-start"
            type="text"
            value={number}
            placeholder="Número de télefono"
            onIonChange={(e) => setNumber(e.detail.value)}
            required
          ></IonInput>
        </IonItem>

        <IonItem>
          <IonInput
            className="ion-padding-start"
            type="password"
            value={password}
            placeholder="Contraseña"
            onIonChange={(e) => setPassword(e.detail.value)}
            required
          ></IonInput>
        </IonItem>

        <IonItem>
          <IonInput
            className="ion-padding-start"
            type="password"
            value={confPassword}
            placeholder="Confirmar Contraseña"
            onIonChange={(e) => setConfPassword(e.detail.value)}
            required
          ></IonInput>
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
      </IonList>
    </form>
  );
};

export default Barbershop;

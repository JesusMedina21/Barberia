import { useState } from "react";
import {
  IonItem,
  IonInput,
  IonButton,
  IonList,
  useIonToast,
} from "@ionic/react";
import styles from "./Client_form.module.css";

const Client = () => {
  const [nombre, setNombre] = useState("");
  const [email, setEmail] = useState("");
  const [genero, setGenero] = useState("");
  const [aceptaTerminos, setAceptaTerminos] = useState(false);
  const [comentarios, setComentarios] = useState("");

  const [presentToast] = useIonToast();

  const handleSubmit = (event) => {
    event.preventDefault();

    console.log({
      nombre,
      email,
      genero,
      aceptaTerminos,
      comentarios,
    });

    presentToast({
      message: "¡Formulario enviado con éxito!",
      duration: 2000,
      color: "success",
    });

    setNombre("");
    setEmail("");
    setGenero("");
    setAceptaTerminos(false);
    setComentarios("");
  };

  return (
    <form className={styles.form} onSubmit={handleSubmit}>
      <IonList>
        <IonItem>
          <IonInput
            className="ion-padding-start"
            type="text"
            value={nombre}
            placeholder="Nombre del usuario"
            onIonChange={(e) => setNombre(e.detail.value)}
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
            type="number"
            value={nombre}
            placeholder="Número de teléfono"
            onIonChange={(e) => setNombre(e.detail.value)}
            required
          ></IonInput>
        </IonItem>

        <IonItem>
          <IonInput
            className="ion-padding-start"
            type="password"
            value={nombre}
            placeholder="Contraseña"
            onIonChange={(e) => setNombre(e.detail.value)}
            required
          ></IonInput>
        </IonItem>

        <IonItem>
          <IonInput
            className="ion-padding-start"
            type="password"
            value={nombre}
            placeholder="Confirmar contraseña"
            onIonChange={(e) => setNombre(e.detail.value)}
            required
          ></IonInput>
        </IonItem>

        <IonItem>
          <IonButton
            type="submit"
            className={`${styles.formButton} ${styles.nextButton}`}
          >
            Registrarse
          </IonButton>
        </IonItem>
      </IonList>
    </form>
  );
};

export default Client;

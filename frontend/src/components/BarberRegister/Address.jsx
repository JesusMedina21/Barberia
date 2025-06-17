import { useState } from "react";
import {
  IonItem,
  IonInput,
  IonButton,
  IonList,
  IonNote
} from "@ionic/react";
import styles from "../Client_form.module.css";

const Address = ({ handleNextStep, handlePrevStep }) => {
  const [address, setAddress] = useState("");
  const [url, setUrl] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();

    console.log({
      address,
      url
    });
  };

  const [websiteUrl, setWebsiteUrl] = useState(''); // Revisar
  const [isValidUrl, setIsValidUrl] = useState(undefined); // Revisar

  const handleSubmit_URL = (e) => {
    e.preventDefault(); // Prevenir el envío por defecto del formulario HTML

    // Validar la URL (puedes usar una expresión regular más robusta o una librería)
    const urlRegex = /^(ftp|http|https):\/\/[^ "]+$/;
    const currentIsValid = urlRegex.test(websiteUrl);
    setIsValidUrl(currentIsValid);

    if (currentIsValid) {
      alert(`URL Válida: ${websiteUrl}`);
      // Aquí enviarías la URL a tu backend o la procesarías
    } else {
      alert('Por favor, ingresa una URL válida (con http:// o https://)');
    }
  }; // Revisar validacion

  return (
    <form className={styles.form} onSubmit={handleSubmit}>
      <IonList>
        <IonItem>
          <IonInput
            className="ion-padding-start"
            type="text"
            value={address}
            placeholder="Dirección"
            onIonChange={(e) => setAddress(e.detail.value)}
            required
          ></IonInput>
        </IonItem>

        <IonItem>
          <IonInput
            className="ion-padding-start"
            type="url"
            value={url}
            placeholder="URL de la foto del perfil"
            onIonChange={(e) => setUrl(e.detail.value)}
            required
          ></IonInput>
        </IonItem>

        {isValidUrl === false && (
          <IonNote color="danger" className="ion-padding-start">
            Por favor, introduce una URL válida (ej. https://ejemplo.com).
          </IonNote>
        )} {/* Revisar mensaje de error */}

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

export default Address;

import {
  IonPage,
  IonContent,
  IonItem,
  IonInput,
  IonButton,
  IonList,
  useIonToast,
} from "@ionic/react";
import { useState } from "react";
import styles from "./SignUp_Login.module.css";
import styles_form from "../components/Client_form.module.css";

const Home = () => {
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
    <IonPage>
      <IonContent className="ion-padding" fullscreen>
        <div className={`${styles.contentFlex} ${styles.contentLogin}`}>
          <div className={`${styles.background} ${styles.bgLogin}`} />
          <div className={styles.contentForm}>
            <h2>BarberApp</h2>
            <p id={styles.startNow}>¡Bienvenido!</p>

            <p>Consigue el estilo que mereces, cerca de ti.</p>
            <p>¿Listo para un nuevo look?</p>

            <form
              className={`${styles.form} ${styles_form.form}`}
              onSubmit={handleSubmit}
            >
              <IonList>
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
                    type="password"
                    value={nombre}
                    placeholder="Contraseña"
                    onIonChange={(e) => setNombre(e.detail.value)}
                    required
                  ></IonInput>
                </IonItem>

                <IonItem>
                  <IonButton
                    type="submit"
                    className={`${styles_form.formButton} ${styles_form.nextButton}`}
                  >
                    Iniciar Seción
                  </IonButton>
                </IonItem>
              </IonList>
            </form>

            <p id={styles.logIn}>
              ¿No tienes cuenta?{" "}
              <IonButton routerLink="signUp">Cree una cuenta</IonButton>
            </p>
          </div>
        </div>
      </IonContent>
    </IonPage>
  );
};

export default Home;

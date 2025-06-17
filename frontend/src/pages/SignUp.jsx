import { IonContent, IonPage, IonButtons, IonButton } from "@ionic/react";
import { useState } from "react";
import styles from "./SignUp_Login.module.css";
import Client from "../components/Client.jsx";
import Barbershop from "../components/BarberRegister/Barbershop.jsx";
import Address from "../components/BarberRegister/Address.jsx";
import Description from "../components/BarberRegister/Description.jsx";
import Timetable from "../components/BarberRegister/Timetable.jsx";

const Home = () => {
  const [form, setForm] = useState(false);
  const [currentStep, setCurrentStep] = useState(1);

  const handleNextStep = () => {
    setCurrentStep(currentStep + 1);
  };

  const handlePrevStep = () => {
    setCurrentStep(currentStep - 1);
  };

  const renderForm = () => {
    switch (currentStep) {
      case 4:
        return <Barbershop handleNextStep={handleNextStep} />;
      case 2:
        return (
          <Address
            handleNextStep={handleNextStep}
            handlePrevStep={handlePrevStep}
          />
        );
      case 3:
        return (
          <Description
            handleNextStep={handleNextStep}
            handlePrevStep={handlePrevStep}
          />
        );
      case 1:
        return <Timetable handlePrevStep={handlePrevStep} />;
    }
  };

  return (
    <IonPage>
      <IonContent className="ion-padding" fullscreen>
        <div className={styles.contentFlex}>
          <div className={styles.background} />
          <div className={styles.contentForm}>
            <h2>BarberApp</h2>
            <p id={styles.startNow}>Empieza Ahora</p>
            {!form ? (
              <>
                <p>Crea una cuenta para descubrir barberias</p>
                <p>y reservar tu corte favorito</p>
              </>
            ) : (
              <>
                <p>Crea un perfil para que</p>
                <p>mas clientes encuentren tu negocio</p>
              </>
            )}
            <IonButtons className={styles.IonButtons} slot="end">
              <IonButton
                className={form ? styles.inactiveButon : ""}
                onClick={() => setForm(false)}
              >
                Cliente
              </IonButton>
              <IonButton
                className={!form ? styles.inactiveButon : ""}
                onClick={() => setForm(true)}
              >
                Barberia
              </IonButton>
            </IonButtons>

            {!form ? <Client /> : renderForm()}

            <p id={styles.logIn}>
              ¿Ya tienes cuenta?{" "}
              <IonButton routerLink="logIn">Inicia sesion</IonButton>
            </p>
          </div>
        </div>
      </IonContent>
    </IonPage>
  );
};

export default Home;

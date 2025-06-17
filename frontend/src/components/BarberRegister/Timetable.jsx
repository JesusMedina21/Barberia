import { useState } from "react";
import {
  IonItem,
  IonInput,
  IonButton,
  IonList,
  IonModal
} from "@ionic/react";
import styles from "../Client_form.module.css";
import Modal from "../Modal.jsx";

const Timetable = ({ handlePrevStep }) => {
  const [description, setDescription] = useState("");
  const [showModal, setShowModal] = useState(false);
  const [openingTime, setOpeningTime] = useState(undefined);
  const [closingTime, setClosingTime] = useState(undefined);

  const numbers = Array.from({ length: 24 }, (_, i) => {
    if(i < 10) return "0" + i;
    return i;
  });

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
          <div>
              <h2>Horario de atención</h2>
              <p className={styles.textLight}>¿En qué horarios pueden atenderse los clientes?</p>
              <p className={styles.textLight}>El tiempo máximo para atender a un cliente es de 1 hora</p>
          </div>
        </IonItem>

        <IonButton onClick={() => setShowModal(true)}>
          Abrir Modal
        </IonButton>

        <IonModal
          className={styles.modal}
          isOpen={showModal}
          onDidDismiss={() => setShowModal(false)}
        >
          <Modal>
            <p className={styles.textLight}>Apertura:</p>

            <select 
              value={openingTime} 
              onIonChange={(e) => setOpeningTime(e.detail.value)}
            >
              {numbers.map(num => <option value={num}>{num}</option>)}
            </select>

            <p className={styles.textLight}>Cierre:</p>

            <select 
              value={closingTime} 
              onIonChange={(e) => setClosingTime(e.detail.value)}
            >
              {numbers.map(num => <option value={num}>{num}</option>)}
            </select>
          </Modal>
        </IonModal>

        <IonItem>
          <p className={styles.textLight}>Horario seleccionado:</p>
        </IonItem>

        <IonItem>
          <IonInput
            className="ion-padding-start"
            type="text"
            value={description}
            placeholder="Dirección"
            onIonChange={(e) => setDescription(e.detail.value)}
            required
          ></IonInput>
        </IonItem>

        <IonItem>
          <IonButton
            type="submit"
            className={`${styles.formButton} ${styles.nextButton}`}
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

export default Timetable;

const HomePage = () => {
  const [showModal, setShowModal] = useState(false);
  const [dataToModal, setDataToModal] = useState('Mensaje de ejemplo');

  // Función para cerrar el modal
  const handleDismissModal = () => {
    setShowModal(false);
  };

  return (
    <IonPage>
      <IonHeader>
        <IonToolbar>
          <IonTitle>Aplicación Principal</IonTitle>
        </IonToolbar>
      </IonHeader>
      <IonContent fullscreen className="ion-padding">
        <h1>Bienvenido</h1>
        <p>Haz clic para abrir el modal.</p>

        <IonButton expand="block" onClick={() => setShowModal(true)}>
          Abrir Modal
        </IonButton>

        {/* El componente IonModal */}
        <IonModal
          isOpen={showModal} // Controla si el modal está abierto o cerrado
          onDidDismiss={() => setShowModal(false)} // Se dispara cuando el modal se cierra (ej. por swipe)
          // Puedes pasar props al componente interno del modal
          // Si necesitas pasar una función para cerrar desde el modal, la pasas aquí
          // y luego la pasas al componente hijo
          // present y onWillDismiss también son útiles
        >
          {/* Aquí renderizas el componente que será el contenido de tu modal */}

          {/* <ModalContent onDismiss={handleDismissModal} data={dataToModal} /> */}
        </IonModal>
      </IonContent>
    </IonPage>
  );
};
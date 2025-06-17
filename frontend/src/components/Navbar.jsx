import { IonHeader, IonToolbar, IonTitle, IonButtons, IonButton } from '@ionic/react';
import _styles from "./Navbar.module.css";

const Navbar = () => {
  return (
    <IonHeader>
      <IonToolbar class="ion-padding-horizontal">
        <IonTitle color="primary-contrast">BarberApp</IonTitle>
        <IonButtons slot="end">
          <IonButton routerLink='/logIn'>Log In</IonButton>
          <IonButton routerLink='/signUp'>Sing Up</IonButton>
        </IonButtons>
      </IonToolbar>
    </IonHeader>
  );
};

export default Navbar;
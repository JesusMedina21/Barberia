import { IonContent, IonHeader, IonPage, IonTitle, IonToolbar } from '@ionic/react';
import ExploreContainer from '../components/ExploreContainer';
import './Home.css';

const Home: React.FC = () => {
  return (
    <IonPage>
      <IonHeader>
        <IonToolbar>
          <IonTitle>Blank</IonTitle>
        </IonToolbar>
      </IonHeader>
      <IonContent fullscreen className="ion-padding">
        {/* Aquí un ejemplo usando clases de Tailwind */}
        <div className="bg-[#48669e] text-white p-4 rounded-lg shadow-lg text-center">
          <h1 className="text-3xl font-bold mb-2">¡Hola Tailwind en Ionic!</h1>
          <p className="text-lg">Esto es un contenedor con estilos de Tailwind CSS.</p>
        </div>
        {/* Tu contenido de Ionic */}
      </IonContent>
    </IonPage>
  );
};

export default Home;

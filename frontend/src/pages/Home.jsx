import { IonContent, IonPage } from '@ionic/react';
import Navbar from '../components/Navbar.jsx';
import SearchBar from '../components/SearchBar.jsx';
import Footer from '../components/Footer.jsx';
import styles from "./Home.module.css";

const Home = () => {
  return (
    <IonPage>
      <Navbar />
      <IonContent className="ion-padding" fullscreen>
        <SearchBar />
        <div className={styles.recommendations}>
          <h2>Recomendaciones</h2>
        </div>
      </IonContent>
      <Footer />
    </IonPage>
  );
};

export default Home;
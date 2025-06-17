import { useState } from 'react';
import { IonSearchbar } from '@ionic/react';
import styles from "./SearchBar.module.css";

const SearchBar = () => {
  const [searchText, setSearchText] = useState('');

  return (
    <div>
      <IonSearchbar
        className={styles.ionSearchbar}
        value={searchText}
        onIonChange={(e) => setSearchText(e.detail.value)}
        placeholder="Buscar barberia"
      ></IonSearchbar>
      {searchText && (
        <p>
          Buscando: {searchText}
        </p>
      )}
    </div>
  );
};

export default SearchBar;
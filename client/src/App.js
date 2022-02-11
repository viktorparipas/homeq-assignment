import React, {useEffect, useState} from "react";
import styles from "./App.module.css";

import ApartmentRow from "./components/ApartmentRow";

function App() {
    const [apartments, setApartments] = useState([]);

    useEffect(() => {
        fetch("http://localhost:8000/apartments")
            .then((res) => res.json())
            .then((data) => setApartments(data));
    }, []);

    return (
        <>
            <main className={styles.app}>
                <nav>
                    <ul className={styles.menu}>
                        <li>
                            <a href="#" className={styles.active}>
                                Apartments
                            </a>
                        </li>
                    </ul>
                </nav>
                <table style={{width: '100%'}}>
                    <tr>
                        <td>id</td>
                        <td>Street</td>
                        <td>Street Number</td>
                        <td>City</td>
                        <td>Rent</td>
                        <td>Latitude</td>
                        <td>Longitude</td>
                    </tr>
                    {apartments?.map((apartment, ix) => (
                        <ApartmentRow key={ix} apartment={apartment}/>
                    ))}
                </table>
            </main>
        </>
    );
}

export default App;

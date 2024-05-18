// frontend/src/App.js

import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
    const [metalType, setMetalType] = useState('gold');
    const [amount, setAmount] = useState(1);
    const [currency, setCurrency] = useState('USD');
    const [convertedPrice, setConvertedPrice] = useState(null);

    const handleConvert = async () => {
        try {
            const response = await axios.post('/convert-price/', {
                metal_type: metalType,
                amount,
                currency
            });
            setConvertedPrice(response.data.converted_price);
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <div className="App">
            <h1>Precious Metals Price Converter</h1>
            <label>
                Metal Type:
                <select value={metalType} onChange={(e) => setMetalType(e.target.value)}>
                    <option value="gold">Gold</option>
                    <option value="silver">Silver</option>
                    <option value="platinum">Platinum</option>
                    <option value="palladium">Palladium</option>
                </select>
            </label>
            <label>
                Amount:
                <input type="number" value={amount} onChange={(e) => setAmount(e.target.value)} />
            </label>
            <label>
                Currency:
                <input type="text" value={currency} onChange={(e) => setCurrency(e.target.value)} />
            </label>
            <button onClick={handleConvert}>Convert</button>
            {convertedPrice && <div>Converted Price: {convertedPrice}</div>}
        </div>
    );
}

export default App;

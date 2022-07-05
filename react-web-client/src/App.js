import React from 'react'

import GlobalCases from './components/GlobalCases';
import logo from './logo.zenysis.png';
import './App.css';

function App() {
    return (
        <div className="App">
            <header className="App-header">
                <img src={logo} className="App-logo" alt="logo" />
            </header>
            <main>
                <h2>Global Covid-19 Cases</h2>
                <GlobalCases />
            </main>
        </div>
    );
}

export default App;

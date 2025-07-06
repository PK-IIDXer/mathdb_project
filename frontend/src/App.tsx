import React, { useState } from 'react';
import './App.css';
import FormulaTypeList from './components/FormulaTypeList';
import SymbolManager from './components/SymbolManager';

function App() {
  const [activeTab, setActiveTab] = useState<'formulatype' | 'symbol'>('formulatype');

  return (
    <div className="App">
      <header style={{ backgroundColor: '#f8f9fa', padding: '20px', borderBottom: '1px solid #dee2e6' }}>
        <h1>数学データベース管理システム</h1>
        <nav style={{ marginTop: '10px' }}>
          <button
            onClick={() => setActiveTab('formulatype')}
            style={{
              padding: '10px 20px',
              marginRight: '10px',
              backgroundColor: activeTab === 'formulatype' ? '#007bff' : '#6c757d',
              color: 'white',
              border: 'none',
              borderRadius: '5px',
              cursor: 'pointer'
            }}
          >
            論理式種類
          </button>
          <button
            onClick={() => setActiveTab('symbol')}
            style={{
              padding: '10px 20px',
              backgroundColor: activeTab === 'symbol' ? '#007bff' : '#6c757d',
              color: 'white',
              border: 'none',
              borderRadius: '5px',
              cursor: 'pointer'
            }}
          >
            記号管理
          </button>
        </nav>
      </header>

      <main style={{ padding: '20px' }}>
        {activeTab === 'formulatype' && <FormulaTypeList />}
        {activeTab === 'symbol' && <SymbolManager />}
      </main>
    </div>
  );
}

export default App;

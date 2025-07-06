import React, { useState, useEffect } from 'react';
import { FormulaType } from '../types/api';
import { formulaTypeApi } from '../services/api';

const FormulaTypeList: React.FC = () => {
  const [formulaTypes, setFormulaTypes] = useState<FormulaType[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchFormulaTypes = async () => {
      try {
        setLoading(true);
        const response = await formulaTypeApi.getAll();
        setFormulaTypes(response.data);
      } catch (err) {
        setError('論理式種類の取得に失敗しました');
        console.error('Error fetching formula types:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchFormulaTypes();
  }, []);

  if (loading) return <div>読み込み中...</div>;
  if (error) return <div style={{ color: 'red' }}>{error}</div>;

  return (
    <div>
      <h2>論理式種類一覧</h2>
      <div style={{ display: 'grid', gap: '10px' }}>
        {formulaTypes.map((formulaType) => (
          <div
            key={formulaType.id}
            style={{
              border: '1px solid #ccc',
              padding: '10px',
              borderRadius: '5px',
              backgroundColor: '#f9f9f9'
            }}
          >
            <h3>{formulaType.name}</h3>
            <p>ID: {formulaType.id}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default FormulaTypeList; 
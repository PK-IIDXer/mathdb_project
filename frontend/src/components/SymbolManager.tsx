import React, { useState, useEffect } from 'react';
import { Symbol, SymbolType } from '../types/api';
import { symbolApi, symbolTypeApi } from '../services/api';

const SymbolManager: React.FC = () => {
  const [symbols, setSymbols] = useState<Symbol[]>([]);
  const [symbolTypes, setSymbolTypes] = useState<SymbolType[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [editingSymbol, setEditingSymbol] = useState<Symbol | null>(null);
  const [formData, setFormData] = useState({
    name: '',
    symbol_type: '',
    arity: 0,
    argument_formula_type: '',
    notes: ''
  });

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      setLoading(true);
      const [symbolsResponse, symbolTypesResponse] = await Promise.all([
        symbolApi.getAll(),
        symbolTypeApi.getAll()
      ]);
      setSymbols(symbolsResponse.data);
      setSymbolTypes(symbolTypesResponse.data);
    } catch (err) {
      setError('データの取得に失敗しました');
      console.error('Error fetching data:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const submitData = {
        ...formData,
        symbol_type: parseInt(formData.symbol_type),
        argument_formula_type: formData.argument_formula_type ? parseInt(formData.argument_formula_type) : null
      };
      
      if (editingSymbol) {
        await symbolApi.update(editingSymbol.id, submitData);
      } else {
        await symbolApi.create(submitData);
      }
      setEditingSymbol(null);
      setFormData({ name: '', symbol_type: '', arity: 0, argument_formula_type: '', notes: '' });
      fetchData();
    } catch (err) {
      setError('保存に失敗しました');
      console.error('Error saving symbol:', err);
    }
  };

  const handleEdit = (symbol: Symbol) => {
    setEditingSymbol(symbol);
    setFormData({
      name: symbol.name,
      symbol_type: symbol.symbol_type.toString(),
      arity: symbol.arity,
      argument_formula_type: symbol.argument_formula_type?.toString() || '',
      notes: symbol.notes
    });
  };

  const handleDelete = async (id: string) => {
    if (window.confirm('この記号を削除しますか？')) {
      try {
        await symbolApi.delete(id);
        fetchData();
      } catch (err) {
        setError('削除に失敗しました');
        console.error('Error deleting symbol:', err);
      }
    }
  };

  if (loading) return <div>読み込み中...</div>;
  if (error) return <div style={{ color: 'red' }}>{error}</div>;

  return (
    <div>
      <h2>記号管理</h2>
      
      <form onSubmit={handleSubmit} style={{ marginBottom: '20px', padding: '20px', border: '1px solid #ccc', borderRadius: '5px' }}>
        <h3>{editingSymbol ? '記号編集' : '新規記号作成'}</h3>
        <div style={{ display: 'grid', gap: '10px' }}>
          <div>
            <label>記号名:</label>
            <input
              type="text"
              value={formData.name}
              onChange={(e) => setFormData({ ...formData, name: e.target.value })}
              required
              style={{ width: '100%', padding: '5px' }}
            />
          </div>
          <div>
            <label>記号種類:</label>
            <select
              value={formData.symbol_type}
              onChange={(e) => setFormData({ ...formData, symbol_type: e.target.value })}
              required
              style={{ width: '100%', padding: '5px' }}
            >
              <option value="">選択してください</option>
              {symbolTypes.map((type) => (
                <option key={type.id} value={type.id}>
                  {type.name}
                </option>
              ))}
            </select>
          </div>
          <div>
            <label>引数の数:</label>
            <input
              type="number"
              value={formData.arity}
              onChange={(e) => setFormData({ ...formData, arity: parseInt(e.target.value) })}
              required
              min="0"
              style={{ width: '100%', padding: '5px' }}
            />
          </div>
          <div>
            <label>備考:</label>
            <textarea
              value={formData.notes}
              onChange={(e) => setFormData({ ...formData, notes: e.target.value })}
              style={{ width: '100%', padding: '5px', height: '60px' }}
            />
          </div>
          <div style={{ display: 'flex', gap: '10px' }}>
            <button type="submit" style={{ padding: '10px 20px', backgroundColor: '#007bff', color: 'white', border: 'none', borderRadius: '5px' }}>
              {editingSymbol ? '更新' : '作成'}
            </button>
            {editingSymbol && (
              <button
                type="button"
                onClick={() => {
                  setEditingSymbol(null);
                  setFormData({ name: '', symbol_type: '', arity: 0, argument_formula_type: '', notes: '' });
                }}
                style={{ padding: '10px 20px', backgroundColor: '#6c757d', color: 'white', border: 'none', borderRadius: '5px' }}
              >
                キャンセル
              </button>
            )}
          </div>
        </div>
      </form>

      <div>
        <h3>記号一覧</h3>
        <div style={{ display: 'grid', gap: '10px' }}>
          {symbols.map((symbol) => (
            <div
              key={symbol.id}
              style={{
                border: '1px solid #ccc',
                padding: '15px',
                borderRadius: '5px',
                backgroundColor: '#f9f9f9'
              }}
            >
              <h4>{symbol.name}</h4>
              <p>ID: {symbol.id}</p>
              <p>引数の数: {symbol.arity}</p>
              <p>備考: {symbol.notes || 'なし'}</p>
              <p>作成日時: {new Date(symbol.created_at).toLocaleString('ja-JP')}</p>
              <div style={{ display: 'flex', gap: '10px', marginTop: '10px' }}>
                <button
                  onClick={() => handleEdit(symbol)}
                  style={{ padding: '5px 10px', backgroundColor: '#28a745', color: 'white', border: 'none', borderRadius: '3px' }}
                >
                  編集
                </button>
                <button
                  onClick={() => handleDelete(symbol.id)}
                  style={{ padding: '5px 10px', backgroundColor: '#dc3545', color: 'white', border: 'none', borderRadius: '3px' }}
                >
                  削除
                </button>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default SymbolManager; 
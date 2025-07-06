import axios from 'axios';
import {
  FormulaType, SymbolType, Symbol, LogicalFormula, LogicalFormulaSymbol,
  InferenceRule, InferenceRuleArgument, InferenceRulePremise,
  Theorem, Proof, ProofInference, ProofInferenceArgument, ProofUnresolvedAssumption
} from '../types/api';

const API_BASE_URL = 'http://localhost:8000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// FormulaType API
export const formulaTypeApi = {
  getAll: () => api.get<FormulaType[]>('/formulatype/'),
  getById: (id: number) => api.get<FormulaType>(`/formulatype/${id}/`),
};

// SymbolType API
export const symbolTypeApi = {
  getAll: () => api.get<SymbolType[]>('/symboltype/'),
  getById: (id: number) => api.get<SymbolType>(`/symboltype/${id}/`),
};

// Symbol API
export const symbolApi = {
  getAll: () => api.get<Symbol[]>('/symbol/'),
  getById: (id: string) => api.get<Symbol>(`/symbol/${id}/`),
  create: (data: Partial<Symbol>) => api.post<Symbol>('/symbol/', data),
  update: (id: string, data: Partial<Symbol>) => api.put<Symbol>(`/symbol/${id}/`, data),
  delete: (id: string) => api.delete(`/symbol/${id}/`),
};

// LogicalFormula API
export const logicalFormulaApi = {
  getAll: () => api.get<LogicalFormula[]>('/logicalformula/'),
  getById: (id: string) => api.get<LogicalFormula>(`/logicalformula/${id}/`),
  create: (data: Partial<LogicalFormula>) => api.post<LogicalFormula>('/logicalformula/', data),
  update: (id: string, data: Partial<LogicalFormula>) => api.put<LogicalFormula>(`/logicalformula/${id}/`, data),
  delete: (id: string) => api.delete(`/logicalformula/${id}/`),
};

// Theorem API
export const theoremApi = {
  getAll: () => api.get<Theorem[]>('/theorem/'),
  getById: (id: string) => api.get<Theorem>(`/theorem/${id}/`),
  create: (data: Partial<Theorem>) => api.post<Theorem>('/theorem/', data),
  update: (id: string, data: Partial<Theorem>) => api.put<Theorem>(`/theorem/${id}/`, data),
  delete: (id: string) => api.delete(`/theorem/${id}/`),
};

// Proof API
export const proofApi = {
  getAll: () => api.get<Proof[]>('/proof/'),
  getById: (id: number) => api.get<Proof>(`/proof/${id}/`),
  create: (data: Partial<Proof>) => api.post<Proof>('/proof/', data),
  update: (id: number, data: Partial<Proof>) => api.put<Proof>(`/proof/${id}/`, data),
  delete: (id: number) => api.delete(`/proof/${id}/`),
};

export default api; 
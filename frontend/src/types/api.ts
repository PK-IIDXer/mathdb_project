export interface FormulaType {
  id: number;
  name: string;
}

export interface SymbolType {
  id: number;
  name: string;
  formula_type: number;
  is_quantifier: boolean;
}

export interface Symbol {
  id: string;
  name: string;
  symbol_type: number;
  arity: number;
  argument_formula_type: number | null;
  notes: string;
  created_at: string;
  updated_at: string;
}

export interface LogicalFormula {
  id: string;
  representation: string;
  created_at: string;
  updated_at: string;
}

export interface LogicalFormulaSymbol {
  id: number;
  logical_formula: string;
  sequence: number;
  symbol: string;
  created_at: string;
  updated_at: string;
}

export interface InferenceRule {
  id: string;
  name: string;
  result_formula: string;
  created_at: string;
  updated_at: string;
}

export interface InferenceRuleArgument {
  id: number;
  inference_rule: string;
  sequence: number;
  symbol: string;
  created_at: string;
  updated_at: string;
}

export interface InferenceRulePremise {
  id: number;
  inference_rule: string;
  sequence: number;
  logical_formula: string;
  solvable_proposition: string | null;
  is_solvable_proposition_mandatory: boolean | null;
  created_at: string;
  updated_at: string;
}

export interface Theorem {
  id: string;
  name: string | null;
  meaning: string | null;
  conclusion: string;
  assumptions: string[];
  created_at: string;
  updated_at: string;
}

export interface Proof {
  id: number;
  theorem: string;
  sequence: number;
  created_at: string;
  updated_at: string;
}

export interface ProofInference {
  id: number;
  proof: number;
  sequence: number;
  inference_rule: string;
  conclusion_formula: string;
  from_nodes: number[];
  created_at: string;
  updated_at: string;
}

export interface ProofInferenceArgument {
  id: number;
  proof_inference: number;
  sequence: number;
  argument_formula: string;
  created_at: string;
  updated_at: string;
}

export interface ProofUnresolvedAssumption {
  id: number;
  proof: number;
  sequence: number;
  formula: string;
  added_by_inference: number;
  resolved_by_inference: number | null;
  created_at: string;
  updated_at: string;
} 
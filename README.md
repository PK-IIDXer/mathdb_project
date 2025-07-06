# 数学データベースプロジェクト

このプロジェクトは、Django（バックエンドAPI）とReact（フロントエンド）で構成されています。

---

## ディレクトリ構成

- `core/` : Djangoアプリ（APIサーバー）
- `frontend/` : Reactアプリ（ユーザーインターフェース）

---

## バックエンド（Django REST Framework）

### 必要要件
- Python 3.x
- pip

### セットアップ
1. 仮想環境の作成（任意）
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows の場合
   # source venv/bin/activate  # Mac/Linux の場合
   ```
2. 依存パッケージのインストール
   ```bash
   pip install django djangorestframework
   ```
3. マイグレーションの適用
   ```bash
   python manage.py migrate
   ```
4. 開発サーバーの起動
   ```bash
   python manage.py runserver
   ```
   デフォルトで http://127.0.0.1:8000/ で起動します。

### 管理画面
- http://127.0.0.1:8000/admin/

### APIエンドポイント
- すべてのAPIは `/api/` 配下にあります。
  例: `http://127.0.0.1:8000/api/formulatype/` など
- 主なエンドポイント一覧:
    - `/api/formulatype/`
    - `/api/symboltype/`
    - `/api/symbol/`
    - `/api/logicalformula/`
    - `/api/logicalformulasymbol/`
    - `/api/inferencerule/`
    - `/api/inferenceruleargument/`
    - `/api/inferencerulepremise/`
    - `/api/theorem/`
    - `/api/proof/`
    - `/api/proofinference/`
    - `/api/proofinferenceargument/`
    - `/api/proofunresolvedassumption/`

---

## フロントエンド（React）

### 必要要件
- Node.js
- npm

### セットアップ
1. フロントエンドディレクトリへ移動
   ```bash
   cd frontend
   ```
2. 依存パッケージのインストール
   ```bash
   npm install
   ```
3. 開発サーバーの起動
   ```bash
   npm start
   ```
   デフォルトで http://localhost:3000/ で起動します。

---

## 備考
- バックエンドとフロントエンドはそれぞれ別プロセスで起動してください。
- APIの詳細仕様はDjangoのViewSet/Serializerを参照してください。 
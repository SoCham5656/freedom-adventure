# Freedom Adventure — プロジェクト概要

## コンセプト

**業務効率化アプリのプラットフォーム**。  
`index.html` がホームページ兼ランチャーとなり、ここから各アプリへ飛べる設計。

テーマは **MapleStory × ワンピース**（明るい空・海・冒険）。
フォント: `Press Start 2P`（ピクセル系）+ `M PLUS Rounded 1c`（日本語）。

---

## アーキテクチャ方針

- **ホームページ**: `index.html`（静的HTML、直接ブラウザで開く）
- **各アプリ**: `apps/<app-name>/` 以下に独立して格納
- **連携方法**: `index.html` の ADVENTURE MAP カードから各アプリの URL へリンク
- **ローカルサーバーアプリ**: `start.bat` で起動、`localhost` でアクセス

---

## 現在のアプリ一覧

### 1. PDF Converter（`apps/pdf-converter/`）
- **概要**: Word / Excel / PowerPoint を一括 PDF 変換
- **技術**: Python + Flask（ポート 5001）+ win32com（Microsoft Office COM）
- **起動**: `start.bat` をダブルクリック
- **UI**: ドラッグ＆ドロップ、複数ファイル対応、元ファイルと同名で PDF 出力
- **依存**: Python + Microsoft Office（インストール済み）、Anaconda 環境で動作確認済み

---

## 今後の方針

- アプリを一つずつ追加していく
- 新しいアプリは `apps/<app-name>/` に格納
- `index.html` の `apps-grid` にカードを追加してリンク
- ロックされた ISLAND カード（Coming Soon）は新アプリ追加時に順次置き換える

---

## 開発環境

- OS: Windows 11
- Python: Anaconda 環境
- ブラウザ: `index.html` をローカルファイルとして直接開いている
- GitHub: https://github.com/SoCham5656/freedom-adventure

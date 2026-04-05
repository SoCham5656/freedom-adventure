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
- **start.bat の書き方**: 日本語 echo は文字化けするため ASCII のみ使用。pip は必ず `python -m pip` で実行する

---

## 現在のアプリ一覧

### 1. PDF Converter（`apps/pdf-converter/`）
- **概要**: Word / Excel / PowerPoint を一括 PDF 変換
- **技術**: Python + Flask（ポート 5001）+ win32com（Microsoft Office COM）
- **起動**: `start.bat` をダブルクリック
- **UI**: ドラッグ＆ドロップ、複数ファイル対応、元ファイルと同名で PDF 出力
- **依存**: Python + Microsoft Office（インストール済み）、Anaconda 環境で動作確認済み

### 2. Proof Agent（`apps/proofreader/`）
- **概要**: 研修資料（PDF / PPTX / DOCX）の誤字脱字・表記ゆれを AI が一括チェック
- **技術**: Python + Flask（ポート 5002）+ Anthropic / OpenAI / Google Gemini API
- **起動**: `start.bat` をダブルクリック
- **UI**: 川崎工場夜景テーマ、仲間キャラ「LUMINA — 鋼鉄の校正師」、AI プロバイダー切り替え対応
- **対応 AI**: Claude（claude-opus-4-6）/ GPT-4o / Gemini 2.0 Flash
- **API キー**: UI 上で入力・localStorage にプロバイダーごとに保存（環境変数 `ANTHROPIC_API_KEY` でも可）
- **校正カテゴリ**: 表記ゆれ・誤字脱字・句読点記号・敬語文体の不統一
- **出力**: 優先度⭐×3段階の Markdown テーブル形式

---

## ホームページ機能

- **BGM プレイヤー**: 右下固定の 🎵 ボタン。クリックでパネル開閉＆再生開始
  - Kevin MacLeod の著作権フリー曲（CC-BY 3.0）を Internet Archive からストリーミング
  - 8曲をシャッフル再生、全曲終了後に再シャッフル
  - 前曲・停止・次曲ボタン、現在再生曲名を表示

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

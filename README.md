# AI Limit Ledger

GitHub Pagesで動く、AIアカウントの7日制限管理ツールです。

UIは静的ファイルだけで動きます。メールアドレス、制限状態、履歴ログは指定したprivate GitHub data repoのJSONファイルに保存します。

## できること

- メールアドレスつきAIアカウントを登録
- Codex / ChatGPT / Claude / Cursor / Gemini などのサービスを管理
- 「制限開始」ボタンで現在時刻から7日後を解除予定として自動記録
- 「解除」ボタンで利用可能に戻す
- `events.json` に履歴ログを保存
- GitHub API更新によりcommit履歴も残す

## 推奨リポジトリ構成

UI repo:

```text
ai-limit-manager-ui
```

GitHub Pages用です。publicでもprivateでも構いません。ここにメールアドレスやGitHub tokenは置きません。

Data repo:

```text
ai-limit-manager-data
```

privateで作成してください。メールアドレスと履歴ログはここに保存されます。

## Data repoに置くファイル

このUIの「データファイル初期化」ボタンで作成できます。手動で用意する場合は以下の3ファイルを置いてください。

```text
data/accounts.json
data/events.json
data/settings.json
```

`data/accounts.json`

```json
{
  "accounts": []
}
```

`data/events.json`

```json
{
  "events": []
}
```

`data/settings.json`

```json
{
  "services": [
    {
      "name": "Codex",
      "defaultLimitDurationDays": 7
    },
    {
      "name": "ChatGPT",
      "defaultLimitDurationDays": 7
    },
    {
      "name": "Claude",
      "defaultLimitDurationDays": 7
    },
    {
      "name": "Cursor",
      "defaultLimitDurationDays": 7
    },
    {
      "name": "Gemini",
      "defaultLimitDurationDays": 7
    }
  ]
}
```

## GitHub token

fine-grained personal access tokenを使ってください。

必要な権限:

- 対象data repoだけを選択
- Repository permissions
- Contents: Read and write

このUIはtokenをソースコードに埋め込みません。設定画面で入力します。保存チェックを外すと、ブラウザにtokenを残しません。

## GitHub Pagesへの公開

このプロジェクトはビルド不要です。`index.html`, `styles.css`, `app.js` をそのままGitHub Pagesで配信できます。

Settings → Pages で以下のように設定します。

```text
Source: Deploy from a branch
Branch: main
Folder: /root
```

## 既存リポジトリへpushする例

ユーザー指定の空リポジトリをUI repoとして使う場合の例です。

```bash
cd /Users/mitsuyoshitsuha/Documents/Codex/ai-limit-manager-ui
git init
git add .
git commit -m "Add AI limit ledger GitHub Pages app"
git branch -M main
git remote add origin https://github.com/shihuiarenjinba-png/-.git
git push -u origin main
```

push後、GitHub上で必要ならrepoをprivateに変更してください。

## 注意

- GitHub Pages上のフロントエンドコードはブラウザから見えます。
- メールアドレスやtokenをUI repoへ直接書かないでください。
- メールアドレスはprivate data repoにだけ保存してください。
- GitHub APIエラー表示ではtoken全文を出さないようにしています。

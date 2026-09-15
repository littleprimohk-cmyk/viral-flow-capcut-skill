# Claude 安裝及使用

同一套故事格式、雙版本審閱及批准規則適用於 Claude。請按實際使用的 Claude 介面安裝。

## A. Claude 網頁／Desktop 的 Skills（亦供 Cowork 使用）

1. 下載 [viral-flow-capcut-claude.zip](../dist/viral-flow-capcut-claude.zip)。在 GitHub 檔案頁按 Download raw file；不要把整個 repository ZIP 當作 skill 上載。
2. 在 Claude 確認已啟用 Code execution and file creation；團隊帳戶亦須允許自訂 Skills。
3. 打開 **Customize → Skills → ＋ → Create skill → Upload a skill**。
4. 上載 ZIP，再啟用 `viral-flow-capcut`。
5. 開新對話，貼下方使用提示。Cowork 亦需啟用帳戶 Skills；只複製到本機 `.claude/skills` 不等於裝入 Cowork。

ZIP 只有一個 `viral-flow-capcut/` 根資料夾，內有 SKILL.md、references 和 scripts；不含 Codex 專用 UI metadata、原片或憑證。

## B. 本機 Claude Code

1. 在 GitHub 按 **Code → Download ZIP**，解壓整套 repository。
2. 在套件資料夾執行：

```sh
python3 install.py --target claude
```

安裝到 `~/.claude/skills/viral-flow-capcut`；若已有版本會停止，不會覆蓋。

3. 開新的本機 Claude Code session，輸入：

```text
/viral-flow-capcut
```

亦可讓 Claude Code 把套件的 `skills/viral-flow-capcut` 完整複製到上述位置。只把 GitHub 網址貼進普通聊天，不等於安裝。這套件無需另裝 Claude plugin。

## 第一次使用提示

> 用 viral-flow-capcut skill 處理這條口播片。先檢查你能否讀取原片和執行本機 Whisper，再根據保留的爆紅格式給我 A、B 兩個完整文字 flow。Hook 要有完整痛點及因果，保留故事細節；Hook 後要有原片 Soft voice, wild truth 和緊接的英文。我批准全文才用 CapCut 剪，預設不加字。先不要建立剪輯專案。

Claude Code 可在提示開頭用 `/viral-flow-capcut`；Claude 一般聊天直接寫 skill 名稱。

## 哪些部分可以執行？

| 環境 | 文字審閱 | 本機 Whisper／CapCut |
|---|---|---|
| Claude 一般網頁聊天 | 可按提供的逐字稿提出兩個 flow；未看原片須標示未核對 | 雲端執行工具不代表可操作你的 Mac |
| Claude Code 本機／有電腦操作能力的 Claude 環境 | 可按可讀取的來源分析 | 需有本機檔案、FFmpeg、Whisper，以及真正可操作 CapCut 的工具和權限 |

安裝 skill 不會自動安裝工具或授權。缺少本機工具時，先交可完成的文字版本並說明欠缺甚麼；不能聲稱已用 Whisper 轉錄或已匯出 CapCut 成片。完整剪片流程目前的實作驗證來自 Codex＋macOS CapCut，尚未在 Claude 完整實剪驗證。

## 安裝後自查

先問：「請用 viral-flow-capcut 說明工作流程，不要剪片。」應提及兩個完整全文、Hook 後品牌句＋本片英文、全文批准後才剪，以及不加字。能讀取 skill 不等於已驗證 CapCut 控制。

私人 GitHub 倉庫需要存取權。沒有權限的團隊成員可由獲授權的人提供專用 ZIP。

## 官方說明

- [Claude：使用及上載 Skills](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
- [Claude Code：Skills、安裝位置及 Cowork 差異](https://code.claude.com/docs/en/skills)

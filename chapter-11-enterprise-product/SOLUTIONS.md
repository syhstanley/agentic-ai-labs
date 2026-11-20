# Chapter 11 Reference Solutions

## 11.1

有價值的 evidence 是「最近 20 件中 7 件因缺欄位退回，平均等待 1.8 天」，不是「大家覺得很麻煩」。

## 11.2

固定流程且 SaaS 已完整支援時通常買比自建好；自建合理於特殊資料、深度整合、差異化流程或治理要求。

## 11.3

```text
annual_capacity = volume * minutes_saved / 60 * loaded_hourly_cost
net_benefit = capacity + avoided_loss + uplift - build - run - review - change
ROI = net_benefit / total_cost
```

不得把每分鐘節省都直接稱為現金節省；要說明釋放產能如何被使用。

## 11.4

Stop criteria 示例：任何越權資料事件、unsafe action、關鍵正確率低於門檻。Success 也包含持續使用率與 review burden。

## 11.5

賣「縮短理賠文件處理時間且保留人工核准」，不賣「萬用 AI Agent」。合約明確 data owner、model changes、incident、SLA 和退出／資料刪除。


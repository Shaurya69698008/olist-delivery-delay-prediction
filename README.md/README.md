
# Supply Chain Delivery Delay Analysis (Olist)

## Overview
This project analyzes delivery performance of the Olist Brazilian E-commerce dataset to identify delivery bottlenecks and predict high-risk delayed orders. It includes SQL analysis, an ML classification model, explanations via SHAP, and exports prepared for Power BI dashboards.

## Files
- `notebooks/delay_analysis.ipynb` — main notebook (EDA, modeling)
- `sql/` — SQL queries used for feature generation
- `data/` — raw CSVs (not uploaded to repo due to size) or link to Kaggle dataset
- `processed/model_input_full.csv` — cleaned features used for modeling
- `predictions_for_powerbi.csv` — model outputs for dashboard
- `xgb_model.joblib` — saved model
- `preprocessor.joblib` — saved preprocessor
- `visuals/` — confusion_matrix.png, roc_curve.png, shap_summary.png, etc.

## How to run
1. Download dataset from Kaggle: https://www.kaggle.com/olistbr/brazilian-ecommerce
2. Open `notebooks/delay_analysis.ipynb` in Colab and follow cells.
3. Run cells in order; artifacts will be saved in `/content/`.

## Key findings
- Top drivers of delay: `processing_time`, `transit_time`, `approx_distance_km`, product categories X/Y.
- Model ROC-AUC: 0.983
- Recommended actions: prioritize high-risk regions, ensure SLA enforcement with sellers, route heavy items via specialized carriers.

## Contact
Shaurya Mehta — shauryamehta2939@gmail.com — LinkedIn: linkedin.com/in/shaurya-mehta-278825227


**Intelligent Delivery ETA Risk Detection System**

**Supply Chain Delivery Delay Prediction (Olist E-commerce Dataset)**
This project builds an end-to-end Delivery Delay Risk Detection System using the Olist Brazilian E-commerce dataset.
It combines data engineering, SQL-based feature creation, machine learning, explainable AI, and dashboarding to identify orders that are likely to miss their estimated delivery date.The workflow is similar to real delivery-risk scoring systems used in logistics, marketplaces, and D2C operations.

**1. Business Problem**
Accurate delivery ETAs are critical for customer satisfaction.
Delays lead to lower NPS, higher cancellations, refund costs, and operational inefficiencies.

**Objective:**
Predict which orders are at high risk of being delivered late — before the delay occurs.

This enables:
* Early customer communication
* Proactive follow-ups with carriers
* Route and seller optimization
* SLA enforcement across the supply network

**2. Project Structure**

<pre>
olist-delivery-delay-prediction/
|
├── data/
│   └── *_sample.csv
|
├── notebooks/
│   └── delay_analysis.ipynb
|
├── models/
│   ├── xgb_model.joblib
│   └── preprocessor.joblib
|
├── plots/
│   ├── confusion_matrix.png
│   ├── roc_curve.png
│   └── shap_summary.png
|
├── powerbi/
│   └── scored_orders_for_powerbi.csv
|
└── README.md
</pre>

**Note:**
The complete Olist dataset is not included in the repository due to size limits.
Download it here: https://www.kaggle.com/olistbr/brazilian-ecommerce

Sampled (5k row) versions of each table are provided for reproducibility.

**3. Data Sources**

This project uses the Olist Brazilian E-commerce dataset, which includes:
| Table       | Description                       |
| ----------- | --------------------------------- |
| Customers   | Customer metadata                 |
| Orders      | Order lifecycle timestamps        |
| Order Items | Products within each order        |
| Sellers     | Seller locations                  |
| Products    | Category, weight, and dimensions  |
| Payments    | Payment details                   |
| Reviews     | Customer feedback                 |
| Geolocation | Latitude/Longitude per ZIP prefix |

**4. Feature Engineering**

Key engineered features include:

**Time-Based Features**
* Processing time (order → shipping limit)
* Transit time (shipping limit → actual delivery)
* Gap between promised and actual delivery
* Temporal patterns (hour, weekday, month)

**Distance Features**
* Haversine distance (when available)
* ZIP-code prefix proxy distance

**Seller & Product Indicators**
* Category-level delay tendencies
* Seller historical delay ratio
* State-level congestion or delay patterns

**Target Definition**
delayed_flag = 1 if delivered_date > estimated_delivery_date else 0

**5. Machine Learning Pipeline**

**Preprocessing**
* Train/test split (80/20, stratified)
* One-hot encoding for categorical features
* Scaling for numerical features
* SMOTE to handle class imbalance (applied only on train set)

**Model**
* XGBoost Classifier
* Tuned using depth, learning rate, tree count, and sampling parameters

Evaluation
| Metric           | Score                                      |
| ---------------- | ------------------------------------------ |
| **ROC–AUC**      | **0.977**                                  |
| Precision        | High (important for early-warning systems) |
| Recall           | Strong performance on delayed class        |
| Confusion Matrix | Included in `/plots/`                      |

**6. Explainable AI (SHAP)**

SHAP values were used to understand model decisions.

**Most influential factors**
* Long processing time (major contributor)
* High transit time
* Heavy/fragile product categories
* Certain high-delay seller states

All SHAP plots are saved in the /plots/ directory.

**7. Power BI Dashboard**

A lightweight dashboard was created to visualize delay risk outputs.

It includes:
* Overall delay risk %
* Delay distribution by state
* Category-wise delay patterns
* High-risk seller mapping
* Order-level risk table for operations

Input file for Power BI:
powerbi/predictions_for_powerbi.csv

**8. How to Run This Project**

**A. Download Dataset**
Download the full Olist dataset from Kaggle:
https://www.kaggle.com/olistbr/brazilian-ecommerce

**B. Open the Notebook**
* Upload/clone this repository
* Open notebooks/delay_analysis.ipynb in Google Colab
* Run the cells sequentially
  
**C. Outputs Generated**
* Running the notebook will generate:
* xgb_model.joblib
* preprocessor.joblib
* Confusion matrix
* ROC curve
* SHAP summary
* Final model scores for Power BI

**9. Key Business Insights**

**Main drivers of delivery delays**
* Sellers exceeding processing SLAs
* Long-distance shipments
* Product categories with complex handling (heavy/fragile)
* Congested/high-delay regions

**Suggested operational actions**
* Prioritize high-risk orders for proactive communication
* Improve seller-level SLA monitoring
* Route optimization for long-distance orders
* Use risk scores to allocate faster carriers
* Trigger early interventions for extremely high-risk shipments

**10. Contact**

**Shaurya Mehta**

**Email:** shauryamehta2939@gmail.com

**LinkedIn:** linkedin.com/in/shaurya-mehta-278825227

**11. Why This Project Matters**

This project reflects a realistic end-to-end workflow that many modern e-commerce, logistics, and marketplace companies rely on. Predicting delivery delays is not just an ML exercise—it directly supports customer satisfaction, operational planning, and revenue protection.
A system like this can help teams:
* Forecast which orders need priority handling
* Identify bottlenecks across sellers and regions
* Improve ETA accuracy
* Reduce late deliveries through early intervention
* Align operations, support, and logistics teams around a shared risk score
The goal of building this was to demonstrate the ability to work across the full analytics stack—data cleaning, SQL transformations, feature engineering, model development, explainability, and dashboard reporting.

**12. Future Improvements**

Some enhancements that can be added to make this an even more production-ready system:
* Add real geolocation distance (lat/long) for all orders to improve accuracy
* Deploy the model as an API endpoint (FastAPI or Flask) for real-time scoring
* Add model monitoring to track drift over time
* Automate weekly data refresh using Airflow or Prefect
* Experiment with other models such as CatBoost or LightGBM
* Integrate a more granular order timeline, including carrier-level data
* Build seller-level dashboards for SLA performance
These additions can turn the project from a strong analysis into a fully deployable ML service.

**13. Limitations**

Like any dataset-driven model, there are practical constraints:
* The Olist dataset does not include real-time carrier events
* Some addresses lack complete geolocation coordinates
* Original timestamps may not reflect real operational scenarios
* A 5k row sample (for GitHub) will not perform as well as the full dataset
* Delays may also be influenced by external factors (weather, festivals), not captured in the data
Despite these limitations, the model performs extremely well on the available data.

**14. Acknowledgements**

Special thanks to the creators of the Olist Brazilian E-commerce dataset for making a rich, multi-table dataset publicly available for research and learning.

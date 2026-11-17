# Airbnb Paris Market Intelligence: Revenue & Pricing Optimization

An end-to-end data analytics and Business Intelligence project analyzing **28,447 Airbnb listing records** in Paris. This project transforms raw marketplace data into a normalized Parquet Star Schema and an interactive 3-page Power BI dashboard to uncover seasonal trends, spatial demand, price elasticity, and RevPAR drivers.

---

## Tech Stack & Data Architecture

* **Data Cleaning & Transformation (`Python` - `pandas`, `pyarrow`):** Handled missing values using grouped median imputation across `room_type` and `property_type`, standardized data types, and exported clean tables into compressed columnar **Parquet** files.


* **Data Modeling (`Star Schema`):** Structured the dataset into a BI-ready Star Schema before Power BI ingestion:


* `fact_performance`: Core transactional metrics (revenue, ADR, occupancy, booking lead time, and Native RevPAR).


* `dim_listing`: Property types, room configurations, guest capacity, and neighborhood coordinates.


* `dim_host`: Host identifiers and Superhost status classifications.




* **Visualization & Analytics (`Power BI`, `DAX`):** Built custom DAX measures for ADR categorization, lead-time segmentation, and multi-page interactive reporting.



---

## Key Analytical Insights

* **Seasonality & Booking Thresholds:** In 2025, total revenue reached **€17.26M** across **7,759 listings** (86.63% active) with a **27.92%** average occupancy rate. Revenue and occupancy peak during the **June** summer holiday and see a secondary surge in **October**. Listings generating **>€20K** in average revenue require at least **11+ booked (unavailable) days** per month, exceeding the **8.49-day** market benchmark.


* **Price Elasticity & Lead Time:** Across the full dataset (**€62.38M** total revenue), **High ADR ($\ge$€250)** listings generate **46.4%** (**€28.97M**) of total revenue. Pricing around **€300** preserves steady occupancy, whereas rates above **€2,000** sharply reduce booking probability. **Last-minute bookings ($\le$7 days)** drive the highest ADR, while **early-bird bookings (>90 days)** secure baseline occupancy through promotional pricing.


* **Spatial & Property Drivers:** Tourist demand concentrates across central and northern Paris, led by **2-guest, 1-bedroom** apartments catering to couples. **Entire homes** exceed **€1.5M** in total Native RevPAR, outperforming all other room types in room-to-revenue conversion.


* **Top-Performing Districts:** The **16th Arrondissement** leads 2025 total revenue (**€1.18M**), sustaining **45% occupancy** even at a **€488.80** average ADR. Meanwhile, the **10th Arrondissement** leads overall dataset Native RevPAR (**€153,437**) through high booking turnover.



---

## Strategic Recommendations

1. **Dynamic Lead-Time Pricing:** Offer early-bird discounts (>90 days) to cross the **11+ booked days** revenue threshold, then capture high margins with premium rates on last-minute ($\le$7 days) bookings.


2. **Focused Asset Acquisition:** Prioritize **1-to-2 bedroom entire-home apartments**, which deliver the highest RevPAR conversion and align with Paris's dominant couple-traveler segment.


3. **Dual-Location Targeting:** Target the **7th and 16th Arrondissements** for high-yield luxury margins (>€440 ADR), or invest in the **10th Arrondissement** to maximize booking volume and total RevPAR.


4. **Off-Peak Supply Activation:** Introduce weekly stay promotions during low-demand months (**February and November**) to convert excess available days (**21.90** market average) into booked nights.



---

## Dashboard Structure

1. **Performance & Revenue Overview:** Executive KPIs, monthly revenue vs. occupancy trends, rating distribution (**4.13** average), and active listing ratios.


2. **Spatial & Revenue Analytics:** Interactive neighborhood map, guest/bedroom capacity breakdowns, property type share, and top districts by revenue.


3. **RevPAR & Pricing Analytics:** ADR tier performance, occupancy-vs-ADR price elasticity scatter plots, booking lead-time clusters, and Native RevPAR rankings.

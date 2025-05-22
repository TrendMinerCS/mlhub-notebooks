# MLHub Notebooks

A curated collection of Jupyter notebooks and Python scripts demonstrating how to use TrendMiner’s MLHub for time-series analytics, contextual data enrichment, machine-learning model development/deployment, and visualization. Each folder groups examples by theme and lists individual notebooks/scripts with concrete, task-oriented use cases.

---

## 📂 Calculations examples

Notebooks illustrating common time-series calculations and KPI reporting on TrendHub data:

- **time_based_report_calculations.ipynb**  
  Compute time-based KPIs (e.g. uptime, cycle time, batch yields) over fixed intervals. Shows how to:  
  - Slice a continuous signal into hourly/daily chunks  
  - Calculate aggregates (mean, min/max, counts) per period  
  - Combine the data in a Pandas DataFrame for further processing

- **value_based_search_and_calculation_example.ipynb**  
  Locate segments of interest by value thresholds (e.g. all periods where temperature > setpoint) and calculate statistics only on those segments. Covers:  
  - Value-based search for runs or events  
  - Rolling and conditional calculations  
  - Combining search results with downstream analytics  

---

## 📂 Contexthub examples

Notebooks for loading and enriching process data with ContextHub metadata and attachments:

- **get_context_item_attachment.ipynb**  
  Download and display attachments (PDFs, images, CSV logs) linked to ContextHub items. Demonstrates:   
  - Retrieving item attachments by ID  
  - Saving and previewing file content in MLHub  

- **loading_additional_context_item_fields.ipynb**  
  Fetch custom fields and tags associated with ContextHub items for richer filtering and analysis. Includes:  
  - Querying standard vs. custom metadata fields  
  - Merging context-item attributes into your DataFrame  
  - Filtering by business-specific context labels  

---

## 📂 Fetching data examples

Programmatic retrieval of TrendHub view data and metadata with interpolation:

- **get_interpolated_data.ipynb**  
  Load uniformly-spaced time-series data (e.g. 1-minute intervals) from an existing TrendHub view. Covers:  
  - Specifying start/end timestamps  
  - Choosing interpolation frequency and method  
  - Handling large date ranges via paging/batching  

---

## 📂 ML tags

Scripts and notebooks for building, evaluating, and deploying ML models as real-time “tags” in MLHub:

- **anomaly_detection.py**  
  Python script that trains an isolation-forest anomaly detector on historical data and deploys it as an ML tag for real-time scoring.

- **Batch_anomaly_detection.ipynb**  
  Notebook showing how to run anomaly detection in batch mode over archived datasets:  
  - Feature extraction for each event  
  - Model training, threshold tuning, and batch scoring  
  - Exporting results to CSV or back into TrendMiner  

- **import_pmml.py**  
  Demonstrates how to import a PMML-serialized model (from external tool) into MLHub as a custom tag.

- **linear_regression_example.py**  
  End-to-end linear regression example: train on historical tag data, evaluate in cross-validation, and publish model as an ML tag.

- **Soft_Sensor_Training_and_Deployment.ipynb**  
  Build a multi-variable soft sensor (e.g. predicting a lab measurement from process signals), package it, and deploy to MLHub for live predictions.

---

## 📂 Plotting examples

Examples of static and interactive visualizations for TrendMiner time-series data:

- **cached_plot_example.ipynb**  
  Leverage MLHub’s plot-caching mechanism to speed up repeated rendering of large datasets. Illustrates:  
  - Caching settings and invalidation  
  - Overlaying multiple tags with different time spans  

- **plotting_example.ipynb**  
  General purpose plotting demo with:  
  - Matplotlib: static trend overlays, rolling-stats ribbons  
  - Plotly: interactive zoom, hover annotations, and export  

- **tag_histogram_examples.ipynb**
  Demo for plotting histograms of tag time series data, including:
  - Interactive selection of a specific tag (from predetermined list)
  - Interactive selection of a given time interval (from predetermined list)

---

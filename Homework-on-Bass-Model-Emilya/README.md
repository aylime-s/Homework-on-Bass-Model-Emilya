## Homework: Bass Diffusion Model – Antigravity A1 Drone

Course: Marketing Analytics

Student: Emilya Sepoyan

Project Overview

Analysis of the potential market diffusion for the **Antigravity A1 drone (2025)**. This project uses historical global drone market data to estimate Bass model parameters (innovation coefficient `p`, imitation coefficient `q`, and market potential `M`) and predict the adoption path of the Antigravity A1 over time. The analysis includes visualizations, forecast tables, and a detailed report.

## Structure

-data/:
  - statistic_id1399076_volume-of-thedrone-market-worldwide-2018-2030.xlsx: Historical drone market data (2018–2030)
  - bass_parameters.csv: Estimated Bass model parameters
  - antigravityA1_forecast.csv: Predicted adoption table

-img/:
  - image1.png: Historical Drone Market Diffusion
  - image2.png: Predicted Adoption Path of Antigravity A1

-scripts/:
  - helper_functions.py: Mathematical core of the Bass model
  - script1.py: Historical data cleaning & Bass parameter estimation
  - script2.py: Adoption forecast & visualization

-report/:
  - report_source.md: Markdown source file for the report
  - AntigravityA1_BassModel_Report.pdf: Final PDF report

-Root (Homework-on-Bass-Model-Emilya/):
  - README.md: Project documentation (this file)
  - requirements.txt: List of Python dependencies

## Data Source & Credibility

- **Historical data:** Statista – “Volume of the drone market worldwide from 2018 to 2030”  
- Data includes global consumer drone market volume in millions of units.  
- Forecasts and model outputs are derived from the Bass Diffusion Model based on this dataset.  

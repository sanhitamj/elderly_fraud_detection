# Elderly Fraud Detection

## Background

For people whose cognitive abilities are compromised, either due to old age or some sort of mental disorder, there are conservators to handle their finances, make transactions on their behalf. In the US, only the state of Minnesota keeps digital record of these transactions. The data for this project is provided by the State of Minnesota and Mr Michael Currant of Guide Change.

These data are from the year 2012 to 2015; the number of people (taken care of) is 9000+. There are different categories of expenses, ranging from rent/property tax, insurance to personal needs, or 'shopping' data.

Currently, the state bureaucrats use red flags like, if the charitable donations are over $100 or if a single cash transaction is over certain amount. This is not a very clever way to handle such big dataset. For 9000+ people, there are more than 100,000 red flags. It is a waste of resources like accounts' time and in turn tax money.

## Goal

The goal of this project is to understand the data and using data-science techniques raise reasonable red flags; and also to catch low-level frauds. It may not be possible to get back to those particular cases, but the idea is to alert the state about how low-level cheating, frauds happen.

## Ongoing Work

Currently, I am working on working on multivariate time-series, made using expenses from different categories. These categories are for example 'Personal Needs', 'Miscellaneous Expenses', 'Rent', etc. The idea is to use each time-series as a point and perform clustering analysis for anomalies in the expenses.

A plot below shows one such time-series for one person.

![Timeseries for Personal Needs and Miscellaneous Expenses](images/ts_casefile\=4832.png)
Format: ![Alt Text](url)



## Technologies used
* MSSQL (Microsoft SQL, Express 2012)
* Jupyter Notebook
* Python
  * sqlalchemy
  * pandas
  * matplotlib
  * numpy
  * datetime


## References

* Signature-Based Methods for Data Streams - Corinna Cortes, Daryl Pregibon
* Grouping Multivariate Time Series: A Case Study - T. Dasu, D. F. Swayne, D. Poole

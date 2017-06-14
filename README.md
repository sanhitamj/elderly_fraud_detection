# Elderly Fraud Detection

## Background

For people whose cognitive abilities are compromised, either due to old age or some sort of mental disorder, there are conservators to handle their finances, make transactions on their behalf. In the US, only the state of Minnesota keeps digital record of these transactions. The data for this project is provided by the State of Minnesota and Mr Michael Curran of Guide Change.

These data are from the year 2012 to 2015; the number of people (taken care of) is 9125.

## Goal

The goal of this project is to understand the data, and using data-science techniques raise reasonable red flags. It may not be possible to get back to those particular cases, but the idea is to alert the state about how low-level cheating, frauds happen.

Currently, the state bureaucrats use red flags like, if the charitable donations are over $100 or if a single cash transaction is over certain amount. This is not a very clever way to handle such big dataset. For 9000+ people, there are almost 200,000 red flags. It is a waste of resources like accountants' time and in turn tax-payers' money.

The other part of the system is that the bureaucrats do not look into the cases for whom monthly income (Estate) is less than $3000. So it is important to find outliers within low-income people too.

Although some of these cases might be investigated in detail, there is no information about that in the dataset. Hence the challenging part of the project is that these are unlabeled data, and this is going to be unsupervised learning.


## Data

The data are provided by Mr Michael Curran of Guide Change; the data in turn came from the state of Minnesota. It is in MSSQL format. (If you are looking ways to read MSSQL tables in Python, find the jupyter notebook - DataPipeline.ipynb - within this project.)

The most important table for this project is -IncomeExpenseTable. The information used from this table has format :

| CaseFileID | Transaction Date | Amount | Transaction Category |
| ---------- | ---------------- | ------ | -------------------- |
| 22208      |  2014-10-27      | 7.36	 | 197 |

There are data for 9125 unique individuals (being taken care of by conservators or guardians); 56 unique categories for expenses; and information of 785478 expense transactions in all.

There are income transactions and a lot more redundant information in this table and other SQL tables too.

## Using the data or Feature Engineering

To begin with, this was the most difficult part of the project.

**A paragraph that only Data Scientist and Machine-Learning people would find interersting**

The was Data-Science, Machine-Learning is taught, we expect a nice, clean X or feature matrix to work with. That is irrespective of whether it is supervised or unsupervised learning. To make a feature matrix like that was a difficult job; how to select features to use, or how to condense information and yet lose nothing important was the challenge. The important lesson is - get hands dirty with data to learn something important.

**Description in English for anyone who is even mildly interested**

A simple idea to begin with -

Rather than dealing with 56 categories of expense, I uesd another SQL table for description of the expenses. Related expenses, for example - different utilities - gas-electricity, cable-phone-internet, water, sewage - were considered as just one type of expense.

The database has information about when the transaction was made. Since different people are on the database for different periods and different length of time, an idea to deal with time-series was dropped. But time information was used in another way.

There are two assumptions in feature engineering

1. The first one is people will spend similar amounts in a given amount of time -

  Of course, people who have more money will spend more money. But if each transaction is normalized with the total money they have spent in that category would give us a handle on spending patterns of people, irrespective of their wealth.

  While looking at the data, visually or mathematically, expense amounts were normalized.

2. The number of transactions will be similar for a given amount of time as well.

  If I were to commit fraud, I won't spend a b!@# load of money in a single transaction. That would certainly invite bureaucratic suspicion. But what if, say I spend 10 dollars every day or 100 dollars a week? That's a not big dollar amount and bureaucrats have no way of catching this kind of fraud (assuming that the goods or services bought using this money helps the conservator or guardian and not the person who owns the money).

  To catch that sort of transactions, I used another feature - number of transactions in a given length of time.

Using these two ideas, some plots were made.

## Ongoing Work

Relevant information for this project is contained in one table. Only these columns are used to model the data-
  * CaseFileID (Unique ID for individuals taken care of)
  * Transation date
    * This column is transformed into, duration. This is basically for how long the individual is on the database.
  * Amount (in USD)
  * Transaction Category for the given transaction. This column is used in multiple ways;
    * How many categories are expenses made
    * How much money has been spent under each category

A linear model is fit to these features to predict the total amount spent.

Further work -
* Find outliers
* Divide people into two income/expenditure groups and fit a model.



Currently, I am working on working on multivariate time-series, made using expenses from different categories. These categories are for example 'Personal Needs', 'Miscellaneous Expenses', 'Rent', etc. The idea is to use each time-series as a point and perform clustering analysis for anomalies in the expenses.

A plot below shows one such time-series for one person, identified with a number, CaseFileID.

![Timeseries for Personal Needs and Miscellaneous Expenses](images/ts_casefile\=4832.png)



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

# Elderly Financial Fraud Detection - Unsupervised Learning


The goal of this project is find outliers from the given data; this information can be supplied to the state accountants to look carefully into each case, individually; also to help people budget their income well.


The data are expense transactions of the people, whose cognitive abilities are compromised. A 'conservator' or a 'guardian' takes care of their financial transactions. These conservators are either professionals or family members, friends, etc.

Currently, only the state of Minnesota keeps digital records of the transactions. The data were collected between 2011 and 2015. It came in as a SQL (MS-SQL Express 2012) file; with 88 tables in all. Only a handful of those tables were useful in this project.

'IncomeExpenseTable' is the table that contains information for transactions for the people that are cared for.

### Previous Red Flags: Reasons and Counts
SQL table - ReportFlags has 37 reasons.
Table - FlaggedReports has 194995 entries.
df3['ReportReason'].value_counts()

|Reason | Count of red flags|
| --- | --- |
|Cash Transaction                                 | 40458|
|Transfers Between Accounts                       | 32630|
|New Substantial Expense                          | 24039|
|Conservator Fees                                 | 15620|
|Unexpected Expense Transaction                   | 13451|
|Large Transaction                                | 11016|
|Large Expense                                    |  7416|
|Bank And Other Fees                              |  6834|
|Prior Year Income Change                         |  5377|
|Prior Year Expense Change                        |  5312|
|Prior Year Income and Expense Change             |  5274|
|Misc Transaction Percentage                      |  4165|
|Gifts Given                                      |  3409|
|Missing Income Transaction                       |  3280|
|Late Annual Report                               |  3269|
|Excessive Charitable Contributions               |  2646|
|Substandard Living Arrangements                  |  2174|
|Prior Year Account Value Change                  |  1852|
|Number of Accounts                               |  1401|
|Unprotected Assets                               |  1288|
|Any Debt                                         |  1032|
|Closed Account With Balance                      |   705|
|Disposed Personal Property                       |   555|
|Large Estate                                     |   523|
|Misc Transaction Count                           |   445|
|Missing Expense Transactions                     |   338|
|Disposed Personal Property With Financial Loss   |   299|
|Loan Or Debt Increase                            |   127|
|Round Transaction Numbers                        |    50|
|Late Charges                                     |    11|


# Top type of expenses from the ConservatorDatabase -

|ID | Expense Description | Unique no of persons | Total inputs |
|---| --------------------|----------------------| --- |  
| 214 | Personal Needs | 7476 | 136282 |
|213 | Miscellaneous | 4903 | 18510 |
| 240 | Prescriptions | | 35835
|239 | Rent | | 38437|
|233 | Utilities (Phone, Cable, Internet) | | 43694|
|187 | Clothing | | |
|183 | Bank Service Charges| | |
|210 | Doctor / Hospital | |  |
|228 | Transfer to  |  |  |
|206 | Med Insurance  |  |  |
|185 | Care Facility  |  |  |
|193 | Conservator/Guardian Fees  |  |  |
|197 | Food - Groceries  |  |  |
|191 | Fees - Attorney  |  |  |
|194 | Other Fees  |  |  |
|232 | Utilities - Gas & Electric  |  |  |
|196 | Food - Dining Out  |  |  |
|221 | Services - Personal Care  |  |  |
|190 | Fees - Accountant  |  |  |
|199 | Gifts Given  |  |  |
|189 | Entertainment  |  |  |
|203 | Household - Other Household  |  |  |
|178 | Wages  |  |  |
|209 | Medical - Dental     |  |  |
|184 | Bond Premium  |  |  |
|202 | Household - Maintenance/Repairs  |  |  |  
|222 | Subscriptions & Dues  |  |  |
|229 | Transportation  |  |  |
|207 | Insurance - Other Insurance  |  |  |
|205 | Insurance - Home/Renter    |  |  |
|226 | Taxes - Real Estate  |  |  |
|179 | Asset Depreciation  |  |  |
|204 | Insurance - Auto  |  |  |
|227 | State Taxes  |  |  |
|212 | Medical: Equipment  |  |  |
|224 | Federal Taxes  |  |  |
|230 | Travel  |  |  |
|234 | Utilities - Water/Sewer  |  |  |
|186 | Charitable Donation  |  |  |
|180 | Automobile - Gasoline  |  |  |
|181 | Automobile - Maintenance  |  |  |
|200 | Hobby  |  |  |
|192 | Fees - Court  |  |  |

### Some of these expenses can be clumped together

|Description | Transaction ID |
| -- | -- |
|Fees - Attorney | 191 |
|Fees - Court | 192 |
| -- | -- |
| Automobile - Gasoline | 180|
| Automobile - Maintenance | 181 |
| Automobile - Payment | 182 |
| Insurance - Auto | 204 |
| -- | -- |
| Household - Laundry, dry cleaning | 201 |
| Household - Maintenance, Repairs | 202 |
| Household - Other Household | 203 |
| Fees - Realtor/Appraiser | 195 |
| Services - Cleaning | 220 |
|  Taxes - Real Estate| 226 |
| Home or Renter Insurance | 205 |


For CaseFileReportId 9423 -

| IncExpId |	CasFil	| Expense	| Amount |	TranDt	| TranCat	| TranDescr |	CourtOrdTran |	CarFac |	NumDays |
|-| ----|-|-|-|-|-|-|-|-|-|
|194493|	9423	|1	|4883.54	|2013-06-28	|226|	Taxes - Real Estate|	0	|1	|1271.0|

The person livd in a care facility but still paying Real Estate Taxes. The last entry for this person is on - '2014-05-06'; it's for the care facility. There is no entry for this person, of selling a house. But probably the person died within a year of paying the real estate taxes, mentioned above.


For CaseFileReportId 13550 -

| IncExpId |	CasFil	| Expense	| Amount |	TranDt	| TranCat	| TranDescr |	CourtOrdTran |	CarFac |	NumDays |
| - | -   |-|-|-|-|-|-|-|-|-|
|312110|	13550|	1|	7000.00|	2013-05-20|	226	|Taxes - Real Estate	|0	|1|	1232.0|

Similar case for this person, with last entry of expenses is on 2014-04-30'; is for Asset Depreciation; the last entry for care facility is on 2014-03-11.

Number of people who live in a care facility, even for part of the time the data were collected, is 2414.

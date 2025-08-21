fyt# Implementation-of-Scoring-Rules-for-Clients
This project implements a scoring system to evaluate the likelihood of recovering customer accounts, based on a set of parameters related to their history of refinancing, delinquency, and cancellation requests. This score can be used by collections departments to assess how feasible it is to recover a customer and define personalized negotiation strategies.

Considered Parameters:
Refinancing: If a customer has carried out refinancing after falling into delinquency, points are deducted. Refinancing due to capital contributions is not penalized.
Delinquency: Points are deducted depending on the number of months the customer has been delinquent (1-3 months: -2 points, 4-6 months: -4 points, 7 or more months: -6 points).
Cancellation Requests: Each cancellation request made by the customer deducts 5 points.
Points Recovery: Customers can recover points by making capital contributions or staying up to date with their payments for more than 12 months.
Each customer starts with an initial score of 100, and the system adjusts this value according to the rules mentioned above. A chart is generated to visualize the health of the portfolio for a given month, and a hypothesis is established: if more than 85% of customers have a score above 90, the portfolio is considered easy to recover. Otherwise, new negotiation tools will need to be implemented.

This project is a practical example of data science applied to account recovery, using Python, pandas for data manipulation, and matplotlib for visualization.

Repository Features:
Python Code: Implementation of scoring rules for clients.
Synthetic Data: Generation of random data to simulate a portfolio of 100 clients.
Visualization: Charts to represent score distribution and hypothesis analysis.
Detailed Instructions: Includes instructions to reproduce the analysis and generate new scenarios.
Ideal for those working in credgit analysis, account recovery, and data science applied to business.
.
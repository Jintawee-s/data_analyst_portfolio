# Loan Risk Case

# import data
library(dplyr)

Loan_Data <- read.csv("Loan_Risk.csv", stringsAsFactors = FALSE)

# review data
head(Loan_Data)

# Q1 : Number of user in each age group
# Results : (1)Gandhinagar (2)Sultan_Pur_Majra (3)Bijapur (4)Katni (5)Dehradun

Loan_Data %>%
  count(Age_Group) %>%
  arrange(n)

# Q2 : Top 7 cities with the most popular
# Results : (1)Vijayanagaram (2)Bhopal (3)Bulandshahr (4)Saharsa[29] (5)Vijayawada (6)Srinagar (7)Indore

Loan_Data %>%
  group_by(CITY) %>%
  summarise(count = n()) %>%
  arrange(desc(count)) %>%
  head(7)
  
# Q3 : Top 3 regions with the highest risk loans
# Results : (1)Eastern (2)Southern (3)Northern

Loan_Data %>%
  filter(Risk_Flag > 0) %>%
  group_by(Region) %>%
  summarise(sum_Risk_Flag = sum(Risk_Flag)) %>%
  arrange(desc(sum_Risk_Flag)) %>%
  head(3)

# Q4 : Top 5 professions with the lowest risk loans
# Results : (1)Physician (2)Statistician (3)Web_designer (4)Drafter (5)Psychologist

Loan_Data %>%
  filter(Risk_Flag < 1) %>%
  group_by(Profession) %>%
  summarise(count = n()) %>%
  arrange(desc(count)) %>%
  head(5)
  
# Q5 : Avg, max and min of income in each region by state

Loan_Data %>%
  filter(Risk_Flag > 0) %>%
  group_by(Region, Rev_State) %>%
  summarise(avg_Income = mean(Income),
            max_Income = max(Income),
            min_Income = min(Income), .groups = 'drop')

# Q6 : Top 10 Ids of non-defaulted clients in high-income loans

Loan_Data %>%
  filter(Risk_Flag < 1, Income_Category == 'High') %>%
  select(Id, Age, Age_Group, Experience,Income, Income_Category) %>%
  arrange(desc(Income)) %>%
  head(10)

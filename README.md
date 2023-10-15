# Careerspace parser
This is a parser for careerspace.app job search site implemented as part of internship assignment.
It collects information about job offers in the category 'Аналитика'. 

This category was broader than I thought - not all of the offers are actually related to the data science field. Due to this, during data collection and analysis of 3 qualification levels (junior, middle, senior) the class 'Не указано' was added for the vacancies which don't offer any information about the level required, whether because it's not applicable to this job (not data science) or it's just not specified by the employer (data science, but no information about the qualification level given).

In the 'tmp' folder you may find:
- an Excel table with information about the vacancy, qualification level, employer, city, min and max wage, possibility of online and hybrid work and url;
- an interactive plot which illustrates the proportions of the 3 qualification levels.

The data was collected on 04/10/2023.

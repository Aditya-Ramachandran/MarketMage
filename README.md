# MarketMage: Supermarket Sales Analysis App


<p align="center">
  <img src="Media/Demo_Video.gif">
</p>


## Overview
MarketMage is a Python-based project that brings your supermarket sales data to life through interactive visualizations and insightful analysis. With a user-friendly interface, it allows you to explore and understand sales trends, profit margins, and regional patterns across different store locations in the US.

## Features
- Dynamic Data Analysis: MarketMage dynamically fetches and processes real-time sales data from diverse supermarket locations.
- Interactive Visualizations: Gain meaningful insights through interactive charts and graphs powered by Plotly.
- Query-based Exploration: Dive deep into sales trends, profit margins, and other key metrics with a variety of predefined queries.
- Segment Analysis: Understand customer behavior by analyzing different customer segments.
Shipping Mode Insights: Explore the impact of various shipping modes on your sales.

## How to use

- Clone this repository to your local machine.
- `cd` into the repository
- Install the required dependencies using `pip install -r requirements.txt.`
- Ensure you have XAMPP or a similar database server installed on your system.
- Set up a MySQL database using XAMPP or your preferred database management tool.
- Connect the app to your own database by updating the connection details in the `DB` class within the `db.py` file.
- Run the app using `streamlit run app.py` in your terminal.

## Tech Stack
MarketMage utilizes the following technologies:

- Python: For data manipulation, querying, and visualization.
- SQL: To fetch, process, and analyze data from the database.
- Streamlit: For creating the user-friendly and interactive app interface.
- Plotly: For generating dynamic and interactive visualizations.

## Future Enhancements
In the future, we plan to enhance MarketMage by adding predictive modeling capabilities that can help in optimizing product restocking strategies.

## Contributing
Contributions are welcome! If you have any ideas for improvements or additional features, feel free to submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.## 
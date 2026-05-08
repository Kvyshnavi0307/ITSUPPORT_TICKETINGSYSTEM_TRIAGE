from openai import OpenAI

client = OpenAI(api_key='YOUR OPENAI API KEY')

def process_tickets():
    try:
        with open('tickets.txt', 'r') as file:
            ticket_data = file.read()

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": """
                You are a data processing tool. Output the ticket analysis in a CSV format.
                Use these columns: Ticket ID, Priority, Sentiment, Summary, Recommended Action.
                Only provide the CSV data, no extra text.
                """},
                {"role": "user", "content": f"Process these tickets into CSV:\n\n{ticket_data}"}
            ]
        )

        csv_content = response.choices[0].message.content

        # Save as a .csv file instead of .txt
        with open('ticket_report.csv', 'w') as csv_file:
            csv_file.write(csv_content)

        print("\n--- CSV REPORT GENERATED ---")
        print("You can now open 'ticket_report.csv' in Excel!")

    except Exception as e:
        print(f"Something went wrong: {e}")

if __name__ == "__main__":
    process_tickets()
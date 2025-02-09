from fpdf import FPDF

def create_pdf(text, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in text.split('\n'):
        pdf.cell(200, 10, txt=line, ln=True, align='L')
    pdf.output(filename)

# The text you want to convert to PDF
text = """
Using Groq in n8n and Make.com

Introduction
Groq is a powerful query language that allows you to extract and manipulate data from various sources. In this document, we will explore how to use Groq in n8n and Make.com to integrate it with their respective workflows.

Using Groq in n8n

### Installing the Groq Node
1. Go to the n8n node library and search for "groq".
2. Click on the "Install" button to add the node to your n8n instance.

### Configuring the Groq Node
1. Create a new workflow in n8n and add the Groq node.
2. Configure the node by providing the Groq query, the data source (e.g., JSON, CSV, etc.), and any necessary authentication credentials.
3. You can also specify the output format (e.g., JSON, CSV, etc.).

### Writing the Groq Query
1. Write your Groq query in the node's configuration panel.
2. The query should be in the Groq syntax, which is similar to GraphQL.
3. For example: query { data { id, name } }

### Running the Workflow
1. Trigger the workflow by clicking the "Run" button or by setting up a trigger (e.g., timer, webhook, etc.).
2. The Groq node will execute the query and return the results in the specified output format.

Using Groq in Make.com

### Creating a New Workflow
1. Go to Make.com and create a new workflow.
2. Add a new "Groq" action to the workflow.

### Configuring the Groq Action
1. Provide the Groq query, the data source (e.g., JSON, CSV, etc.), and any necessary authentication credentials.
2. You can also specify the output format (e.g., JSON, CSV, etc.).

### Writing the Groq Query
1. Write your Groq query in the action's configuration panel.
2. The query should be in the Groq syntax, which is similar to GraphQL.
3. For example: query { data { id, name } }

### Running the Workflow
1. Trigger the workflow by clicking the "Run" button or by setting up a trigger (e.g., timer, webhook, etc.).
2. The Groq action will execute the query and return the results in the specified output format.

Tips and Considerations
- Make sure you have the necessary permissions and authentication credentials to access the data source.
- Test your Groq query in a playground or a local environment before running it in n8n or Make.com.
- Be mindful of the query's performance and adjust the query accordingly to avoid overwhelming the data source.
- You can also use Groq's built-in functions and operators to manipulate the data and perform complex queries.

Conclusion
By following these steps, you should be able to use Groq in n8n and Make.com to extract and manipulate data from various sources. Happy querying!
"""

# Create the PDF
filename = "Converted.pdf"
create_pdf(text, filename)
print(f"PDF created successfully: {filename}")
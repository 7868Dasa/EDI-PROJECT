import streamlit as st

 

# Define Streamlit app title
st.title('EDIFACT Purchase Order Message Generator')

 

# Define EDIFACT message elements
interchange_header = "UNB+UNOC:3+sender_id+receiver_id+210323:0945+1'"
message_header = "UNH+1+ORDERS:D:96A:UN'"
buyer_details = "NAD+BY+buyer_id::9'"
seller_details = "NAD+SU+seller_id::9'"
order_details = "LIN+1++product_code:EN'"
order_quantity = "QTY+21:50'"
message_trailer = "UNT+6+1'"
interchange_trailer = "UNZ+1+1'"

 

# Define Streamlit input fields
sender_id = st.text_input('Enter sender ID:')
receiver_id = st.text_input('Enter receiver ID:')
buyer_id = st.text_input('Enter buyer ID:')
seller_id = st.text_input('Enter seller ID:')
product_code = st.text_input('Enter product code:')
order_qty = st.number_input('Enter order quantity:', min_value=1)

 

# Generate EDIFACT message from user input
if st.button('Generate EDIFACT Message'):
    # Replace message elements with user input
    interchange_header = interchange_header.replace("sender_id", sender_id)
    interchange_header = interchange_header.replace("receiver_id", receiver_id)
    buyer_details = buyer_details.replace("buyer_id", buyer_id)
    seller_details = seller_details.replace("seller_id", seller_id)
    order_details = order_details.replace("product_code", product_code)
    order_quantity = order_quantity.replace(str(order_qty), str(order_qty))

 

    # Combine message elements into EDIFACT message
    edifact_message = interchange_header + message_header + buyer_details + seller_details + order_details + order_quantity + message_trailer + interchange_trailer

 

    # Display generated EDIFACT message
    st.write('Generated EDIFACT message:')
    st.write(edifact_message)
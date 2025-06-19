1. Add Item to Cart
Test Design Techniques: Equivalence Partitioning (EP), Boundary Value Analysis (BVA), Use Case Testing

Test Cases:
Equivalence Partitioning

Test Case: Add a valid grocery item to the cart.

Input: Click “Add to Cart” on a product in the “Fresh” category.

Expected Outcome: Item is added, cart updates with correct quantity.

Error Guessing

Test Case: Attempt to add a product when there is no stock.

Input: Product with stock = 0

Expected Outcome: Error message “Out of Stock” shown, item not added.

Use Case Testing

Test Case: Add multiple quantities of the same product.

Input: Add same product three times

Expected Outcome: Cart shows correct total quantity (3).

Boundary Value Analysis

Test Case: Add maximum allowed quantity of a product (e.g., 99 units).

Input: Add 99 units via quantity selector

Expected Outcome: Cart accepts quantity and calculates total price.

2. Remove Item from Cart
Test Design Techniques: Use Case Testing, Error Guessing

Test Cases:
Use Case Testing

Test Case: Remove an item from the cart.

Input: Click "Remove" on a cart item.

Expected Outcome: Item is removed; cart total is updated.

Error Guessing

Test Case: Try removing an item when the cart is empty.

Input: Click remove without any items.

Expected Outcome: No action; possibly message “Cart is empty.”

3. Checkout Process
Test Design Techniques: Use Case Testing, Equivalence Partitioning, Error Guessing

Test Cases:
Use Case Testing

Test Case: Complete checkout with valid details.

Input: Valid name, address, payment info

Expected Outcome: Order confirmed; success message and confirmation email sent.

Error Guessing

Test Case: Checkout with missing address.

Input: Leave address field blank

Expected Outcome: Error “Address is required.”

Equivalence Partitioning

Test Case: Use different valid payment methods (card, PayPal, etc.)

Input: Choose valid method

Expected Outcome: Payment processed; confirmation displayed.

Error Guessing

Test Case: Enter invalid payment info.

Input: Card number “1234 5678 0000”

Expected Outcome: Error “Invalid payment details.”

4. Responsive Layout and UI
Test Design Techniques: Use Case Testing, Error Guessing

Test Cases:
Use Case Testing

Test Case: Open the homepage on a desktop browser.

Input: Chrome, 1920x1080

Expected Outcome: Proper layout, all sections visible.

Use Case Testing

Test Case: Open the homepage on a mobile device.

Input: iPhone 13

Expected Outcome: Mobile layout loads, menu collapses correctly.

Error Guessing

Test Case: Rotate mobile device from portrait to landscape.

Input: Rotate during checkout

Expected Outcome: Layout adapts with no distortion or data loss.

5. Product Filtering by Category
Test Design Techniques: Equivalence Partitioning, Use Case Testing

Test Cases:
Equivalence Partitioning

Test Case: Select a valid category (e.g., “Healthy Food”)

Input: Click category tab

Expected Outcome: Page displays only relevant products.

Error Guessing

Test Case: Select a category with no products

Input: Click on a category with 0 items

Expected Outcome: Message “No items available.”

6. Contact/Support Form
Test Design Techniques: Boundary Value Analysis (BVA), Error Guessing

Test Cases:
BVA

Test Case: Submit form with valid 100-character message.

Input: Name, email, 100-char message

Expected Outcome: Support ticket submitted, confirmation shown.

Error Guessing

Test Case: Leave all fields empty and click submit

Input: Blank form

Expected Outcome: Error messages for each field.

Error Guessing

Test Case: Enter invalid email format.

Input: “user@domain”

Expected Outcome: “Invalid email format” message shown.



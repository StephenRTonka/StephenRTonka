**\# XPath Task 2** 

1. //header//button\[.//svg//\*\[name()='path' and contains(@d, 'M12 12c2.21')\]\]

2. //input\[@placeholder='Email address'\]               ← Email input field

//input\[@placeholder='Password'\]                    ← Password input field  
//button\[text()='Sign In'\]                          ← Sign In button  
//a\[text()='Create a new account'\]                  ← Create a new account link  
//a\[text()='Go to Home'\]                             ← Go to Home link

3. //input\[@placeholder='Full Name'\]              ← Full Name input field

//input\[@placeholder='Email address'\]          ← Email input field  
//input\[@placeholder='Password'\]               ← Password input field  
//button\[text()='Sign Up'\]                     ← Sign Up button

4. //button\[text()='Confirm'\] 

5. \# Quantity input for Oranges

//h2\[text()='Oranges'\]/ancestor::div\[contains(@class,'product')\]  
//input\[@type='number'\]

\# Add to Cart button for Oranges  
//h2\[text()='Oranges'\]/ancestor::div\[contains(@class,'product')\]  
//button\[contains(text(), 'Add to cart')\]

\# Add to Wish List button for Oranges  
//h2\[text()='Oranges'\]/ancestor::div\[contains(@class,'product')\]  
//button\[contains(@aria-label, 'Add to Wishlist')\]

